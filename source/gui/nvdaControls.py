# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2016-2024 NV Access Limited, Derek Riemer, Cyrille Bougot, Luke Davis, Leonard de Ruijter
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import collections
import enum
import typing
from typing import (
	List,
	OrderedDict,
	Type,
)
import warnings

import wx
from wx.lib import scrolledpanel
from wx.lib.mixins import listctrl as listmix

import config
from config.featureFlag import (
	FeatureFlag,
	FlagValueEnum as FeatureFlagEnumT,
)
import gui.message
from .dpiScalingHelper import DpiScalingHelperMixin
from . import (
	guiHelper,
)
import winUser

from collections.abc import Callable


__all__ = [
	"AutoWidthColumnListCtrl",
	"SelectOnFocusSpinCtrl",
	"ListCtrlAccessible",
	"CustomCheckListBox",
	"AutoWidthColumnCheckListCtrl",
	"DPIScaledDialog",
	"MessageDialog",
	"_ContinueCancelDialog",
	"EnhancedInputSlider",
	"TabbableScrolledPanel",
	"FeatureFlagCombo",
]


class AutoWidthColumnListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
	"""
	A list control that allows you to specify a column to resize to take up the remaining width of a wx.ListCtrl.
	It also changes L{OnGetItemText} to call an optionally provided callable,
	and adds a l{sendListItemFocusedEvent} method.
	"""

	def __init__(
		self,
		parent,
		id=wx.ID_ANY,
		autoSizeColumn="LAST",
		itemTextCallable=None,
		pos=wx.DefaultPosition,
		size=wx.DefaultSize,
		style=0,
	):
		"""initialiser
		Takes the same parameter as a wx.ListCtrl with the following additions:
		@param autoSizeColumn: defaults to "LAST" which results in the last column being resized.
			Pass the column number to be resized, valid values: 1 to N
		@type autoSizeColumn: int
		@param itemTextCallable: A callable to be called to get the item text for a particular item's column in the list.
			It should accept the same parameters as L{OnGetItemText},
		@type itemTextCallable: L{callable}
		"""
		if itemTextCallable is not None:
			if not isinstance(itemTextCallable, Callable):
				raise TypeError("itemTextCallable should be None or a callable")
			self._itemTextCallable = itemTextCallable
		else:
			self._itemTextCallable = self._super_itemTextCallable
		wx.ListCtrl.__init__(self, parent, id=id, pos=pos, size=size, style=style)
		listmix.ListCtrlAutoWidthMixin.__init__(self)
		self.setResizeColumn(autoSizeColumn)
		self.Bind(wx.EVT_WINDOW_DESTROY, source=self, id=self.GetId, handler=self._onDestroy)

	def _onDestroy(self, evt):
		evt.Skip()
		self._itemTextCallable = None

	def _super_itemTextCallable(self, item, column):
		return super(AutoWidthColumnListCtrl, self).OnGetItemText(item, column)

	def OnGetItemText(self, item, column):
		return self._itemTextCallable(item, column)

	def sendListItemFocusedEvent(self, index):
		evt = wx.ListEvent(wx.wxEVT_LIST_ITEM_FOCUSED, self.Id)
		evt.EventObject = self
		evt.Index = index
		self.ProcessEvent(evt)


class SelectOnFocusSpinCtrl(wx.SpinCtrl):
	"""
	A spin control that automatically selects the value when the control gains focus.
	This makes editing the values quicker.
	"""

	def __init__(
		self,
		parent,
		id=wx.ID_ANY,
		value=wx.EmptyString,
		pos=wx.DefaultPosition,
		size=wx.DefaultSize,
		style=wx.SP_ARROW_KEYS | wx.ALIGN_RIGHT,
		min=0,
		max=100,
		initial=0,
		name="labelStr",
	):
		"""initialiser - Takes the same parameters as a wx.SpinCtrl."""
		wx.SpinCtrl.__init__(self, parent, id, value, pos, size, style, min, max, initial, name)
		self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)

	def OnSetFocus(self, evt):
		numChars = len(str(self.GetValue()))
		self.SetSelection(0, numChars)
		evt.Skip()


