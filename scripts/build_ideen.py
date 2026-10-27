"""Erzeugt data/ideen.json: vorbereitete Projektthemen für die Themenwerkstatt.

Je Thema: Suchbegriffe (zum Wiedererkennen einer Eingabe), Aspekte mit Stichworten (für die Auswahl
passender Schwerpunkte) und Inhaltsfeldern. Alles ist ein Vorschlag, fachlich zu prüfen.
Prüft, dass jedes Inhaltsfeld in data/inhaltsfelder_sek1.csv vorkommt.
"""
import csv, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FELDER = {(r["fach"], r["inhaltsfeld"]) for r in csv.DictReader(open(os.path.join(ROOT, "data", "inhaltsfelder_sek1.csv"), encoding="utf-8"))}

M, D, K, MU, S, AL, PH, CH, BI = "Mathematik", "Deutsch", "Kunst", "Musik", "Sport", "Arbeitslehre", "Physik", "Chemie", "Biologie"
EK, GE, PW, ET, MFS, INF, EV, KR = "Erdkunde", "Geschichte", "Politik und Wirtschaft", "Ethik", "Moderne Fremdsprachen", "Informatik", "Evangelische Religion", "Katholische Religion"
L1, L2, L3 = "Persönliche Lebenswelten „Ich und die Anderen“", "Öffentlich-gesellschaftliche Lebenswelten „Ich und die Gesellschaft“", "Kulturelle Lebenswelten „Ich und die Welt“"

