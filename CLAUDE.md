# Kompetenzgraph Hessen

## Worum es geht
Plattform, die die hessischen Kerncurricula (KC) aller Fächer als Kompetenzgraph darstellt. Später sollen die Schulcurricula der Johann-Christian-Senckenberg-Schule (JCS, Integrierte Gesamtschule, Runkel) eingebunden werden. Ziel ist, für themenorientiertes Arbeiten und Projektlernen (Vorbild TheA, THEO) gemeinsame Anknüpfungspunkte über Fächer und Jahrgangsstufen zu finden.

Optisches Vorbild: dunkle „Weltraum“-Ansicht mit leuchtenden Knoten, Filterleiste links, Kompetenz-Inspektor rechts, Zähler unten (angelehnt an ein Bildungsplan-Tool aus Baden-Württemberg). Fächer liegen als farbige Inseln (Wolken) je Aufgabenfeld, Themen als leuchtende Knoten in der Mitte, Linien erscheinen nur bei Auswahl. Eigenen Namen behalten, keine fremden Marken übernehmen.

## Aktueller Stand (26.10.2026)
- 17 Fächer einer IGS 5 bis 10: Deutsch, Moderne Fremdsprachen, Kunst, Musik, Sport, Mathematik, Informatik, Physik, Chemie, Biologie, Erdkunde, Geschichte, PoWi, Arbeitslehre, Ethik, Ev. Religion, Kath. Religion
- Inhaltsfelder (129) in allen drei KC-Fassungen (Hauptschule, Realschule, Gymnasium) mit Seitenangabe je Fassung; Filter „KC-Fassung“ auf der Seite
- Schwerpunkte für alle 17 Fächer (834 Knoten): Pilot Gymnasium 166 in `kerncurricula.py`, alles andere in `schwerpunkte_sek1.csv` (1.284 Zeilen, eine je Fassung). Spalte `hinweis` sagt, wie erfasst: leer = von Hand gegen PDF geprüft, „von Hand aus Kap. 6 zusammengefasst“ = mit Belegstelle automatisch der Fassung zugeordnet, „automatisch ausgelesen, am Original prüfen“ = Entwurf aus Tabellen/Aufzählungen
- 20 Themenvorschläge mit 138 Verknüpfungen über alle 17 Fächer (`themen.csv`, Vorschlag)
- 33 belegte Querbezüge zwischen Fächern (`querbezuege.csv`, aus Kap. 3 bis 5); Kompetenzbereiche bisher nur Pilotfächer
- Prüfliste für die Fachschaften: `output/Pruefliste_Fachschaften.xlsx` (Themen, SDG-Zuordnungen, neu erfasste Schwerpunkte, mit Auswahlliste zur Bewertung)
- BNE als zuschaltbare Ebene: Grundlage § 6 Abs. 4 HSchG; 11 Belege, wo das KC selbst Nachhaltigkeit nennt; 17 SDGs mit amtlichem Zieltext und 63 schulrelevanten Unterzielen; 64 Zuordnungen zu Inhaltsfeldern, 60 davon mit Unterziel (Vorschlag). Themen und Fächer zeigen die Ziele ihrer Inhaltsfelder.
- Themenwerkstatt (Knopf oben): eigenes Thema mit Titel, Stichworten und Jahrgang gegen die KC prüfen; Treffer je Fach ankreuzen oder im Graphen anklicken; Abdeckung (Fächer, SDGs); Entwürfe im Browser (localStorage), Export als .md und .json, Import der .json. Suche tolerant (Umlaute, Endungen, auf Wunsch Wortteile) über Titel, Schwerpunkte, Themen-/SDG-Stichworte und einen Wortindex der Kap.-6-Beschreibungen
- Ideen finden: Thema in einem Satz eingeben („Ich renoviere mein Zimmer“), die Werkstatt schlägt Aspekte mit passenden Inhaltsfeldern und Schwerpunkten vor. In der claude.ai-Fassung arbeitet Claude (Fähigkeit `sample`) in zwei Schritten: erst gliedert Claude das Thema in 4 bis 6 Teilbereiche mit Leitfrage und Fächern, die Lehrkraft prüft, benennt um oder wählt ab; dann ordnet Claude jedem gewählten Teilbereich 2 bis 4 zentrale Schwerpunkte zu (nur aus den vorhandenen KC-Einträgen). Ohne Claude und auf GitHub Pages greifen die feste Ideenliste `data/ideen.json` (14 Beispielthemen) und die 20 Themen des Graphen. Angekreuzt werden Schwerpunkte, ein Inhaltsfeld nur ohne eigenen Schwerpunkt, damit der Graph übersichtlich bleibt. Alles ist Vorschlag
- Webseite: `docs/index.html` (wird aus `web/template.html` gebaut, GitHub Pages liefert `docs/` aus)
- Online: https://st-bauer.github.io/kompetenzgraph-hessen/ (Repo st-bauer/kompetenzgraph-hessen, öffentlich)
- claude.ai-Fassung mit Claude-Ideen: https://claude.ai/artifact/2Bq8sXb4aoj6dfXzQmgP5C (veröffentlicht aus `docs/index.html` mit `capabilities: {sample: {}, downloads: true}`; `downloads` braucht der Export, weil claude.ai Download-Links blockiert)
- Tabelle: `output/Kerncurricula_Hessen_Sek1.xlsx`