class ListCtrlAccessible(wx.Accessible):
	"""WX Accessible implementation for checkable lists which aren't fully accessible."""

	def GetRole(self, childId):
		if childId == winUser.CHILDID_SELF:
			return super().GetRole(childId)
		return (wx.ACC_OK, wx.ROLE_SYSTEM_CHECKBUTTON)

	def GetState(self, childId):
		if childId == winUser.CHILDID_SELF:
			return super().GetState(childId)
		states = wx.ACC_STATE_SYSTEM_SELECTABLE | wx.ACC_STATE_SYSTEM_FOCUSABLE
		if self.Window.IsChecked(childId - 1):
			states |= wx.ACC_STATE_SYSTEM_CHECKED
		if self.Window.IsSelected(childId - 1):
			states |= wx.ACC_STATE_SYSTEM_SELECTED
			# wx doesn't seem to  have a method to check whether a list item is focused.
			# Therefore, assume that a selected item is focused when the list itself has focus,
			# which is the case in single select list boxes.
			if self.Window.HasFocus():
				states |= wx.ACC_STATE_SYSTEM_FOCUSED
		return (wx.ACC_OK, states)


class CustomCheckListBox(wx.CheckListBox):
	"""Custom checkable list to fix a11y bugs in the standard wx checkable list box."""

	def __init__(self, *args, **kwargs):
		super(CustomCheckListBox, self).__init__(*args, **kwargs)
		# Register a custom wx.Accessible implementation to fix accessibility incompleties
		self.SetAccessible(ListCtrlAccessible(self))
		# Register ourself with ourself's selected event, so that we can notify winEvent of the state change.
		self.Bind(wx.EVT_CHECKLISTBOX, self.notifyIAccessible)

	def notifyIAccessible(self, evt):
		# Notify winEvent that something changed.
		# We must do this, so that NVDA receives a stateChange.
		evt.Skip()
		winUser.NotifyWinEvent(
			winUser.EVENT_OBJECT_STATECHANGE,
			self.Handle,
			winUser.OBJID_CLIENT,
			evt.Selection + 1,
		)