# (Thema, Suchbegriffe, [(Aspekt, Stichworte, [(Fach, Inhaltsfeld), ...]), ...])
IDEEN = [
    ("Ich renoviere mein Zimmer", "Zimmer renovieren streichen tapezieren einrichten wohnen Wohnung Kinderzimmer umgestalten", [
        ("Grundriss, Maßstab und Fläche", "Fläche Umfang Maßstab Figuren Koordinatensystem Grundriss", [(M, "Ebene Figuren"), (M, "Umgang mit Größen"), (M, "Messvorgänge")]),
        ("Material berechnen und Kosten planen", "Volumen Körper Prozent Kosten Rechnen Dreisatz Zuordnungen", [(M, "Körper"), (M, "Operationen und ihre Eigenschaften"), (M, "Darstellungen"), (AL, "Ökonomisch geprägte Situationen und Strukturen des Zusammenlebens")]),
        ("Farben und Raumwirkung", "Farbe Gestaltung Raum Wirkung Bild Material", [(K, "Medien, Techniken und Verfahren der Bildgestaltung"), (K, "Strategien kreativer und künstlerischer Prozesse der Bilderfindung"), (K, "Wahrnehmung der Umwelt")]),
        ("Licht, Strom und Sicherheit", "Licht Stromkreis Elektrizität Gefahren Energie", [(PH, "Elektrizität im Alltag"), (PH, "Erweiterung der Sinne"), (PH, "Energie in Umwelt und Technik")]),
        ("Werkzeuge, Stoffe und Umwelt", "Werkstoffe Stoffe Eignung Gefahrenpotenzial Kunststoffe Technik", [(CH, "Welt der Stoffe – Identifikation und Ordnung von Stoffen"), (AL, "Technische Systeme und Prozesse")]),
        ("Mein Raum, meine Identität", "Selbst Identität Familie Wohnen Persönlichkeit", [(ET, "Selbst und Welt"), (K, "Kunst als Korrelat der Persönlichkeit"), (MFS, L1)]),
    ]),
    ("Wir planen ein Fest", "Fest Feier Party planen Schulfest feiern Buffet Einladung", [
        ("Einkauf, Mengen und Kosten", "Brüche Prozent Kosten Zuordnungen Rechnen", [(M, "Zahlen"), (M, "Operationen und ihre Eigenschaften"), (M, "Darstellungen")]),
        ("Essen, Ernährung und Unverträglichkeiten", "Ernährung Stoffwechsel Verdauung", [(BI, "Stoffwechsel und Regelmechanismen")]),
        ("Feste in Religionen und Kulturen", "Feste Religionen Rituale Kultur", [(EV, "Religionen"), (KR, "Religionen"), (ET, "Religionen, Weltbilder und Kulturen"), (GE, "Alltagskulturen")]),
        ("Einladung, Plakat und Programm", "Schreiben Text Medien Präsentation Gestaltung", [(D, "Schreibformen"), (D, "Text-/Medienformen"), (K, "Distributions- und Präsentationsformen für Bilder"), (MFS, L1)]),
        ("Musik und Tanz", "Musik Tanz Bewegung Rhythmus Gesang", [(MU, "Gesang und Instrumentalspiel"), (MU, "Bewegung und Gestaltungsmedien"), (S, "Bewegung gymnastisch, rhythmisch und tänzerisch gestalten")]),
        ("Licht und Technik", "Stromkreis Elektrizität", [(PH, "Elektrizität im Alltag")]),
    ]),
    ("Wir legen einen Schulgarten an", "Schulgarten Garten Beet pflanzen Hochbeet Gemüse Insekten Bienen", [
        ("Pflanzen, Tiere und Lebensräume", "Pflanzen Ökosystem Nahrungskette Arten Lebensraum Blütenpflanzen", [(BI, "Wechselwirkungen in Ökosystemen"), (BI, "Fortpflanzung und Entwicklung"), (BI, "Vielfalt, Veränderung und Abstammung von Lebewesen")]),
        ("Boden, Wasser und Dünger", "Boden Wasser Stoffe Luft", [(CH, "Schatzkiste der Natur – Chemie in Alltag und Technik"), (EK, "Natur/Umwelt")]),
        ("Beete planen und vermessen", "Fläche Maßstab Figuren Messen", [(M, "Ebene Figuren"), (M, "Messvorgänge")]),
        ("Ernte, Verkauf und Ernährung", "Ernährung Konsum Einkommen", [(BI, "Stoffwechsel und Regelmechanismen"), (AL, "Ökonomisch geprägte Situationen und Strukturen des Zusammenlebens")]),
        ("Verantwortung für die Schöpfung", "Natur Verantwortung Schöpfung", [(ET, "Mensch, Natur und Technik"), (EV, "Mensch und Welt"), (KR, "Mensch und Welt")]),
        ("Wetter und Jahreszeiten", "Wetter Klima Temperatur", [(PH, "Wettererscheinungen und Klima")]),
    ]),
    ("Rund ums Fahrrad", "Fahrrad Rad fahren Radtour Mobilität Verkehr Schulweg", [
        ("Geschwindigkeit, Kraft und Bewegung", "Geschwindigkeit Kräfte Trägheit Bewegung", [(PH, "Fortbewegung und Mobilität"), (PH, "Technik im Dienst des Menschen")]),
        ("Licht und Dynamo", "Licht Stromkreis Energieumwandlung", [(PH, "Elektrizität im Alltag"), (PH, "Energie in Umwelt und Technik")]),
        ("Strecken, Karten und Orientierung", "Karte Maßstab Orientierung Weg", [(EK, "Räumliches Orientierungswissen"), (M, "Umgang mit Größen"), (M, "Funktionen und Gleichungen")]),
        ("Mobilität und Umwelt", "Verkehr Umwelt Klima Stadt", [(EK, "Mensch/Gesellschaft"), (PW, "Gesellschaft und Natur")]),
        ("Fahren, Rollen, Gleiten", "Wagnis Gleichgewicht Sicherheit", [(S, "Fahren, Rollen, Gleiten")]),
        ("Reparieren und Technik", "Technik Werkzeug", [(AL, "Technische Systeme und Prozesse")]),
    ]),
    ("Wir planen eine Klassenfahrt", "Klassenfahrt Ausflug Reise planen Fahrt Jugendherberge", [
        ("Route, Karte und Ziel", "Karte Orientierung Region Raum", [(EK, "Räumliches Orientierungswissen"), (EK, "Geographie auf regionaler Ebene")]),
        ("Kosten und Zeitplan", "Kosten Prozent Zeit Rechnen", [(M, "Operationen und ihre Eigenschaften"), (M, "Umgang mit Größen"), (AL, "Ökonomisch geprägte Situationen und Strukturen des Zusammenlebens")]),
        ("Geschichte vor Ort", "Mittelalter Städte Herrschaft Raum", [(GE, "Epochenbezug Mittelalter"), (GE, "Bewältigung und Nutzung von Räumen")]),
        ("Gemeinschaft und Regeln", "Regeln Gemeinschaft Verantwortung", [(ET, "Gewissen und Verantwortung"), (PW, "Individuum und Gesellschaft")]),
        ("Berichten und präsentieren", "Bericht Präsentation Text Medien", [(D, "Schreibformen"), (D, "Rede- und Gesprächsformen")]),
        ("Bewegung draußen", "Laufen Wasser Spiele", [(S, "Laufen, Springen, Werfen"), (S, "Bewegen im Wasser"), (S, "Spielen")]),
    ]),
    ("Wir gründen einen Schulkiosk", "Kiosk Schülerfirma Verkauf Pausenverkauf Laden Unternehmen Geschäft", [
        ("Preise, Gewinn und Buchführung", "Prozent Kosten Gewinn Daten Diagramm", [(M, "Operationen und ihre Eigenschaften"), (M, "Statistische Erhebungen und ihre Auswertung"), (M, "Darstellungen")]),
        ("Wirtschaften und Verbraucher", "Wirtschaft Markt Konsum Verbraucher", [(PW, "Wirtschaft"), (AL, "Ökonomisch geprägte Situationen und Strukturen des Zusammenlebens")]),
        ("Arbeit organisieren", "Arbeit Organisation Beruf", [(AL, "Organisation von Arbeit"), (AL, "Berufswegeplanung")]),
        ("Gesundes Angebot", "Ernährung Gesundheit", [(BI, "Stoffwechsel und Regelmechanismen"), (AL, "Erhalt der psychischen und physischen Gesundheit")]),
        ("Werbung und Plakate", "Werbung Medien Gestaltung", [(D, "Text-/Medienformen"), (K, "Distributions- und Präsentationsformen für Bilder")]),
        ("Fair und nachhaltig", "Nachhaltigkeit Konsum Recycling Gerechtigkeit", [(PW, "Gesellschaft und Natur"), (CH, "Magie des Kohlenstoffs – Organische Verbindungen"), (ET, "Recht und Gerechtigkeit")]),
    ]),
    ("Unser Ort früher und heute", "Ort Heimat Dorf Stadt Runkel Burg Ortsgeschichte früher heute Gemeinde Heimatort", [
        ("Mittelalter, Burg und Stadt", "Mittelalter Burg Herrschaft Städte", [(GE, "Epochenbezug Mittelalter"), (GE, "Herrschaft")]),
        ("Leben früher", "Alltag Wohnen Arbeit Ernährung", [(GE, "Alltagskulturen"), (GE, "Wirtschaft")]),
        ("Raum, Karte und Landschaft", "Karte Raum Region Landschaft", [(EK, "Geographie auf regionaler Ebene"), (EK, "Räumliches Orientierungswissen"), (GE, "Bewältigung und Nutzung von Räumen")]),
        ("Gemeinde und Mitbestimmung", "Gemeinde Demokratie Beteiligung", [(PW, "Demokratie")]),
        ("Kirche vor Ort", "Kirche Gemeinde", [(EV, "Kirche"), (KR, "Kirche")]),
        ("Interviews und Ortschronik", "Gespräch Interview Bericht Text", [(D, "Rede- und Gesprächsformen"), (D, "Schreibformen")]),
    ]),
    ("Die Lahn: Leben am Fluss", "Lahn Fluss Wasser Ufer Hochwasser Gewässer Flusslandschaft", [
        ("Wasser als Lebensraum", "Ökosystem Gewässer Arten Nahrungskette", [(BI, "Wechselwirkungen in Ökosystemen")]),
        ("Wasserqualität untersuchen", "Wasser Nachweis Stoffe Gemisch Trennverfahren", [(CH, "Welt der Stoffe – Identifikation und Ordnung von Stoffen"), (CH, "Der Mix macht's – Stoffgemische")]),
        ("Fluss, Landschaft und Hochwasser", "Fluss Wasser Natur Raum Klima", [(EK, "Natur/Umwelt"), (EK, "Umwelt-Gesellschaft-Beziehungen und globale Probleme"), (PH, "Wettererscheinungen und Klima")]),
        ("Handel und Siedlung am Fluss", "Städte Handel Mittelalter Raum", [(GE, "Epochenbezug Mittelalter"), (GE, "Bewältigung und Nutzung von Räumen")]),
        ("Energie aus Wasser", "Energie Energieversorgung regenerative", [(PH, "Zukunftssichere Energieversorgung")]),
        ("Messen und darstellen", "Daten Diagramm Messen", [(M, "Statistische Erhebungen und ihre Auswertung"), (M, "Messvorgänge")]),
    ]),
    ("Mein Smartphone", "Handy Smartphone Medien Internet Social Media digital Apps", [
        ("Wie funktioniert das Gerät?", "Hardware Computer Daten Elektrizität", [(INF, "Hardware und Rechnerarchitektur"), (PH, "Elektrizität im Alltag")]),
        ("Internet, Daten und Sicherheit", "Internet Datenschutz Datensicherheit Verschlüsselung", [(INF, "Internet und HTML"), (INF, "Kryptologie")]),
        ("Medien nutzen und bewerten", "Medien Text Wirkung", [(D, "Text-/Medienformen"), (D, "Lese- und Rezeptionsstrategien")]),
        ("Rohstoffe und Recycling", "Metalle Rohstoffe Recycling", [(CH, "Welt der Stoffe – Identifikation und Ordnung von Stoffen"), (EK, "Umwelt-Gesellschaft-Beziehungen und globale Probleme")]),
        ("Kommunikation und Verantwortung", "Wahrheit Verantwortung Medien", [(ET, "Wahrheit und Wirklichkeit"), (ET, "Gewissen und Verantwortung"), (PW, "Demokratie")]),
        ("Kosten und Verträge", "Kosten Prozent Verbraucher", [(M, "Operationen und ihre Eigenschaften"), (PW, "Wirtschaft")]),
    ]),
    ("Was ist in meinem Pausenbrot?", "Pausenbrot Frühstück Ernährung Essen Lebensmittel gesund Pause", [
        ("Nährstoffe und Verdauung", "Ernährung Verdauung Stoffwechsel", [(BI, "Stoffwechsel und Regelmechanismen"), (BI, "Funktionsteilung im Organismus")]),
        ("Stoffe in Lebensmitteln", "Nachweis Stoffe organische", [(CH, "Welt der Stoffe – Identifikation und Ordnung von Stoffen"), (CH, "Magie des Kohlenstoffs – Organische Verbindungen")]),
        ("Woher kommt unser Essen?", "Landwirtschaft Handel Globalisierung Ressourcen", [(EK, "Umwelt-Gesellschaft-Beziehungen und globale Probleme"), (PW, "Internationale Beziehungen und Globalisierung")]),
        ("Einkaufen, Preise und Verpackung", "Konsum Kosten Recycling", [(AL, "Ökonomisch geprägte Situationen und Strukturen des Zusammenlebens"), (PW, "Wirtschaft")]),
        ("Essen in Kulturen und Religionen", "Essen Religionen Kultur", [(GE, "Alltagskulturen"), (ET, "Religionen, Weltbilder und Kulturen")]),
        ("Bewegung und Fitness", "Fitness Gesundheit Ausdauer", [(S, "Den Körper trainieren, die Fitness verbessern"), (AL, "Erhalt der psychischen und physischen Gesundheit")]),
    ]),
    ("Weniger Müll an unserer Schule", "Müll Abfall Recycling Plastik Mülltrennung Upcycling Verpackung", [
        ("Stoffe trennen und wiederverwerten", "Stoffgemische Trennverfahren Kunststoffe Recycling", [(CH, "Der Mix macht's – Stoffgemische"), (CH, "Magie des Kohlenstoffs – Organische Verbindungen")]),
        ("Müll zählen und auswerten", "Daten Statistik Diagramm", [(M, "Statistische Erhebungen und ihre Auswertung"), (M, "Darstellungen")]),
        ("Müll und Umwelt weltweit", "Umwelt Ressourcen globale Probleme", [(EK, "Umwelt-Gesellschaft-Beziehungen und globale Probleme"), (PW, "Gesellschaft und Natur")]),
        ("Ökosysteme in Gefahr", "Gefährdung Ökosystem Eingriffe", [(BI, "Wechselwirkungen in Ökosystemen")]),
        ("Kunst aus Abfall", "Material Gestaltung Techniken", [(K, "Medien, Techniken und Verfahren der Bildgestaltung")]),
        ("Kampagne an der Schule", "Medien Rede Appellieren", [(D, "Rede- und Gesprächsformen"), (D, "Text-/Medienformen")]),
    ]),
    ("Energie sparen in der Schule", "Energie sparen Strom Heizung Klimaschutz Energiedetektive Schulgebäude", [
        ("Energieformen und Energieverbrauch", "Energie Energieformen Energieerhaltung", [(PH, "Energie in Umwelt und Technik"), (PH, "Elektrizität im Alltag")]),
        ("Wärme und Dämmung", "Wärme Temperatur thermische", [(PH, "Wettererscheinungen und Klima")]),
        ("Erneuerbare Energien", "regenerative Energieversorgung", [(PH, "Zukunftssichere Energieversorgung")]),
        ("Verbrauch messen und darstellen", "Daten Diagramm Funktionen", [(M, "Statistische Erhebungen und ihre Auswertung"), (M, "Funktionen und Gleichungen")]),
        ("Klima und Verantwortung", "Klima Verantwortung Nachhaltigkeit", [(EK, "Umwelt-Gesellschaft-Beziehungen und globale Probleme"), (ET, "Mensch, Natur und Technik"), (PW, "Gesellschaft und Natur")]),
    ]),
    ("Wir führen ein Theaterstück auf", "Theater Musical Aufführung Bühne Schauspiel Rolle Szene", [
        ("Text und Szene", "Szene Drama Rolle Text", [(D, "Text-/Medienformen"), (D, "Lesarten und Rezeptionskonventionen"), (D, "Rede- und Gesprächsstrategien")]),
        ("Musik und Klang", "Musik Klang Gesang Instrument", [(MU, "Gesang und Instrumentalspiel"), (MU, "Klang"), (MU, "Ausdruck und Wirkung")]),
        ("Bühnenbild und Kostüm", "Gestaltung Material Bild", [(K, "Medien, Techniken und Verfahren der Bildgestaltung"), (K, "Strategien kreativer und künstlerischer Prozesse der Bilderfindung")]),
        ("Bewegung und Ausdruck", "Ausdruck Tanz Körper", [(S, "Bewegung gymnastisch, rhythmisch und tänzerisch gestalten")]),
        ("Licht und Ton", "Licht Schall Stromkreis", [(PH, "Erweiterung der Sinne"), (PH, "Elektrizität im Alltag")]),
        ("Ein Stück in der Fremdsprache", "Kultur Sprache", [(MFS, L3)]),
    ]),
    ("Familiengeschichten: Woher wir kommen", "Familie Herkunft Migration Familiengeschichte Wurzeln Heimat Einwanderung", [
        ("Eigenes und Fremdes", "Identität Fremdes Herkunft", [(GE, "Eigenes und Fremdes"), (ET, "Selbst und Welt")]),
        ("Migration heute", "Migration Integration Globalisierung", [(PW, "Internationale Beziehungen und Globalisierung"), (EK, "Mensch/Gesellschaft")]),
        ("Geschichte im 20. Jahrhundert", "Neuordnungen 1945 1989 Nationalsozialismus", [(GE, "Epochenbezug Neueste Zeit")]),
        ("Sprachen und Kulturen", "Kultur Sprache", [(MFS, L3), (MFS, L1)]),
        ("Glaube und Weltdeutung", "Religionen Dialog", [(EV, "Religionen"), (KR, "Religionen"), (ET, "Religionen, Weltbilder und Kulturen")]),
        ("Erzählen und Interviews", "Erzählen Gespräch Schreiben", [(D, "Schreibformen"), (D, "Rede- und Gesprächsformen")]),
    ]),
]

out, fehlt = [], []
for thema, such, aspekte in IDEEN:
    eintrag = {"thema": thema, "such": such, "aspekte": []}
    for aspekt, stich, felder in aspekte:
        for f in felder:
            if f not in FELDER:
                fehlt.append((thema, f))
        eintrag["aspekte"].append({"aspekt": aspekt, "stichworte": stich, "felder": [f"{a}|{b}" for a, b in felder]})
    out.append(eintrag)
assert not fehlt, fehlt
json.dump(out, open(os.path.join(ROOT, "data", "ideen.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "Themen,", sum(len(t["aspekte"]) for t in out), "Aspekte,", sum(len(a["felder"]) for t in out for a in t["aspekte"]), "Verweise")