## Struktur
```
data/aufgabenfelder.csv Inseln im Graphen: Aufgabenfeld, Farbe, Lage (x, y)
data/faecher.csv        Fächer mit Kurzname, Aufgabenfeld und Farbe
data/themen.csv         Themenvorschläge: Thema, Fach, Inhaltsfeld, Stichwort aus dem KC, Stufe oder Seite (Kap. 6)
data/inhaltsfelder_sek1.csv  Inhaltsfelder aller Fächer, Seite je KC-Fassung (leer = nicht in dieser Fassung)
data/schwerpunkte_sek1.csv   Schwerpunkte Haupt- und Realschule (eine Zeile je Fassung, Stufe im KC-Wortlaut)
data/querbezuege.csv    belegte Querbezüge zwischen Fächern (Kanten im Graphen)
data/bne_sdg.csv        17 SDGs mit offizieller Farbe und amtlichem Zieltext
data/bne_unterziele.csv Auswahl schulrelevanter Unterziele im amtlichen deutschen Wortlaut (Quelle: Destatis, sdg-indikatoren.de)
data/bne_belege.csv     Stellen, an denen das KC Nachhaltigkeit nennt (Beleg)
data/bne_vorschlaege.csv  SDG-Zuordnung zu Inhaltsfeldern mit Unterziel (Vorschlag)
data/suchindex.json     Wörter je Inhaltsfeld aus Kap. 6 (nur für die Suche der Themenwerkstatt, wird nicht angezeigt)
data/ideen.json         Ideenliste der Werkstatt: Beispielthemen mit Aspekten und Inhaltsfeldern (aus build_ideen.py, Vorschlag)
data/kerncurricula.py   Pilotdaten Gymnasium (Schwerpunkte, Kompetenzbereiche, Querbezüge, Hinweise)
data/quellen_sek1.csv   Alle KC- und Leitfaden-PDFs Sek I mit URL (Stand 26.10.2026)
scripts/build_xlsx.py   erzeugt die Excel-Tabelle
scripts/build_graph.py  erzeugt output/data.json und docs/index.html
scripts/fetch_pdfs.py   lädt PDFs aus quellen_sek1.csv und extrahiert Text (quellen/, nicht im Repo)
scripts/kc_seiten.py    zeigt KC-Text mit Seitenzahl, Hilfe beim Erfassen
scripts/schwerpunkte_auslesen.py  Entwurf aus vierspaltigen Schwerpunkt-Tabellen (Kap. 7.2/7.3), danach von Hand prüfen
scripts/inhaltsfelder_auslesen.py Entwurf aus beschriebenen Inhaltsfeldern (Aufzählungen bzw. Satz „Im Mittelpunkt …“)
scripts/tabelle_auslesen.py       Entwurf aus Spaltentabellen über Wortkoordinaten (Mathematik Kap. 7.3, Kath. Religion Kap. 8.3)
scripts/build_pruefliste.py       erzeugt die Prüfliste für die Fachschaften
scripts/build_suchindex.py        erzeugt data/suchindex.json (braucht quellen/txt)
scripts/build_ideen.py            pflegt die Ideenliste, prüft die Inhaltsfelder, schreibt data/ideen.json
web/template.html       Graph-Seite (d3 7.8.5 per CDN, Platzhalter /*__DATA__*/null)
docs/                   veröffentlichte Seite für GitHub Pages (nicht von Hand bearbeiten)
notizen/                Arbeitsnotizen, nicht Teil der App (z. B. themen_recherche.md: Themen anderer Schulen, nur Orientierung)
```

## Befehle
```
pip install openpyxl
python3 scripts/build_xlsx.py
python3 scripts/build_suchindex.py   # nur nach Änderungen an Inhaltsfeldern, braucht quellen/
python3 scripts/build_ideen.py       # nach Änderungen an der Ideenliste
python3 scripts/build_graph.py
python3 scripts/build_pruefliste.py
python3 scripts/fetch_pdfs.py --fach Biologie --schulform Realschule
python3 scripts/fetch_pdfs.py --alle
python3 scripts/kc_seiten.py biologie_realschule --kapitel
python3 scripts/kc_seiten.py biologie_realschule 41-48 --breite 80
python3 scripts/schwerpunkte_auslesen.py biologie_realschule 41 48 Biologie
```
`pdftotext` kommt aus poppler (`brew install poppler`). Der Server des Kultusministeriums bricht bei vielen Abrufen mit 503 ab, das Skript wartet dann und versucht es erneut.
`docs/index.html` im Browser öffnen (Internet nötig wegen d3 vom CDN).

