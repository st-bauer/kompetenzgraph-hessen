# Kompetenzgraph Hessen

## Worum es geht
Plattform, die die hessischen Kerncurricula (KC) aller Fächer als Kompetenzgraph darstellt. Später sollen die Schulcurricula der Johann-Christian-Senckenberg-Schule (JCS, Integrierte Gesamtschule, Runkel) eingebunden werden. Ziel ist, für themenorientiertes Arbeiten und Projektlernen (Vorbild TheA, THEO) gemeinsame Anknüpfungspunkte über Fächer und Jahrgangsstufen zu finden.

Optisches Vorbild: dunkle „Weltraum“-Ansicht mit leuchtenden Knoten, Filterleiste links, Kompetenz-Inspektor rechts, Zähler unten (angelehnt an ein Bildungsplan-Tool aus Baden-Württemberg). Eigenen Namen behalten, keine fremden Marken übernehmen.

## Aktueller Stand (Pilot, 26.10.2026)
- Fächer: Biologie, Chemie, Physik, Erdkunde, Politik und Wirtschaft
- Fassung: nur Gymnasium (Sek I)
- 36 Inhaltsfelder, 166 Schwerpunkte, 13 belegte Querbezüge, 11 Themenvorschläge (47 Verknüpfungen)
- Webseite: `docs/index.html` (wird aus `web/template.html` gebaut, GitHub Pages liefert `docs/` aus)
- Veröffentlicht als privates claude.ai-Artifact (Vorschau): https://claude.ai/artifact/2Bq8sXb4aoj6dfXzQmgP5C
- Tabelle: `output/Kerncurricula_Hessen_Pilot_Sek1_Gym.xlsx`

## Struktur
```
data/kerncurricula.py   Datenbasis (Inhaltsfelder, Schwerpunkte, Kompetenzbereiche, Querbezüge, Vorschläge, Hinweise)
data/quellen_sek1.csv   Alle KC- und Leitfaden-PDFs Sek I mit URL (Stand 26.10.2026)
scripts/build_xlsx.py   erzeugt die Excel-Tabelle
scripts/build_graph.py  erzeugt output/data.json und docs/index.html
scripts/fetch_pdfs.py   lädt PDFs aus quellen_sek1.csv und extrahiert Text
web/template.html       Graph-Seite (d3 7.8.5 per CDN, Platzhalter /*__DATA__*/null)
docs/                   veröffentlichte Seite für GitHub Pages (nicht von Hand bearbeiten)
```

## Befehle
```
pip install openpyxl
python3 scripts/build_xlsx.py
python3 scripts/build_graph.py
python3 scripts/fetch_pdfs.py --fach Biologie --schulform Realschule
```
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
  - `AK` / Kantentyp `vorschlag`: eigene Bündelung über gemeinsame Stichworte. Immer als „Vorschlag, fachlich zu prüfen“ kennzeichnen.
- Keine Vermutungen als Fakten darstellen. Unsicheres klar markieren (Spalte „Hinweis“).
- Stufen exakt so übernehmen, wie das KC sie benennt. Sie sind je Fach verschieden:
  Biologie „bis Ende 5/6“, Chemie „1. Lernjahr“, Physik „nach ca. der Hälfte des Stundenkontingents“, jeweils plus „bis Ende 9/10“. Erdkunde und PoWi sind im Gymnasium nicht gestuft.

## Bekannte Lücken
- PoWi-PDF: rechter Rand der quer gesetzten Tabellen wurde beim Auslesen abgeschnitten. Stichworte am Original prüfen.
- Abbildungen (Basiskonzept-Zuordnung Physik, Verzahnung Erdkunde/PoWi/Geschichte) fehlen, weil sie nur als Grafik vorliegen.
- Haupt- und Realschulfassungen fehlen, für die IGS aber nötig.
- Primarstufe und Oberstufe noch nicht geprüft.

## Nächste Schritte
1. Haupt- und Realschulfassungen der fünf Pilotfächer ergänzen (Schulform als eigenes Feld bzw. Filter).
2. Weitere Fächer aus `quellen_sek1.csv` aufnehmen, Geschichte zuerst (gesellschaftswissenschaftliches Aufgabenfeld).
3. Schulcurricula der JCS als zweite Ebene: Zuordnung von Unterrichtseinheiten zu Schwerpunkten und zu Jahrgängen.
4. Ein reales TheA/THEO-Thema als Testfall durchspielen.
5. Datenbasis langfristig von Python-Listen auf JSON oder SQLite umstellen.

## Schreibregeln für Texte und Oberfläche
- Deutsch, natürlicher Ton.
- Immer männliche und weibliche Form ausschreiben (Lehrerinnen und Lehrer, Schülerinnen und Schüler), kein Gendersternchen.
- Keine Gedankenstriche (—) in Fließtexten, keine Konstruktionen nach dem Muster „nicht X, sondern Y“.
- Schlanke Lösungen bevorzugen, schrittweise mit dem Nutzer verfeinern.
