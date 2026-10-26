import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
from kerncurricula import *

OUT = os.path.join(ROOT, "output", "Kerncurricula_Hessen_Pilot_Sek1_Gym.xlsx")

# ---------------- Workbook ----------------
F = "Arial"
HFILL = PatternFill("solid", fgColor="1F4E5F")
HFONT = Font(name=F, bold=True, color="FFFFFF", size=10)
BFONT = Font(name=F, size=10)
WRAP = Alignment(wrap_text=True, vertical="top")
thin = Side(style="thin", color="D0D7DE")
BORDER = Border(bottom=thin)
FACHFILL = {
    "Biologie": "E8F5E9", "Chemie": "E3F2FD", "Physik": "EDE7F6",
    "Erdkunde": "FFF3E0", "Politik und Wirtschaft": "FCE4EC",
}

def sheet(ws, headers, rows, widths, fach_col=None):
    ws.append(headers)
    for c in ws[1]:
        c.fill, c.font, c.alignment = HFILL, HFONT, Alignment(wrap_text=True, vertical="center")
    for r in rows:
        ws.append(list(r))
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.font, c.alignment, c.border = BFONT, WRAP, BORDER
        if fach_col is not None:
            fach = row[fach_col].value
            if fach in FACHFILL:
                row[fach_col].fill = PatternFill("solid", fgColor=FACHFILL[fach])
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    ws.row_dimensions[1].height = 30

wb = Workbook()
ov = wb.active
ov.title = "Übersicht"

# IDs
if_rows = [(f"IF-{i:02d}",) + r for i, r in enumerate(IF, 1)]
sp_rows = [(f"SP-{i:03d}",) + r for i, r in enumerate(SP, 1)]
ak_rows = []
for t, items in AK:
    for it in items:
        ak_rows.append((t,) + it + ("Vorschlag, fachlich zu prüfen",))

ws = wb.create_sheet("Inhaltsfelder")
sheet(ws, ["ID", "Fach", "Basiskonzept(e)", "Inhaltsfeld", "Seite (Kap. 6)", "Hinweis"],
      if_rows, [8, 20, 42, 52, 13, 44], fach_col=1)
ws = wb.create_sheet("Schwerpunkte")
sheet(ws, ["ID", "Fach", "Inhaltsfeld", "Stufe laut KC", "Inhaltlicher Schwerpunkt", "Seite"],
      sp_rows, [9, 20, 40, 30, 70, 10], fach_col=1)
ws = wb.create_sheet("Kompetenzbereiche")
sheet(ws, ["Fach", "Kompetenzbereich", "Teilbereiche / Operatoren", "Seite", "Hinweis"],
      KB, [20, 34, 80, 8, 36], fach_col=0)
ws = wb.create_sheet("Querbezüge belegt")
sheet(ws, ["Fach (Quelle)", "Bezug zu", "Aussage im KC (sinngemäß)", "Fundstelle"],
      QB, [22, 28, 90, 26])
ws = wb.create_sheet("Anknüpfungspunkte")
sheet(ws, ["Thema", "Fach", "Inhaltsfeld", "Stichwort aus dem KC", "Stufe laut KC", "Status"],
      ak_rows, [26, 20, 40, 60, 30, 26], fach_col=1)
ws = wb.create_sheet("Hinweise und Lücken")
sheet(ws, ["Punkt", "Hinweis"], HIN, [20, 110])

# Übersicht
ov["A1"] = "Kerncurricula Hessen, Sek I Gymnasium: Pilot-Datenbasis"
ov["A1"].font = Font(name=F, bold=True, size=14)
ov["A2"] = "Stand der Auswertung: 26.10.2026. Quelle: Hessisches Kultusministerium, Seite 'Sekundarstufe I – Kerncurricula'."
ov["A2"].font = Font(name=F, size=10, italic=True)
ov.append([])
ov.append(["Fach", "Inhaltsfelder", "Schwerpunkte", "Anknüpfungspunkte", "Quelle (PDF)"])
for c in ov[4]:
    c.fill, c.font = HFILL, HFONT
r = 5
for fach, url in URL.items():
    ov.cell(r, 1, fach)
    ov.cell(r, 2, f'=COUNTIF(Inhaltsfelder!B:B,A{r})')
    ov.cell(r, 3, f'=COUNTIF(Schwerpunkte!B:B,A{r})')
    ov.cell(r, 4, f'=COUNTIF(Anknüpfungspunkte!B:B,A{r})')
    ov.cell(r, 5, url).hyperlink = url
    ov.cell(r, 1).fill = PatternFill("solid", fgColor=FACHFILL[fach])
    for col in range(1, 6):
        ov.cell(r, col).font = BFONT if col != 5 else Font(name=F, size=10, color="0563C1", underline="single")
    r += 1
ov.cell(r, 1, "Summe").font = Font(name=F, bold=True, size=10)
for col, L in [(2, "B"), (3, "C"), (4, "D")]:
    ov.cell(r, col, f"=SUM({L}5:{L}{r-1})").font = Font(name=F, bold=True, size=10)
r += 2
ov.cell(r, 1, "Tabellenblätter").font = Font(name=F, bold=True, size=11)
for name, desc in [
    ("Inhaltsfelder", "Alle Inhaltsfelder je Fach mit Basiskonzept(en) und Seitenangabe"),
    ("Schwerpunkte", "Inhaltliche Schwerpunkte je Inhaltsfeld und Stufe (Knoten für die spätere Grafik)"),
    ("Kompetenzbereiche", "Fachliche Kompetenzbereiche und Teilbereiche"),
    ("Querbezüge belegt", "Fächerübergreifende Bezüge, die ausdrücklich im KC stehen"),
    ("Anknüpfungspunkte", "Themenvorschläge über gemeinsame Stichworte, zu prüfen"),
    ("Hinweise und Lücken", "Was fehlt oder abweicht"),
]:
    r += 1
    ov.cell(r, 1, name).font = Font(name=F, bold=True, size=10)
    ov.cell(r, 2, desc).font = BFONT
ov.column_dimensions["A"].width = 24
ov.column_dimensions["B"].width = 16
ov.column_dimensions["C"].width = 16
ov.column_dimensions["D"].width = 20
ov.column_dimensions["E"].width = 90

wb.save(OUT)
print(OUT, len(IF), len(SP), len(KB), len(QB), len(ak_rows))