class AutoWidthColumnCheckListCtrl(AutoWidthColumnListCtrl, listmix.CheckListCtrlMixin):
	"""
	An L{AutoWidthColumnListCtrl} with accessible checkboxes per item.
	In contrast with L{CustomCheckableListBox}, this class supports multiple columns.
	Also note that this class ignores the L{CheckListCtrlMixin.OnCheckItem} callback.
	If you want to be notified of checked/unchecked events,
	create an event handler for wx.EVT_CHECKLISTBOX.
	This event is only fired when an item is toggled with the mouse or keyboard.
	"""

	def __init__(
		self,
		parent,
		id=wx.ID_ANY,
		autoSizeColumn="LAST",
		pos=wx.DefaultPosition,
		size=wx.DefaultSize,
		style=0,
		check_image=None,
		uncheck_image=None,
		imgsz=(16, 16),
	):
		AutoWidthColumnListCtrl.__init__(
			self,
			parent,
			id=id,
			pos=pos,
			size=size,
			style=style,
			autoSizeColumn=autoSizeColumn,
		)
		listmix.CheckListCtrlMixin.__init__(self, check_image, uncheck_image, imgsz)
		# Register a custom wx.Accessible implementation to fix accessibility incompleties
		self.SetAccessible(ListCtrlAccessible(self))
		# Register our hook to check/uncheck items with space.
		# Use wx.EVT_CHAR_HOOK, because EVT_LIST_KEY_DOWN isn't triggered for space.
		self.Bind(wx.EVT_CHAR_HOOK, self.onCharHook)
		# Register an additional event handler to call sendCheckListBoxEvent for mouse clicks if appropriate.
		self.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)

	def GetCheckedItems(self):
		return tuple(i for i in range(self.ItemCount) if self.IsChecked(i))

	def SetCheckedItems(self, indexes):
		for i in indexes:
			assert 0 <= i < self.ItemCount, "Index (%s) out of range" % i
		for i in range(self.ItemCount):
			self.CheckItem(i, i in indexes)

	CheckedItems = property(fget=GetCheckedItems, fset=SetCheckedItems)

	def onCharHook(self, evt):
		key = evt.GetKeyCode()
		if key != wx.WXK_SPACE:
			evt.Skip()
			return
		index = self.FocusedItem
		if index == -1:
			evt.Skip()
			return
		self.ToggleItem(index)
		self.sendCheckListBoxEvent(index)

	def onLeftDown(self, evt):
		"""Additional event handler for mouse clicks to call L{sendCheckListBoxEvent}."""
		(index, flags) = self.HitTest(evt.GetPosition())
		evt.Skip()
		if flags == wx.LIST_HITTEST_ONITEMICON:
			self.sendCheckListBoxEvent(index)

	def CheckItem(self, index, check=True):
		"""
		Adapted from L{CheckListCtrlMixin} to ignore the OnCheckItem callback and to call L{notifyIAccessible}.
		"""
		img_idx = self.GetItem(index).GetImage()
		if img_idx == 0 and check:
			self.SetItemImage(index, 1)
		elif img_idx == 1 and not check:
			self.SetItemImage(index, 0)
		self.notifyIAccessible(index)

	def notifyIAccessible(self, index):
		# Notify winEvent that something changed.
		# We must do this, so that NVDA receives a stateChange.
		winUser.NotifyWinEvent(winUser.EVENT_OBJECT_STATECHANGE, self.Handle, winUser.OBJID_CLIENT, index + 1)

	def sendCheckListBoxEvent(self, index):
		evt = wx.CommandEvent(wx.wxEVT_CHECKLISTBOX, self.Id)
		evt.EventObject = self
		evt.Int = index
		self.ProcessEvent(evt)


class DPIScaledDialog(wx.Dialog, DpiScalingHelperMixin):
	"""Automatically calls constructors in the right order, passing on arguments, and providing scaling features.
	Until wxWidgets/wxWidgets#334 is resolved, and we have updated to that build of wx.
	"""

	def __init__(self, *args, **kwargs):
		"""Called in place of wx.Dialog __init__ arguments are forwarded on.
		Expected args (from wx docs):
		parent, id, title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE, name=wx.DialogNameStr
		where:
		wx.DEFAULT_DIALOG_STYLE = (wxCAPTION | wxSYSTEM_MENU | wxCLOSE_BOX)
		"""
		wx.Dialog.__init__(self, *args, **kwargs)
		DpiScalingHelperMixin.__init__(self, self.GetHandle())


class MessageDialog(gui.message.MessageDialog):
	"""Provides a more flexible message dialog.

	.. warning:: This class is deprecated.
		Use :class:`gui.messageDialog.MessageDialog` instead.
		This class is an adapter around that class, and will be removed in 2026.1.

	Consider overriding _addButtons, to set your own buttons and behaviour.
	"""

	# We don't want the new message dialog's guard rails, as they may be incompatible with old code
	_FAIL_ON_NO_BUTTONS = False
	_FAIL_ON_NONMAIN_THREAD = False

	# Dialog types currently supported
	DIALOG_TYPE_STANDARD = 1
	DIALOG_TYPE_WARNING = 2
	DIALOG_TYPE_ERROR = 3

	@staticmethod
	def _legacyDialogTypeToDialogType(dialogType: int) -> gui.message.DialogType:
		match dialogType:
			case MessageDialog.DIALOG_TYPE_ERROR:
				return gui.message.DialogType.ERROR
			case MessageDialog.DIALOG_TYPE_WARNING:
				return gui.message.DialogType.WARNING
			case _:
				return gui.message.DialogType.STANDARD

	def __new__(cls, *args, **kwargs):
		warnings.warn(
			"gui.nvdaControls.MessageDialog is deprecated. Use gui.messageDialog.MessageDialog instead.",
			DeprecationWarning,
		)
		return super().__new__(cls, *args, **kwargs)

	def __init__(
		self,
		parent: wx.Window | None,
		title: str,
		message: str,
		dialogType: int = DIALOG_TYPE_STANDARD,
	):
		super().__init__(
			parent,
			message=message,
			title=title,
			dialogType=self._legacyDialogTypeToDialogType(dialogType),
			buttons=None,
		)

	def _addButtons(self, buttonHelper: guiHelper.ButtonHelper) -> None:
		"""Adds ok / cancel buttons. Can be overridden to provide alternative functionality."""
		self.addOkButton(returnCode=wx.OK)
		self.addCancelButton(returnCode=wx.CANCEL)


