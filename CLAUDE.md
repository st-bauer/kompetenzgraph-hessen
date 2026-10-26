# Kompetenzgraph Hessen

## Worum es geht
Plattform, die die hessischen Kerncurricula (KC) aller Fächer als Kompetenzgraph darstellt. Später sollen die Schulcurricula der Johann-Christian-Senckenberg-Schule (JCS, Integrierte Gesamtschule, Runkel) eingebunden werden. Ziel ist, für themenorientiertes Arbeiten und Projektlernen (Vorbild TheA, THEO) gemeinsame Anknüpfungspunkte über Fächer und Jahrgangsstufen zu finden.

Optisches Vorbild: dunkle „Weltraum“-Ansicht mit leuchtenden Knoten, Filterleiste links, Kompetenz-Inspektor rechts, Zähler unten (angelehnt an ein Bildungsplan-Tool aus Baden-Württemberg). Eigenen Namen behalten, keine fremden Marken übernehmen.

## Aktueller Stand (26.10.2026)
- 17 Fächer einer IGS 5 bis 10: Deutsch, Moderne Fremdsprachen, Kunst, Musik, Sport, Mathematik, Informatik, Physik, Chemie, Biologie, Erdkunde, Geschichte, PoWi, Arbeitslehre, Ethik, Ev. Religion, Kath. Religion
- Inhaltsfelder (129) in allen drei KC-Fassungen (Hauptschule, Realschule, Gymnasium) mit Seitenangabe je Fassung; Filter „KC-Fassung“ auf der Seite
- Schwerpunkte für die 5 Pilotfächer in allen drei Fassungen: Gymnasium 166 (Pilot), Haupt- und Realschule 304 Zeilen in `schwerpunkte_sek1.csv`; Erdkunde und PoWi nutzen Stichworte aus Kap. 6, das in allen Fassungen gleich lautet
- Kompetenzbereiche, 13 belegte Querbezüge und 11 Themenvorschläge (47 Verknüpfungen) bisher nur Pilotfächer, Fassung Gymnasium
- BNE als zuschaltbare Ebene: Grundlage § 6 Abs. 4 HSchG; 11 Belege, wo das KC selbst Nachhaltigkeit nennt; 17 SDGs mit 64 Zuordnungen (Vorschlag)
- Webseite: `docs/index.html` (wird aus `web/template.html` gebaut, GitHub Pages liefert `docs/` aus)
- Online: https://st-bauer.github.io/kompetenzgraph-hessen/ (Repo st-bauer/kompetenzgraph-hessen, öffentlich)
- Tabelle: `output/Kerncurricula_Hessen_Sek1.xlsx`

## Struktur
```
data/faecher.csv        Fächer mit Kurzname und Farbe (Reihenfolge = Anordnung im Graphen)
data/inhaltsfelder_sek1.csv  Inhaltsfelder aller Fächer, Seite je KC-Fassung (leer = nicht in dieser Fassung)
data/schwerpunkte_sek1.csv   Schwerpunkte Haupt- und Realschule (eine Zeile je Fassung, Stufe im KC-Wortlaut)
data/bne_sdg.csv        17 SDGs mit offizieller Farbe
data/bne_belege.csv     Stellen, an denen das KC Nachhaltigkeit nennt (Beleg)
data/bne_vorschlaege.csv  SDG-Zuordnung zu Inhaltsfeldern (Vorschlag)
data/kerncurricula.py   Pilotdaten Gymnasium (Schwerpunkte, Kompetenzbereiche, Querbezüge, Themenvorschläge, Hinweise)
data/quellen_sek1.csv   Alle KC- und Leitfaden-PDFs Sek I mit URL (Stand 26.10.2026)
scripts/build_xlsx.py   erzeugt die Excel-Tabelle
scripts/build_graph.py  erzeugt output/data.json und docs/index.html
scripts/fetch_pdfs.py   lädt PDFs aus quellen_sek1.csv und extrahiert Text (quellen/, nicht im Repo)
scripts/kc_seiten.py    zeigt KC-Text mit Seitenzahl, Hilfe beim Erfassen
scripts/schwerpunkte_auslesen.py  Entwurf aus vierspaltigen Schwerpunkt-Tabellen (Kap. 7.2/7.3), danach von Hand prüfen
web/template.html       Graph-Seite (d3 7.8.5 per CDN, Platzhalter /*__DATA__*/null)
docs/                   veröffentlichte Seite für GitHub Pages (nicht von Hand bearbeiten)
```

