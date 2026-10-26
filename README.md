# Kompetenzgraph Hessen

Prototyp, der die hessischen Kerncurricula der Sekundarstufe I als Netz aus Fächern, Inhaltsfeldern und inhaltlichen Schwerpunkten zeigt. Grundlage für themenorientiertes Arbeiten und Projektlernen an der JCS.

## Schnellstart
```
pip install openpyxl
python3 scripts/build_xlsx.py     # Tabelle in output/
python3 scripts/build_graph.py    # Graph-Seite docs/index.html
```
Dann `docs/index.html` im Browser öffnen.

## Online stellen
Das Projekt ist für GitHub Pages vorbereitet: Die fertige Seite liegt in `docs/`. Die Befehle zum einmaligen Einrichten stehen in `CLAUDE.md` unter „Online stellen“. Am einfachsten sagen Sie in Claude Code: „Stell das Projekt nach CLAUDE.md auf GitHub Pages online.“

## Mit Claude Code weiterarbeiten
Ordner öffnen, `claude` starten. `CLAUDE.md` enthält Ziel, Datenregeln, bekannte Lücken und nächste Schritte. Ein guter erster Auftrag:

> Lies CLAUDE.md. Lade mit scripts/fetch_pdfs.py die Realschulfassung Biologie und ergänze sie in data/kerncurricula.py mit Schulform als neuem Feld.

## Quelle
Hessisches Kultusministerium, Kerncurricula Sekundarstufe I:
https://kultus.hessen.de/unterricht/kerncurricula-und-lehrplaene/kerncurricula/sekundarstufe-i-kerncurricula