class _ContinueCancelDialog(MessageDialog):
	"""
	This implementation of a `gui.nvdaControls.MessageDialog`, provides `Continue` and `Cancel` buttons as its controls.
	These serve the same functions as `OK` and `Cancel` in other dialogs, but may be more desirable in some situations.
	It also supports NVDA's context sensitive help.
	"""

	def __init__(
		self,
		parent: wx.Frame,
		title: str,
		message: str,
		dialogType: int = MessageDialog.DIALOG_TYPE_STANDARD,
		continueButtonFirst: bool = True,
		helpId: str | None = None,
	) -> None:
		"""Creates a ContinueCancelDialog MessageDialog.

		:param parent: The parent window for the dialog, usually `gui.mainFrame`.
		:param title: The title or caption of the dialog.
		:param message: The message to be shown in the dialog.
		:param dialogType: One of the dialog type constants from `MessageDialog`, defaults to standard.
		:param continueButtonFirst: If True, the Continue button will appear first, and be selected when the dialog
			opens; if False, the Cancel button will. Defaults to True.
		:param helpId: a helpId, as used with the `gui.contextHelp` module, enabling the help key (`F1`)
			to open a browser to a specific heading in the NVDA user guide.
		"""
		self.continueButtonFirst: bool = continueButtonFirst
		if helpId is not None:
			self.helpId = helpId
		super().__init__(parent, title, message, dialogType)
		if helpId is not None:
			# Help event has already been bound (in supersuperclass), so we need to re-bind it.
			self.bindHelpEvent(helpId, self)

	def _addButtons(self, buttonHelper: guiHelper.ButtonHelper) -> None:
		"""Override to add Continue and Cancel buttons."""
		self.addOkButton(
			# Translators: The label for the Continue button in an NVDA dialog.
			label=_("&Continue"),
			returnCode=wx.OK,
			defaultFocus=self.continueButtonFirst,
		)
		self.addCancelButton(
			# Translators: The label for the Cancel button in an NVDA dialog.
			label=_("Cancel"),
			returnCode=wx.CANCEL,
			defaultFocus=not self.continueButtonFirst,
		)


class EnhancedInputSlider(wx.Slider):
	def __init__(self, *args, **kwargs):
		super(EnhancedInputSlider, self).__init__(*args, **kwargs)
		self.Bind(wx.EVT_CHAR, self.onSliderChar)

	def SetValue(self, i):
		super(EnhancedInputSlider, self).SetValue(i)
		evt = wx.CommandEvent(wx.wxEVT_COMMAND_SLIDER_UPDATED, self.GetId())
		evt.SetInt(i)
		self.ProcessEvent(evt)
		# HACK: Win events don't seem to be sent for certain explicitly set values,
		# so send our own win event.
		# This will cause duplicates in some cases, but NVDA will filter them out.
		winUser.user32.NotifyWinEvent(
			winUser.EVENT_OBJECT_VALUECHANGE,
			self.Handle,
			winUser.OBJID_CLIENT,
			winUser.CHILDID_SELF,
		)

	def onSliderChar(self, evt):
		key = evt.KeyCode
		if key == wx.WXK_UP:
			newValue = min(self.Value + self.LineSize, self.Max)
		elif key == wx.WXK_DOWN:
			newValue = max(self.Value - self.LineSize, self.Min)
		elif key == wx.WXK_PAGEUP:
			newValue = min(self.Value + self.PageSize, self.Max)
		elif key == wx.WXK_PAGEDOWN:
			newValue = max(self.Value - self.PageSize, self.Min)
		elif key == wx.WXK_HOME:
			newValue = self.Max
		elif key == wx.WXK_END:
			newValue = self.Min
		else:
			evt.Skip()
			return
		self.SetValue(newValue)