## Online stellen (GitHub Pages)
Einmalig:
```
git init && git add . && git commit -m "Kompetenzgraph Hessen: Pilot"
gh repo create st-bauer/kompetenzgraph-hessen --public --source=. --push
gh api -X POST repos/st-bauer/kompetenzgraph-hessen/pages -f "source[branch]=main" -f "source[path]=/docs"
```
Adresse danach: https://st-bauer.github.io/kompetenzgraph-hessen/

Bei jeder Änderung: Skripte ausführen, dann `git add . && git commit -m "…" && git push`. GitHub Pages aktualisiert sich nach etwa einer Minute.

Vor dem öffentlichen Teilen klären: Nutzungsbedingungen des Hessischen Kultusministeriums für die Weiterverwendung der KC-Texte (bisher nicht geprüft). Die Seite enthält gekürzte Auszüge mit Quellenangabe.

## Datenregeln (verbindlich)
- Nur aufnehmen, was im KC steht. Jede Zeile braucht eine Seitenangabe zum Original.
- Inhaltliche Schwerpunkte dürfen gekürzt werden, der Sinn bleibt erhalten. Verbindlich ist der Wortlaut im PDF.
- Fächerübergreifende Verbindungen strikt trennen:
  - `QB` / Kantentyp `beleg`: steht ausdrücklich im KC (mit Fundstelle).
  - `themen.csv` / Kantentyp `vorschlag`: eigene Bündelung über gemeinsame Stichworte aus dem KC. Immer als „Vorschlag, fachlich zu prüfen“ kennzeichnen.
- BNE: `bne_belege.csv` nur, wo das KC selbst Nachhaltigkeit nennt. SDG- und Unterziel-Zuordnungen sind immer Vorschlag (die KC nennen keine SDGs). Ziel- und Unterzieltexte nur im amtlichen Wortlaut, nicht umformulieren.
- Keine Vermutungen als Fakten darstellen. Unsicheres klar markieren (Spalte „Hinweis“).
- Stufen exakt so übernehmen, wie das KC sie benennt. Sie sind je Fach verschieden:
  Gymnasium: Biologie „bis Ende 5/6“, Chemie „1. Lernjahr“, Physik „nach ca. der Hälfte des Stundenkontingents“, jeweils plus „bis Ende 9/10“. Erdkunde und PoWi sind im Gymnasium nicht gestuft.
  Haupt-/Realschule: Biologie „Jahrgangsstufe 5/6“, Chemie „1. Lernjahr“, Physik wie Gymnasium, jeweils plus „zusätzlich dazu nach Abschluss der Jahrgangsstufe 9“ (HS) bzw. „10“ (RS). Erdkunde „am Ende der Jahrgangsstufe 6“ (Kap. 7.2 entfällt), PoWi ohne Kap. 7.

## Bekannte Lücken
- PoWi-PDF: rechter Rand der quer gesetzten Tabellen wurde beim Auslesen abgeschnitten. Stichworte am Original prüfen.
- Abbildungen (Basiskonzept-Zuordnung Physik, Verzahnung Erdkunde/PoWi/Geschichte) fehlen, weil sie nur als Grafik vorliegen.
- Automatisch ausgelesene Schwerpunkte (Mathematik, Kath. Religion, Informatik, Ethik, Kunst, Arbeitslehre, Geschichte-Epochen) sind ungeprüft; einzelne Punkte brechen am Seitenende ab.
- Deutsch: Jahrgangsschwerpunkte stehen im KC nur als Hervorhebung im Druck und fehlen; erfasst ist Kap. 6 (Abschluss). Sport, Musik, Fremdsprachen, Ev. Religion ebenfalls nur Kap. 6.
- Nicht aufgenommen: Latein, Griechisch, Chinesisch, Arabisch, alevitische, jüdische und islamische Religion.
- Deutsch: Zuordnung der Inhaltsfelder zu Kompetenzbereichen nicht erfasst. Kunst: Zuordnung zu Kernbereichen nur als Grafik.
- Primarstufe und Oberstufe noch nicht geprüft.

## Nächste Schritte
1. Prüfliste an die Fachschaften geben, Rückmeldungen in die CSV-Dateien übernehmen.
2. Jahrgangsschwerpunkte (Kap. 7.1/7.2) für Deutsch, Sport, Musik, Fremdsprachen, Ev. Religion ergänzen.
3. Schulcurricula der JCS als zweite Ebene: Zuordnung von Unterrichtseinheiten zu Schwerpunkten und zu Jahrgängen.
4. Ein reales TheA/THEO-Thema als Testfall durchspielen.
5. Restliche Pilotdaten aus `kerncurricula.py` in CSV überführen (Inhaltsfelder und Themen sind schon umgestellt).

## Schreibregeln für Texte und Oberfläche
- Deutsch, natürlicher Ton.
- Immer männliche und weibliche Form ausschreiben (Lehrerinnen und Lehrer, Schülerinnen und Schüler), kein Gendersternchen.
- Keine Gedankenstriche (—) in Fließtexten, keine Konstruktionen nach dem Muster „nicht X, sondern Y“.
- Schlanke Lösungen bevorzugen, schrittweise mit dem Nutzer verfeinern.