## Befehle
```
pip install openpyxl
python3 scripts/build_xlsx.py
python3 scripts/build_graph.py
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
  - `AK` / Kantentyp `vorschlag`: eigene Bündelung über gemeinsame Stichworte. Immer als „Vorschlag, fachlich zu prüfen“ kennzeichnen.
- BNE: `bne_belege.csv` nur, wo das KC selbst Nachhaltigkeit nennt. SDG-Zuordnungen sind immer Vorschlag (die KC nennen keine SDGs).
- Keine Vermutungen als Fakten darstellen. Unsicheres klar markieren (Spalte „Hinweis“).
- Stufen exakt so übernehmen, wie das KC sie benennt. Sie sind je Fach verschieden:
  Gymnasium: Biologie „bis Ende 5/6“, Chemie „1. Lernjahr“, Physik „nach ca. der Hälfte des Stundenkontingents“, jeweils plus „bis Ende 9/10“. Erdkunde und PoWi sind im Gymnasium nicht gestuft.
  Haupt-/Realschule: Biologie „Jahrgangsstufe 5/6“, Chemie „1. Lernjahr“, Physik wie Gymnasium, jeweils plus „zusätzlich dazu nach Abschluss der Jahrgangsstufe 9“ (HS) bzw. „10“ (RS). Erdkunde „am Ende der Jahrgangsstufe 6“ (Kap. 7.2 entfällt), PoWi ohne Kap. 7.

## Bekannte Lücken
- PoWi-PDF: rechter Rand der quer gesetzten Tabellen wurde beim Auslesen abgeschnitten. Stichworte am Original prüfen.
- Abbildungen (Basiskonzept-Zuordnung Physik, Verzahnung Erdkunde/PoWi/Geschichte) fehlen, weil sie nur als Grafik vorliegen.
- Schwerpunkte fehlen für die 12 Nicht-Pilotfächer. Jedes Fach ist anders aufgebaut (Tabellen nur in Bio, Ch, Ph; Geschichte mit Epochenbezügen, Deutsch nach Kompetenzbereichen usw.).
- Nicht aufgenommen: Latein, Griechisch, Chinesisch, Arabisch, alevitische, jüdische und islamische Religion.
- Deutsch: Zuordnung der Inhaltsfelder zu Kompetenzbereichen nicht erfasst. Kunst: Zuordnung zu Kernbereichen nur als Grafik.
- Primarstufe und Oberstufe noch nicht geprüft.

## Nächste Schritte
1. Schwerpunkte für Geschichte und Arbeitslehre erfassen (gesellschaftswissenschaftliches Aufgabenfeld), danach weitere Fächer.
2. SDG-Vorschläge fachlich prüfen lassen (Fachschaften, BNE-Beauftragte).
3. Schulcurricula der JCS als zweite Ebene: Zuordnung von Unterrichtseinheiten zu Schwerpunkten und zu Jahrgängen.
4. Ein reales TheA/THEO-Thema als Testfall durchspielen.
5. Restliche Pilotdaten aus `kerncurricula.py` in CSV überführen (Inhaltsfelder sind schon umgestellt).

## Schreibregeln für Texte und Oberfläche
- Deutsch, natürlicher Ton.
- Immer männliche und weibliche Form ausschreiben (Lehrerinnen und Lehrer, Schülerinnen und Schüler), kein Gendersternchen.
- Keine Gedankenstriche (—) in Fließtexten, keine Konstruktionen nach dem Muster „nicht X, sondern Y“.
- Schlanke Lösungen bevorzugen, schrittweise mit dem Nutzer verfeinern.