class TabbableScrolledPanel(scrolledpanel.ScrolledPanel):
	"""
	This class was created to ensure a ScrolledPanel scrolls to nested children of the panel when navigating
	with tabs (#12224). A PR to wxPython implementing this fix can be tracked on
	https://github.com/wxWidgets/Phoenix/pull/1950
	"""

	def GetChildRectRelativeToSelf(self, child: wx.Window) -> wx.Rect:
		"""
		window.GetRect returns the size of a window, and its position relative to its parent.
		When calculating ScrollChildIntoView, the position relative to its parent is not relevant unless the
		parent is the ScrolledPanel itself. Instead, calculate the position relative to scrolledPanel
		"""
		childRectRelativeToScreen = child.GetScreenRect()
		scrolledPanelScreenPosition = self.GetScreenPosition()
		return wx.Rect(
			childRectRelativeToScreen.x - scrolledPanelScreenPosition.x,
			childRectRelativeToScreen.y - scrolledPanelScreenPosition.y,
			childRectRelativeToScreen.width,
			childRectRelativeToScreen.height,
		)

	def ScrollChildIntoView(self, child: wx.Window) -> None:
		"""
		Overrides child.GetRect with `GetChildRectRelativeToSelf` before calling
		`super().ScrollChildIntoView`. `super().ScrollChildIntoView` incorrectly uses child.GetRect to
		navigate scrolling, which is relative to the parent, where it should instead be relative to this
		ScrolledPanel.
		"""
		oldChildGetRectFunction = child.GetRect
		child.GetRect = lambda: self.GetChildRectRelativeToSelf(child)
		try:
			super().ScrollChildIntoView(child)
		finally:
			# ensure child.GetRect is reset properly even if super().ScrollChildIntoView throws an exception
			child.GetRect = oldChildGetRectFunction


