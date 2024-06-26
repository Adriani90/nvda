# NVDA NVDA_VERSION Brukermanual

[TOC]

<!-- KC:title: NVDA NVDA_VERSION Tastaturkommandoer Hurtigreferanse -->



## introduksjon {#Introduction}

Velkommen til NVDA!

NonVisual Desktop Access (NVDA) er en gratis skjermleser for Microsoft Windows-operativsystemet. Den er laget med åpen kildekode.
NVDA gir tilbakemeldinger via syntetisk tale og punktskrift, og gjør blinde og svaksynte personer i stand til å bruke datamaskiner som kjører Windows til samme pris som det seende personer betaler.
NVDA er utviklet av [NV Access](https://www.nvaccess.org/), med bidrag fra fellesskapet.

### Generelle funksjoner {#GeneralFeatures}

NVDA lar blinde og svaksynte få tilgang til og bruke Windows operativsystem og mange tredjeparts programmer.

Blant de viktigste funksjonene er:

* Støtte for populære programmer, inkludert nettlesere, e-postklienter, internett-chatteprogrammer og kontorpakker
* Innebygget syntetisk tale som støtter over 80 språk
* Lesing av tekstformatering hvor dette er tilgjengelig, for eksempel fontnavn og -størrelse, stil og stavefeil
* Automatisk lesing av tekst under musen og valgfri hørbar indikasjon der muspekeren er plassert
* Støtte for mange leselister, inkludert innskriving av punktskrift på leselister med tastatur
* Mulig å kjøre fra en USB-minnepinne eller annet flyttbart medium uten behov for installasjon
* Talende installasjonsprogram som er enkelt å bruke
* Oversatt til 54 språk
* Støtte for moderne Windows-operativsystemer, inkludert både 32- og 64-bits varianter
* Mulig å kjøre i Windows-pålogging og i andre sikre skjermer
* Annonserer kontroller og tekst når en bruker berøringskommandoer
* Støtte for vanlige tilgjengelighetsgrensesnitt som Microsoft Active Accessibility, Java Access Bridge, IAccessible2 og UI Automation (UI Automation støttes bare i Windows 7 og senere)
* Støtte for Windows kommandolinje og konsoll-programmer

### Internasjonalisering {#Internationalization}

Det er viktig at mennesker hvor som helst i verden, uansett hvilket språk de snakker, får lik tilgang til teknologi.
Foruten engelsk, har NVDA blitt oversatt til 54 språk, inkludert: afrikaans, albansk, amharisk, arabisk, aragonsk, bulgarsk, burmansk, dansk, farsi, finsk, fransk, galisisk, georgisk, gresk, hebraisk, hindi, irsk, islandsk, italiensk, japansk, kannada, katalansk, kinesisk (tradisjonell og forenklet), kirgisisk, kroatisk, kurdisk, litauisk, makedonsk, mongolsk, nederlandsk, nepali, norsk, polsk, portugisisk (Brasil og Portugal), punjabi, rumensk, russisk, serbisk, slovakisk, slovensk, spansk (Colombia og Spania), svensk, tamil, thai, tsjekkisk, tyrkisk, tysk (Tyskland og Sveits), ukrainsk, ungarsk og vietnamesisk.

### Talesyntesestøtte {#SpeechSynthesizerSupport}

Foruten å formidle meldinger og brukergrensesnitt på flere språk, kan NVDA også la brukeren lese innhold på alle språk, så lenge hun/han har en talesyntese som kan snakke det språket.

Med NVDA følger [eSpeak NG](https://github.com/espeak-ng/espeak-ng), en flerspråklig talesyntese som er gratis og laget med åpen kildekode.

Informasjon om andre talesynteser som NVDA støtter finnes i [Støttede talesynteser](#SupportedSpeechSynths)-seksjonen.

### Punktskriftstøtte {#BrailleSupport}

For brukere som har leselist, kan NVDA gi informasjon i punktskrift. Skriving av både uforkortet og forkortet punktskrift via et punktskrifttastatur støttes også.

Se seksjonen [Støttede leselister](#SupportedBrailleDisplays) for informasjon om de støttede leselistene.

NVDA støtter punktskrift for mange språk, inkludert fullskrift, kortskrift og datapunktskrift.

### Lisens og kopibeskyttelse {#LicenseAndCopyright}

NVDA er kopibeskyttet NVDA_COPYRIGHT_YEARS NVDA bidragsytere.

NVDA dekkes av GNU General Public License (versjon 2).
Du er fri til å dele eller endre denne programvaren på alle måter du vil så lenge lisensen medfølger, og du gjør all kildekode tilgjengelig for alle som ønsker den.
Dette gjelder både originale og modifiserte eksemplarer av denne programvaren, samt eventuelle avledede verk.
For ytterligere opplysninger, kan du [se den fullstendige lisensen.](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)

## Systemkrav {#SystemRequirements}

* Operativsystem: Alle 32- og 64-bits versjoner av Windows 7, Windows 8, Windows 8.1 og Windows 10, og alle serveroperativsystemer fra og med Windows Server 2008 R2.
* For Windows 7 krever NVDA Service Pack 1 eller høyere.
* For Windows Server 2008 R2 krever NVDA Service Pack 1 eller høyere.
* Minne: 256 mb RAM eller mer
* Prosessorhastighet: 1,0 GHz eller høyere
* Omtrent 90 MB lagringsplass.

## Få tak i og installer NVDA {#GettingAndSettingUpNVDA}

Hvis du ennå ikke har fått tak i en kopi av NVDA, kan du laste den ned fra [www.nvaccess.org](NVDA_URL).

Gå til nedlastingssiden. Der finner du en lenke for å laste ned den nyeste versjonen av NVDA.

Når du kjører fila du akkurat har lastet ned, vil den starte en midlertidig kopi av NVDA. Du vil så bli spurt om du ønsker å installere NVDA, lage en flyttbar kopi eller bare fortsette å bruke den midlertidige kopien.

Dersom du planlegger å alltid bruke NVDA på denne datamaskinen, bør du velge å installere NVDA. Å installere NVDA gir tilgang til ekstra funksjonalitet slik som automatisk start etter innlogging, muligheten til å lese påloggingsvinduet og andre sikre skjermer i Windows (som ikke kan gjøres med portable eller midlertidige kopier) og oppretting av snarveier i startmenyen og på skrivebordet.

Fra den installerte kopien av NVDA kan du selv lage en flyttbar kopi når du måtte ønske det. Hvis du ønsker å ta NVDA med deg på en USB-minnepenn eller et annet skrivbart medium, bør du lage en flyttbar kopi.

Den portable kopien kan også installeres på en datamaskin på et senere tidspunkt.

Om du imidlertid skulle ønske å kopiere NVDA til et ikke skrivbart medium som for eksempel en CD, bør du bare kopiere pakken du har lastet ned.

Kjøring av en flyttbar kopi direkte fra et ikke skrivbart medium støttes ikke.

Bruk av en midlertidig kopi av NVDA er også en mulighet (for eksempel for å demonstrere programvaren), selv å det å starte NVDA på denne måten hver gang kan bli nokså tidkrevende.

### Begrensninger i flyttbar og midlertidig utgave {#PortableAndTemporaryCopyRestrictions}

Bortsett fra manglende mulighet for å kunne starte automatisk under og/eller etter innlogging, har flyttbare og midlertidige kopier av NVDA også disse begrensningene:

* kan ikke samhandle med programmer som kjører med administrative privilegier, med mindre NVDA også kjøres med slike privilegier (ikke anbefalt).
* kan ikke lese brukerkontokontrollskjermer (UAC) når du starter et program med administrative privilegier.
* Windows 8 og senere: kan ikke støtte inndata fra berøringsskjerm.
* Windows 8 og senere: kan ikke tilby nettmodus og uttale av skrevne bokstaver i apper fra Windows Store.
* Windows 8 og senere: lyddemping støttes ikke.

## Installere NVDA {#InstallingNVDA}

Hvis du installerer NVDA direkte fra pakken du har lastet ned, kan du trykke på knappen "Installer NVDA".

Hvis du alt har lukket denne dialogen eller ønsker å installere fra en flyttbar kopi, velger du menyelementet "Installer NVDA" som du finner under "Verktøy" i NVDA-menyen.

Installasjonsdialogen som vises, vil bekrefte om du ønsker å installere NVDA og om denne installasjonen vil oppdatere en tidligere installasjon.

Ved å trykke på "Fortsett"-knappen starter du installasjonen av NVDA.

Det finnes også noen få valg i denne dialogen som blir forklart nedenfor.

Så snart installasjonen er fullført, vil du få ei melding om at installasjonen var vellykket.

Trykk på OK-knappen for å starte den nylig installerte kopien av NVDA.

#### Start i Windows pålogging {#StartAtWindowsLogon}

Dette valget lar deg avgjøre om NVDA skal starte automatisk eller ikke når du er i innloggingsvinduet i Windows, før du har skrevet inn et passord. Dette gjelder også for brukerkontokontroll og andre sikre skjermer.

#### Lag snarvei på skrivebordet (ctrl+alt+n) {#CreateDesktopShortcut}

Dette valget lar deg avgjøre om NVDA skal lage en snarvei på skrivebordet for å starte NVDA. Velger du at snarveien skal opprettes, blir det også knyttet en hurtigtast, Ctrl+Alt+n, til den. Med denne hurtigtasten kan du starte NVDA når du vil.

#### Kopier flyttbar konfigurasjon til gjeldende brukerkonto {#CopyPortableConfigurationToCurrentUserAccount}

Dette er et valg som er tilgjengelig bare når du installerer fra en flyttbar kopi av NVDA. Installerer du fra pakken du har lastet ned, finner du ikke denne muligheten.

Dette valget lar deg avgjøre om brukerkonfigurasjonen fra den kjørende kopien av NVDA skal kopieres til konfigurasjonen for den innloggede brukeren på PC-en, for bruk med den installerte kopien av NVDA. Dette vil ikke kopiere konfigurasjonen for andre brukere av PC-en, og det vil heller ikke kopiere innstillinger til systemkonfigurasjonen for bruk i Windows pålogging eller på andre sikre skjermer.

### Lag en flyttbar kopi {#CreatingAPortableCopy}

Hvis du vil lage en flyttbar kopi direkte fra NVDAs nedlastingsfil, trykker du rett og slett på "Lag flyttbar kopi".

Hvis du alt har lukket denne dialogen, eller hvis du kjører en installert kopi av NVDA, velger du menyelementet Lag flyttbar kopi som du finner under Verktøy i NVDA-menyen.

Dialogen som da vises, lar deg velge hvor den flyttbare kopien skal lages. Dette kan være i ei mappe på harddisken din, eller et sted på en USB-minnepinne eller et annet flyttbart medium.

Det er også mulig å velge om NVDA skal kopiere den påloggende brukerens gjeldende NVDA-konfigurasjon for bruk med den nye, flyttbare kopien av NVDA. Dette valget er bare tilgjengelig når du lager en flyttbar kopi fra en installert kopi av NVDA, men ikke fra den nedlastede pakken.

Trykk på Fortsett for å lage den flyttbare kopien.

Så snart den nye kopien er laget, vil det dukke opp ei melding som forteller deg at jobben er vellykket utført.

Trykk på OK for å fjerne denne dialogen.

## Kom i gang med NVDA {#GettingStartedWithNVDA}
### Start NVDA {#LaunchingNVDA}

Hvis du har installert NVDA med installasjonsprogrammet, er det å starte NVDA så enkelt som enten å trykke Ctrl+Alt+n, eller velge NVDA fra NVDA-menyen under Programmer på startmenyen.

I tillegg kan du også skrive NVDA i dialogboksen Kjør, og trykke Enter.

Du kan også sende noen [kommandolinjeparametre](#CommandLineOptions) som tillater deg å starte NVDA på nytt (-r), avslutte NVDA (-q), slå av programtillegg (--disable-addons), osv.

For installerte kopier lagrer NVDA som standard konfigurasjonen i "roaming"-appdatamappa under gjeldende bruker, "C:\Users\<bruker>\AppData\Roaming"). Dette kan endres slik at NVDA isteden laster konfigurasjonen fra den lokale appdata-mappa. Se seksjonen om [systemparametre](#SystemWideParameters) for flere detaljer.

For å starte den flyttbare versjonen, går du til mappa du pakket NVDA ut i, og trykker enter. Du kan også dobbeltklikke på nvda.exe.

Når NVDA starter, vil du først høre en stigende tonerekke (som forteller deg at NVDA lastes).
Avhengig av hvor rask maskinen er, eller hvis du kjører NVDA fra et USB-minne eller annet langsommere medium, kan det ta litt tid å starte NVDA.
Hvis det tar ekstra lang tid, bør NVDA si "Laster NVDA. Vennligst vent..."

Hvis du ikke hører noe av dette, eller du hører Windows' feilmeldingslyd, eller en synkende tonerekke, betyr dette at NVDA har en feil. Kanskje du da vil sende en feilrapport til utviklerne? Vennligst sjekk NVDAs nettside for hvordan du gjør dette.

#### Velkomstdialog {#WelcomeDialog}

Når NVDA starter for første gang, vil du bli møtt av en dialogboks som gir deg litt grunnleggende informasjon om NVDA-spesialtasten og NVDA-menyen. (Vennligst se nærmere avsnittene om disse temaene.)

Dialogboksen inneholder også en kombinasjonsboks og tre avkryssingsbokser.

Kombinasjonsboksen lar deg velge tastaturoppsett.

Den første avkryssingsboksen lar deg kontrollere om NVDA skal bruke CapsLock som en NVDA-valgtast.

Den andre avkryssingsboksen lar deg avgjøre om NVDA skal starte automatisk etter at du har logget inn i Windows. Dette valget er bare tilgjengelig i installerte kopier av NVDA.

Den tredje avkryssingsboksen lar deg kontrollere om denne velkomstdialogen skal vises hver gang NVDA starter.

### Om tastaturkommandoer i NVDA {#AboutNVDAKeyboardCommands}
#### NVDA-tasten {#TheNVDAModifierKey}

NVDA-spesifikke tastaturkommandoer utføres vanligvis ved å trykke en spesiell tast kalt NVDA-tasten, sammen med én eller flere andre taster. Unntak fra dette er først og fremst kommandoer for tekstlesing med stasjonært tastaturoppsett, der en bare bruker tastene på det numeriske tastaturet, men det finnes noen andre unntak også.

NVDA kan konfigureres slik at enten insert-tasten på det numeriske tastaturet, den utvidede insert-tasten eller CapsLock-tasten kan brukes som NVDA-tast.

Som standard er begge insert-tastene definert som NVDA-taster.

Hvis du ønsker at en av NVDA-tastene skal opptre som opprinnelig tast (for eksempel fordi du ønsker å trykke CapsLock når du har satt CapsLock til å være NVDA-tast) kan du trykke på tasten to ganger i rask rekkefølge.

#### Tastaturoppsett {#KeyboardLayouts}

NVDA leveres for tida med to sett med tastaturkommandoer, også kjent som tastaturoppsett: stasjonært og bærbart tastaturoppsett.

Som standard er NVDA satt opp til å bruke stasjonært tastaturoppsett. Du kan enkelt bytte til bærbart tastaturoppsett under kategorien Tastatur i [NVDA-innstillinger](#NVDASettings), som du finner under Brukervalg i NVDA-menyen.

Stasjonært tastaturoppsett gjør omfattende bruk av insert-tastene (med NumLock av).

Selv om mange bærbare PC-er ikke har noe fysisk numerisk tastatur, er det vanlig at de kan emulere numerisk tastatur ved å holde nede FN-tasten mens en trykker bokstaver, tall og tegn på høyre side av tastaturet (7, 8, 9, u, i, o, j, k, l osv.). Om dette ikke lar seg gjøre på din bærbare PC, eller om du ikke får slått av NumLock, kan det være lurt av deg å bytte til bærbart tastaturoppsett i stedet.

### Berøringsgester i NVDA {#NVDATouchGestures}

Kjører du NVDA på en enhet med berøringsskjerm og bruker Windows 8 eller høyere, kan du også kontrollere NVDA direkte via berøringsgester.

Så lenge NVDA kjører, vil all berøring av skjermen gå direkte til NVDA. Derfor vil handlinger som kan utføres normalt uten NVDA ikke fungere.

#### Utforsk skjermen {#ExploringTheScreen}

Den mest grunnleggende handlingen du kan utføre med berøringsskjermen er å annonsere kontrollen eller teksten på et hvilket som helst sted på skjermen. For å gjøre dette, plasserer du én finger et vilkårlig sted på skjermen.

Du kan også holde fingeren på skjermen og flytte den rundt for å få opplest andre kontroller eller tekst som fingeren beveger seg over.

#### Berøringsgester {#TouchGestures}

Når NVDA-kommandoer blir beskrevet seinere i denne brukerhåndboka, vil de ofte også inneholde en berøringsgest som kan brukes for å aktivere kommandoen på berøringsskjermen.
Her følger noen instruksjoner for hvordan du utfører de ulike berøringsgestene.

##### Trykk {#toc25}

Trykk raskt på skjermen med én eller flere fingrer.

Å trykke én gang med én finger er kjent som et trykk. Å trykke med to fingrer samtidig er kjent som et tofingertrykk, osv.

Hvis samme trykk-kommando blir utført raskt flere ganger etter hverandre, vil NVDA oppfatte dette som en multitrykkgest. Å trykke to ganger vil altså ressultere i et dobbelttrykk. Tre trykk etter hverandre vil resultere i et trippeltrykk, osv.

Disse multitrykkgestene gjenkjenner selvfølgelig også hvor mange fingrer som ble brukt, så det er mulig å ha gester som trippeltrykk med to fingrer, trykk med fire fingrer osv.

##### Sveip {#toc26}

Sveip raskt med fingeren over skjermen.

Det er fire mulige sveipegester, avhengig av retningen: sveip mot venstre, sveip mot høyre, sveip opp og sveip ned.

Akkurat som ved trykk, kan mer enn én finger brukes for å utføre gesten. Derfor er gester som sveip opp med to fingrer og sveip mot venstre med fire fingrer mulige.

#### Berøringsmodi {#TouchModes}

Siden det er langt flere NVDA-kommandoer enn mulige berøringsgester, har NVDA flere berøringsmodi du kan veksle mellom, og som gjør ulike undergrupper av kommandoer tilgjengelige.

De to modiene er tekstmodus og objektmodus.

Visse NVDA-kommandoer som oppgis i denne brukermanualen kan ha en berøringsmodus oppgitt i klammer etter berøringsgesten. For eksempel betyr sveip opp (tekstmodus) at kommandoen blir utført når du sveiper opp, men bare når du er i tekstmodus.

Hvis en kommando ikke har en modus knyttet til seg, vil det si at kommandoen fungerer uansett modus.

<!-- KC:beginInclude -->
For å bytte mellom modi, trykker du med tre fingrer.
<!-- KC:endInclude -->

#### Skjermtastatur {#TouchKeyboard}

Skjermtastaturet brukes til å skrive tekst og kommandoer fra en berøringsskjerm. Når du har fokus på et skrivefelt, henter du fram skjermtastaturet ved å dobbelttrykke på ikonet for skjermtastaturet nederst på skjermen. For nettbrett som Microsoft Surface Pro er skjermtastaturet alltid tilgjengelig så lenge et tastatur ikke er tilkoblet. For å ta bort skjermtastaturet kan du dobbelttrykke på ikonet for skjermtastatur eller flytte bort fra skrivefeltet.

For å finne taster på skjermtastaturet når skjermtastaturet er aktivt, flytter du fingeren til der skjermtastaturet er (normalt nederst på skjermen). Der bruker du én finger til å navigere omkring på skrivebordet. Når du finner tasten du vil trykke på, dobbelttrykker du eller løfter fingeren, avhengig av hvilket valg du har gjort i [kategorien Innstillinger for berøringsinteraksjon](#TouchInteraction) i NVDA-innstillingene.

#### Tastaturhjelp {#InputHelpMode}

Mange NVDA-kommandoer er nevnt gjennom hele resten av denne brukermanualen, men en enkel måte å utforske alle de forskjellige tastaturkommandoene på er å slå på tastaturhjelp.

For å slå på tastaturhjelp, trykker du NVDA+1.
For å slå den av, trykker du NVDA+1 en gang til.

Når tastaturhjelp er slått på, vil hvert tastetrykk du utfører på tastaturet eller hver gest du utfører på en berøringsskjerm gi som respons handlingen og hva den gjør (hvis den gjør noe).

Tastene vil ikke utføre sin funksjon når du er i tastaturhjelpmodus, slik at du kan trykke hvilke taster du vil.

### NVDA-menyen {#TheNVDAMenu}

NVDA-menyen lar deg kontrollere NVDAs innstillinger, hjelp, lagre/tilbakestille konfigurasjonen, endre taleordlister, få tilgang til flere verktøy og å avslutte NVDA.

For å gå til NVDA-menyen fra hvor som helst i Windows mens NVDA kjører, trykker du NVDA+n.
Du kan også gå til NVDA-menyen via systemstatusfeltet i Windows.
Enten høyreklikk på NVDA-ikonet i systemstatusfeltet, eller få tilgang til systemstatusfeltet ved å trykke Win+b, pil ned til NVDA-ikonet og trykk deretter på meny-tasten. Den finner du rett til venstre for høyre Ctrl-tast på de fleste tastaturer.

Når menyen vises, kan du bruke piltastene til å navigere i den, og enter-tasten for å aktivere et element.

### Grunnleggende NVDA-kommandoer {#BasicNVDACommands}

<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Berøring |Beskrivelse|
|---|---|---|---|---|
|Stopp tale |Ctrl |Ctrl |Trykk med to fingrer |Slutter øyeblikkelig å snakke|
|Pause tale |Skift |Skift |ingen |Pauser øyeblikkelig tale. Ved å trykke igjen vil talen fortsette der den slapp (hvis pause støttes av gjeldende talesyntese)|
|NVDA-meny |NVDA+n |NVDA-n |Dobbelttrykk med to fingrer |Åpner NVDA-menyen slik at du får tilgang til innstillinger, verktøy og hjelp osv.|
|Bytt talemodus |NVDA+s |NVDA+s |ingen |Bytter talemodus mellom tale, pip og av.|
|Slå av/på tastaturhjelpmodus |NVDA+1 |NVDA+1 |ingen |Når du trykker en tast i denne modusen vil tasten bli lest sammen med beskrivelse av eventuell NVDA-kommando tilknyttet den|
|Avslutt NVDA |NVDA+q |NVDA+q |ingen |Avslutter NVDA|
|Slipp neste tast gjennom |NVDA+F2 |NVDA+F2 |ingen |Lar NVDA slippe neste tastetrykk rett gjennom til det aktive programmet, selv om det normalt er håndtert som en NVDA-tastekommando|
|Slå programdvalemodus på/av |NVDA+Skift+s |NVDA+Skift+z |ingen |Dvalemodus deaktiverer alle NVDA-kommandoer og tale/punktskrift for det gjeldende programmet. Dette er mest nyttig i programmer som har sin egen tale eller skjermleserfunksjon. Trykk denne kommandoen på nytt for å deaktivere dvalemodus.|

### Rapportering av systeminformasjon {#ReportingSystemInformation}

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Rapporter dato/klokkeslett |NVDA+F12 |Ett trykk rapporterer gjeldende tid, to trykk rapporterer dato|
|Rapporter batteristatus |NVDA+Skift+b |Rapporterer batteristatus, dvs. om strøm er i bruk eller nåværende ladeprosent.|
|Rapporter tekst i utklippstavle |NVDA+c |Rapporterer tekst i utklippstavlen hvis det er noen.|

<!-- KC:endInclude -->

## Navigere med NVDA {#NavigatingWithNVDA}

NVDA lar deg utforske og navigere i systemet på flere måter, inkludert både normal samhandling og lesing.

### Objekter {#Objects}

Hvert program og selve operativsystemet består av mange objekter. Et objekt er et enkelt element som en tekststreng, knapp, boks, glidebryter, liste eller et redigerbart tekstfelt.

### Navigere med Systemfokus {#SystemFocus}

Systemfokus, også kjent som fokus, er [objektet](#Objects) som mottar tastetrykk som trykkes på tastaturet. For eksempel, hvis du skriver i et redigerbart tekstfelt, er tekstfeltet i fokus.

Den vanligste måten å navigere rundt i Windows med NVDA, er å ganske enkelt flytte systemfokus ved hjelp av standard tastaturkommandoer i Windows. Eksempler på dette kan være å trykke Tab og Skift+Tab for å gå fram og tilbake mellom kontrollene, trykke Alt for å komme til menylinjen og deretter bruke piltastene for å navigere i menyer, og trykke Alt+Tab for å flytte mellom kjørende programmer. Mens du gjør dette, vil NVDA gi informasjon om objektet som har fokus, slik som navn, type, verdi, tilstand, beskrivelse, tastatursnarvei og informasjon om posisjon.

Det er noen viktige kommandoer som er nyttige når du flytter sammen med Systemfokus:
<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Beskrivelse|
|---|---|---|---|
|Les gjeldende fokus |NVDA+Tab |NVDA+Tab |Leser gjeldende objekt eller kontroll som har systemfokus. Ved å trykke to ganger staves informasjonen|
|Les tittel |NVDA+t |NVDA+t |Leser tittelen på det aktive vinduet. Ved å trykke to ganger staves informasjonen. Ved å trykke tre ganger kopieres den til utklippstavlen|
|Les det aktive vinduet |NVDA+b |NVDA+b |Leser alle kontrollene i det aktive vinduet (nyttig for dialoger)|
|Les statuslinje |NVDA+End |NVDA+Skift+End |Leser Statuslinjen hvis NVDA finner en, og flytter navigasjonsobjektet til denne plasseringen. Ved å trykke to ganger staves informasjonen. Ved å trykke tre ganger kopieres den til utklippstavlen|

<!-- KC:endInclude -->

### Navigere med Systemmarkøren {#SystemCaret}

Når [objekter](#Objects) som tillater navigering og/eller redigering av tekst er [fokusert](#SystemFocus), kan du bevege deg i teksten ved hjelp av systemmarkøren, også kjent som redigeringsmarkøren.

Når fokus er på et objekt som har systemmarkør, kan du bruke piltastene, side opp, side ned, home, end osv. for å bevege deg rundt i teksten.
Du kan også endre teksten om kontrollen støtter redigering.
NVDA vil annonsere det når du flytter mellom tegn, ord og linje, og vil også opplyse når du markerer eller avmarkerer tekst.

NVDA har følgende tastaturkommandoer i tilknytning til systemmarkøren:
<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Beskrivelse|
|---|---|---|---|
|Si alle |NVDA+Pil ned |NVDA+a |Starter lesing fra systemmarkørens gjeldende posisjon, og flytter systemmarkøren under lesing|
|Les gjeldende linje |NVDA+Pil opp |NVDA+l |Leser linjen der systemmarkøren befinner seg. Ved å trykke to ganger staves linjen. Ved å trykke tre ganger staves linjen med tegnbeskrivelse.|
|Les gjeldende valgt tekst |NVDA+Skift+Pil opp |NVDA+Skift+s |Leser teksten som for øyeblikket er markert|
|Neste setning |Alt+PilNed |Alt+PilNed |Flytter markøren til neste setning og leser den. (støttes bare i|

Microsoft Word og Outlook) |

|Forrige setning |Alt+PilOpp |Alt+PilOpp |Flytter markøren til forrige setning og leser den.|

(støttes bare i Microsoft Word og Outlook) |

Når fokus er i en tabell, er følgende tastekommandoer også tilgjengelige:

| Navn |Tast |Beskrivelse|
|---|---|---|
|Gå til forrige kolonne |Ctrl+Alt+PilVenstre |Flytter systemmarkøren til forrige kolonne (i samme rad)|
|Gå til neste kolonne |Ctrl+Alt+PilHøyre |Flytter systemmarkøren til neste kolonne (i samme rad)|
|Gå til forrige rad |Ctrl+Alt+PilOpp |Flytter systemmarkøren til forrige rad (i samme kolonne)|
|Gå til neste rad |Ctrl+Alt+PilNed |Flytter systemmarkøren til neste rad (i samme kolonne)|

<!-- KC:endInclude -->

### Objektnavigasjon {#ObjectNavigation}

Det meste av tiden vil du arbeide med programmer ved hjelp av kommandoer som flytter [fokuset](#SystemFocus) og [markøren](#SystemCaret). Men noen ganger kan du ønske å utforske det gjeldende programmet eller operativsystemet uten å flytte fokus eller markør. Kanskje ønsker du også å arbeide med [objekter](#Objects) som ikke kan nås normalt ved hjelp av tastaturet. I disse tilfellene kan du bruke objektnavigasjon.

Objektnavigasjon lar deg flytte mellom og få informasjon om de enkelte [objekter](#Objects).

Når du flytter til et objekt, vil NVDA annonsere det på samme måte som NVDA også annonserer systemfokus.
For å lese all tekst slik den vises på skjermen, kan du i stedet bruke [flatlesing](#ScreenReview).

I stedet for å måtte flytte fram og tilbake mellom hvert enkelt objekt på systemet, er objektene organisert hierarkisk. Dette betyr at noen objekter inneholder andre objekter, og du må flytte inni dem for å få tilgang til de objektene de inneholder. For eksempel inneholder en liste listeelementer, så du må flytte inne i listen for å få tilgang til elementene den inneholder.

Hvis du har fokus på et listeelement, og flytter til neste eller forrige, kommer du til andre listeelementer i samme liste.
Å flytte til et listeelement i hovedobjektet vil ta deg tilbake til listen. Du kan deretter flytte forbi listen hvis du ønsker tilgang til andre objekter.

Tilsvarende inneholder en verktøylinje kontroller, så du må flytte inne i verktøylinjen for å få tilgang til kontrollene i verktøylinjen.

Objektet som leses kalles navigasjonsobjektet.

Når du navigerer til et objekt, kan du se på innholdet i det ved hjelp av [tekstlesingskommandoer](#ReviewingText) når du er i [modus for objektlesing](#ObjectReview).
Som standard flyttes navigasjonsobjektet sammen med systemfokus, men denne oppførselen kan slås av og på.

Merk at punktskriften følger både [fokus](#SystemFocus) og [markør](#SystemCaret), så vel som objektnavigasjon og tekstlesing som standard.
Hvis du vil at den bare skal følge fokus og markør, må du [konfigurere punktskrift til å knyttes til](#BrailleTether) fokus. I dette tilfellet vil leselisten ikke følge objektnavigasjon og tekstlesing.

Om du vil at leselisten skal følge objektnavigasjon og tekstlesing i stedet, må du [konfigurere punktskrift til å knyttes til](#BrailleTether) lesing.

Ved objektnavigering bruker du følgende taster:
<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Berøring |Beskrivelse|
|---|---|---|---|---|
|Les gjeldende objekt |NVDA+Numerisk 5 |NVDA+Ctrl+o |ingen |Leser det gjeldende navigasjonsobjektet. Ved å trykke to ganger staves informasjonen, og trykker du tre ganger kopieres objektets navn og verdi til utklippstavlen.|
|Gå til innholdsobjektet |NVDA+Numerisk 8 |NVDA+Skift+Pil opp |Sveip opp (objektmodus) |Flytter til objektet som inneholder gjeldende navigasjonsobjekt|
|Gå til forrige objekt |NVDA+Numerisk 4 |NVDA+Skift+Pil venstre |Sveip mot venstre (objektmodus) |Flytter til objektet før den gjeldende navigasjonsobjektet|
|Gå til neste objekt |NVDA+Numerisk 6 |NVDA+Skift+Pil høyre |Sveip mot høyre (objektmodus) |Flytter til objektet etter gjeldende navigasjonsobjekt|
|Gå til første beholderobjekt |NVDA+Numerisk 2 |NVDA+Skift+Pil ned |Sveip ned (objektmodus) |Flytter til det første innholdsobjektet i det gjeldende navigasjonsobjektet|
|Gå til fokusobjekt |NVDA+Numerisk minus |NVDA+Slett bakover |ingen |Flytter til objektet som for øyeblikket har systemfokus, og plasserer også lesemarkøren i posisjonen for systemmarkøren, hvis den vises|
|Aktiver nåværende navigasjonsobjekt |NVDA+Numerisk Enter |NVDA+Enter |Dobbelttrykk |Aktiverer gjeldende navigasjonsobjekt (som å klikke med musen eller trykke mellomrom når den har systemfokus)|
|Flytt systemfokus eller markør til gjeldende leseposisjon |NVDA+Skift+Numerisk minus |NVDA+Skift+Slett bakover |ingen |Flytter systemfokus til gjeldende navigasjonsobjekt når kommandoen trykkes én gang. Trykkes kommandoen to ganger, flyttes systemmarkøren til posisjonen for lesemarkøren|
|Rapporter om lesemarkørens plassering |NVDA+Numerisk Del |NVDA+Del |ingen |Leser informasjon om tekst eller objekt ved lesemarkøren. Dette kan for eksempel omfatte hvor i dokumentet en er (i prosent), avstand fra kanten av arket eller eksakt skjermposisjon. Ved å trykke to ganger kan en få flere detaljer|

<!-- KC:endInclude -->

Merk: Numeriske taster (taster på talltastaturet) krever at NumLock-tasten er slått av for å fungere.

### Lese tekst {#ReviewingText}

NVDA lar deg lese innholdet [på skjermen](#ScreenReview), i gjeldende [dokument](#DocumentReview) eller i gjeldende [object](#ObjectReview) tegn for tegn, ord for ord eller linje for linje.

Dette er mest nyttig på steder (inkludert Windows ledetekst) der det ikke finnes [systemmarkør](#SystemCaret).
For eksempel kan du bruke den til å lese teksten i en lang informasjonmelding i en dialog.

Når du flytter lesemarkøren, følger systemmarkøren ikke med, slik at du kan se gjennom teksten uten å miste redigeringsposisjonen.
Men som standard følger lesemarkøren med når systemmarkøren beveger seg. Dette kan slås av og på.

Merk at leselisten følger [fokuset](#SystemFocus) og [markøren](#SystemCaret) som standard, i stedet for objektnavigasjon og tekstlesing.
Hvis du vil at den skal følge objektnavigasjon og tekstlesing i stedet, må du [konfigurere punktskrift til å knyttes til](#BrailleTether) lesing.

Følgende kommandoer er tilgjengelige for lesing av tekst:
<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Berøring |Beskrivelse|
|---|---|---|---|---|
|Gå til øverste linje i lesing |Skift+Numerisk 7 |NVDA+Ctrl+Home |ingen |Flytter lesemarkøren til øverste linje i teksten|
|Gå til forrige linje i lesing |Numerisk 7 |NVDA+Pil opp |bla opp (tekstmodus) |Flytter lesemarkøren til forrige tekstlinje|
|Les gjeldende linje i lesing |Numpad8 |NVDA+Skift+punktum |ingen |Les gjeldende tekstlinje der lesemarkøren er plassert. Ved å trykke to ganger staves linjen. Hvis du trykker tre ganger, staves linjen med tegnbeskrivelser.|
|Gå til neste linje i lesing |Numerisk 9 |NVDA+Pil ned |bla ned (tekstmodus) |Flytt lesemarkøren til neste tekstlinje|
|Gå til nederste linje i lesing |Skift+Numerisk 9 |NVDA+Ctrl+End |ingen |Flytter lesemarkøren til siste linje av teksten|
|Gå til forrige ord i lesing |Numerisk 4 |NVDA+Ctrl?Pil venstre |bla med to fingrer mot venstre (tekstmodus) |Flytter lesemarkøren til forrige ord i teksten|
|Les gjeldende ord i lesing |Numerisk 5 |NVDA+Ctrl+punktum |ingen |Les gjeldende ord i teksten der lesemarkøren er plassert. Ved å trykke to ganger staves ordet. Hvis du trykker tre ganger, staves ordet med tegnbeskrivelser.|
|Gå til neste ord i lesing |Numerisk 6 |NVDA+Ctrl+Pil høyre |bla med to fingrer mot høyre (tekstmodus) |Flytt lesemarkøren til neste ord i teksten|
|Gå til starten av linjen i lesing |Skift+Numerisk 1 |NVDA+Home |none |Flytter lesemarkøren til begynnelsen av linjen i teksten|
|Gå til forrige tegn i lesing |Numerisk 1 |NVDA+Pil venstre |bla mot venstre (tekstmodus) |Flytter lesemarkøren til forrige tegn på den gjeldende linjen i teksten|
|Les gjeldende tegn i lesing |Numerisk 2 |NVDA+punktum |ingen |Les gjeldende tegn på linjen der lesemarkøren er plassert. Ved å trykke to ganger leses en beskrivelse eller eksempel på det tegnet. Hvis du trykker tre ganger, leses den numeriske verdien av tegnet i desimal og heksadesimal.|
|Gå til neste tegn i lesing |Numerisk 3 |NVDA+Pil høyre |bla mot høyre (tekstmodus) |Flytter lesemarkøren til neste tegn på gjeldende linje i teksten|
|Gå til slutten av linjen i lesing |Skift+Numerisk 3 |NVDA+End |ingen |Flytter lesemarkøren til slutten av gjeldende linje i teksten|
|Si alle ved lesing |Numerisk pluss |NVDA+Skift+a |Bla ned med tre fingrer (tekstmodus) |Leser fra gjeldende posisjon av lesemarkøren, og følger under lesing|
|Velg og kopier fra lesemarkøren |NVDA+F9 |NVDA+F9 |ingen |Starter velg og kopier-prosessen fra den gjeldende posisjonen til lesemarkøren. Selve handlingen blir ikke utført før du forteller NVDA hvor slutten på det valgte tekstområdet er|
|Velg og kopier til lesemarkøren |NVDA+F10 |NVDA+F10 |ingen |Ved første trykk velges tekst fra det tidligere satte startmerket fram til og med gjeldende posisjon for lesemarkøren. Etter å ha trykket på tasten en gang til, vil teksten bli kopiert til utklippstavlen i Windows|
|Les tekstformatering |NVDA+f |NVDA+f |ingen |Les formateringen av teksten der lesemarkøren befinner seg. Ved å trykke to ganger vises informasjonen i nettmodus|

<!-- KC:endInclude -->

Merk: NUMPAD-taster krever at Numlock slås av for å fungere.

En god metode for å huske disse lesekommandoene når du bruker stasjonær modus, er å tenke på dem som et rutenett av tre og tre ruter. Fra topp til bunn er det linje, ord og tegn og fra venstre til høyre er det tidligere, gjeldende og neste.
Oppsettet er illustrert slik:

|Forrige linje |Gjeldende linje |Neste linje|
|Forrige ord |Gjeldende ord |Neste ord|
|Forrige tegn |Gjeldende tegn |Neste tegn|

### Lesemodi {#ReviewModes}

NVDAs [kommandoer for tekstlesing](#ReviewingText) kan vise innhold innenfor gjeldende navigasjonsobjekt, gjeldende dokument eller skjerm, avhengig av hvilket lesemodus som er valgt.
Lesemodi er en erstatning for det eldre konseptet Flat lesing i NVDA.
Følgende kommandoer veksler mellom lesemodi:
<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Berøring |Beskrivelse|
|---|---|---|---|---|
|Bytt til neste lesemodus |NVDA+numerisk 7 |NVDA+PageUp |bla opp med to fingrer |Bytter til neste tilgjengelige|

lesemodus |

|Bytt til forrige lesemodus |NVDA+numerisk 1 |NVDA+PageDown |bla ned med to fingrer |Bytter til forrige tilgjengelige lesemodus|

<!-- KC:endInclude -->

#### Objektlesing {#ObjectReview}

Når du er i objektlesemodus, vil du bare se innholdet i gjeldende [navigasjonsobjekt](#ObjectNavigation). For objekter som skrivbare tekstfelt eller andre tekstkontroller vil dette normalt være tekstinnholdet. For andre objekter kan dette være navnet og/eller verdien.

#### Dokumentlesing {#DocumentReview}

Når [navigasjonsobjektet](#ObjectNavigation) er i et dokument i nettmodus (som ei nettside) eller et annet komplekst dokument (som et OpenOffice-dokument), er det mulig å bytte til modus for dokumentlesing. I denne modusen kan du lese teksten i hele dokumentet.

Når du bytter fra objektlesing til dokumentlesing, blir lesemarkøren plassert i dokumentet i posisjonen for navigasjonsobjektet.

Når du flytter deg omkring i dokumentet med lesekommandoer, blir navigasjonsobjektet automatisk oppdatert til objektet som for øyeblikket finnes i posisjonen for lesemarkøren.

Merk at NVDA vil bytte automatisk fra objektlesing til dokumentlesing når du navigerer i dokumenter i nettmodus.

#### Skjermlesing {#ScreenReview}

Modus for skjermlesing lar deg lese teksten på skjermen slik den presenteres visuelt i det gjeldende programmet. Dette tilsvarer skjermlesing eller muspekerfunksjonalitet i mange andre skjermleserprogrammer for Windows.

Når du bytter til modus for skjermlesing, settes lesemarkøren i skjermposisjonen for det gjeldende [navigasjonsobjektet](#ObjectNavigation).

Når du flytter deg omkring i dokumentet med lesekommandoer, blir navigasjonsobjektet automatisk oppdatert til objektet som for øyeblikket finnes i skjermposisjonen for lesemarkøren.

Merk at i enkelte nyere programmer vil NVDA ikke kunne se teksten som vises på skjermen, enten hele teksten eller deler av den. Dette skyldes nyere teknologier for oppbygging av skjermbildet som det nå er umulig for NVDA å støtte.

### Navigere med musen {#NavigatingWithTheMouse}

Når du beveger musen, leser NVDA som standard den teksten som er under muspekeren når pekeren beveger seg over den.
Når dette er støttet, vil NVDA lese det omkringliggende tekstavsnittet, men enkelte kontroller kan bare leses som linje.

NVDA kan konfigureres til også å lese typen [objekt](#Objects) under musen når den beveger seg (f.eks liste, knapp, etc.). Dette kan være nyttig for helt blinde brukere, siden teksten i noen tilfeller ikke er nok.

NVDA gir brukerne en måte å forstå hvor musen er plassert i forhold til dimensjonene på skjermen ved å indikere muspekerens koordinater som pipelyder. Jo høyere musen er på skjermen, jo høyere på toneskalaen er pipene. Jo lenger til venstre eller høyre musen er plassert på skjermen, desto lenger til venstre eller høyre vil lyden bli avspilt (forutsatt at brukeren har stereohøyttalere eller hodetelefoner).

Disse ekstra musfunksjonene er ikke aktivert som standard i NVDA. Hvis du ønsker å dra nytte av dem, kan du konfigurere dem fra kategorien [Musinnstillinger](#MouseSettings), som finnes i innstillingsmenyen i NVDA.

Selv om en fysisk mus eller styreflate bør brukes til å navigere med musen, har NVDA noen få tastekommandoer knyttet til mus:
<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Beskrivelse|
|---|---|---|---|
|Klikk med venstre musknapp |Numerisk skråstrek |NVDA+PilVenstre |Klikker på venstre musknapp én gang. Dobbeltklikk kan utføres ved å trykke på denne tasten to ganger i rask rekkefølge|
|Lås venstre musknapp |Skift+Numerisk skråstrek |NVDA+Skift+Pil venstre |Låser venstre musknapp nede. Trykk igjen for å slippe den. Når du drar musen, trykker du denne tasten for å låse den venstre knappen nede og deretter flytte musen enten fysisk eller ved å bruke en av de andre kommandoene for flytting av musen|
|Klikk høyre musknapp |Numerisk stjerne |NVDA+Pil høyre |Klikker på høyre musknapp én gang.|
|Lås høyre musknapp |Skift+Numerisk stjerne |NVDA+Skift+Pil høyre |Låser høyre musknapp nede. Trykk igjen for å slippe den. Når du drar musen, trykker du denne tasten for å låse den høyre knappen nede og deretter flytte musen enten fysisk eller ved å bruke en av de andre kommandoene for flytting av musen|
|Flytt musen til gjeldende navigasjonsobjekt |NVDA+Numerisk skråstrek |NVDA+Skift+m |Flytter muspekeren til posisjonen til det gjeldende navigasjonsobjektet og lesemarkøren|
|Naviger til objektet under musen |NVDA+Numerisk stjerne |NVDA+Skift+n |Sett navigasjonsobjektet til objektet i posisjonen til muspekeren|

<!-- KC:endInclude -->

## Nettmodus {#BrowseMode}

Komplekse skrivebeskyttede dokumenter som nettsider leses i NVDA i det vi kaller nettmodus.
Dette gjelder dokumenter i Mozilla Firefox, Microsoft Internet Explorer, Mozilla Thunderbird, HTML-meldinger i Microsoft Outlook, Google Chrome, Adobe Reader og Adobe Flash. Du kan også velge å bruke nettmodus i Microsoft Word.

I nettmodus er innholdet i dokumentet tilgjengelig i en flat representasjon som du kan navigere i med piltastene som om det var et vanlig tekstdokument.
Alle NVDAs tastekommandoer for [systemmarkør](#SystemCaret) vil fungere i denne modusen, f.eks si alle, les formatering, tabellnavigeringskommandoene osv.
Informasjon som hvorvidt teksten er en lenke, overskrift, osv. blir opplyst sammen med teksten når du flytter deg rundt i dokumentet.

Noen ganger trenger du å kommunisere direkte med kontroller i disse dokumentene. For eksempel må du gjøre dette for redigerbare tekstfelt og lister, slik at du kan skrive tegn og bruke piltastene til å arbeide med kontrollen. Dette gjør du ved å bytte til fokusmodus, hvor nesten alle tastetrykk blir sendt til kontrollen.

I nettmodus vil NVDA som standard automatisk bytte til fokusmodus hvis du flytter til eller klikker på en kontroll som krever det.
Motsatt vil det å flytte til eller klikke på en kontroll som ikke krever fokusmodus bytte tilbake til nettmodus.
Du kan også trykke på Enter eller mellomrom for å bytte til fokusmodus i kontroller som krever det.
Ved å trykke escape byttes det tilbake til nettmodus.
I tillegg kan du manuelt aktivere fokusmodus. Den vil forbli aktiv inntil du velger å deaktivere den.

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Veksle mellom nett-/fokusmodus |NVDA+Space |Veksler mellom fokusmodus og nettmodus|
|Avslutt fokusmodus |Escape |Bytter tilbake til nettmodus hvis fokusmodus tidligere ble satt til automatisk|
|Oppdater nettmodusdokument |NVDA+F5 |Oppdaterer gjeldende dokumentinnhold (nyttig hvis vist innhold synes å mangle i dokumentet. Ikke tilgjengelig i Microsoft Word og Outlook.)|
|Finn |NVDA+Ctrl+f |Åpner en dialogboks der du kan skrive inn tekst du vil finne i det gjeldende dokumentet|
|Finn neste |NVDA+F3 |Finner neste forekomst av teksten i dokumentet som du tidligere søkte etter|
|Finn forrige |NVDA+Skift+F3 |Finner forrige forekomst av teksten i dokumentet som du tidligere søkte etter|
|Åpne lang beskrivelse |NVDA+d |Åpner et nytt vindu som inneholder en lang beskrivelse av elementet du er på, hvis det har en slik beskrivelse.|

<!-- KC:endInclude -->

### Enkeltbokstavnavigasjon {#SingleLetterNavigation}

For raskere navigasjon, tilbyr NVDA også enkelttegn-tastekommandoer for å hoppe til bestemte felt i dokumentet når en er i nettmodus.

Merk at ikke alle disse kommandoene støttes for alle typer dokumenter.

<!-- KC:beginInclude -->
Følgende taster brukt alene hopper til neste tilgjengelige element. Bruker du dem sammen med Skift-tasten, hjopper hopper de til forrige element:

* h: overskrift
* l: liste
* i: listeelement
* t: tabell
* k: lenke
* n: tekst uten lenke
* f: Skjemafelt
* u: ikke besøkt lenke
* v: besøkt lenke
* e: redigeringsfelt
* b: Knapp
* x: avkryssingsboks
* c: kombinasjonsboks
* r: radioknapp
* q: blokksitat
* s: separator
* m: ramme
* g: grafikk
* d: ARIA-landemerke
* o: innebygd objekt (lyd- og videospiller, program, dialog, etc.)
* 1 til 6: overskriftene på nivå 1 til 6
* a: merknad (kommentar, forfatterrevisjon, etc.)
* w: skrivefeil

For å gå til begynnelsen eller slutten av beholderelementer som lister og tabeller:

| Navn |Tast |Beskrivelse|
|---|---|---|
|Gå til begynnelsen av beholderen |Skift+komma |Flytter til begynnelsen av beholderen (liste, tabell, etc.) hvor markøren er plassert)|
|Flytt forbi slutten av beholderen |komma |Flytter forbi slutten av beholderen (liste, tabell, etc.) hvor markøren er plassert|

<!-- KC:endInclude -->

Noen nettapplikasjoner som Gmail, Twitter og Facebook bruker enkeltbokstaver som hurtigtaster. Hvis du ønsker å benytte disse mens du fortsatt vil bruke piltastene for å lese i nettmodus, kan du deaktivere kommandoene for enkeltbokstavnavigasjon i NVDA midlertidig.
<!-- KC:beginInclude -->
For å slå enkeltbokstavnavigasjon på eller av for gjeldende dokument, trykker du NVDA+Skift+Mellomrom.
<!-- KC:endInclude -->

### Elementlisten {#ElementsList}

Elementlisten gir tilgang til en liste over ulike typer elementer i dokumentet som er relevant i programmet. For eksempel kan listen i en nettleser liste lenker, overskrifter, skjemafelt, knapper eller landemerker.

Radioknapper lar deg bytte mellom de ulike elementtypene. Det er også et redigeringsfelt i dialogen som lar deg filtrere listen for å hjelpe deg å søke etter et bestemt element på siden. Når du har valgt et element, kan du bruke knappene i dialogboksen for å flytte til eller aktivere dette elementet.
<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Nettmodus elementliste |NVDA+F7 |Lister ulike typer elementer i det gjeldende dokumentet|

<!-- KC:endInclude -->

### Innebygde objekter {#ImbeddedObjects}

Sider kan inkludere rikt innhold ved hjelp av teknologier som Adobe Flash, Oracle Java og HTML5, så vel som applikasjoner og dialoger.
Når disse blir oppdaget i nettmodus, vil NVDA opplyse "innebygd objekt", "applikasjon" eller "dialog", ut fra hva som er relevant.
Du kan flytte deg raskt til dem med enkeltbokstavkommandoene o og Skift+o.
For å samhandle med disse objektene kan du trykke Enter på dem.

Hvis det er tilgjengelig, kan du deretter tabbe rundt i det og samhandle med det som i alle andre programmer.
En tastekommando er tilgjengelig for å gå tilbake til den opprinnelige siden som inneholder det innebygde objektet:
<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Gå til innhold i nettmodusdokument |NVDA+Ctrl+Mellomrom |Flytter fokus ut av det nåværende innebygde objektet, og inn i dokumentet som inneholder det|

<!-- KC:endInclude -->

## Lese matematisk innhold {#ReadingMath}

Ved hjelp av MathPlayer 4 fra Design Science kan NVDA lese og interaktivt navigere i matematisk innhold som støttes. Dette forutsetter at MathPlayer 4 er installert på PC-en.

MathPlayer er tilgjengelig som en gratis nedlasting fra: https://www.dessci.com/en/products/mathplayer/

NVDA støtter følgende typer matematisk innhold:

* MathML i Mozilla Firefox, Microsoft Internet Explorer og Google Chrome.
* Design Science MathType i Microsoft Word og PowerPoint. MathType må være installert for at dette skal fungere. Prøveversjonen er tilstrekkelig.
* MathML i Adobe Reader.
Merk at dette ikke er en offisiell standard ennå, så det finnes for tiden ingen offentlig tilgjengelig programvare som kan produsere dette innholdet.
* Matematikk i Kindle for PC for bøker med tilgjengelig matematikk.
Når du leser et dokument, vil NVDA uttale tilgjengelig matematisk innhold når det dukker opp. Bruker du leselist, vil matematisk innhold også bli vist i punktskrift.

++ Interaktiv navigasjon ++[InteractiveNavigation]
Om du arbeider primært med tale, vil du antakelig i de fleste tilfeller ønske å utforsske uttrykket i mindre segmenter, heller enn å høre hele uttrykket på én gang.

Hvis du er i nettmodus, kan du gjøre dette ved å flytte markøren til det matematiske innholdet og trykke Enter.

Om du ikke er i nettmodus:

1. Flytt lessemarkøren til det matematiske innholdet.
Som standard følger lesemarkøren systemmarkøren, så du kan normalt benytte systemmarkøren for å flytte til ønsket innhold.
1. Deretter aktiverer du følgende kommando:

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Samhandle med matematisk innhold |NVDA+Alt+m |Starter samhandling med matematisk innhold.|

<!-- KC:endInclude -->
Her kan du bruke MathPlayer-kommandoer, slik som piltastene, for å utforske uttrykket. For eksempel kan du flytte deg gjennom uttrykket ved hjelp av pil venstre og pil høyre, og du kan zoome deg inn på en del av uttrykket med pil ned.

Vennligst se [dokumentasjonen for MathPlayer om navigasjonskommandoer
https://www.dessci.com/en/products/mathplayer/navigation_commands.htm] for mer informasjon.

Når du ønsker å returnere til dokumentet, trykker du rett og slett på Escape-tasten.

## Punktskrift {#Braille}

Har du tilgang til en leselist, kan NVDA presentere informasjon i punktskrift. Om leselisten har et punktskrifttastatur, kan du også skrive inn uforkortet og forkortet punktskrift.

Vennligst se delen [Støttede leselister](#SupportedBrailleDisplays) for informasjon om leselistene NVDA har støtte for.

Du kan konfigurere punktskrift ved å bruke [Punktskrift-kategorien](#BrailleSettings) i [NVDAs Innstillinger-dialog](#NVDASettings).

### Forkortinger for kontrolltype, situasjon og landemerke {#BrailleAbbreviations}

For å få plass til så mye informasjon som mulig på ei leselist, har følgende forkortinger blitt definert. Disse angir så vel kontrolltype og situasjon som landemerker.

| Forkorting |Kontrolltype|
|---|---|
|prg |program|
|bsit |blokksitat|
|knp |knapp|
|ktknp |nedtrekksknapp|
|snrknp |snurreknapp|
|splknp |splittknapp|
|bknp |bytteknapp|
|kbo |kombinasjonsboks|
|avk |avkryssingsboks|
|dlg |dialog|
|dok |dokument|
|red |redigerbart tekstfelt|
|pored |redigerbart passordfelt|
|innbgd |innebygd objekt|
|slnot |sluttnotat|
|fnot |fotnote|
|gr |grafikk|
|grp |gruppe|
|hN |overskrift på nivå N, f.eks. h1, h2.|
|hjlp |hjelpeballong|
|lmk |landemerke|
|lnk |lenke|
|blnk |besøkt lenke|
|lst |liste|
|mny |meny|
|mnyln |menylinje|
|mnyknp |menyknapp|
|me |menyelement|
|pnl |panel|
|fdr |framdriftsindikator|
|rknp |radioknapp|
|rlflt |rullefelt|
|del |del|
|stln |statuslinje|
|fktrl |fanekontroll|
|tbl |tabell|
|cN |tabellkolonne nummer N, f.eks. c1, c2.|
|rN |tabellrad nummer N, f.eks. r1, r2.|
|term |terminal|
|vkln |verktøylinje|
|vktps |verktøytips|
|tv |trevisning|
|tvknp |trevisningsknapp|
|tve |trevisningselement|
|lv N |et trevisningselement har et hierarkisk nivå N||
|vd |vindu|
|| separator|

Følgende situasjonsindikatorer er også definert:

| Forkorting |Kontrollsituasjon|
|---|---|
|... |Vist når et objekt har støtte for autofullfør|
|| vist når et objekt (f.eks. en bytteknapp) blir trykket på|
|| vist når et objekt (f.eks. en bytteknapp) ikke blir trykket på|
|| vist når et objekt (f.eks. en avkryssingsboks) er avkrysset|
|| vist når et objekt (f.eks. en avkryssingsboks) er halvveis avkrysset|
|| vist når et objekt (f.eks. en avkryssingsboks) ikke er avkrysset|
|- |vist når et objekt (f.eks. et element i en trevisning) er sammentrekkbart|
|+ |vist når et objekt (f.eks. et element i en trevisning) er utvidbart|
|*** |vist når en beskyttet kontroll eller et beskyttet dokument blir oppdaget|
|klk |vist når et objekt er klikkbart|
|kmnt |vist når det er en kommentar til en celle i et regneark eller del av en tekst i et dokument|
|frml |vist når det er en formel i en regnearkcelle|
|ugyldig |vist når det er gjort en ugyldig oppføring|
|lbskr |vist når et objekt (vanligvis en grafikk)) har en lang beskrivelse|
|mln |vist når et redigeringsfelt tillater skriving av flere tekstlinjer, som kommentarfelt på nettsider|
|pkrv |vist når et påkrevd skjemafelt blir funnet|
|skrbsk |vist når et objekt (for eksempel et redigerbart tekstfelt) er skrivebeskyttet|
|vlg |vist når et objekt er valgt|
|ivlg |vist når et objekt ikke er valgt|
|sort stig |vist når et objekt er sortert i stigende rekkefølge|
|sort synk |vist når et objekt er sortert i synkende rekkefølge|
|umny |vist når et objekt har en sprettopp (vanligvis en undermeny)|

Til slutt er følgende forkortinger for landemerker definert:

| Forkorting |Landemerke|
|---|---|
|bnr |banner|
|iinf |innholdsinfo|
|kmpl |komplementær|
|skjm |skjema|
|hoved |hoved|
|nav |navigasjon|
|søk |søk|
|rgn |region|

### Skrive punktskrift {#BrailleInput}

NVDA støtter skriving av både uforkortet og forkortet punktskrift via et punktskrifttastatur.

Du kan velge oversettingstabellen som oversetter fra punktskrift til tekst ved hjelp av innstillingen [inndatatabell](#BrailleSettingsInputTable) i kategorien Punktskrift som du finner i [NVDAs Innstillinger](#NVDASettings)-dialog.
Skriver du uforkortet punktskrift, settes teksten inn så snart den er skrevet. Skriver du forkortet punktskrift, settes teksten inn så snart du trykker mellomrom eller Enter når du har skrevet et ord.

Legg merke til at oversettingen bare gjelder ordet du skriver i punktskrift, og ikke omfatter eksisterende tekst. Hvis du for eksempel benytter en punktskrifttabell som begynner tall med talltegn og du flytter markøren til slutten av et tall, vil du måtte skrive talltegn igjen for å skrive flere tall.

<!-- KC:beginInclude -->
Et trykk på punkt 7 sletter sist skrevne punktskriftcelle eller bokstav.
Punkt 8 oversetter skrevet punktskrift og trykker Enter-tasten.
Ved å trykke punkt 7 og 8 oversettes skrevet punktskrift, men uten å legge til et mellomrom eller trykke Enter.
<!-- KC:endInclude -->

## Gjenkjenning av innhold {#ContentRecognition}

Når forfattere ikke bidrar med tilstrekkelig informasjon til at en skjermleserbruker skal kunne finne ut av innholdet i noe, kan ulike verktøy brukes for å forsøke å gjenkjenne innholdet i et bilde.

NVDA støtter funksjonaliteten for optisk tegngjenkjenning (OCR) som er bygd inn i Windows 10 for å gjenkjenne tekst fra bilder. Det finnes også verktøy for gjenkjenning av innhold i NVDA-tillegg.

Når du bruker en kommando for innholdsgjenkjenning, gjenkjenner NVDA innholdet fra gjeldende [navigasjonsobjekt](#ObjectNavigation).

Som standard følger navigasjonsobjektet systemfokus eller markøren i nettmodus, så du kan vanligvis bare flytte fokus eller nettmodusmarkøren slik du vil. Hvis du for eksempel flytter nettmodusmarkøren til en grafikk, vil gjenkjenningsverktøyet gjenkjenne innholdet fra grafikken som standard. Imidlertid ønsker du kanskje å kunne bruke objektnavigasjon direkte for å eksempelvis gjenkjenne innholdet i et helt programvindu.

Så snart gjenkjenning er fullført, vil resultatet bli vist i et dokument tilsvarende nettmodus, slik at du kan lese innholdet ved hjelp av piltastene etc.

Et trykk på mellomrom eller Enter vil aktivere (normalt klikke) på teksten under markøren hvis mulig.

Et trykk på Escape forkaster gjenkjenningsresultatet.

### Windows 10 OCR {#Win10Ocr}

Windows 10 inkluderer OCR for mange språk. NVDA kan bruke dette til å gjenkjenne tekst fra bilder eller utilgjengelige programmer.

Du kan sette språket som skal brukes for tekstgjenkjenning i kategorien [Windows 10 OCR](#Win10OcrSettings) i dialogen for [innstillinger i NVDAs](#NVDASettings).

Du kan legge til flere språk ved å åpne Startmenyen, velge Innstillinger, velge Tid & språk, deretter velge Region & språk og til slutt velge Legg til språk.

<!-- KC:beginInclude -->
For å gjenkjenne teksten i gjeldende navigasjonsobjekt med Windows 10 OCR: Trykk NVDA+r.
<!-- KC:endInclude -->

## Applikasjonsspesifike funksjoner {#ApplicationSpecificFeatures}

NVDA tilbyr sine egne ekstra funksjoner for enkelte programmer for å gjøre visse oppgaver enklere eller for å gi tilgang til funksjonalitet som ellers ikke er tilgjengelig for brukere med skjermleser.

### Microsoft Word {#MicrosoftWord}
#### Automatisk lesing av kolonne- og radoverskrifter {#WordAutomaticColumnAndRowHeaderReading}

NVDA er i stand til å annonsere relevante rad- og kolonneoverskrifter automatisk når en navigerer i tabeller i Microsoft Word. Dette krever først og fremst at valget Rapporter rad- og kolonneoverskrifter i tabeller er slått på. Dette valget finner du under Innstillinger for dokumentformatering i [Innstillinger](#NVDASettings)-dialogen i NVDA. Dernest må NVDA vite hvilken rad eller kolonne som inneholder overskriftene i en angitt tabell.

Etter at du har flyttet til første celle i kolonnen eller raden som inneholder overskriftene, bruker du en av følgende kommandoer:

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Sett kolonneoverskrifter |NVDA+Skift+c |Trykker du kommandoen én gang, forteller du NVDA at dette er første overskriftscelle på raden som inneholder kolonneoverskrifter som skal annonseres automatisk når du flytter mellom kolonner nedenfor denne raden. Trykker du to ganger, fjerner du denne innstillingen.|
|Sett radoverskrifter |NVDA+Skift+r |Trykker du kommandoen én gang, forteller du NVDA at dette er første overskriftscelle i kolonnen som inneholder radoverskrifter som skal|

annonseres automatisk når du flytter mellom rader etter denne kolonnen. Trykker du to ganger, fjerner du denne innstillingen. |
<!-- KC:endInclude -->

Disse innstillingene blir lagret i dokumentet som bokmerker, som er kompatible med andre skjermleserprogrammer som JAWS.

Dette betyr at brukere av andre skjermlesere som åpner dokumentet på et seinere tidspunkt allerede har kolonne- og radoverskrifter automatisk definert.

#### Nettmodus i Microsoft Word {#BrowseModeInMicrosoftWord}

Akkurat som på Internett, kan nettmodus også brukes i Microsoft Word for at du skal kunne bruke funksjoner som Hurtignavigasjon og Elementlisten.

<!-- KC:beginInclude -->
For å slå Nettmodus på og av i Microsoft Word, trykker du NVDA+mellomrom.
<!-- KC:endInclude -->

For mer informasjon om Nettmodus og Hurtignavigasjon, kan du se delen om [Nettmodus](#BrowseMode).

##### Elementlisten {#WordElementsList}

<!-- KC:beginInclude -->
Når du er i Nettmodus i Microsoft Word, får du tilgang til Elementlisten ved å trykke NVDA+f7.
<!-- KC:endInclude -->
Elementlisten kan liste overskrifter, lenker, merknader (som inkluderer kommentarer og sporendringer) og feil (for tiden begrenset til stavefeil).

#### Rapportering av kommentarer {#WordReportingComments}

<!-- KC:beginInclude -->
For å få lest eventuelle kommentarer i gjeldende markørposisjon, trykker du NVDA+Alt+c.
<!-- KC:endInclude -->
Alle kommentarer i dokumentet, sammen med andre sporede endringer, kan også listes i NVDAs elementliste når du velger Merknader som type.

### Microsoft Excel {#MicrosoftExcel}
#### Automatisk lesing av kolonne- og radoverskrifter {#ExcelAutomaticColumnAndRowHeaderReading}

NVDA er i stand til å annonsere relevante rad- og kolonneoverskrifter automatisk når en navigerer i arbeidsark i Microsoft Excel. Dette krever først og fremst at valget Rapporter rad- og kolonneoverskrifter i tabeller er slått på. Dette valget finner du under Innstillinger for dokumentformatering i [Innstillinger](#NVDASettings)-dialogen i NVDA. Dernest må NVDA vite hvilken rad eller kolonne som inneholder overskriftene.

Etter at du har flyttet til første celle i kolonnen eller raden som inneholder overskriftene, bruker du en av følgende kommandoer:

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Sett kolonneoverskrifter |NVDA+Skift+c |Trykker du kommandoen én gang, forteller du NVDA at dette er første overskriftscelle på raden som inneholder kolonneoverskrifter som skal annonseres automatisk når du flytter mellom kolonner nedenfor denne raden. Trykker du to ganger, fjerner du denne innstillingen.|
|Sett radoverskrifter |NVDA+Skift+r |Trykker du kommandoen én gang, forteller du NVDA at dette er første overskriftscelle i kolonnen som inneholder radoverskrifter som skal|

annonseres automatisk når du flytter mellom rader etter denne kolonnen. Trykker du to ganger, fjerner du denne innstillingen. |
<!-- KC:endInclude -->

Disse innstillingene blir lagret i arbeidsboka som definerte navneområder, som er kompatible med andre skjermleserprogrammer som JAWS.

Dette betyr at brukere av andre skjermlesere som åpner arbeidsboka på et seinere tidspunkt allerede har kolonne- og radoverskrifter automatisk definert.

##### Elementlisten {#ExcelElementsList}

Akkurat som på nettet, har NVDA en elementliste for Microsoft Excel som lar deg liste og få tilgang til ulike typer informasjon.

<!-- KC:beginInclude -->
For å få tilgang til Elementlisten i Excel, trykker du NVDA+F7.
<!-- KC:endInclude -->

Disse typene informasjon er tilgjengelige i Elementlisten:

* Diagrammer: Dette lister alle diagrammer i det aktive arbeidsarket.
Du kan velge et diagram og trykke Enter eller Gå til-knappen for å sette fokus på diagrammet. Deretter kan du navigere i det og lese det ved hjelp av piltastene.
* Kommentarer: Dette lister alle celler i gjeldende arbeidsark som inneholder kommentarer.
Cellens adresse sammen med kommentaren(e) vises for hver celle. Trykker du Enter eller Gå til-knappen når du er på en listet kommentar, vil du gå direkte til cellen.
* Formler: Dette lister alle celler i arbeidsarket som inneholder en formel.
Cellens adresse sammen med dens formel vises for hver celle. Trykker du Enter eller Gå til-knappen når du er på en listet formel, vil du gå direkte til cellen.
* Ark: Dette lister alle ark i arbeidsboka.
Trykk F2 når du er på et ark for å gi arket et nytt navn.
Trykker du Enter eller Gå til-knappen når du er på et listet ark, vil du bytte til dette arket.
* Skjemafelt: Dette lister alle skjemafelt i det aktive arbeidsarket.
For hvert skjemafelt viser Elementlisten den alternative teksten for feltet sammen med adressene for feltene det dekker.
Velger du et skjemafelt og trykker Enter eller Gå til-knappen på det, flytter du til dette feltet i nettmodus.

#### Rapportere kommentarer {#ExcelReportingComments}

<!-- KC:beginInclude -->
For å få lest eventuelle kommentarer i gjeldende celle med fokus, trykker du NVDA+Alt+c.
<!-- KC:endInclude -->

Alle kommentarer i arbeidsarket kan også listes i NVDAs elementliste.

#### Lese beskyttede celler {#ExcelReadingProtectedCells}

Hvis en arbeidsbok har blitt beskyttet, kan det være umulig å flytte fokus til bestemte celler som har blitt låst for redigering.
<!-- KC:beginInclude -->
For å tillate flytting til låste celler, bytter du til nettmodus ved å trykke NVDA+mellomrom, og deretter bruker du standard forflytningskommandoer i Excel
som piltastene til å flytte omkring til alle celler i gjeldende arbeidsark.
<!-- KC:endInclude -->

#### Skjemafelt {#ExcelFormFields}

Arbeidsark i Excel kan omfatte skjemafelt. Du får tilgang til disse via Elementlisten, eller ved hjelp av kommandoene f og Skift+f, som er enkeltbokstavs navigasjonskommandoer for skjemafelt.

Når du flytter til et skjemafelt i nettmodus, kan du trykke Enter eller mellomrom for enten å aktivere det eller bytte til fokusmodus, slik at du kan samhandle med det, avhengig av kontrollen.

For mer informasjon om nettmodus og enkeltbokstavnavigasjon, viser vi til delen [Nettmodus](#BrowseMode).

### Microsoft PowerPoint {#MicrosoftPowerPoint}

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Slå på/av lesing av foredragsholders notater |Ctrl+Skift+s |Når du kjører en presentasjon, vil denne kommandoen bytte mellom foredragsholders notater for gjeldende bilde og innholdet i bildet. Dette påvirker bare det NVDA leser, og ikke det som vises på skjermen.|

<!-- KC:endInclude -->

### Foobar2000 {#Foobar2000}

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Les gjenværende tid |Ctrl+Skift+r |Leser gjenværende tid for sporet som spilles nå, hvis noe.|
|Les brukt tid |Ctrl+Skift+e |Leser brukt tid for sporet som spilles nå, hvis noe.|
|Les sporlengde |Ctrl+Skift+t |Leser lengden for sporet som spilles nå, hvis noe.|

<!-- KC:endInclude -->

Merk at hurtigtastene ovenfor bare fungerer med standard formateringsstreng for foobar sin statuslinje.

### Miranda IM {#MirandaIM}

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Les siste melding |NVDA+Ctrl+1-4 |Leser en av de siste meldingene, avhengig av tallet trykket. F.eks vil NVDA+Ctrl+2 lese nest nyeste melding.|

<!-- KC:endInclude -->

### Poedit {#Poedit}

<!-- KC:beginInclude -->

| Navn |Tast |Beskrivelse|
|---|---|---|
|Les Kommentarvinduet |Ctrl+Skift+c |Leser eventuelle kommentarer i kommentarvinduet.|
|Les merknader for oversettere |Ctrl+Skift+a |Leser eventuelle merknader for oversettere.|

<!-- KC:endInclude -->

### Skype {#Skype}

<!-- KC:beginInclude -->
Når du er i en samtale:

| Navn |Tast |Beskrivelse|
|---|---|---|
|Les melding |NVDA+Ctrl+1-0 |Leser og flytter lesemarkøren til en nylig melding, avhengig av tallet som er trykket; f.eks. vil NVDA+Ctrl+2 lese nest nyeste melding.|

<!-- KC:endInclude -->

### Kindle for PC {#Kindle}

NVDA støtter lesing av og navigering i bøker i Amazon Kindle for PC. Denne funksjonaliteten er bare tilgjengelig med bøker merket med "Screen Reader: Supported", og dette kan du sjekke på detaljsiden for boka.

Nettmodus benyttes for å lese boka. Dette slås på automatisk når du åpner en bok eller setter fokus på bokområdet.

Bytting av side vil skje automatisk når du flytter markøren eller bruker Si alt-kommandoen.
<!-- KC:beginInclude -->
Du kan manuelt bla til neste side med pageDown-tasten og til forrige side med pageUp-tasten.
<!-- KC:endInclude -->

Enkeltbokstavnavigasjon støttes for lenker og grafikker, men bare innenfor gjeldende side.
Navigering på lenker omfatter også fotnoter.

NVDA tilbyr tidlig støtte for lesing og interaktiv navigasjon av matematisk innhold for bøker med tilgjengelig matematikk.

Vennligst se delen [Lese matematisk innhold](#ReadingMath) for mer informasjon.

#### Tekstvalg {#KindleTextSelection}

Kindle lar deg utføre ulike funksjoner på valgt tekst, som å få en ordlistedefinisjon,
legge til notater og markeringer, kopiere teksten til utklippstavlen og søke på nettet.
For å gjøre dette, må du først velge tekst, slik du normalt ville gjort i nettmodus; f.eks. ved å bruke Skift og piltastene.
<!-- KC:beginInclude -->
Så snart du har valgt tekst, trykker du applikasjonstasten eller Skift+F10 for å se tilgjengelige valg for å arbeide med utvalget.
<!-- KC:endInclude -->

Om du gjør dette uten å ha valgt tekst, vil valg bli vist for ordet under markøren.

#### Brukernotater {#KindleUserNotes}

Du kan legge til et notat angående et ord eller en tekstpassasje. For å gjøre dette, velger du først relevant tekst og går til alternativene for utvalget, som beskrevet ovenfor. Velg deretter Legg til notat.

Når du leser i nettmodus, vil NVDA referere til disse notatene som kommentarer.

For å se på, redigere eller slette et notat:

1. Flytt markøren til teksten som inneholder notatet.
1. Gå til alternativene for utvalget som beskrevet ovenfor.
1. Velg Rediger notat.

### Azardi {#Azardi}

<!-- KC:beginInclude -->
Når du er i tabellvisningen over bøker som er lagt til:

| Navn |Tast |Beskrivelse|
|---|---|---|
|Enter |Enter |Åpner valgt bok.|
|Kontekstmeny |applikasjonstasten |Åpner kontekstmenyen for den valgte boka.|

<!-- KC:endInclude -->

## Konfigurere NVDA {#ConfiguringNVDA}

Det meste av konfigureringen kan gjøres ved hjelp av dialogbokser som du får tilgang til via undermenyen Preferanser i NVDA-menyen.

Mange av disse innstillingene finner du i dialogen [Innstillinger i NVDA](#NVDASettings).

I alle dialogbokser trykker du på knappen OK for å akseptere eventuelle endringer du har gjort. For å avbryte eventuelle endringer trykker du på knappen Avbryt eller på Escape-tasten.

I noen dialoger kan du trykke på knappen Bruk for at innstillingene skal tas i bruk umiddelbart, uten å lukke dialogen.

Noen innstillinger kan også endres ved hjelp av hurtigtaster. Disse er oppgitt, der det er relevant, i delene nedenfor.

### NVDA-innstillinger {#NVDASettings}

<!-- KC:settingsSection: || Navn | Stasjonær tast | Bærbar tast | Beskrivelse | -->
NVDAs innstillingsdialog inneholder mange konfigurasjonsparametre som kan endres.

Denne dialogen inneholder en liste med flere kategorier med innstillinger du kan velge fra.

Når du velger en kategori, vil flere innstillinger knyttet til denne kategorien bli vist i dialogen. Disse innstillingene kan tas i bruk ved å trykke på knappen Bruk, og dialogen blir da stående åpen.

Vil du lagre innstillingene dine og lukke innstillingsdialogen, kan du trykke på OK-knappen.

Noen innstillingskategorier har tilordnede hurtigtaster. Trykker du på en slik hurtigtast, blir NVDAs innstillingsdialog åpnet i nettopp den kategorien du har valgt.

Som standard kan du ikke nå alle kategorier med hurtigtastkommandoer.

Ønsker du å få tilgang til kategorier som ikke har en tilordnet hurtigtast, kan du benytte dialogen [Inndatabevegelser](#InputGestures) for å legge til en tilpasset bevegelse som en tastaturkommando eller berøringsbevegelse for den kategorien.

Innstillingskategoriene som du finner i innstillingsdialogen i NVDA blir beskrevet nedenfor.

#### Generelt (NVDA+Ctrl+g) {#GeneralSettings}

Kategorien Generelt i NVDAs innstillingsdialog inneholder valg for NVDAs generelle oppførsel, som hvilket språk som skal benyttes i grensesnittet og om NVDA skal se etter oppdateringer.

Denne kategorien inneholder disse valgene:

##### Språk {#GeneralSettingsLanguage}

Dette er en kombinasjonsboks som lar deg velge språket som NVDAs brukergrensesnitt og meldinger skal vises i. Det er mange språk å velge mellom, men standardvalg er "Brukerstandard, Windows". Denne innstillingen ber NVDA bruke språket som for øyeblikket er valgt i Windows.

Legg merke til at NVDA må startes på nytt når språket endres. NVDA vil spørre deg om du ønsker å starte NVDA på nytt hvis du endrer innstillingen, og lagre endringene dine.

Trykk på OK, og NVDA vil starte på nytt.

##### Lagre konfigurasjon ved avslutning {#GeneralSettingsSaveConfig}

Denne innstillingen er en avkryssingsboks som, hvis den er avkrysset, vil be NVDA lagre gjeldende konfigurasjon automatisk når du avslutter NVDA.

##### Vis avslutningsalternativer når NVDA avsluttes {#GeneralSettingsShowExitOptions}

Dette valget er en avkryssingsboks som lar deg velge om det skal vises en dialog med spørsmål om hvilken handling du vil utføre når du avslutter NvDA.
Om du setter kryss her, vil en dialog dukke opp når du forsøker å avslutte NVDA. Den vil spørre deg om du ønsker å avslutte, starte på nytt, starte på nytt med tillegg deaktivert, eller installere ventende oppdateringer (hvis noen finnes).

Lar du avkryssingsboksen stå tom, vil NVDA avslutte umiddelbart uten spørsmål.

##### Spill av lyd når NVDA startes eller avsluttes {#GeneralSettingsPlaySounds}

Dette valget er en avkryssingsboks som, hvis den er avkrysset, ber NVDA spille av lyder når den startes eller avsluttes.

##### Loggnivå {#GeneralSettingsLogLevel}

Dette er en kombinasjonsboks som lar deg avgjøre hvor mye NVDA logger når den kjører.

Generelt bør ikke brukerne ha behov for å endre denne innstillinger, siden ikke for mye blir logget som standard. Skulle du som bruker likevel ønske å logge mer informasjon, for eksempel i forbindelse med en feilrapport, kan denne innstillingen være nyttig.

##### Start NVDA automatisk når jeg har logget inn i Windows {#GeneralSettingsStartAfterLogOn}

Hvis dette valget er slått på, vil NVDA starte automatisk så snart du har logget inn i Windows.

Dette valget er bare tilgjengelig i installerte kopier av NVDA.

##### Bruk NVDA i innloggingsvinduet i Windows (krever administratorrettigheter) {#GeneralSettingsStartOnLogOnScreen}

Slå på dette valget hvis du logger inn i Windows ved å oppgi brukernavn og passord, og behøver skjermleserstøtte i innloggingsvinduet. Da vil NVDA starte automatisk i innloggingsvinduet når Windows starter.

Dette valget er bare tilgjengelig i installerte kopier av NVDA.

##### Bruk gjeldende lagrede innstillinger i innloggingsvinduet og på andre sikre skjermer (krever administratorrettigheter {#GeneralSettingsCopySettings}

Ved å trykke på denne knappen kopieres de gjeldende lagrede brukerinnstillingene i NVDA til NVDAs mappe for systeminnstillinger. NVDA vil da benytte disse innstillingene når NVDA kjøres i innloggingsvinduet, i dialogen for brukerkontokontroll og på andre sikre skjermer i Windows.

For å være sikker på at alle innstillinger dine blir overført, bør du først lagre innstillingene ved enten å trykke NVDA+Ctrl+c eller velge Lagre innstillinger i NVDA-menyen.

Dette valget er bare tilgjengelig i installerte kopier av NVDA.

##### Se etter oppdateringer for NVDA automatisk {#GeneralSettingsCheckForUpdates}

Hvis dette er slått på, vil NVDA automatisk se etter oppdaterte versjoner av NVDA og fortelle deg det hvis en oppdatering er tilgjengelig.

Du kan også se etter oppdateringer manuelt. Det gjør du ved å velge Se etter oppdateringer under Hjelp i NVDA-menyen.

Når NVDA ser etter oppdateringer, manuelt eller automatisk, må NVDA sende litt informasjon til oppdateringsserveren for å kunne motta riktig oppdatering til systemet ditt. Følgende informasjon blir alltid sendt:

* Gjeldende versjon av NVDA
* Versjon av operativsystemet
* Om operativsystemet er 64- eller 32-biters

##### La NVDA-prosjektet få tilgang til bruksstatistikk for NVDA {#GeneralSettingsGatherUsageStats}

Hvis dette er aktivert, vil NV Access benytte informasjon fra Se etter oppdateringer for å spore antallet brukere, inkludert visse demografiske verdier slik som operativsystem og opprinnelsesland.
Vær oppmerksom på at selv om din IP-adresse vil bli brukt til å avgjøre landet ditt under oppdateringssjekken, blir aldri IP-adressen beholdt.
Bortsett fra informasjonen som er påkrevd for å se etter oppdateringer, sendes også følgende ekstra informasjon:

* Språket som brukes i NVDAs grensesnitt
* Om denne kopien av NVDA er flyttbar eller installert
* Navnet på gjeldende talesyntese som er i bruk (inkludert navnet på tillegget driveren kommer fra)
* Navnet på gjeldende leselist som er i bruk (inkludert navnet på tillegget driveren kommer fra)
* Gjeldende punktskrifttabell for utdata (hvis punktskrift benyttes)

Denne informasjonen hjelper NV Access i stor grad med å prioritere framtidig utvikling av NVDA.

##### Varsle om ventende oppdatering ved oppstart {#GeneralSettingsNotifyPendingUpdates}

Hvis dette er slått på, vil NVDA si ifra ved oppstart når det finnes en ventende oppdatering. Du får også et valg om å installere den.

Du kan også installere en ventende oppdatering selv fra Avslutt NVDA-dialogen (hvis aktivert), fra NVDA-menyen eller når du ser etter en oppdatering fra Hjelp-menyen.

#### Taleinnstillinger (NVDA+Ctrl+v) {#SpeechSettings}

Kategorien Tale i NVDAs innstillingsdialog inneholder valg som lar deg endre både talesyntese og stemmekarakteristika for den valgte talesyntesen.

Ønsker du en raskere, alternativ måte for å kunne kontrollere stemmeparametre fra hvor som helst, bør du se på delen [Innstillingsring for talesyntese](#SynthSettingsRing).

Kategorien Taleinnstillinger inneholder følgende valg:

##### Velg talesyntese {#SpeechSettingsChange}

Det første valget i kategorien Taleinnstillinger er knappen Endre ... Med denne knappen aktiverer du dialogen [Velg talesyntese](#SelectSynthesizer), der du kan velge aktiv talesyntese og enhet for utdata.

Denne dialogen åpnes oppå innstillingsdialogen i NVDA.

Når du lagrer eller avbryter innstillingene i Velg talesyntese, går du tilbake til NVDAs innstillingsdialog.

##### Stemme {#SpeechSettingsVoice}

Stemmevalget er en kombinasjonsboks som lister alle stemmene i gjeldende talesyntese som du har installert.

Du kan bruke piltastene for å lytte til alle tilgjengelige stemmer. Pil venstre og pil opp bringer deg oppover i listen, mens pil høyre og pil ned bringer deg nedover.

##### Variant {#SpeechSettingsVariant}

Hvis du benytter talesyntesen eSpeak NG som leveres som del av NvDA, er dette en kombinasjonsboks som lar deg velge varianten talesyntesen skal snakke med.
eSpeak NG sine varianter ligner ganske mye på stemmer, i det at de tilbyr litt ulike attributter til stemmen i eSpeak NG.

Noen varianter vil høres ut som en mann, noen som en kvinne, og noen vil til og med høres ut som en frosk.

##### Hastighet {#SpeechSettingsRate}

Dette valget vil la deg endre hastigheten på talen.

Dette er en glidebryter som går fra 0 til 100, der 0 er langsomst, og 100 hurtigst.

##### Tonehøyde {#SpeechSettingsPitch}

Dette valget lar deg endre tonehøyden - stemmeleiet - til den gjeldende stemmen.

Dette er en glidebryter som går fra 0 til 100, der 0 er laveste tonehøyde og 100 det høyeste.

##### Lydnivå {#SpeechSettingsVolume}

Dette er en glidebryter som går fra 0 til 100, der 0 er laveste volum, og 100 det høyeste.

##### Bøyning {#SpeechSettingsInflection}

Dette valget er en skyvebryter som lar deg velge hvor mye bøyning (stigning og fall i tonehøyde) du ønsker at talesyntesen skal snakke med. (Den eneste talesyntesen som tilbyr denne funksjonen nå, er eSpeak NG.)

##### Skift språk automatisk {#SpeechSettingsLanguageSwitching}

Denne avkryssingsboksen lar deg avgjøre om NVDA skal skifte talesyntesespråk automatisk hvis teksten som lesess, spesifiserer språket sitt.

Denne funksjonen er slått på som standard.

For tiden er det bare eSpeak NG som støtter automatisk språkskifte.

##### Skift dialekt automatisk {#SpeechSettingsDialectSwitching}

Denne avkryssingsboksen lar deg avgjøre hvorvidt endringer i dialekt skal gjøres, og ikke bare skifte av språk.

Om du for eksempel leser med amerikansk engelsk, men dokumentet ditt spesifiserer at noe av teksten er på britisk engelsk, vil talesyntesen bytte aksent dersom dette valget er slått på.

Dette valget er slått av som standard.

<!-- KC:setting -->

##### Nivå for tegnsetting/symbol {#SpeechSettingsSymbolLevel}

Tast: NVDA+p

Dette lar deg velge nivå for tegnsetting og andre symboler som skal uttales som ord.

Eksempel: Om "alle" er valgt, vil samtlige symboler bli uttalt som ord.

Dette valget gjelder for samtlige talesynteser, ikke bare for den som er aktiv for øyeblikket.

##### Stol på stemmens språk ved behandling av tegn og symboler {#SpeechSettingsTrust}

Dette valget forteller NVDA hvorvidt NVDA skal stole på språket til gjeldende stemme ved behandling av symboler og bokstaver. Valget er slått på som standard.

Finner du ut at NVDA leser tegnsetting på feil språk for en bestemt talesyntese eller stemme, kan det være du vil slå av dette valget for å tvinge NVDA til å bruke den globale språkinnstillingen sin i stedet.

##### Tonehøydeendring for stor bokstav i prosent {#SpeechSettingsCapPitchChange}

Dette redigeringsfeltet lar deg skrive inn verdien stemmen vil endre tonehøyden med når stor bokstav uttales.

Verdien er en prosentverdi, der en negativ verdi reduserer tonehøyden og en positiv verdi øker den.

Vil du ikke ha noen tonehøydeendring, bør du la verdien være 0.

##### Si "stor" før store bokstaver {#SpeechSettingsSayCapBefore}

Dette valget er en avkryssingsboks som, når den er avkrysset, gjør at NVDA sier ordet "stor" før en stor bokstav. Dette gjelder når bokstavene uttales individuelt, som ved staving.

Normalt øker NVDA tonehøyden litt for stor bokstav, men noen talesynteser støtter ikke dette helt godt. I slike tilfeller kan dette valget kanskje være nyttig.

##### Pip for store bokstaver {#SpeechSettingsBeepForCaps}

Hvis denne avkryssingsboksen er avkrysset, vil NVDA lage et lite pip hver gang den oppdager en stor bokstav for seg selv.

Som med avkryssingsboksen "Si "stor" før store bokstaver" kan dette være nyttig for talesynteser som ikke klarer å endre tonehøyde ved store bokstaver.

##### Bruk stavefunksjonalitet dersom støttet {#SpeechSettingsUseSpelling}

Noen ord består av bare én bokstav, men uttalen kan være forskjellig ut fra om bokstaven uttales som en sparat bokstav (som ved staving) eller som et ord.

For eksempel er "a" på engelsk både en bokstav og et ord, og det uttales forskjellig i hvert tilfelle.

Dette valget lar talesyntesen differensiere mellom disse to tilfellene dersom talesyntesen har støtte for dette. De fleste talesynteser har det.

Dette valget bør normalt være slått på.

Imidlertid håndterer ikke enkelte talesynteser basert på Microsoft Speech API dette korrekt, og de kan oppføre seg rart når dette valget er slått på.

Har du problemer med uttalen av enkeltbokstaver, kan du forsøke å slå av dette valget.

#### Velg talesyntese (NVDA+Ctrl+s) {#SelectSynthesizer}

Talesyntese-dialogen, som kan åpnes ved å aktivere knappen Endre ... i talekategorien i NVDAs innstillingsdialog, lar deg velge hvilken talesyntese NVDA skal snakke med.

Så snart du har valgt den talesyntesen du ønsker å bruke, kan du trykke på OK, og NVDA laster umiddelbart inn den valgte talesyntesen.
Skulle det oppstå en feil ved innlasting av den nye talesyntesen, vil NVDA varsle deg med en melding, og deretter fortsette å bruke den gamle talesyntesen.

##### Talesyntese {#SelectSynthesizerSynthesizer}

Dette valget lar deg avgjøre hvilken talesyntese du vil at NVDA skal bruke for taleutdata.

Se i delen [Støttede talesynteser](#SupportedSpeechSynths) for å finne en liste over talesynteser NVDA støtter..

Et spesielt element som alltid vil være til stede i denne listen, er "Ingen tale". Dette vil la deg bruke NVDA uten noen som helst form for tale.

Dette valget kan være nyttig for en som ønsker å bruke NVDA bare med punktskrift, eller for utviklere som bare vil benytte taleviseren.

##### Enhet for utdata {#SelectSynthesizerOutputDevice}

Dette valget lar deg velge hvilket lydkort NVDA skal instruere den valgte talesyntesen om å snakke gjennom.

<!-- KC:setting -->

##### Modus for lyddemping {#SelectSynthesizerDuckingMode}

Tast: NVDA+Skift+d

I Windows 8 og nyere, lar dette valget deg velge om NVDA skal senke lydnivået på andre programmer når NVDA snakker, eller hele tiden mens NVDA er i gang.

* Ingen lyddemping: NVDA vil aldri senke lydnivået på annen lyd.
* Demp annen lyd ved tale og lyd fra NVDA: NVDA vil bare senke nivået på annen lyd når NVDA snakker eller spiller av lyd. Dette fungerer kanskje ikke for alle talesynteser.
* Demp alltid annen lyd: NVDA vil holde lydnivået på annen lyd lavere så lenge NVDA er i gang.

Dette valget er bare tilgjengelig dersom NVDA er installert. Det er ikke mulig å støtte lyddemping i flyttbare eller midlertidige kopier av NVDA.

#### Innstillingsringen for talesyntese {#SynthSettingsRing}

Hvis du ønsker å endre taleinnstillingene raskt, uten å gå via talekategorien i NVDAs innstillingsdialog, finnes det noen tastekommandoer i NVDA som lar deg bevege deg gjennom de vanligste taleinnstillingene. Disse kommandoene er tilgjengelige uansett hvor du er, så lenge NVDA kjører:
<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Beskrivelse|
|---|---|---|---|
|Gå til neste talesynteseinnstilling |NVDA+Ctrl+PilHøyre |NVDA+Skift+Ctrl+PilHøyre |Går til neste tilgjengelige talesynteseinnstilling etter den gjeldende, og begynner fra begynnelsen igjen etter den siste|
|Gå til forrige talesynteseinnstilling |NVDA+Ctrl+PilVenstre |NVDA+Skift+Ctrl+PilVenstre |Går til neste tilgjengelige talesynteseinnstilling før den gjeldende, og begynner fra slutten igjen etter den første|
|Øk gjeldende talesynteseinnstilling |NVDA+Ctrl+PilOpp |NVDA+Skift+Ctrl+PilOpp |øker den gjeldende talesynteseinnstillingen du er på, f.eks. øker talehastigheten, velger neste stemme, øker lydnivået|
|Reduser gjeldende talesynteseinnstilling |NVDA+Ctrl+PilNed |NVDA+Skift+Ctrl+PilNed |reduserer den gjeldende talesynteseinnstillingen du er på, f.eks. reduserer talehastigheten, velger forrige stemme, reduserer lydnivået|

<!-- KC:endInclude -->

#### Punktskrift {#BrailleSettings}

Kategorien Punktskrift i NVDAs innstillingsdialog inneholder valg som lar deg endre flere aspekter ved bruk av punktskrift for inn- og utdata.

Denne kategorien inneholder disse valgene:

##### Endre leselist {#BrailleSettingsChange}

Knappen Endre ... i kategorien Punktskrift i NVDAs innstillingsdialog aktiverer dialogen [Velg leselist](#SelectBrailleDisplay). Denne dialogen lar deg velge den aktive leselisten.

Denne dialogen åpner seg over NVDAs innstillingsdialog.
::Lagrer eller avbryter du innstillingene i dialogen Velg leselist, vil du gå tilbake til NVDAs innstillingsdialog.

##### Utdatatabell {#BrailleSettingsOutputTable}

Det neste valget du kommer til i denne kategorien er kombinasjonsboksen for utdatatabell i punktskrift.

I denne kombinasjonsboksen vil du finne punktskrifttabeller for en rekke språk, punktskriftstandarder og nivåer. Den valgte tabellen vil bli brukt til å oversette punktskrift for visning på leselisten din.

Du kan flytte deg mellom punktskrifttabellene i listen ved å bruke piltastene.

##### Inndatatabell {#BrailleSettingsInputTable}

Som et slags supplement til forrige valg, er den neste innstillingen du finner kombinasjonsboksen for inndatatabell i punktskrift.

Den valgte tabellen vil bli brukt til å oversette punktskriften du skriver på punktskrifttastaturet på leselisten din til tekst.

Du kan flytte deg mellom punktskrifttabellene i listen ved å bruke piltastene.

Legg merke til at dette valget bare vil være nyttig for deg hvis leselisten din har et punktskrifttastatur, og denne funksjonen støttes at leselistdriveren.

Om inndata ikke støttes på en leselist som har punktskrifttastatur, vil dette være omtalt i delen [Støttede leselister](#SupportedBrailleDisplays).

##### Utvid ordet under markøren til datapunktskrift {#BrailleSettingsExpandToComputerBraille}

Dette valget lar ordet som vises under punktskriftmarkøren bli vist i uforkortet datapunktskrift.

Innstillingen er nyttig særlig hvis du har valgt å vise punktskriften som forkortet 6-punkts punktskrift.

##### Vis markør {#BrailleSettingsShowCursor}

Dette valget lar deg slå punktskriftmarkøren på og av.

Dette gjelder for systemmarkør og lesemarkør, men ikke for valgindikator.

##### Blinkende markør {#BrailleSettingsBlinkCursor}

Dette valget tillater punktskriftmarkøren å blinke.

Hvis blinking er slått av, vil punktskriftmarkøren være i konstant "oppe"-posisjon.

Valgindikatoren berøres ikke av dette valget. Den vises alltid som punkt 7 og 8 uten blinking.

##### Blinkehastighet for markør (ms) {#BrailleSettingsBlinkRate}

Dette valget er et numerisk felt som lar deg endre markørens blinkehastighet i millisekunder.

##### Markørutseende for fokus {#BrailleSettingsCursorShapeForFocus}

Dette valget lar deg endre utseendet (punktmønsteret) på punktskriftmarkøren når punktskrift er knyttet til fokus.

Valgindikatoren er ikke berørt av dette valget. Den er alltid punkt 7 og 8 uten blinking.

##### Markørutseende for lesing {#BrailleSettingsCursorShapeForReview}

Dette valget lar deg velge utseendet (punktmønsteret) på punktskriftmarkøren når punktskrift er knyttet til lesing.

Valgindikatoren er ikke berørt av dette valget. Den er alltid punkt 7 og 8 uten blinking.

##### Tidsavbrudd for melding (sek) {#BrailleSettingsMessageTimeout}

Dette valget er et numerisk felt som kontrollerer hvor lenge meldinger i NVDA vises på leselisten.

Ved å spesifisere 0, slås visning av meldinger av fullstendig.

##### Vis meldinger uten tidsavbrudd {#BrailleSettingsNoMessageTimeout}

Dette valget lar NVDA vise meldinger på leselisten uten at de forsvinner automatisk etter en viss tid.

<!-- KC:setting -->

##### Knytt punktskrift til {#BrailleTether}

Tast: NVDA+Ctrl+t

Dette valget lar deg avgjøre hvorvidt leselisten skal følge systemfokus, navigasjonsobjektet/lesemarkøren, eller begge.

Når "automatisk" er valgt, vil NVDA følge systemfokus og -markøren som standard.
I dette tilfellet, når navigasjonsobjektets eller lesemarkørens posisjon endres som følge av eksplisitt brukersamhandling, vil NVDA knytte seg midlertidig til lesemarkør, til fokus eller markør endres.

##### Les avsnittsvis {#BrailleSettingsReadByParagraph}

Hvis dette valget er slått på, vil punktskrift bli vist som avsnitt i stedet for linjer.

Kommandoene for neste og forrige linje vil tilsvarende gå til neste eller forrige avsnitt. Dette betyr at du ikke behøver å bla med leselisten ved slutten av hver linje; heller ikke når mer tekst ville fått plass på leselista. Dette kan gi mulighet for mer flyt i lesingen av større mengder tekst.

Valget er avslått som standard.

##### Unngå ordsplitting når mulig {#BrailleSettingsWordWrap}

Hvis dette valget er slått på, vil et ord som er for langt til å vises på slutten av leselisten ikke bli splittet. I stedet vil det være noe tomrom på slutten av leselisten. Når du blar framover med leselisten, vil du kunne lese hele ordet. Dette kalles noen ganger også "tekstomslutting".

Legg merke til at hvis ordet er for langt til å få plass på leselisten i seg selv, må ordet fortsatt splittes.

Hvis dette valget er avslått, vil så mye som mulig av ordet på slutten av leselisten bli vist. Når du blar framover med leselisten, vil du kunne lese resten av ordet.

Å slå på dette valget vil kunne gi bedre flyt i lesingen, men vil ofte innebære at du må bla mer med leselisten.

##### Presentasjon av fokuskontekst {#BrailleSettingsFocusContextPresentation}

Dette valget lar deg avgjøre hvilken kontekstinformasjon NVDA vil vise på leselisten når et objekt får fokus.

Kontekstinformasjon refererer til hierarkiet av objekter som inneholder fokus.

Når du for eksempel fokuserer på et listeelement, er dette listeelementet en del av en liste. Denne listen kan være en del av en dialog, osv.

Se delen om [objektnavigasjon](#ObjectNavigation) for mer informasjon om hierarkiet som gjelder objekter i NVDA.

Når innstillingen er satt til å fylle leselisten for endringer i kontekst, vil NVDA forsøke å vise så mye kontekstinformasjon som mulig på leselisten, men bare om de delene av konteksten som har blitt endret.

Når det gjelder eksempelet ovenfor, vil dette si at når du endrer fokus til listen, vil NVDA vise listeelementet på leselisten. Om det er nok ledig plass på leselisten, vil NVDA videre forsøke å vise at listeelementet er en del av en liste.
Om du så begynner å gå gjennom listen ved hjelp av piltastene, er det forutsatt at du er oppmerksom på at du fortsatt er i listen. Følgelig vil NVDA bare vise det fokuserte listeelementet for de gjenværende elementene i listen.

Hvis du vil lese konteksten igjen, for eksempel at du er i en liste og at listen er del av en dialog, må du bla leselisten bakover.

Når dette valget er satt til å alltid fylle leselisten, vil NVDA forsøke å vise så mye kontekstinformasjon på leselisten som mulig, uavhengig av om du har sett den samme kontekstinformasjonen før eller ikke.

Dette har den fordelen at NVDA vil få plass til så mye informasjon som mulig på leselisten.

Ulempen ved dette er at det alltid vil være en forskjell i posisjonen hvor fokuset begynner på leselisten. Dette kan gjøre det vanskelig å for eksempel skumme raskt gjennom en lang liste med elementer, fordi du hele tiden må flytte fingeren for å finne begynnelsen på elementet.

Dette var standard i NVDA 2017.2 og tidligere.

Når du setter innstillingen for presentasjon av fokuskontekst til å bare vise kontekstinformasjonen når du blar bakover, vil NVDA aldri vise kontekstinformasjon på leselisten som standard.

For å holde oss til eksempelet ovenfor, vil NVDA vise at du har satt fokus på et listeelement.

For at du da skal kunne lese konteksten, for eksempel at du er i en liste og at listen er en del av en dialog, må du bla bakover med leselisten.

For å kunne bytte presentasjon av fokuskontekst fra hvor som helst, kan du definere en tilpasset gest ved hjelp av dialogen [Inndatagester](#InputGestures).

#### Velg leselist (NVDA+Ctrl+a) {#SelectBrailleDisplay}

Dialogen Velg leselist, som kan åpnes ved å aktivere knappen Endre ... i dialogen Punktskrift i NVDAs innstillingsdialog, lar deg velge hvilken leselist NVDA skal benytte for å vise punktskrift.

Når du har valgt leselisten du vil bruke, kan du trykke på OK, og NVDA vil laste inn valgt leselist.

Om det oppstår feil ved lasting av leselistdriveren, vil NVDA varsle deg om det med en melding, og vil fortsette å benytte den tidligere leselisten, hvis det finnes noen.

##### Leselist {#SelectBrailleDisplayDisplay}

Denne kombinasjonsboksen presenterer flere alternativer, avhengig av hvilke leselistdrivere som er tilgjengelige på PC-en din.

Flytt deg gjennom valgene med piltastene.

Ingen leselist betyr at du ikke benytter punktskrift.

Vennligst se delen [Støttede leselister](#SupportedBrailleDisplays) for mer informasjon om leselistene som støttes.

##### Port {#SelectBrailleDisplayPort}

Dette valget vil, dersom det er tilgjengelig, la deg velge hvilken port eller type tilkobling som brukes til kommunikasjon med leselisten du har valgt.

Dette er en kombinasjonsboks med de valgene som er tilgjengelig for leselisten din.

Som standard skal NVDA oppdage port automatisk. Dette betyr at tilkoblingen til punktskriftenheten vil bli etablert automatisk ved at NVDA søker etter tilgjengelige USB- og bluetooth-enheter på PC-en din.

Imidlertid vil du kunne velge hvilken port som skal brukes for noen leselister.

Vanlige alternativer er "automatisk" (som instruerer NVDA om å benytte prosedyren for automatisk valg av port), "USB", "Bluetooth" og seriell port hvis leselisten din støtter denne typen kommunikasjon.

Dette valget vil ikke være tilgjengelig dersom leselisten din bare støtter automatisk oppdaging av port.

Se dokumentasjonen for leselisten din i delen
[Støttede leselister](#SupportedBrailleDisplays) for å finne flere detaljer om de støttede typene av kommunikasjon og tilgjengelige porter.

#### Tastatur (NVDA+Ctrl+k) {#KeyboardSettings}

Kategorien Tastatur i NVDAs innstillingdsdialog inneholder innstillinger som avgjør hvordan NVDA oppfører seg når du bruker og skriver på tastaturet ditt.

I denne kategorien finner du følgende valg:

##### Tastaturoppsett {#KeyboardSettingsLayout}

Denne kombinasjonsboksen lar deg velge hvilket tastaturoppsett NVDA skal ha. For øyeblikket er de to alternativene som leveres med NvDA stasjonært og bærbart.

##### Bruk CapsLock som NVDA-tast {#KeyboardSettingsCapsModifier}

Om denne avkryssingsboksen er avkrysset, kan CapsLock brukes som NVDA-tast.

##### Bruk utvidet Insert som NVDA-tast {#KeyboardSettingsExtendedInsert}

Hvis denne avkryssingsboksen er avkrysset, vil utvidet Insert (som du normalt finner ovenfor piltastene på et stasjonært tastatur, nær Home og End) kunne brukes som NVDA-tast.

##### Bruk numerisk Insert som NVDA-tast {#KeyboardSettingsNumpadInsert}

Hvis denne avkryssingsboksen er avkrysset, kan Insert-tasten på det numeriske tastaturet brukes som NVDA-tast.

Dersom ingen tast er definert som NVDA-tast, blir det umulig å få tilgang til en del NVDA-kommandoer. Derfor vil NVDAs innstillingsdialog vise en feilmelding dersom ingen tast er valgt når du trykker på OK- eller Bruk-knappen.

Etter at du har fjernet feilmeldingen, må du velge minst én tast som NVDA-tast før du kan trykke OK for å avslutte dialogen på riktig måte.

<!-- KC:setting -->

##### Si skrevne tegn {#KeyboardSettingsSpeakTypedCharacters}

Tast: NVDA+2

Når dette valget er slått på, vil NVDA annonsere alle tegn du skriver på tastaturet.

<!-- KC:setting -->

##### Si skrevne ord {#KeyboardSettingsSpeakTypedWords}

Tast: NVDA+3

Når dette valget er slått på, vil NVDA annonsere alle ord du skriver på tastaturet.

##### Avbryt tale ved skriving av tegn {#KeyboardSettingsSpeechInteruptForCharacters}

Hvis på, vil dette valget føre til at talen blir avbrutt hver gang et tegn skrives. Dette valget er slått på som standard.

##### Speech interrupt for Enter key {#KeyboardSettingsSpeechInteruptForEnter}

   If on, this option will cause speech to be interrupted each time the Enter key is pressed. This is on by
   default.

##### Allow skim reading in Say All {#KeyboardSettingsSkimReading}

   If on, certain navigation commands (such as quick navigation in browse mode or moving by line or paragraph) do
   not stop Say All, rather Say All jumps to the new position and continues reading.

##### Beep if Typing Lowercase Letters when Caps Lock is On {#KeyboardSettingsBeepLowercase}

   When enabled, a warning beep will be heard if a letter is typed with the shift key while caps lock is on.
   Generally, typing shifted letters with caps lock is unintentional and is usually due to not realizing that
   caps lock is enabled.
   Therefore, it can be quite helpful to be warned about this.

<!-- KC:setting -->

##### Si kommandotaster {#KeyboardSettingsSpeakCommandKeys}

Tast: NVDA+4

Når dette valget er på, vil NVDA annonsere alle taster du trykker på tastaturet som ikke er bokstaver eller tegn. Dette omfatter tastekombinasjoner som Ctrl + en bokstav.

##### Play sound for spelling errors while typing {#KeyboardSettingsAlertForSpellingErrors}

   When enabled, a short buzzer sound will be played when a word you type contains a spelling error.
   This option is only available if reporting of spelling errors is enabled in NVDA's [Document Formatting
   Settings #DocumentFormattingSettings], found in the NVDA Settings dialog.

##### Håndtere tastetrykk fra andre programmer {#KeyboardSettingsHandleKeys}

Dette valget lar brukeren avgjøre om tastetrykk generert av programmer som skjermtastaturer og programmer for talegjenkjenning skal håndteres av NvDA.

Dette valget er slått på som standard, men noen brukere ønsker kanskje å slå dette av. Det kan for eksempel gjelde for brukere som skriver vietnamesisk med skriveprogrammet Unikey, siden dette vil generere feilaktig inndata.

#### Mus (NVDA+Ctrl+m) {#MouseSettings}

   The Mouse category in the NVDA Settings dialog allows NVDA to track the mouse, play mouse coordinate beeps and
   sets other mouse usage options.
   This category contains the following options:

##### Report Mouse Shape Changes {#MouseSettingsShape}

   A checkbox, that when checked means that NVDA will announce the shape of the mouse pointer each time it
   changes.
   The mouse pointer in Windows changes shape to convey certain information such as when something is editable,
   or when something is loading etc.

<!-- KC:setting -->

##### Slå på mussporing {#MouseSettingsTracking}

Tast: NVDA+m

Når dette er slått på, vil NVDA annonsere teksten som for øyeblikket er under muspekeren, etter hvert som du flytter muspekeren omkring på skjermen.

Dette lar deg finne ting på skjermen ved å fysisk flytte musen, heller enn å forsøke å finne dem ved bruk av objektnavigasjon.

##### Text unit resolution {#MouseSettingsTextUnit}

   If NVDA is set to announce the text under the mouse as you move it, this option allows you to choose exactly
   how much text will be spoken.
   The options are character, word, line and paragraph.

##### Report role when mouse enters object {#MouseSettingsRole}

   If this checkbox is checked, NVDA will announce the role (type) of object as the mouse moves inside it.

##### Play audio coordinates when mouse moves {#MouseSettingsAudio}

   Checking this checkbox makes NVDA play beeps as the mouse moves, so that the user can work out where the mouse
   is in regards to the dimensions of the screen.
   The higher the mouse is on the screen, the higher the pitch of the beeps.
   The further left or right the mouse is located on the screen, the further left or right the sound will be
   played (assuming the user has stereo speakers or headphones).

##### Brightness controls audio coordinates volume {#MouseSettingsBrightness}

   If the "play audio coordinates when mouse moves" checkbox is checked, then checking this checkbox means that
   the volume of the audio coordinates beeps is controlled by how bright the screen is under the mouse.
   This setting is unchecked by default.

#### Berøringssamhandling {#TouchInteraction}

Denne innstillingskategorien, som er tilgjengelig bare på datamaskiner som kjører Windows 8 og senere med berøringsfunksjonalitet, lar deg stille inn hvordan NVDA samhandler med berøringsskjermer.

Denne kategorien inneholder følgende valg:

##### Touch typing mode {#TouchTypingMode}

   This checkbox allows you to specify the method you wish to use when entering text using the touch keyboard.
   If this checkbox is checked, when you locate a key on the touch keyboard, you can lift your finger and the
   selected key will be pressed.
   If this is unchecked, you need to double-tap on the touch keyboard key to press the key.

#### Lesemarkør {#ReviewCursorSettings}

Kategorien Lesemarkør i NVDAs innstillingsdialog brukes til å konfigurere oppførselen til lesemarkøren i NVDA.

Denne kategorien inneholder følgende valg:

<!-- KC:setting -->

##### Følg systemfokus {#ReviewCursorFollowFocus}

Tast: NVDA+7

   When enabled, The review cursor will always be placed in the same object as the current system focus whenever
   the focus changes.

<!-- KC:setting -->

##### Følg systemmarkør {#ReviewCursorFollowCaret}

Tast: NVDA+6

   When enabled, the review cursor will automatically be moved to the position of the System caret each time it
   moves.

##### Følg musmarkør {#ReviewCursorFollowMouse}

   When enabled, the review cursor will follow the mouse as it moves.

##### Enkel lesemodus {#ReviewCursorSimple}

   When enabled, NVDA will filter the hierarchy of objects that can be navigated to exclude objects that aren't
   of interest to the user; e.g. invisible objects and objects used only for layout purposes.
   To toggle simple review mode from anywhere, please assign a custom gesture using the [Input Gestures dialog
   #InputGestures].

#### Objektpresentasjon (NVDA+Ctrl+o) {#ObjectPresentationSettings}

   The Object Presentation category in the NVDA Settings dialog is used to set how much information NVDA will
   present about controls such as description, position information and so on.

Denne kategorien inneholder følgende valg:

##### Rapporter verktøytips {#ObjectPresentationReportToolTips}

   A checkbox that when checked tells NVDA to report tool tips as they appear.
   Many Windows and controls show a small message (or tool tip) when you move the mouse pointer over them, or
   sometimes when you move the focus to them.

##### Rapporter hjelpeballonger {#ObjectPresentationReportBalloons}

   This checkbox when checked tells NVDA to report help balloons as they appear.
   Help Balloons are like tool tips, but are usually larger in size, and are associated with system events such
   as a network cable being unplugged, or perhaps to alert you about Windows security issues.

##### Report Object Shortcut Keys {#ObjectPresentationShortcutKeys}

   When this checkbox is checked, NVDA will include the shortcut key that is associated with a certain object or
   control when it is reported.
   For example the File menu on a menu bar may have a shortcut key of alt+f.

##### Report object position information {#ObjectPresentationPositionInfo}

   This option lets you choose whether you wish to have an object's position (e.g. 1 of 4) reported when moving
   to the object with the focus or object navigation.

##### Guess Object Position Information when unavailable {#ObjectPresentationGuessPositionInfo}

   If reporting of object position information is turned on, this option allows NVDA to guess object position
   information when it is otherwise unavailable for a particular control.
   When on, NVDA will report position information for more controls such as menus and toolbars, however this
   information may be slightly inaccurate.

##### Report Object descriptions {#ObjectPresentationReportDescriptions}

   Uncheck this checkbox if you don't wish to have the description reported along with objects.

<!-- KC:setting -->

##### Progress bar output {#ObjectPresentationProgressBarOutput}

Tast: NVDA+u

   This option controls how NVDA reports progress bar updates to you.
   It has the following options:

   * Off: Progress bars will not be reported as they change.
   * Speak: This option tells NVDA to speak the progress bar in percentages. Each time the progress bar changes,
   NVDA will speak the new value.
   * Beep: This tells NVDA to beep each time the progress bar changes. The higher the beep, the closer the
   progress bar is to completion.
   * Beep and speak: This option tells NVDA to both beep and speak when a progress bar updates.

##### Report background progress bars {#ObjectPresentationReportBackgroundProgressBars}

   This is an option that, when checked, tells NVDA to keep reporting a progress bar, even if it is not
   physically in the foreground.
   If you minimize or switch away from a window that contains a progress bar, NVDA will keep track of it,
   allowing you to do other things while NVDA tracks the progress bar.

<!-- KC:setting -->

##### Report dynamic content changes {#ObjectPresentationReportDynamicContent}

Tast: NVDA+5

   Toggles the announcement of new content in particular objects such as terminals and the history control in
   chat programs.

##### Play a sound when auto-suggestions appear {#ObjectPresentationSuggestionSounds}

   Toggles announcement of appearance of auto-suggestions, and if enabled, NVDA will play a sound to indicate
   this.
   Auto-suggestions are lists of suggested entries based on text entered into certain edit fields and documents.
   For example, when you enter text into the search box in Start menu in Windows Vista and later, Windows
   displays a list of suggestions based on what you typed.
   For some edit fields such as search fields in various Windows 10 apps, NVDA can notify you that a list of
   suggestions has appeared when you type text.
   The auto-suggestions list will close once you move away from the edit field, and for some fields, NVDA can
   notify you of this when this happens.

#### Input Composition {#InputCompositionSettings}

   The Input Composition category allows you to control how NVDA reports the input of Asian characters, such as
   with IME or Text Service input methods.
   Note that due to the fact that input methods vary greatly by available features and by how they convey
   information, it will most likely be necessary to configure these options differently for each input method to
   get the most efficient typing experience.

##### Automatically report all available candidates {#InputCompositionReportAllCandidates}

   This option, which is on by default, allows you to choose whether or not all visible candidates should be
   reported automatically when a candidate list appears or its page is changed.
   Having this option on for pictographic input methods such as Chinese New ChangJie or Boshiami is useful, as
   you can automatically hear all symbols and their numbers and you can choose one right away.
   However, for phonetic input methods such as Chinese New Phonetic, it may be more useful to turn this option
   off, as all the symbols will sound the same and you will have to use the arrow keys to navigate the list items
   individually to gain more information from the character descriptions for each candidate.

##### Announce Selected Candidate {#InputCompositionAnnounceSelectedCandidate}

   This option, which is on by default, allows you to choose whether NVDA should announce the selected candidate
   when a candidate list appears or when the selection is changed.
   For input methods where the selection can be changed with the arrow keys (such as Chinese New Phonetic) this
   is necessary, but for some input methods it may be more efficient typing with this option turned off.
   Note that even with this option off, the review cursor will still be placed on the selected candidate allowing
   you to use object navigation / review to manually read this or other candidates.

##### Always include short character descriptions for candidates {#InputCompositionCandidateIncludesShortCharacterDescription}

   This option, which is on by default, allows you to choose whether or not NVDA should provide a short
   description for each character in a candidate, either when it's selected or when it's automatically read when
   the candidate list appears.
   Note that for locales such as Chinese, the announcement of extra character descriptions for the selected
   candidate is not affected by this option.
   This option may be useful for Korean and Japanese input methods.

##### Report changes to the reading string {#InputCompositionReadingStringChanges}

   Some input methods such as Chinese New Phonetic and New ChangJie have a reading string (sometimes known as a
   precomposition string).
   You can choose whether or not NVDA should announce new characters being typed into this reading string with
   this option.
   This option is on by default.
   Note some older input methods such as Chinese ChangJie may not use the reading string to hold precomposition
   characters, but instead use the composition string directly. Please see the next option for configuring
   reporting of the composition string.

##### Report changes to the composition string {#InputCompositionCompositionStringChanges}

   After reading or precomposition data has been combined into a valid pictographic symbol, most input methods
   place this symbol into a composition string for temporary storage along with other combined symbols before
   they are finally inserted into the document.
   This option allows you to choose whether or not NVDA should report new symbols as they appear in the
   composition string.
   This option is on by default.

#### Nettmodus (NVDA+Ctrl+b) {#BrowseModeSettings}

   The Browse Mode category in the NVDA Settings dialog is used to configure NVDA's behavior when you read and
   navigate complex documents such as web pages.

Denne kategorien inneholder følgende valg:

##### Maximum Number of Characters on One Line {#BrowseModeSettingsMaxLength}

   This field sets the maximum length of a line in browse mode (in characters).

##### Maximum Lines Per Page {#BrowseModeSettingsPageLines}

   This field sets the amount of lines you will move by when pressing page up or page down while in browse mode.

<!-- KC:setting -->

##### Bruk skjermoppsett {#BrowseModeSettingsScreenLayout}

Tast: NVDA+v

   This option allows you to specify whether content in browse mode should place content such as links and other
   fields on their own line, or if it should keep them in the flow of text as it is visually shown. If the option
   is enabled then things will stay as they are visually shown, but if it is disabled then fields will be placed
   on their own line.

##### Automatic Say All on page load {#BrowseModeSettingsAutoSayAll}

   This checkbox toggles the automatic reading of a page after it loads in browse mode.
   This option is enabled by default.

##### Include layout tables {#BrowseModeSettingsIncludeLayoutTables}

   This option affects how NVDA handles tables used purely for layout purposes.
   When on, NVDA will treat these as normal tables, reporting them based on [Document Formatting Settings
   #DocumentFormattingSettings] and locating them with quick navigation commands.
   When off, they will not be reported nor found with quick navigation.
   However, the content of the tables will still be included as normal text.
   This option is turned off by default.
   To toggle inclusion of layout tables from anywhere, please assign a custom gesture using the [Input Gestures
   dialog #InputGestures].

##### Configuring reporting of fields such as links and headings {#BrowseModeLinksAndHeadings}

   Please see the options in the [Document Formatting category](#DocumentFormattingSettings) of the [NVDA Settings
   #NVDASettings] dialog to configure the fields that are reported when navigating, such as links, headings and
   tables.

##### Automatic focus mode for focus changes {#BrowseModeSettingsAutoPassThroughOnFocusChange}

   This option allows focus mode to be invoked if focus changes.
   For example, when on a web page, if you press tab and you land on a form, if this option is checked, focus
   mode will automatically be invoked.

##### Automatic focus mode for caret movement {#BrowseModeSettingsAutoPassThroughOnCaretMove}

   This option, when checked, allows NVDA to enter and leave focus mode when using arrow keys.
   For example, if arrowing down a web page and you land on an edit box, NVDA will automatically bring you into
   focus mode. If you arrow out of the edit box, NVDA will put you back in browse mode.

##### Audio indication of Focus and Browse modes {#BrowseModeSettingsPassThroughAudioIndication}

   If this option is enabled, NVDA will play special sounds when it switches between browse mode and focus mode,
   rather than speaking the change.

##### Trap non-command gestures from reaching the document {#BrowseModeSettingsTrapNonCommandGestures}

   Enabled by default, this option allows you to choose if gestures (such as key presses) that do not result in
   an NVDA command and are not considered to be a command key in general, should be trapped from going through to
   the document you are currently focused on.
   As an example, if enabled, if the letter j was pressed, it would be trapped from reaching the document, even
   though it is not a quick navigation command nor is it likely to be a command in the application itself.

#### Dokumentformatering (NVDA+Ctrl+d) {#DocumentFormattingSettings}

   Most of the checkboxes in this category are for configuring what type of formatting you wish to have reported
   as you move the cursor around documents.
   For example, if you check the report font name checkbox, each time you arrow onto text with a different font,
   the name of the font will be announced.
   The document formatting options are organized into groups.
Du kan konfigurere rapportering av:

* Font
* Fontnavn
* Fontstørrelse
* Fontattributter
   * Emphasis
   * Style
* Farger
* Dokumentinformasjon
* Kommentarer
   * Editor revisions
* Stavefeil
   * Pages and spacing
* Sidetall
* Linjenummer
   * Line indentation reporting [(Off, Speech, Tones, Both Speech and Tones)](#lineIndentationOptions)
* Avsnittsinnrykk (for eksempel hengende innrykk og innrykk av første linje)
* Linjeavstand (enkel, dobbel, etc.)
* Justering
* Tabellinformasjon
* Tabeller
   * Row/column headers
* Cellekoordinater
   * Cell borders [(Off, Styles, Both Colors and Styles)
* Elementer
* Overskrifter
* Lenker
* Lister
* Blokksitater
* Landemerker
* Rammer
* Klikkbar

-
   To toggle these settings from anywhere, please assign custom gestures using the [Input Gestures dialog
   #InputGestures].

##### Report formatting changes after the cursor {#DocumentFormattingDetectFormatAfterCursor}

   If enabled, this setting tells NVDA to try and detect all the formatting changes on a line as it reports it,
   even if doing this may slow down NVDA's performance.
   By default, NVDA will detect the formatting at the position of the System caret / Review Cursor, and in some
   instances may detect formatting on the rest of the line, only if it is not going to cause a performance
   decrease.
   Enable this option while proof reading documents in applications such as WordPad, where formatting is
   important.

##### Rapportering av linjeinnrykk {#DocumentFormattingSettingsLineIndentation}

Dette valget lar deg konfigurere hvordan innrykk på begynnelsen av linjer rapporteres.

Kombinasjonsboksen "Rapporter linjeinnrykk med" har fire valg:

* Av: NVDA vil ikke behandle innrykk spesielt.
* Tale: Om tale er valgt og innrykk endres, vil NVDA si noe sånt som "tolv mellomrom" eller "fire tabulator."
* Toner: Om toner er valgt og innrykk endres, vil toner indikere omfanget av endringen av innrykket. Tonehøyden vil øke for hvert mellomrom, og for en tabulator vil tonehøyden øke tilsvarende fire mellomrom.
* Både tale og toner: Dette valget rapporterer innrykk ved hjelp av begge metodene ovenfor.

#### Innstillinger for OCR i Windows 10 {#Win10OcrSettings}

Innstillingene i denne kategorien lar deg konfigurere [Windows 10 OCR](#Win10Ocr).

Denne kategorien består av følgende valg:

##### Språk for gjenkjenning {#Win10OcrSettingsRecognitionLanguage}

Denne kombinasjonsboksen lar deg velge språket som skal brukes for tekstgjenkjenning.

### Diverse innstillinger {#MiscSettings}

I tillegg til dialogen [NCDA-Innstillinger](#NVDASettings), inneholder undermenyen Preferanser i NVDA-menyen flere andre elementer som er omtalt nedenfor.

#### Taleordlister {#SpeechDictionaries}

   The speech dictionaries menu (found in the Preferences menu) contains dialogs that allow you to manage the way
   NVDA pronounces particular words or phrases.
   There are currently three different types of speech dictionaries.
   They are:

   * Default: rules in this dictionary affect all speech in NVDA.
   * Voice: rules in this dictionary affect speech for the synthesizer voice currently being used.
   * Temporary: rules in this dictionary affect all speech in NVDA, but only for the current session. These rules
   are temporary and will be lost if NVDA is restarted.
-

   You need to assign custom gestures using the [Input Gestures dialog](#InputGestures) if you wish to open any of
   these dictionary dialogs from anywhere.
   All dictionary dialogs contain a list of rules which will be used for processing the speech.
   The dialog also contains Add, Edit and Remove buttons.
   To add a new rule to the dictionary, press the Add button, and fill in the fields in the dialog box that
   appears and then press Ok.
   You will then see your new rule in the list of rules.
   However, to make sure your rule is actually saved, make sure to press Ok to exit the dictionary dialog
   completely once you have finished adding/editing rules.
   The rules for NVDA's speech dictionaries allow you to change one string of characters into another.
   For example, you could create a rule which causes NVDA to say the word "frog" instead of "bird" whenever the
   word "bird" is encountered.
   In the Add rule dialog, the easiest way to do this is to type the word bird in the Pattern field, and the word
   frog in the Replacement field.
   You may also want to type a description of the rule in the Comment field (something like: changes bird to
   frog).
   NVDA's speech dictionaries however are much more powerful than simple word replacement.
   The Add rule dialog also contains a checkbox to say whether or not you want the rule to be case sensitive
   (meaning that NVDA should care whether the characters are uppercase or lowercase.
   NVDA ignores case by default).
   Finally, a set of radio buttons allows you to tell NVDA whether your pattern should match anywhere, should
   only match if it is a complete word or should be treated as a "Regular expression".
   Setting the pattern to match as a whole word means that the replacement will only be made if the pattern does
   not occur as part of a larger word; i.e. a character other than an alphanumeric character or an underscore (or
   no character at all) comes both immediately before and after the pattern.
   Thus, using the earlier example of replacing the word "bird" with "frog", if you were to make this a whole
   word replacement, it would not match "birds" or "bluebird".
   A regular expression is a pattern containing special symbols that allow you to match on more than one
   character at a time, or match on just numbers, or just letters, as a few examples.
   Regular expressions are not covered in this user guide, but there are many tutorials on the web which can
   provide you with more information.

+++ Uttale av tegnsetting/symboler +++[SymbolPronunciation]
   This dialog allows you to change the way punctuation and other symbols are pronounced, as well as the symbol
   level at which they are spoken.
   The language for which symbol pronunciation is being edited will be shown in the dialog's title.
   Note that this dialog respects the "Trust voice's language for processing symbols and characters" option found
   in the [Speech category](#SpeechSettings) of the [NVDA Settings](#NVDASettings) dialog; i.e. it uses the voice
   language rather than the NVDA global language setting when this option is enabled.
   To change a symbol, first select it in the Symbols list.
   * The Replacement field allows you to change the text that should be spoken in place of this symbol.
   * Using the Level field, you can adjust the lowest symbol level at which this symbol should be spoken.
   * The Send actual symbol to synthesizer field specifies when the symbol itself (in contrast to its
   replacement) should be sent to the synthesizer.
   This is useful if the symbol causes the synthesizer to pause or change the inflection of the voice.
   For example, a comma causes the synthesizer to pause.
   There are three options:
   * never: Never send the actual symbol to the synthesizer.
   * always: Always send the actual symbol to the synthesizer.
   * only below symbols' level: Send the actual symbol only if the configured speech symbol level is lower than
   the level set for this symbol.
   For example, you might use this so that a symbol will have its replacement spoken at higher levels without
   pausing, while still being indicated with a pause at lower levels.
-
-
   You can add new symbols by pressing the Add button.
   In the dialog that appears, enter the symbol and press the OK button.
   Then, change the fields for the new symbol as you would for other symbols.
   You can remove a symbol you previously added by pressing the Remove button.
   When you are finished, press the OK button to save your changes or the Cancel button to discard them.

+++ Inndatagester +++[InputGestures]
   In this dialog, you can customize the input gestures (keys on the keyboard, buttons on a braille display,
   etc.) for NVDA commands.
   Only commands that are applicable immediately before the dialog is opened are shown.
   For example, if you want to customize commands related to browse mode, you should open the Input Gestures
   dialog while you are in browse mode.
   The tree in this dialog lists all of the applicable NVDA commands grouped by category.
   You can filter them by entering one or more words from the command's name into the Filter by edit box in any
   order.
   Any gestures associated with a command are listed beneath the command.
   To add an input gesture to a command, select the command and press the Add button.
   Then, perform the input gesture you wish to associate; e.g. press a key on the keyboard or a button on a
   braille display.
   Often, a gesture can be interpreted in more than one way.
   For example, if you pressed a key on the keyboard, you may wish it to be specific to the current keyboard
   layout (e.g. desktop or laptop) or you may wish it to apply for all layouts.
   In this case, a menu will appear allowing you to select the desired option.
   To remove a gesture from a command, select the gesture and press the Remove button.
   When you are finished making changes, press the OK button to save them or the Cancel button to discard them.

++ Lagre konfigurasjonen og laste den inn på nytt ++[SavingAndReloading]
   By default NVDA will automatically save your settings on exit.
   Note, however, that this option can be changed under the general options in the preferences menu.
   To save the settings manually at any time, choose the Save configuration item in the NVDA menu.
   If you ever make a mistake with your settings and need to revert back to the saved settings, choose the
   "revert to saved configuration" item in the NVDA menu.
   You can also reset your settings to their original factory defaults by choosing Reset Configuration To Factory
   Defaults, which is also found in the NVDA menu.
   The following NVDA key commands are also useful:

<!-- KC:beginInclude -->

| Navn |Stasjonær tast |Bærbar tast |Beskrivelse|
|---|---|---|---|
|Lagre konfigurasjon |NVDA+Ctrl+c |NVDA+Ctrl+c |Lagrer din gjeldende konfigurasjon slik at den ikke forsvinner når du avslutter NVDA|
|Tilbakestill konfigurasjon |NVDA+Ctrl+r |NVDA+Ctrl+r |Trykk én gang for å tilbakestille konfigurasjonen din til da du sist lagret den. Tre trykk vil tilbakestille den til fabrikkstandard.|

<!-- KC:endInclude -->

### Konfigurasjonsprofiler {#ConfigurationProfiles}

   Sometimes, you may wish to have different settings for different situations.
   For example, you may wish to have reporting of indentation enabled while you are editing or reporting of font
   attributes enabled while you are proofreading.
   NVDA allows you to do this using configuration profiles.
   A configuration profile contains only those settings which are changed while the profile is being edited.
   Most settings can be changed in configuration profiles except for those in the General category of the [NVDA
   Settings #NVDASettings] dialog, which apply to the entirety of NVDA.
   Configuration profiles can be manually activated.
   They can also be activated automatically due to triggers such as switching to a particular application.

#### Grunnleggende behandling {#ProfilesBasicManagement}

   You manage configuration profiles by selecting "Configuration profiles" in the NVDA menu.
   You can also do this using a key command:
<!-- KC:beginInclude -->

   * NVDA+Ctrl+p: Show the Configuration Profiles dialog.
-
<!-- KC:endInclude -->

   The first control in this dialog is the profile list from which you can select one of the available profiles.
   When you open the dialog, the profile you are currently editing is selected.
   Additional information is also shown for active profiles, indicating whether they are manually activated,
   triggered and/or being edited.
   To rename or delete a profile, press the Rename or Delete buttons, respectively.
   Press the Close button to close the dialog.

+++ Lage en profil +++[ProfilesCreating]
   To create a profile, press the New button.
   In the New Profile dialog, you can enter a name for the profile.
   You can also select how this profile should be used.
   If you only want to use this profile manually, select Manual activation, which is the default.
   Otherwise, select a trigger which should automatically activate this profile.
   For convenience, if you haven't entered a name for the profile, selecting a trigger will fill in the name
   accordingly.
   See [below](#ConfigProfileTriggers) for more information about triggers.
   Pressing OK will create the profile and close the Configuration Profiles dialog so you can edit it.

+++ Manuell aktivering +++[ConfigProfileManual]
   You can manually activate a profile by selecting a profile and pressing the Manual activate button.
   Once activated, other profiles can still be activated due to triggers, but any settings in the manually
   activated profile will override them.
   For example, if a profile is triggered for the current application and reporting of links is enabled in that
   profile but disabled it in the manually activated profile, links will not be reported.
   However, if you have changed the voice in the triggered profile but have never changed it in the manually
   activated profile, the voice from the triggered profile will be used.
   Any settings you change will be saved in the manually activated profile.
   To deactivate a manually activated profile, select it in the Configuration Profiles dialog and press the
   Manual deactivate button.

+++ Triggers +++[ConfigProfileTriggers]
   Pressing the Triggers button in the Configuration Profiles dialog allows you to change the profiles which
   should be automatically activated for various triggers.
   The Triggers list shows the available triggers, which are as follows:
   * Current application: Triggered when you switch to the current application.
   * Say all: Triggered while reading with the say all command.

   To change the profile which should be automatically activated for a trigger, select the trigger and then
   select the desired profile from the Profile list.
   You can select "(normal configuration)" if you don't want a profile to be used.
   Press the Close button to return to the Configuration Profiles dialog.

#### Redigere en profil {#ConfigProfileEditing}

   If you have manually activated a profile, any settings you change will be saved to that profile.
   Otherwise, any settings you change will be saved to the most recently triggered profile.
   For example, if you have associated a profile with the Notepad application and you switch to Notepad, any
   changed settings will be saved to that profile.
   Finally, if there is neither a manually activated nor a triggered profile, any settings you change will be
   saved to your normal configuration.
   To edit the profile associated with say all, you must [manually activate](#ConfigProfileManual) that profile.

#### Temporarily Disabling Triggers {#ConfigProfileDisablingTriggers}

   Sometimes, it is useful to temporarily disable all triggers.
   For example, you might wish to edit a manually activated profile or your normal configuration without
   triggered profiles interfering.
   You can do this by checking the Temporarily disable all triggers checkbox in the Configuration Profiles
   dialog.
   To toggle disabling triggers from anywhere, please assign a custom gesture using the [Input Gestures dialog
   #InputGestures].

### Location of Configuration files {#LocationOfConfigurationFiles}

   Portable versions of NVDA store all settings and add-ons in a directory called userConfig, found in the NVDA
   directory.
   Installed versions of NVDA store all settings and add-ons in a special NVDA directory located in your Windows
   user profile.
   This means that each user on the system can have their own NVDA settings.
   To get to your settings directory for an installed version of NVDA, on the start menu you can go to programs
   -> NVDA -> explore user configuration directory.
   Settings for NVDA when running on the logon or UAC screens are stored in the systemConfig directory in NVDA's
   installation directory.
   Usually, this configuration should not be touched.
   To change NVDA's configuration on the logon/UAC screens, configure NVDA as you wish while logged into Windows,
   save the configuration, and then press the "Use currently saved settings on the logon and other secure
   screens" button in the General category of the [NVDA Settings](#NVDASettings) dialog.

## Ekstra verktøy {#ExtraTools}
### Loggviser {#LogViewer}

   The log viewer, found under Tools in the NVDA menu, allows you to view all the logging output that has
   occurred up until now from when you last started NVDA.
   Apart from reading the content, you can also Save a copy of the log file, or refresh the viewer so that it
   shows the most recent output since the Log viewer was opened.
   These actions are available under the viewer's Log menu.

### Taleviser {#SpeechViewer}

   For sighted software developers or people demoing NVDA to sighted audiences, a floating window is available
   that allows you to view all the text that NVDA is currently speaking.
   To enable the speech viewer, check the "Speech Viewer" menu item under Tools in the NVDA menu.
   Uncheck the menu item to disable it.
   The speech viewer window contains a check box labeled "Show speech viewer on startup".
   If this is checked, the speech viewer will open when NVDA is started.
   The speech viewer window will always attempt to re-open with the same dimensions and location as when it was
   closed.
   While the speech viewer is enabled, it constantly updates to show you the most current text being spoken.
   However, if you click or focus inside the viewer, NVDA will temporarily stop updating the text, so that you
   are able to easily select or copy the existing content.
   To toggle the speech viewer from anywhere, please assign a custom gesture using the [Input Gestures dialog
   #InputGestures].

### Tilleggsbehandler {#AddonsManager}

   The Add-ons Manager, accessed by selecting Manage add-ons under Tools in the NVDA menu, allows you to install,
   uninstall, enable and disable add-on packages for NVDA.
   These packages are provided by the community and contain custom code that may add or change features in NVDA
   or even provide support for extra Braille displays or speech synthesizers.
   The Add-ons Manager contains a list that displays all the add-ons currently installed in your NVDA user
   configuration.
   Package name, status, version and author are shown for each add-on, though further information such as a
   description and URL can be viewed by selecting the add-on and pressing the About add-on button.
   If there is help available for the selected add-on, you can access it by pressing the Add-on help button.
   To browse and download available add-ons online, press the Get add-ons button.
   This button opens the [NVDA Add-ons page](https://addons.nvda-project.org/).
   If NVDA is installed and running on your system, you can open the add-on directly from the browser to begin
   the installation process as described below.
   Otherwise, save the add-on package and follow the instructions below.
   To install an Add-on you previously obtained, press the Install button.
   This will allow you to browse for an add-on package (.nvda-addon file) somewhere on your computer or on a
   network.
   Once you press Open, the installation process will begin.
   When an add-on is being installed, NVDA will first ask you to confirm that you really wish to install the
   add-on.
   As the functionality of add-ons is unrestricted inside NVDA, which in theory could include accessing your
   personal data or even the entire system if NVDA is an installed copy, it is very important to only install
   add-ons from sources you trust.
   Once the add-on is installed, NVDA must be restarted for the add-on to start running.
   Until you do, a status of "install" will show for that add-on in the list.
   To remove an add-on, select the add-on from the list and press the Remove button.
   NVDA will ask if you really wish to do this.
   As with installing, NVDA must be restarted for the add-on to be fully removed.
   Until you do, a status of "remove" will be shown for that add-on in the list.
   To disable an add-on, press the "disable" button.
   To enable a previously disabled add-on, press the "enable" button.
   You can disable an add-on if the add-on status indicates it is "enabled", or enable it if the add-on is
   "disabled".
   For each press of the enable/disable button, add-on status changes to indicate what will happen when NVDA
   restarts.
   If the addon was previously disabled, a status will show "enabled after restart". If the addon was previously
   "Enabled", a status will show "disabled after restart"
   Just like when you install or remove add-ons, you need to restart NVDA in order for changes to take effect.
   The manager also has a Close button to close the dialog.
   If you have installed, removed or changed the status of an add-on, NVDA will first ask you if you wish to
   restart so that your changes can take effect.
   In the past, it was possible to extend NVDA's functionality by copying individual plugins and drivers into
   your NVDA user Configuration directory.
   Although this version of NVDA may still load them, they will not be shown in the Add-on Manager.
   It is best to remove these files from your configuration and install the appropriate add-on if one is
   available.
   To access the Add-ons Manager from anywhere, please assign a custom gesture using the [Input Gestures dialog
   #InputGestures].

### Python-konsoll {#PythonConsole}

   The NVDA Python console, found under Tools in the NVDA menu, is a development tool which is useful for
   debugging, general inspection of NVDA internals or inspection of the accessibility hierarchy of an
   application.
   For more information, please see the [NVDA Developer Guide
   https://www.nvaccess.org/files/nvda/documentation/developerGuide.html].

### Reload plugins {#ReloadPlugins}

   This item, once activated, reloads app modules and global plugins without restarting NVDA, which can be useful
   for developers.

## Støttede talesynteser {#SupportedSpeechSynths}

Denne delen inneholder informasjon om talesynteser som støttes av NVDA.

En mer omfattende liste over gratis og kommersielle talesynteser du kan kjøpe og laste ned for bruk sammen med NVDA, finner du på siden [extra voices](https://github.com/nvaccess/nvda/wiki/ExtraVoices).

### eSpeak NG {#eSpeakNG}

Talesyntesen [eSpeak NG](https://github.com/espeak-ng/espeak-ng) er bygd inn i NVDA og krever ikke installasjon av andre drivere eller komponenter for å kunne brukes.

NVDA benytter eSpeak NG som standard.

Siden denne talesyntesen er bygd inn i NVDA, er dette et utmerket valg når du kjører NVDA fra en USB-minnepenn på andre systemer.

Hver stemme som leveres med eSpeak NG snakker et eget språk. eSpeak NG støtter over 43 ulike språk.

Det er også mange varianter som kan velges for å justere lyden av stemmen.

### Microsoft Speech API version 4 (SAPI 4) {#SAPI4}

   SAPI 4 is an older Microsoft standard for software speech synthesizers.
   NVDA still supports this for users who already have SAPI 4 synthesizers installed.
   However, Microsoft no longer support this and needed components are no longer available from Microsoft.
   When using this synthesizer with NVDA, the available voices (accessed from the [Speech category
   #SpeechSettings] of the [NVDA Settings](#NVDASettings) dialog or by the [Synth Settings Ring
   #SynthSettingsRing]) will contain all the voices from all the installed SAPI 4 engines found on your system.

### Microsoft Speech API version 5 (SAPI 5) {#SAPI5}

   SAPI 5 is a Microsoft standard for software speech synthesizers.
   Many speech synthesizers that comply with this standard may be purchased or downloaded for free from various
   companies and websites, though your system will probably already come with at least one SAPI 5 voice
   preinstalled.
   When using this synthesizer with NVDA, the available voices (accessed from the [Speech category
   #SpeechSettings] of the [NVDA Settings](#NVDASettings) dialog or by the [Synth Settings Ring
   #SynthSettingsRing]) will contain all the voices from all the installed SAPI 5 engines found on your system.

### Microsoft Speech Platform {#MicrosoftSpeechPlatform}

The Microsoft Speech Platform provides voices for many languages which are normally used in the development of
server-based speech applications.
These voices can also be used with NVDA.
To use these voices, you will need to install two components:

* Microsoft Speech Platform - Runtime (Version 11), x86: http://www.microsoft.com/download/en/details.aspx?id=27225
* Microsoft Speech Platform - Runtime Languages (Version 11): http://www.microsoft.com/download/en/details.aspx?id=27224
  * This page includes many files for both speech recognition and text-to-speech.
  Choose the files containing the TTS data for the desired languages/voices.
  For example, the file MSSpeech_TTS_en-US_ZiraPro.msi is a U.S. English voice.

### Windows OneCore-stemmer {#OneCore}

   Windows 10 includes new voices known as "OneCore" or "mobile" voices.
   Voices are provided for many languages, and they are more responsive than the Microsoft voices available using
   Microsoft Speech API version 5.
   Please see this Microsoft article for a list of available voices and instructions to install them:
   https://support.microsoft.com/en-us/help/22797/windows-10-narrator-tts-voices
   Please note that the faster rates available with Narrator are not currently available with NVDA.
   Also, the speed you select in the Windows Settings affects the rate set in NVDA.
   These are issues we cannot resolve without changes to Windows.
   We are hopeful that these will be addressed in a future Windows update.

### Audiologic Tts3 {#Audiologic}

   This is a commercial speech synthesizer specifically for the Italian language.
   You must have the synthesizer installed on your system in order for it to be used with NVDA.
   For more information, please visit the Audiologic website at [www.audiologic.it](http://www.audiologic.it).
   This synthesizer does not support [spelling functionality](#SpeechSettingsUseSpelling).

## Støttede leselister {#SupportedBrailleDisplays}

Denne delen inneholder informasjon om leselistene som støttes av NVDA.

### Freedom Scientific Focus/PAC Mate-serien {#FreedomScientificFocus}

Alle Focus- og PAC Mate-leselister [Freedom Scientific](http://www.freedomscientific.com/) støttes når de er tilkoblet via USB eller bluetooth.
Freedom Scientific sine leselistdrivere må være installert på systemet ditt for at NVDA skal fungere med disse leselistene.
Hvis du ikke alt har driverne, kan du få tak i dem her: http://www2.freedomscientific.com/downloads/focus-40-blue/focus-40-14-blue-downloads.asp.
Sellv om denne siden bare omtaler Focus Blue-leselistene, vil driverne støtte samtlige Focus- og PAC Mate-leselister fra Freedom Scientific.

Om systemet ditt kjører 64 bit Windows og driverne allerede er blitt installert av en annen skjermleser, vil du antakelig fortsatt behøve å installere driverne fra denne lenken, ettersom filene NVDA har bruk for antakelig ikke ble installert av den andre skjermleseren.

Som standard kan NVDA oppdage og koble seg til disse leselistene enten via USB eller bluetooth.

Når du konfigurerer leselisten, kan du imidlertid eksplisitt velge "USB" eller "Bluetooth"-port for å begrense hvilken tilkoblingstype som skal brukes. Dette kan være nyttig hvis du vil koble Focus-leselisten til NVDA via bluetooth, men samtidig kunne lade den via USB fra PC-en.

Her følger tastetilordningene for denne lesselisten med NVDA.
Vennligst se i dokumentasjonen for leselisten for å få en beskrivelse av hvor du finner disse tastene.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |topRouting1 (første celle på leselisten)|
|Gå framover med leselisten |topRouting20/40/80 (siste celle på leselisten)|
|Gå bakover med leselisten |leftAdvanceBar|
|Gå framover med leselisten |rightAdvanceBar|
|Bytt punktskrift knyttet til |leftGDFButton+rightGDFButton|
|Bytt handling på venstre wiz-hjul |leftWizWheelPress|
|Gå bakover med venstre wiz-hjulhandling |leftWizWheelUp|
|Gå framover med venstre wiz-hjulhandling |leftWizWheelDown|
|Bytt handling på høyre wiz-hjul |rightWizWheelPress|
|Move back using right wiz wheel action |rightWizWheelUp|
|Move forward using right wiz wheel action |rightWizWheelDown|
|Route to braille cell |routing|
|Skift+Tab |brailleSpaceBar+punkt1+punkt2|
|Tab |brailleSpaceBar+punkt4+punkt5|
|Pil opp |brailleSpaceBar+punkt1|
|Pil ned |brailleSpaceBar+punkt4|
|Ctrl+Pil venstre |brailleSpaceBar+punkt2|
|Ctrl+Pil høyre |brailleSpaceBar+punkt5|
|Pil venstre |brailleSpaceBar+punkt3|
|Pil høyre |brailleSpaceBar+punkt6|
|Home |brailleSpaceBar+punkt1+punkt3|
|End |brailleSpaceBar+punkt4+punkt6|
|control+home key |brailleSpaceBar+punkt1+punkt2+punkt3|
|control+end key |brailleSpaceBar+punkt4+punkt5+punkt6|
|alt key |brailleSpaceBar+punkt1+punkt3+punkt4|
|alt+tab key |brailleSpaceBar+punkt2+punkt3+punkt4+punkt5|
|alt+Skift+tab key |brailleSpaceBar+punkt1+punkt2+punkt5+punkt6|
|windows+tab key |brailleSpaceBar+punkt2+punkt3+punkt4|
|escape key |brailleSpaceBar+punkt1+punkt5|
|windows key |brailleSpaceBar+punkt2+punkt4+punkt5+punkt6|
|space key |brailleSpaceBar|
|windows+d key (minimize all applications) |brailleSpaceBar+punkt1+punkt2+punkt3+punkt4+punkt5+punkt6|
|Rapporter gjeldende linje |brailleSpaceBar+punkt1+punkt4|
|NVDA menu |brailleSpaceBar+punkt1+punkt3+punkt4+punkt5|

For nyere Focus-modeller som har vippeknapper (Focus 40, Focus 80 og Focus Blue):

| Navn |Tast|
|---|---|
|Move braille display to previous line |leftRockerBarUp, rightRockerBarUp|
|Move braille display to next line |leftRockerBarDown, rightRockerBarDown|

Bare for Focus 80:

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |leftBumperBarUp, rightBumperBarUp|
|Gå framover med leselisten |leftBumperBarDown, rightBumperBarDown|

<!-- KC:endInclude -->

### Optelec ALVA 6-serien/protokollkonverterer {#OptelecALVA}

Både ALVA BC640 og BC680-leselistene fra [Optelec](http://www.optelec.com/) kan tilkobles både med USB og bluetooth.

Alternativt kan du koble til en eldre Optelec-leselist, som Braille Voyager, via en protokollkonverterer som leveres av Optelec.
   You do not need any specific drivers to be installed to use these displays.
   Just plug in the display and configure NVDA to use it.
   Note: NVDA might be unable to use an ALVA BC6 display over Bluetooth when it is paired using the ALVA
   Bluetooth utility.
   When you have paired your device using this utility and NVDA is unable to detect your device, we recommend you
   to pair your ALVA display the regular way using the Windows Bluetooth settings.
   Note: while some of these displays do have a braille keyboard, they handle translation from braille to text
   themselves by default.
   This means that NVDA's braille input system is not in use in the default situation (i.e. the input braille
   table setting has no effect).
   For ALVA displays with recent firmware, it is possible to disable this HID keyboard simulation using an input
   gesture.
   Following are key assignments for this display with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |t1 eller etouch1|
|Flytt leselisten til forrige linje |t2|
|Flytt til gjeldende fokus |t3|
|Flytt leselisten til neste linje |t4|
|Gå framover med leselisten |t5 eller etouch3|
|Route to braille cell |routing|
|Rapporter tekstformatering under punktskriftcellen |sekundær markørhenter|
|Toggle simulering av HID-tastatur |t1+spEnter|
|Move to top line in review |t1+t2|
|Move to bottom line in review |t4+t5|
|Bytt leselist knyttet til |t1+t3|
|Rapporter tittel |etouch2|
|Rapporter statuslinje |etouch4|
|Skift+Tab |sp1|
|Alt |sp2|
|Escape |sp3|
|Tab |sp4|
|Pil opp |spUp|
|Pil ned |spDown|
|Pil venstre |spLeft|
|Pil høyre |spRight|
|Enter |spEnter, enter|
|Rapporter dato/tid |sp1+sp2|
|NVDA-meny |sp1+sp3|
|Win+d (minimer alle programmer) |sp1+sp4|
|Win+b (fokus på systemkurv) |sp3+sp4|
|Win |sp2+sp3, windows|
|Alt+tab |sp2+sp4|
|Ctrl+Home |t3+spUp|
|Ctrl+End |t3+spDown|
|Home |t3+spLeft|
|End |t3+spRight|
|Alt |alt|
|Ctrl |control|

<!-- KC:endInclude -->

### Handy Tech-leselister {#HandyTech}

NVDA støtter de fleste leselister fra [Handy Tech](http://www.handytech.de/) når de er koblet til via USB, serieport eller bluetooth.
   For older USB displays, you will need to install the USB drivers from Handy Tech on your system.
   The following displays are not supported out of the box, but can be used via [Handy Tech's universal driver
   https://handytech.de/en/service/downloads-and-manuals/handy-tech-software/braille-display-drivers] and NVDA
   add-on:

* Braillino
* Bookworm
* Modular-leselister med internprogramvare versjon 1.13 eller lavere. Vær oppmerksom på at internprogramvaren på disse leselistene kan oppdateres.

   Following are the key assignments for Handy Tech displays with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |venstre, opp, b3|
|Gå framover med leselisten |høyre, ned, b6|
|Flytt leselisten til forrige linje |b4|
|Flytt leselisten til neste linje |b5|
|Route to braille cell |routing|
|Skift+Tab |esc, venstre trippeltast opp+ned|
|Alt |b2+b4+b5|
|Escape |b4+b6|
|Tab |enter, høyre trippeltast opp+ned|
|enter key |esc+enter, left+right triple action key up+down, joystickAction|
|Pil opp |joystickUp|
|Pil ned |joystickDown|
|leftArrow key |joystickLeft|
|rightArrow key |joystickRight|
|NVDA-meny |b2+b4+b5+b6|
|Bytt punktskrift knyttet til |b2|
|Bytt punktskriftmarkør |b1|
|Bytt presentasjon av fokuskontekst |b7|
|Bytt punktskrift inndata |mellomrom+b1+b3+b4 (mellomrom+stor B)|

<!-- KC:endInclude -->

### MDV Lilli {#MDVLilli}

   The Lilli braille display available from [MDV](http://www.mdvbologna.it/) is supported.
   You do not need any specific drivers to be installed to use this display.
   Just plug in the display and configure NVDA to use it.
   Following are the key assignments for this display with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Scroll braille display backward |LF|
|Gå framover med leselisten |RG|
|Move braille display to previous line |UP|
|Move braille display to next line |DN|
|Route to braille cell |route|
|Skift+Tab |SLF|
|Tab |SRG|
|Alt+Tab |SDN|
|Alt+Skift+Tab |SUP|

<!-- KC:endInclude -->

### Baum/Humanware/APH/Orbit-leselister {#Baum}

Flere leselister fra [Baum](http://www.baum.de/cms/en/), [HumanWare](http://www.humanware.com/), [APH](http://www.aph.org/) og [Orbit](http://www.orbitresearch.com/) er støttes når de er tilkoblet via USB, bluetooth eller serieport. Disse omfatter:

* Baum: SuperVario, PocketVario, VarioUltra, Pronto!, SuperVario2, Vario 340
* HumanWare: Brailliant, BrailleConnect, Brailliant2
* APH: Refreshabraille
* Orbit: Orbit Reader 20

Enkelte andre leselister produsert av BAUM kan også fungere, men dette har ikke blitt testet.

Om du oppretter en tilkobling via USB til leselister som ikke benytter HID, må du først installere USB-driverne som leveres av produsenten.

VarioUltra og Pronto! benytter HID.

Refreshabraille og Orbit Reader 20 kan benytte HID hvis de konfigureres for det.

   The USB serial mode of the Orbit Reader 20 is currently only supported in Windows 10.
   USB HID should generally be used instead.
   Following are the key assignments for these displays with NVDA.
   Please see your display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |d2|
|Gå framover med leselisten |d5|
|Flytt leselisten til forrige linje |d1|
|Flytt leselisten til neste linje |d3|
|Route to braille cell |routing|

For leselister som har en joystick:

| Navn |Tast|
|---|---|
|Pil opp |opp|
|Pil ned |ned|
|Pil venstre |venstre|
|Pil høyre |høyre|
|Enter |velg|

<!-- KC:endInclude -->

### hedo ProfiLine USB {#HedoProfiLine}

   The hedo ProfiLine USB from [hedo Reha-Technik](http://www.hedo.de/) is supported.
   You must first install the USB drivers provided by the manufacturer.
   Following are the key assignments for this display with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |K1|
|Gå framover med leselisten |K3|
|Flytt leselist til forrige linje |B2|
|Flytt leselisst til neste linje |B5|
|Route to braille cell |routing|
|Bytt punktskrift knyttet til |K2|
|Say all |B6|

<!-- KC:endInclude -->

### hedo MobilLine USB {#HedoMobilLine}

   The hedo MobilLine USB from [hedo Reha-Technik](http://www.hedo.de/) is supported.
   You must first install the USB drivers provided by the manufacturer.
   Following are the key assignments for this display with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |K1|
|Gå framover med leselisten |K3|
|Move braille display to previous line |B2|
|Move braille display to next line |B5|
|Route to braille cell |routing|
|Toggle braille tethered to |K2|
|Say all |B6|

<!-- KC:endInclude -->

### HumanWare Brailliant BI/B Series / BrailleNote Touch {#HumanWareBrailliant}

   The Brailliant BI and B series of displays from [HumanWare](http://www.humanware.com/), including the BI 14, BI
   32, BI 40 and B 80, are supported when connected via USB or bluetooth.
   If connecting via USB with the protocol set to HumanWare, you must first install the USB drivers provided by
   the manufacturer.
   USB drivers are not required if the protocol is set to OpenBraille.
   The BrailleNote Touch is also supported, and does not require any drivers to be installed.
   Following are the key assignments for the Brailliant BI/B and BrailleNote touch displays with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.

#### Key assignments for All models {#toc219}

<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |venstre|
|Gå framover med leselisten |høyre|
|Flytt leselisten til forrige linje |opp|
|Flytt leselisten til neste linje |ned|
|Route to braille cell |routing|
|Bytt punktskrift knyttet til |opp+ned|
|Pil opp |mellomrom+punkt1|
|Pil ned |mellomrom+punkt4|
|Pil venstre |mellomrom+punkt3|
|Pil høyre |mellomrom+punkt6|
|Skift+Tab |mellomrom+punkt1+punkt3|
|Tab |mellomrom+punkt4+punkt6|
|Alt |mellomrom+punkt1+punkt3+punkt4 (mellomrom+m)|
|Escape |mellomrom+punkt1+punkt5 (mellomrom+e)|
|Enter |punkt8|
|windows key |mellomrom+punkt3+punkt4|
|Alt+Tab |mellomrom+punkt2+punkt3+punkt4+punkt5 (mellomrom+t)|
|NVDA-meny |mellomrom+punkt1+punkt3+punkt4+punkt5 (mellomrom+n)|
|windows+d key (minimize all applications) |mellomrom+punkt1+punkt4+punkt5 (mellomrom+d)|
|Say all |mellomrom+punkt1+punkt2+punkt3+punkt4+punkt5+punkt6|

<!-- KC:endInclude -->

#### Tastetilordninger for Brailliant BI 32, BI 40 og B 80 {#toc220}

<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|NVDA-meny |c1+c3+c4+c5 (kommando n)|
|windows+d key (minimize all applications) |c1+c4+c5 (command d)|
|Say all |c1+c2+c3+c4+c5+c6|

<!-- KC:endInclude -->

#### Tastetilordninger for Brailliant BI 14 {#toc221}

<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Pil opp |joystick opp|
|Pil ned |joystick ned|
|Pil venstre |joystick venstre|
|Pil høyre |joystick høyre|
|Enter |joystick-handling|

<!-- KC:endInclude -->

### HIMS Braille Sense/Braille EDGE/Smart Beetle/Sync Braille-serien {#Hims}

   NVDA supports Braille Sense, Braille EDGE, Smart Beetle and Sync Braille displays from [Hims
   http://www.hims-inc.com/] when connected via USB or bluetooth.
   If connecting via USB, you will need to install the USB drivers from HIMS on your system.
   You can download these from here: http://www.himsintl.com/upload/HIMS_USB_Driver_v25.zip
   Following are the key assignments for these displays with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Route to braille cell |routing|
|Gå bakover med leselisten |leftSideScrollUp, rightSideScrollUp, leftSideScroll|
|Gå framover med leselisten |leftSideScrollDown, rightSideScrollDown, rightSideScroll|
|Flytt leselisten til forrige linje |leftSideScrollUp+rightSideScrollUp|
|Flytt leselisten til neste linje |leftSideScrollDown+rightSideScrollDown|
|Move to previous line in review |rightSideUpArrow|
|Move to next line in review |rightSideDownArrow|
|Move to previous character in review |rightSideLeftArrow|
|Move to next character in review |rightSideRightArrow|
|Move to current focus |leftSideScrollUp+leftSideScrollDown, rightSideScrollUp+rightSideScrollDown,|

   leftSideScroll+rightSideScroll |

|Ctrl |smartbeetle:f1, brailleedge:f3|
|Windows |f7, smartbeetle:f2|
|Alt |punkt1+punkt3+punkt4+mellomrom, f2, smartbeetle:f3, brailleedge:f4|
|Skift |f5|
|Insert |punkt2+punkt4+space, f6|
|applications key |punkt1+punkt2+punkt3+punkt4+space, f8|
|CapsLock |punkt1+punkt3+punkt6+mellomrom|
|Tab |punkt4+punkt5+mellomrom, f3, brailleedge:f2|
|Skift+Alt+Tab |f2+f3+f1|
|Alt+Tab |f2+f3|
|Skift+Tab |punkt1+punkt2+mellomrom|
|End |punkt4+punkt6+mellomrom|
|control+end key |punkt4+punkt5+punkt6+space|
|home key |punkt1+punkt3+space, smartbeetle:f4|
|control+home key |punkt1+punkt2+punkt3+space|
|Alt+F4 |punkt1+punkt3+punkt5+punkt6+mellomrom|
|Pil venstre |punkt3+mellomrom, leftSideLeftArrow|
|control+Skift+leftArrow key |punkt2+punkt8+mellomrom+f1|
|control+leftArrow key |punkt2+space|
|Skift+Alt+Pil venstre |punkt2+punkt7+f1|
|Alt+Pil venstre |punkt2+punkt7|
|Pil høyre |punkt6+mellomrom, leftSideRightArrow|
|Ctrl+Skift+Pil høyre |punkt5+punkt8+mellomrom+f1|
|Ctrl+Pil høyre |punkt5+mellomrom|
|Skift+Alt+Pil høyre |punkt5+punkt7+f1|
|Alt+Pil høyre |punkt5+punkt7|
|pageUp key |punkt1+punkt2+punkt6+space|
|control+pageUp key |punkt1+punkt2+punkt6+punkt8+space|
|PilOpp key |punkt1+space, leftSideUpArrow|
|Ctrl+Skift+Pil opp |punkt2+punkt3+punkt8+mellomrom+f1|
|Ctrl+Pil opp |punkt2+punkt3+mellomrom|
|Skift+Alt+Pil opp |punkt2+punkt3+punkt7+f1|
|Alt+Pil opp |punkt2+punkt3+punkt7|
|shift+PilOpp key |leftSideScrollDown+space|
|PageDown |punkt3+punkt4+punkt5+mellomrom|
|Ctrl+PageDown |punkt3+punkt4+punkt5+punkt8+mellomrom|
|PilNed key |punkt4+space, leftSideDownArrow|
|Ctrl+Skift+Pil ned |punkt5+punkt6+punkt8+mellomrom+f1|
|Ctrl+Pil ned |punkt5+punkt6+mellomrom|
|Skift+Alt+Pil ned |punkt5+punkt6+punkt7+f1|
|Alt+Pil ned |punkt5+punkt6+punkt7|
|shift+PilNed key |mellomrom+rightSideScrollDown|
|escape key |punkt1+punkt5+space, f4, brailleedge:f1|
|delete key |punkt1+punkt3+punkt5+space, punkt1+punkt4+punkt5+space|
|f1 key |punkt1+punkt2+punkt5+space|
|F3 |punkt1+punkt2+punkt4+punkt8|
|F4 |punkt7+F3|
|Windows+b |punkt1+punkt2+f1|
|windows+d key |punkt1+punkt4+punkt5+f1|
|control+insert key |smartbeetle:f1+rightSideScroll|
|alt+insert key |smartbeetle:f3+rightSideScroll|

<!-- KC:endInclude -->

### Seika leselister {#Seika}

Leselistene Seika Versjon 3, 4 og 5 (40 celler) og Seika80 (80 celler) fra [Nippon Telesoft](http://www.nippontelesoft.com/) støttes.

Du kan finner mer informasjon om disse leselistene her: http://www.seika-braille.com/.

Du må først installere USB-driverne fra produsenten før disse leselistene kan brukes sammen med NVDA.

Følgende er tastetilordningene for disse leselistene med NVDA. Se i dokumentasjonen for disse leselistene for å få en beskrivelse av hvor de ulike tastene er å finne.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |venstre|
|Gå framover med leselisten |høyre|
|Flytt leselisten til forrige linje |b3|
|Flytt leselisten til neste linje |b4|
|Bytt punktskrift knyttet til |b5|
|Say all |b6|
|Tab |b1|
|Skift+Tab |b2|
|Alt+Tab |b1+b2|
|NVDA-meny |venstre+høyre|
|Route to braille cell |routing|

<!-- KC:endInclude -->

### Papenmeier BRAILLEX nyere modeller {#Papenmeier}

Følgende leselister støttes:

* BRAILLEX EL 40c, EL 80c, EL 20c, EL 60c (USB)
* BRAILLEX EL 40s, EL 80s, EL 2d80s, EL 70s, EL 66s (USB)
* BRAILLEX Trio (USB og bluetooth)
* BRAILLEX Live 20, BRAILLEX Live og BRAILLEX Live Plus (USB and bluetooth)

   If BrxCom is installed, NVDA will use BrxCom.
   BrxCom is a tool that allows keyboard input from the braille display to function independently from a screen
   reader.
   A new version of BrxCom which works with NVDA will be released by Papenmeier soon.
   Keyboard input is possible with the Trio and BRAILLEX Live models.
   Most devices have an Easy Access Bar (EAB) that allows intuitive and fast operation.
   The EAB can be moved in four directions where generally each direction has two switches.
   The C and Live series are the only exceptions to this rule.
   The c-series and some other displays have two routing rows whereby the upper row is used to report formatting
   information.
   Holding one of the upper routing keys and pressing the EAB on c-series devices emulates the second switch
   state.
   The live series displays have one routing row only and the EAB has one step per direction.
   The second step may be emulated by pressing one of the routing keys and pressing the EAB in the corresponding
   direction.
   Pressing and holding the up, down, right and left keys (or EAB) causes the corresponding action to be
   repeated.
   Generally, the following keys are available on these braille displays:

| Navn |Tast|
|---|---|
|l1 |Left front key|
|l2 |Left rear key|
|r1 |Right front key|
|r2 |Right rear key|
|up |1 Step up|
|up2 |2 Steps up|
|left |1 Step left|
|left2 |2 Steps left|
|right |1 Step right|
|right2 |2 Steps right|
|dn |1 Step down|
|dn2 |2 Steps down|

   Following are the Papenmeier command assignments for NVDA:

<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |venstre|
|Gå framover med leselisten |høyre|
|Flytt leselisten til forrige linje |opp|
|Flytt leselisten til neste linje |ned|
|Route to braille cell |routing|
|Report current character in review |l1|
|Aktiver gjeldende navigasjonsobjekt |l2|
|Bytt knytt punktskrift til |r2|
|Rapporter tittel |l1+opp|
|Rapporter statuslinje |l2+ned|
|Move to containing object |up2|
|Move to first contained object |dn2|
|Move to previous object |left2|
|Move to next object |right2|
|Report text formatting under braille cell |upper routing row|

<!-- KC:endInclude -->

   The Trio model has four additional keys which are in front of the braille keyboard.
   These are (ordered from left to right):

   * left thumb key (lt)
   * space
   * space
   * right thumb key (rt)

   Currently, the right thumb key is not in use.
   The inner keys are both mapped to space.

| Navn |Tast|
|---|---|

<!-- KC:beginInclude -->

|escape key |space with dot 7|
|PilOpp key |space with dot 2|
|leftArrow key |space with dot 1|
|rightArrow key |space with dot 4|
|PilNed |space with dot 5|
|control key |lt+punkt2|
|alt key |lt+punkt3|
|control+escape key |space with dot 1 2 3 4 5 6|
|tab key |space with dot 3 7|

<!-- KC:endInclude -->

### Papenmeier Braille BRAILLEX eldre modeller {#PapenmeierOld}

   The following Braille displays are supported:

   * BRAILLEX EL 80, EL 2D-80, EL 40 P
   * BRAILLEX Tiny, 2D Screen

   Note that these displays can only be connected via a serial port.
   Therefore, you should select the port to which the display is connected after you have chosen this driver in
   the [Select Braille Display](#SelectBrailleDisplay) dialog.
   Some of these devices have an Easy Access Bar (EAB) that allows intuitive and fast operation.
   The EAB can be moved in four directions where generally each direction has two switches.
   Pressing and holding the up, down, right and left keys (or EAB) causes the corresponding action to be
   repeated.
   Older devices do not have an EAB; front keys are used instead.
   Generally, the following keys are available on braille displays:

| Navn |Tast|
|---|---|
|l1 |Left front key|
|l2 |Left rear key|
|r1 |Right front key|
|r2 |Right rear key|
|up |1 Step up|
|up2 |2 Steps up|
|left |1 Step left|
|left2 |2 Steps left|
|right |1 Step right|
|right2 |2 Steps right|
|dn |1 Step down|
|dn2 |2 Steps down|

   Following are the Papenmeier command assignments for NVDA:
<!-- KC:beginInclude -->
   Devices with EAB:

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |venstre|
|Gå framover med leselisten |høyre|
|Flytt leselisten til forrige linje |opp|
|Flytt leselisten til neste linje |ned|
|Route to braille cell |routing|
|Report current character in review |l1|
|Activate current navigator object |l2|
|Report title |l1up|
|Report Status Bar |l2down|
|Move to containing object |up2|
|Move to first contained object |dn2|
|Move to next object |right2|
|Move to previous object |left2|
|Report text formatting under braille cell |upper routing strip|

BRAILLEX Tiny:

| Navn |Tast|
|---|---|
|Report current character in review |l1|
|Aktiver gjeldende navigasjonsobjekt |l2|
|Gå bakover med leselisten |venstre|
|Gå framover med leselisten |høyre|
|Flytt leselisten til forrige linje |opp|
|Flytt leselisten til neste linje |ned|
|Toggle braille tethered to |r2|
|Move to containing object |r1+up|
|Move to first contained object |r1+dn|
|Move to previous object |r1+left|
|Move to next object |r1+right|
|Report text formatting under braille cell |upper routing strip|
|Report title |l1+up|
|Report status bar |l2+down|

BRAILLEX 2D Screen:

| Navn |Tast|
|---|---|
|Report current character in review |l1|
|Activate current navigator object |l2|
|Toggle braille tethered to |r2|
|Report text formatting under braille cell |upper routing strip|
|Flytt leselisten til forrige linje |opp|
|Gå bakover med leselisten |venstre|
|Gå framover med leselisten |høyre|
|Flytt leselisten til neste linje |ned|
|Gå til neste objekt |left2|
|Move to containing object |up2|
|Move to first contained object |dn2|
|Gå til forrige objekt |right2|

<!-- KC:endInclude -->

### HumanWare BrailleNote {#HumanWareBrailleNote}

   NVDA supports the BrailleNote notetakers from [Humanware](http://www.humanware.com) when acting as a display
   terminal for a screen reader.
   The following models are supported:

   * BrailleNote Classic (serial connection only)
   * BrailleNote PK (Serial and bluetooth connections)
   * BrailleNote MPower (Serial and bluetooth connections)
   * BrailleNote Apex (USB and Bluetooth connections)

   For BrailleNote Touch, please refer to the [Brailliant BI Series / BrailleNote Touch](HumanWareBrailliant)
   section.
   Except for BrailleNote PK, both braille (BT) and QWERTY (QT) keyboards are supported.
   For BrailleNote QT, PC keyboard emulation isn't supported.
   You can also enter braille dots using the QT keyboard.
   Please check the braille terminal section of the BrailleNote manual guide for details.
   If your device supports more than one type of connection, when connecting your BrailleNote to NVDA, you must
   set the braille terminal port in braille terminal options.
   Please check the BrailleNote manual for details.
   In NVDA, you may also need to set the port in the [Select Braille Display](#SelectBrailleDisplay) dialog.
   If you are connecting via USB or bluetooth, you can set the port to "Automatic", "USB" or "Bluetooth",
   depending on the available choices.
   If connecting using a legacy serial port (or a USB to serial converter) or if none of the previous options
   appear, you must explicitly choose the communication port to be used from the list of hardware ports.
   Before connecting your BrailleNote Apex using its USB client interface, you must install the drivers provided
   by HumanWare.
   On the BrailleNote Apex BT, you can use the scroll wheel located between dots 1 and 4 for various NVDA
   commands.
   The wheel consists of four directional dots, a center click button, and a wheel that spins clockwise or
   counterclockwise.
   Following are the BrailleNote command assignments for NVDA.
   Please check your BrailleNote's documentation to find where these keys are located.

<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |bakover|
|Gå framover med leselisten |framover|
|Flytt leselisten til forrige linje |forrige|
|Flytt leselisten til neste linje |neste|
|Route to braille cell |routing|
|NvDA-meny |mellomrom+punkt1+punkt3+punkt4+punkt5 (mellomrom+n)|
|Toggle braille tethered to |previous+next|
|Up arrow key |mellomrom+punkt1|
|Down arrow key |mellomrom+punkt4|
|Left Arrow key |mellomrom+punkt3|
|Right arrow key |mellomrom+punkt6|
|Page up key |mellomrom+punkt1+punkt3|
|Page down key |mellomrom+punkt4+punkt6|
|Home |mellomrom+punkt1+punkt2|
|End |mellomrom+punkt4+punkt5|
|Ctrl+Home |mellomrom+punkt1+punkt2+punkt3|
|Ctrl+End |mellomrom+punkt4+punkt5+punkt6|
|Space key |space|
|Enter |mellomrom+punkt8|
|Backspace |mellomrom+punkt7|
|Tab key |mellomrom+punkt2+punkt3+punkt4+punkt5 (mellomrom+t)|
|Shift+tab keys |mellomrom+punkt1+punkt2+punkt5+punkt6|
|Windows key |mellomrom+punkt2+punkt4+punkt5+punkt6 (mellomrom+w)|
|Alt key |mellomrom+punkt1+punkt3+punkt4 (mellomrom+m)|
|Toggle input help |mellomrom+punkt2+punkt3+punkt6 (mellomrom+lower h)|

   Following are commands assigned to BrailleNote QT when it is not in braille input mode.

| Navn |Tast|
|---|---|
|NvDA menu |read+n|
|Up arrow key |PilOpp|
|Down arrow key |PilNed|
|Left Arrow key |leftArrow||
|Right arrow key |rightArrow|
|Page up key |function+PilOpp|
|Page down key |function+PilNed|
|Home key |function+leftArrow|
|End key |function+rightArrow|
|Control+home keys |read+t|
|Ctrl+End |read+b|
|Enter |Enter|
|Slett bakover |Slett bakover|
|Tab |Tab|
|Skift+Tab |Skift+Tab|
|Windows-tast |read+w|
|Alt |read+m|
|Slå hjelp for inndata på/av |read+1|

Følgende er kommandoer knyttet til rullehjulet:

| Navn |Tast|
|---|---|
|Pil opp |Pil opp|
|Pil ned |Pil ned|
|Venstre piltast |Pil venstre|
|Høyre piltast |Pil høyre|
|Enter |Senterknapp|
|Tab |rull hjulet med klokken|
|Skift+Tab |rull hjulet mot klokken|

<!-- KC:endInclude -->

### EcoBraille {#EcoBraille}

NVDA støtte EcoBraille-leselister fra [ONCE](http://www.once.es/).

Følgende modeller støttes:

* EcoBraille 20
* EcoBraille 40
* EcoBraille 80
* EcoBraille Plus

I NVDA kan du sette serieporten leselisten er koblet til i dialogen [Velg leselist](#SelectBrailleDisplay).
   Following are the key assignments for EcoBraille displays.
   Please see the [EcoBraille documentation](ftp://ftp.once.es/pub/utt/bibliotecnia/Lineas_Braille/ECO/) for
   descriptions of where these keys can be found.

<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |T2|
|Gå framover med leselisten |T4|
|Flytt leselisten til forrige linje |T1|
|Flytt leselisten til neste linje |T5|
|Route to braille cell |Routing|
|Activate current navigator object |T3|
|Switch to next review mode |F1|
|Move to containing object |F2|
|Switch to previous review mode |F3|
|Move to previous object |F4|
|Report current object |F5|
|Move to next object |F6|
|Move to focus object |F7|
|Move to first contained object |F8|
|Flytt systemfokus eller markør til gjeldende leseposisjon |F9|
|Report review cursor location |F0|
|Toggle braille tethered to |A|

<!-- KC:endInclude -->

### SuperBraille {#SuperBraille}

   The SuperBraille device, mostly available in Taiwan, can be connected to by either USB or serial.
   As the SuperBraille does not have any physical typing keys or scrolling buttons, all input must be performed
   via a standard computer keyboard.
   Due to this, and to maintain compatibility with other screen readers in Taiwan, two key bindings for scrolling
   the braille display have been provided:
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |numerisk minus|
|Gå framover med leselisten |numerisk pluss|

<!-- KC:endInclude -->

### Eurobraille Esys/Esytime/Iris leselister {#Eurobraille}

   The Esys, Esytime and Iris displays from [Eurobraille](http://www.eurobraille.fr/) are supported by NVDA.
   Esys and Esytime-Evo devices are supported when connected via USB or bluetooth.
   Older Esytime devices only support USB.
   Iris displays can only be connected via a serial port.
   Therefore, for these displays, you should select the port to which the display is connected after you have
   chosen this driver in the Braille Settings dialog.
   Iris and Esys displays have a braille keyboard with 10 keys.
   Of the two keys placed like a space bar, the left key is corresponding to the backspace key and the right key
   to the space key.
   Following are the key assignments for these displays with NVDA.
   Please see the display's documentation for descriptions of where these keys can be found.
<!-- KC:beginInclude -->

| Navn |Tast|
|---|---|
|Gå bakover med leselisten |switch1-6Venstre, l1|
|Gå framover med leselisten |switch1-6Høyre, l8|
|Flytt til gjeldende fokus |switch1-6Venstre+switch1-6Høyre, l1+l8|
|Route to braille cell |routing|
|Report text formatting under braille cell |doubleRouting|
|Move to previous line in review |joystick1Up|
|Move to next line in review |joystick1Down|
|Move to previous character in review |joystick1Left|
|Move to next character in review |joystick1Right|
|Switch to previous review mode |joystick1Left+joystick1Up|
|Switch to next review mode |joystick1Right+joystick1Down|
|Erase the last entered braille cell or character |backSpace|
|Translate any braille input and press the enter key |backSpace+space|
|insert key |punkt3+punkt5+space, l7|
|delete key |punkt3+punkt6+space|
|home key |punkt1+punkt2+punkt3+space, joystick2Left+joystick2Up|
|end key |punkt4+punkt5+punkt6+space, joystick2Right+joystick2Down|
|PilVenstre |punkt2+space, joystick2Left, leftArrow|
|Pil høyre |punkt5+mellomrom, joystick2Høyre, Pil høyre|
|Pil opp |punkt1+mellomrom, joystick2Opp, Pil opp|
|Pil ned |punkt6+mellomrom, joystick2Ned, Pil ned|
|enter key |joystick2Center|
|pageUp key |punkt1+punkt3+space|
|pageDown key |punkt4+punkt6+space|
|numerisk 1 |punkt1+punkt6+backspace|
|numerisk 2 |punkt1+punkt2+punkt6+backspace|
|numerisk 3 |punkt1+punkt4+punkt6+backspace|
|numpad4 key |punkt1+punkt4+punkt5+punkt6+backspace|
|numpad5 key |punkt1+punkt5+punkt6+backspace|
|numpad6 key |punkt1+punkt2+punkt4+punkt6+backspace|
|numpad7 key |punkt1+punkt2+punkt4+punkt5+punkt6+backspace|
|numpad8 key |punkt1+punkt2+punkt5+punkt6+backspace|
|numpad9 key |punkt2+punkt4+punkt6+backspace|
|numpadInsert key |punkt3+punkt4+punkt5+punkt6+backspace|
|numpadDecimal key |punkt2+backspace|
|numpadDivide key |punkt3+punkt4+backspace|
|numpadMultiply key |punkt3+punkt5+backspace|
|numpadMinus key |punkt3+punkt6+backspace|
|numpadPlus key |punkt2+punkt3+punkt5+backspace|
|numpadEnter key |punkt3+punkt4+punkt5+backspace|
|escape key |punkt1+punkt2+punkt4+punkt5+space, l2|
|Tab |punkt2+punkt5+punkt6+mellomrom, l3|
|Skift+Tab |punkt2+punkt3+punkt5+mellomrom|
|printScreen key |punkt1+punkt3+punkt4+punkt6+space|
|Pause |punkt1+punkt4+mellomrom|
|applications key |punkt5+punkt6+backspace|
|F1 |punkt1+slett bakover|
|F2 |punkt1+punkt2+slett bakover|
|F3 |punkt1+punkt4+slett bakover|
|F4 |punkt1+punkt4+punkt5+slett bakover|
|F5 |punkt1+punkt5+slett bakover|
|F6 |punkt1+punkt2+punkt4+slett bakover|
|F7 |punkt1+punkt2+punkt4+punkt5+slett bakover|
|F8 |punkt1+punkt2+punkt5+slett bakover|
|F9 |punkt2+punkt4+slett bakover|
|F10 |punkt2+punkt4+punkt5+slett bakover|
|F11 |punkt1+punkt3+slett bakover|
|F12 |punkt1+punkt2+punkt3+slett bakover|
|Windows-tasten |punkt1+punkt2+punkt3+punkt4+slett bakover|
|CapsLock |punkt7+slett bakover, punkt8+slett bakover|
|NumLock |punkt3+slett bakover, punkt6+slett bakover|
|Skift |punkt7+mellomrom, l4|
|Toggle shift key |punkt1+punkt7+space, punkt4+punkt7+space|
|Ctrl |punkt7+punkt8+mellomrom, l5|
|Toggle control key |punkt1+punkt7+punkt8+space, punkt4+punkt7+punkt8+space|
|Alt |punkt8+mellomrom, l6|
|Toggle alt key |punkt1+punkt8+space, punkt4+punkt8+space|
|ToggleHID keyboard input simulation |esytime):l1+joystick1Down, esytime):l8+joystick1Down|

<!-- KC:endInclude -->

### BRLTTY {#BRLTTY}

[BRLTTY](http://www.brltty.com/) er et separat program som kan brukes til å støtte flere leselister.

For å kunne bruke dette programmet, må du installere [BRLTTY for Windows](http://www.brltty.com/download.html). Du bør laste ned og installere den nyeste installasjonspakken, som vil  hete noe slikt som brltty-win-5.2-2.exe.

Når du konfigurerer leselisten og porten som skal brukes, så følg nøye med på introduksjonene, særlig om du har en USB-leselist og allerede har installert produsentens drivere.

For leselister som har punktskrifttastatur, støtter BRLTTY nå skriving av punktskrift selv. Derfor er NVDAs valg for inndatatabell ikke relevant i et slikt tilfelle.

Her er BRLTTYs kommandotilordninger for NVDA. Vennligst se [BRLTTY key binding lists](http://mielke.cc/brltty/doc/KeyBindings/) for informasjon om hvordan BRLTTY-kommandoer er knyttet til knapper og kontroller på leselister.
<!-- KC:beginInclude -->

| Navn |BRLTTY-kommando|
|---|---|
|Gå bakover med leselisten |fwinlt (gå til venstre ett vindu)|
|Gå framover med leselisten |fwinrt (gå til høyre ett vindu)|
|Flytt leselisten til forrige linje |lnup (gå opp en linje)|
|Flytt leselisten til neste linje |lndn (gå ned en linje)|
|Hent markør til punktskriftcelle |route (bring markør til tegn)|

<!-- KC:endInclude -->

## Avanserte temaer {#AdvancedTopics}
### Kommandolinjevalg {#CommandLineOptions}

   NVDA can accept one or more additional options when it starts which alter its behavior.
   You can pass as many options as you need.
   These options can be passed when starting from a shortcut (in the shortcut properties), from the Run dialog
   (Start Menu -> Run or Windows+r) or from a Windows command console.
   Options should be separated from the name of NVDA's executable file and from other options by spaces.
   For example, the Desktop shortcut that NVDA creates during installation has the -r option, which tells NVDA to
   close the currently running copy before starting the new one.
   Another useful option is --disable-addons, which tells NVDA to suspend all running add-ons.
   This allows you to determine whether a problem is caused by an add-on and to recover from serious problems
   caused by add-ons.
   As an example, you can exit the currently running copy of NVDA by entering the following in the Run dialog:
   nvda -q
   Some of the command line options have a short and a long version, while some of them have only a long version.
   For those which have a short version, you can combine them like this:

|nvda -rm |This will exit the currently running copy of NVDA and will start a new copy with startup sounds|

   disabled, etc. |

|nvda -rm --disable-addons |Same as above, but with add-ons disabled|

   Some of the command line options accept additional parameters; e.g. how detailed the logging should be or the
   path to the user configuration directory.
   Those parameters should be placed after the option, separated from the option by a space when using the short
   version or an equals sign (=) when using the long version; e.g.:

|nvda -l 10 |Tells NVDA to start with log level set to debug|
|nvda --log-file=c:\nvda.log |Tells NVDA to write its log to c:\nvda.log|
|nvda --log-level=20 -f c:\nvda.log |Tells NVDA to start with log level set to info and to write its log to|

   c:\nvda.log |
   Following are the command line options for NVDA:

| Short |Long |Beskrivelse|
|---|---|---|
|-h |--help |show command line help and exit|
|-q |--quit |Quit already running copy of NVDA|
|-r |--replace |Quit already running copy of NVDA and start this one|
|-k |--check-running |Report whether NVDA is running via the exit code; 0 if running, 1 if not running|
|-f LOGFILENAME |--log-file=LOGFILENAME |The file where log messages should be written to|
|-l LOGLEVEL |--log-level=LOGLEVEL |The lowest level of message logged (debug 10, info 20, warning 30,|

   error 40, critical 50), default is warning |

|-c CONFIGPATH |--config-path=CONFIGPATH |The path where all settings for NVDA are stored|
|-m |--minimal |No sounds, no interface, no start message, etc.|
|-s |--secure |Secure mode (disable Python console)|
|None |--disable-addons |Addons will have no effect|
|None |--debug-logging |Enable debug level logging just for this run. This setting will override any other|

   log level ( --loglevel, -l) argument given. |

|None |--no-sr-flag |Don't change the global system screen reader flag|
|None |--install |Installs NVDA (starting the newly installed copy)|
|None |--install-silent |Silently installs NVDA (does not start the newly installed copy)|
|None |--create-portable |Creates a portable copy of NVDA (starting the newly created copy). Requires|

   --portable-path to be specified |

|None |--create-portable-silent |Creates a portable copy of NVDA (does not start the newly installed copy).|

   Requires --portable-path to be specified |

|None |--portable-path=PORTABLEPATH |The path where a portable copy will be created|

### Systeminnstillinger {#SystemWideParameters}

   NVDA allows some values to be set in the system registry which alter the system wide behavior of NVDA.
   These values are stored in the registry under one of the following keys:

   * 32-bit system: "HKEY_LOCAL_MACHINE\SOFTWARE\nvda"
   * 64-bit system: "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\nvda"

   The following values can be set under this registry key:

| Navn |Type |Possible values |Beskrivelse|
|---|---|---|---|
|configInLocalAppData |DWORD |0 (default) to disable, 1 to enable |If enabled, stores the NVDA user|

   configuration in the local application data instead of the roaming application data |

|serviceDebug |DWORD |0 (default) to disable, 1 to enable |If enabled, disables secure mode on windows|

   secure desktops, allowing the use of the Python console and Log viewer. Due to several major security
   implications, the use of this option is strongly discouraged |

## Mer informasjon {#FurtherInformation}

Trenger du mer informasjon eller assistanse angående NVDA, anbefaler vi at du besøker NVDAs nettsted på NVDA_URL. Her vil du finne tilleggsdokumentasjon, så vel som teknisk støtte og ressurser fra NVDA-samfunnet.

Dette nettstedet tilbyr også informasjon og ressurser angående utviklingen av NVDA.