class FeatureFlagCombo(wx.Choice):
	"""Creates a combobox (wx.Choice) with a list of feature flags."""

	def __init__(
		self,
		parent: wx.Window,
		keyPath: List[str],
		conf: config.ConfigManager,
		pos=wx.DefaultPosition,
		size=wx.DefaultSize,
		style=0,
		validator=wx.DefaultValidator,
		name=wx.ChoiceNameStr,
		onChoiceEventHandler: typing.Callable[[wx.CommandEvent], None] | None = None,
	):
		"""
		:param parent: The parent window.
		:param keyPath: The list of keys required to get to the config value.
		:param conf: The config.conf object.
		:param pos: The position of the control. Forwarded to wx.Choice
		:param size: The size of the control. Forwarded to wx.Choice
		:param style: The style of the control. Forwarded to wx.Choice
		:param validator: The validator for the control. Forwarded to wx.Choice
		:param name: The name of the control. Forwarded to wx.Choice
		:param onChoiceEventHandler: Event handler bound for EVT_CHOICE
		"""
		self._confPath = keyPath
		self._conf = conf
		configValue = self._getConfigValue()
		self._optionsEnumClass: Type[FeatureFlagEnumT] = configValue.enumClassType
		translatedOptions: typing.OrderedDict[FeatureFlagEnumT, str] = collections.OrderedDict(
			{
				value: value.displayString
				for value in self._optionsEnumClass
				if value != self._optionsEnumClass.DEFAULT
			},
		)
		if self._optionsEnumClass.DEFAULT in translatedOptions:
			raise ValueError(
				f"The translatedOptions dictionary should not contain the key {self._optionsEnumClass.DEFAULT!r}"
				" It will be added automatically. See _setDefaultOptionLabel",
			)
		self._translatedOptions = self._createOptionsDict(translatedOptions)
		choices = list(self._translatedOptions.values())
		super().__init__(
			parent,
			choices=choices,
			pos=pos,
			size=size,
			style=style,
			validator=validator,
			name=name,
		)
		if onChoiceEventHandler is not None:
			self.Bind(
				wx.EVT_CHOICE,
				onChoiceEventHandler,
			)
		self.SetSelection(self._getChoiceIndex(configValue.value))
		self.defaultValue = self._getConfSpecDefaultValue()
		"""The default value of the config spec. Not the "behavior of default".
		This is provided to maintain compatibility with other controls in the
		advanced settings dialog.
		"""

	def _getChoiceIndex(self, value: FeatureFlagEnumT) -> int:
		return list(self._translatedOptions.keys()).index(value)

	def _getConfSpecDefaultValue(self) -> FeatureFlagEnumT:
		defaultValueFromSpec = self._conf.getConfigValidation(self._confPath).default
		if not isinstance(defaultValueFromSpec, FeatureFlag):
			raise ValueError(f"Default spec value is not a FeatureFlag, but {type(defaultValueFromSpec)}")
		return defaultValueFromSpec.value

	def _getConfigValue(self) -> FeatureFlag:
		keyPath = self._confPath
		if not keyPath or len(keyPath) < 1:
			raise ValueError("Key path not provided")

		conf = self._conf
		for nextKey in keyPath:
			conf = conf[nextKey]

		if not isinstance(conf, FeatureFlag):
			raise ValueError(f"Config value is not a FeatureFlag, but a {type(conf)}")
		return conf

	def isValueConfigSpecDefault(self) -> bool:
		"""Does the current value of the control match the default value from the config spec?
		This is not the same as the "behaviour of default".
		"""
		return self.GetSelection() == self.defaultValue

	def resetToConfigSpecDefault(self) -> None:
		"""Set the value of the control to the default value from the config spec."""
		self.SetSelection(self._getChoiceIndex(self.defaultValue))

	def _getControlCurrentValue(self) -> enum.Enum:
		return list(self._translatedOptions.keys())[self.GetSelection()]

	def _getControlCurrentFlag(self) -> FeatureFlag:
		flagValue = self._getControlCurrentValue()
		currentFlag = self._getConfigValue()
		return FeatureFlag(flagValue, currentFlag.behaviorOfDefault)

	def saveCurrentValueToConf(self) -> None:
		"""Set the config value to the current value of the control."""
		flagValue = self._getControlCurrentValue()
		keyPath = self._confPath
		if not keyPath or len(keyPath) < 1:
			raise ValueError("Key path not provided")
		lastIndex = len(keyPath) - 1

		conf = self._conf
		for index, nextKey in enumerate(keyPath):
			if index == lastIndex:
				conf[nextKey] = flagValue.name
				return
			else:
				conf = conf[nextKey]

	def _createOptionsDict(
		self,
		translatedOptions: OrderedDict[FeatureFlagEnumT, str],
	) -> OrderedDict[enum.Enum, str]:
		behaviorOfDefault = self._getConfigValue().behaviorOfDefault
		translatedStringForBehaviorOfDefault = translatedOptions[behaviorOfDefault]
		# Translators: Label for the default option for some feature-flag combo boxes.
		# Such as, in the Advanced settings panel option, 'Load Chromium virtual buffer when document busy.'.
		# e.g. "Default (Yes)".
		# The placeholder {default} is replaced with the label of the option which describes current default behavior
		# in NVDA.
		defaultOptionLabel: str = _("Default ({default})").format(
			default=translatedStringForBehaviorOfDefault,
		)
		return collections.OrderedDict(
			{
				self._optionsEnumClass.DEFAULT: defaultOptionLabel,  # make sure default is the first option.
				**translatedOptions,
			},
		)
