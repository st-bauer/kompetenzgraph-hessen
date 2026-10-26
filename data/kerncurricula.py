"""Datenbasis Kompetenzgraph Hessen.

Alle Inhalte stammen aus den Kerncurricula Sek I (Fassung Gymnasium) des Hessischen Kultusministeriums.
Seitenangaben beziehen sich auf die jeweiligen PDFs (siehe URL).
AK = Anknüpfungspunkte: Vorschläge, NICHT im KC belegt.
"""

URL = {
    "Biologie": "https://kultus.hessen.de/sites/kultus.hessen.de/files/2021-06/kerncurriculum_biologie_gymnasium.pdf",
    "Chemie": "https://kultus.hessen.de/sites/kultus.hessen.de/files/2021-06/kerncurriculum_chemie_gymnasium-1.pdf",
    "Physik": "https://kultus.hessen.de/sites/kultus.hessen.de/files/2024-02/kc_physik_uesekii_201102-uea.pdf",
    "Erdkunde": "https://kultus.hessen.de/sites/kultus.hessen.de/files/2021-06/kerncurriculum_erdkunde_gymnasium.pdf",
    "Politik und Wirtschaft": "https://kultus.hessen.de/sites/kultus.hessen.de/files/2021-07/kerncurriculum_politik_und_wirtschaft_gymnasium.pdf",
}

# ---------------- Inhaltsfelder ----------------
# (Fach, Basiskonzept(e), Inhaltsfeld, Seite, Hinweis)
IF = [
    ("Biologie", "Struktur und Funktion", "Biologische Strukturen und ihre Funktion", "S. 28", ""),
    ("Biologie", "Struktur und Funktion", "Informationsfluss im Organismus und zwischen Organismen", "S. 28 f.", ""),
    ("Biologie", "System", "Funktionsteilung im Organismus", "S. 29", ""),
    ("Biologie", "System", "Wechselwirkungen in Ökosystemen", "S. 29 f.", ""),
    ("Biologie", "System", "Stoffwechsel und Regelmechanismen", "S. 30", ""),
    ("Biologie", "Entwicklung", "Fortpflanzung und Entwicklung", "S. 31", ""),
    ("Biologie", "Entwicklung", "Sexualität des Menschen", "S. 31", ""),
    ("Biologie", "Entwicklung", "Vielfalt, Veränderung und Abstammung von Lebewesen", "S. 31 f.", ""),
    ("Chemie", "Struktur-Eigenschafts-Beziehungen; Stoff-Teilchen-Beziehungen", "Welt der Stoffe – Identifikation und Ordnung von Stoffen", "S. 22 f.", "Basiskonzepte laut Spalte 'Nutzung fachlicher Konzepte'"),
    ("Chemie", "Struktur-Eigenschafts-Beziehungen; Stoff-Teilchen-Beziehungen", "Der Mix macht's – Stoffgemische", "S. 23 f.", ""),
    ("Chemie", "Struktur-Eigenschafts-Beziehungen; Chemische Reaktion; Energetische Betrachtungen", "Verwandlungen – Chemische Reaktion", "S. 24 f.", ""),
    ("Chemie", "Struktur-Eigenschafts-Beziehungen; Stoff-Teilchen-Beziehungen; Chemische Reaktion", "Tafel des Wissens – Periodensystem der Elemente", "S. 25", ""),
    ("Chemie", "Struktur-Eigenschafts-Beziehungen; Chemische Reaktion; Energetische Betrachtungen", "Schatzkiste der Natur – Chemie in Alltag und Technik", "S. 26", ""),
    ("Chemie", "Stoff-Teilchen-Beziehungen; Struktur-Eigenschafts-Beziehungen; Chemische Reaktion", "Blick hinter die Kulissen – Aufbau von Stoffen und chemische Bindung", "S. 26 f.", ""),
    ("Chemie", "Energetische Betrachtungen; Struktur-Eigenschafts-Beziehungen; Chemische Reaktion; Stoff-Teilchen-Beziehungen", "Magie des Kohlenstoffs – Organische Verbindungen", "S. 27 f.", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Haus der Naturwissenschaften", "S. 22", "Zuordnung Basiskonzept je Inhaltsfeld nur in Abb. 2, nicht als Text auslesbar"),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Erweiterung der Sinne", "S. 22 f.", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Energie in Umwelt und Technik", "S. 23", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Elektrizität im Alltag", "S. 24", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Wettererscheinungen und Klima", "S. 24 f.", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Fortbewegung und Mobilität", "S. 25", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Technik im Dienst des Menschen", "S. 25 f.", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Zukunftssichere Energieversorgung", "S. 26", ""),
    ("Physik", "Materie, Wechselwirkung, System, Energie (fachweit)", "Physik in der Verantwortung", "S. 27", ""),
    ("Erdkunde", "System, Struktur, Funktion, Prozess, Maßstabsebenen (fachweit)", "Umwelt-Gesellschaft-Beziehungen und globale Probleme", "S. 24 f.", "Keine Aufteilung nach Jahrgangsstufen im Gymnasium-KC"),
    ("Erdkunde", "System, Struktur, Funktion, Prozess, Maßstabsebenen (fachweit)", "Natur/Umwelt", "S. 25", ""),
    ("Erdkunde", "System, Struktur, Funktion, Prozess, Maßstabsebenen (fachweit)", "Mensch/Gesellschaft", "S. 25", ""),
    ("Erdkunde", "System, Struktur, Funktion, Prozess, Maßstabsebenen (fachweit)", "Geographie auf regionaler Ebene", "S. 26", ""),
    ("Erdkunde", "System, Struktur, Funktion, Prozess, Maßstabsebenen (fachweit)", "Erde als Planet", "S. 26", ""),
    ("Erdkunde", "System, Struktur, Funktion, Prozess, Maßstabsebenen (fachweit)", "Räumliches Orientierungswissen", "S. 26", ""),
    ("Politik und Wirtschaft", "Systeme und Strukturen; Prozesse und Handlungen; Akteure (immer alle drei)", "Demokratie", "S. 25", "Text im PDF am rechten Rand teilweise abgeschnitten, Wortlaut im Original prüfen"),
    ("Politik und Wirtschaft", "Systeme und Strukturen; Prozesse und Handlungen; Akteure (immer alle drei)", "Wirtschaft", "S. 25 f.", "Text teilweise abgeschnitten"),
    ("Politik und Wirtschaft", "Systeme und Strukturen; Prozesse und Handlungen; Akteure (immer alle drei)", "Individuum und Gesellschaft", "S. 26", "Text teilweise abgeschnitten"),
    ("Politik und Wirtschaft", "Systeme und Strukturen; Prozesse und Handlungen; Akteure (immer alle drei)", "Gesellschaft und Natur", "S. 26", "Text teilweise abgeschnitten"),
    ("Politik und Wirtschaft", "Systeme und Strukturen; Prozesse und Handlungen; Akteure (immer alle drei)", "Recht und Rechtsprechung", "S. 26", "Text teilweise abgeschnitten"),
    ("Politik und Wirtschaft", "Systeme und Strukturen; Prozesse und Handlungen; Akteure (immer alle drei)", "Internationale Beziehungen und Globalisierung", "S. 27", "Text teilweise abgeschnitten"),
]

# ---------------- Schwerpunkte ----------------
B56, B910 = "bis Ende 5/6", "zusätzlich bis Ende 9/10"
C1, C910 = "1. Lernjahr", "zusätzlich bis Ende 9/10"
P1, P910 = "nach ca. Hälfte des Stundenkontingents", "zusätzlich bis Ende 9/10"
OHNE = "keine Stufung im KC (gilt bis Ende 9/10)"

SP = []
def add(fach, feld, stufe, items, seite):
    for it in items:
        SP.append((fach, feld, stufe, it, seite))

# Biologie Kap. 7.3
add("Biologie", "Biologische Strukturen und ihre Funktion", B56, [
    "Bau und Funktion von Organen und Organsystemen von Wirbeltieren oder dem Menschen",
    "Körperformen ausgewählter Organismen und deren Bedeutung für die Lebensweise",
    "Prinzip der Oberflächenvergrößerung anhand von Lunge oder Darm",
    "Gegenspielerprinzip am Beispiel der Skelettmuskulatur"], "S. 41")
add("Biologie", "Biologische Strukturen und ihre Funktion", B910, [
    "Weitergabe genetischer Informationen",
    "Strukturen und Funktionen auf makroskopischer Ebene (Organe, Organsysteme)",
    "Strukturen und Funktionen auf mikroskopischer Ebene (Zellaufbau ausgewählter Zellen)",
    "Schlüssel-Schloss-Prinzip, Oberflächenvergrößerung (auch zellulär), Gegenspielerprinzip"], "S. 41")
add("Biologie", "Informationsfluss im Organismus und zwischen Organismen", B56, [
    "Informationswege im Organismus auf phänomenologischer Ebene",
    "Einfache Beispiele für Verhaltensweisen aus der Tierwelt"], "S. 42")
add("Biologie", "Informationsfluss im Organismus und zwischen Organismen", B910, [
    "Verhaltensweisen von Tieren (intra- und interspezifisch) und des Menschen (soziale Verhaltensweisen, Sexualverhalten)",
    "Leistungsstärke, Belastbarkeit und Gesundheitsschutz von Sinnesorganen (Auge oder Ohr)",
    "Auslösung der Erregung und Erregungsweiterleitung zum Gehirn",
    "Hormone als Botenstoffe im Organismus"], "S. 42")
add("Biologie", "Funktionsteilung im Organismus", B56, [
    "Aufgabenteilung im Organismus: Organsysteme wie Herz-Lungen-System oder Verdauungssystem",
    "Strukturgebundene physiologische Prozesse und ihr Zusammenwirken"], "S. 43")
add("Biologie", "Funktionsteilung im Organismus", B910, [
    "Gewebe und ihre Aufgaben, Spezialisierung von Körperzellen",
    "Vernetzung der Einzelstrukturen im Organismus zum System",
    "Immunsystem: Immunität, Infektionskrankheiten (AIDS und Hepatitis)"], "S. 43")
add("Biologie", "Wechselwirkungen in Ökosystemen", B56, [
    "Tiere und Pflanzen eines ausgewählten Ökosystems: Nahrungsketten und Nahrungsnetze",
    "Kausale Beziehungen zwischen Produzenten, Konsumenten und Destruenten"], "S. 43 f.")
add("Biologie", "Wechselwirkungen in Ökosystemen", B910, [
    "Mehrfaktorielle Beziehungen in Ökosystemen: abiotische und biotische Faktoren, Trophieebenen",
    "Erweiterung der Artenkenntnis",
    "Vernetzung verschiedener Ökosysteme",
    "Gefährdung von Ökosystemen durch Eingriffe des Menschen"], "S. 43 f.")
add("Biologie", "Stoffwechsel und Regelmechanismen", B56, [
    "Regelung der Körpertemperatur und Steuerung von Körperbewegungen",
    "Zusammenhänge zwischen Stoff- und Energieumwandlungen (Verdauung, Atmung, Fotosynthese)",
    "Aspekte zur ausgewogenen Ernährung",
    "Nahrungsbeziehungen, Nahrungsketten und Nahrungsnetze",
    "Auswirkungen von Eingriffen des Menschen in ökologische Beziehungen"], "S. 44 f.")
add("Biologie", "Stoffwechsel und Regelmechanismen", B910, [
    "Regelmechanismen physiologischer Prozesse",
    "Wirkung von Störfaktoren auf Regelmechanismen",
    "Stoffkreisläufe (z. B. Kohlenstoffkreislauf) und globale ökologische Beziehungen",
    "Eingriffe des Menschen in Ökosysteme und systemische Folgen (z. B. Artensterben)",
    "Hormonelle Steuerungen"], "S. 44 f.")
add("Biologie", "Fortpflanzung und Entwicklung", B56, [
    "Fortpflanzungsstrategien bei Wirbeltieren und Blütenpflanzen",
    "Geschlechtliche und ungeschlechtliche Vermehrung",
    "Unterschiedliche Entwicklungsprozesse der Lebewesen"], "S. 45")
add("Biologie", "Fortpflanzung und Entwicklung", B910, [
    "Grundlagen der Vererbung: Mitose und Meiose, genetische Information, Merkmalsausprägung",
    "Vermehrung bei Bakterien und Viren"], "S. 45 f.")
add("Biologie", "Sexualität des Menschen", B56, [
    "Äußere Geschlechtsmerkmale, Veränderung während der Pubertät",
    "Zeugung, Schwangerschaft, Geburt, Empfängnisverhütung",
    "Sexuelle Selbstbestimmung, Rollenverhalten, soziales Miteinander"], "S. 46")
add("Biologie", "Sexualität des Menschen", B910, [
    "Hormone, Empfängnis und Empfängnisverhütung, Reproduktionsmedizin, Schwangerschaftsabbruch",
    "Heterosexuelle und homosexuelle Partnerschaften",
    "Einflüsse auf sexuelles Verhalten, Rollenverhalten, Verantwortung, Selbstbestimmung"], "S. 46")
add("Biologie", "Vielfalt, Veränderung und Abstammung von Lebewesen", B56, [
    "Individuelle Veränderungen biologischer Strukturen durch äußere Einflüsse (z. B. Krafttraining)",
    "Zusammenhang zwischen Körperbau, Lebensweise und Lebensraum",
    "Abstammung und Züchtung, Wild- und Nutzformen"], "S. 47")
add("Biologie", "Vielfalt, Veränderung und Abstammung von Lebewesen", B910, [
    "Mutation und Modifikation, Variabilität innerhalb einer Art",
    "Mutation, Rekombination und Selektion als Evolutionsmechanismen",
    "Eroberung von Wasser, Land oder Luft; Artenvielfalt und Artensterben",
    "Stammbäume, Abstammung des Menschen"], "S. 47")

# Chemie Kap. 7.2
add("Chemie", "Welt der Stoffe – Identifikation und Ordnung von Stoffen", C1, [
    "Chemiespezifischer Stoffbegriff, Stoffeigenschaften, Stoffgruppen",
    "Ordnung von Stoffen anhand verschiedener Kriterien",
    "Stoffidentifikation, Mess- und Nachweisverfahren",
    "Produkt- und Umweltrelevanz von Stoffen, Gefahrenpotenzial"], "S. 30")
add("Chemie", "Welt der Stoffe – Identifikation und Ordnung von Stoffen", C910, [
    "Stoffgruppen nach fachsystematischen Kriterien: Säuren, Laugen, Metalle, Nichtmetalle, Salze, Kunststoffe",
    "Alltags-, Lebens- und Umweltrelevanz von Luft und Wasser",
    "Eignung von Werkstoffen"], "S. 30")
add("Chemie", "Der Mix macht's – Stoffgemische", C1, [
    "Reinstoffe, Stoffgemische und Gemischtypen",
    "Produktherstellung durch Misch- und Trennverfahren",
    "Beziehung zwischen Stoffeigenschaften und anzuwendendem Verfahren"], "S. 30 f.")
add("Chemie", "Der Mix macht's – Stoffgemische", C910, [
    "Zielführende Trenn- und Mischverfahren: Destillation, Neutralisation"], "S. 30 f.")
add("Chemie", "Verwandlungen – Chemische Reaktion", C1, [
    "Abgrenzung physikalischer und chemischer Vorgänge",
    "Aggregatzustand und Aggregatzustandsänderungen",
    "Kennzeichen chemischer Reaktionen",
    "Endotherme und exotherme Reaktionen",
    "Wortgleichungen"], "S. 31")
add("Chemie", "Verwandlungen – Chemische Reaktion", C910, [
    "Aktivierungsenergie, Erhaltung der Masse, Energiebilanz, Donator-Akzeptor-Prinzip",
    "Reaktionsgleichungen mit Stoff- und Reaktionssymbolen, Stöchiometrie"], "S. 31")
add("Chemie", "Tafel des Wissens – Periodensystem der Elemente", C1, ["Elementsymbole"], "S. 32")
add("Chemie", "Tafel des Wissens – Periodensystem der Elemente", C910, [
    "Aufbau des PSE: Gruppen, Perioden, Ordnungszahl, Kernladungszahl, Atommassen",
    "Elektronenkonfiguration und Reaktionsverhalten",
    "Formeln, Stoffdaten, Elektronegativität"], "S. 32")
add("Chemie", "Schatzkiste der Natur – Chemie in Alltag und Technik", C1, [
    "Lösevorgänge im Alltag", "Prinzipien von Affinitätsreihen"], "S. 32")
add("Chemie", "Schatzkiste der Natur – Chemie in Alltag und Technik", C910, [
    "Alltagsrelevante Stoffe und Reaktionen: Säuren, Laugen, Metalle, Nichtmetalle, Salze, Luft, Wasser, Boden",
    "Gefahrenpotenzial bei Stoffen und Reaktionen",
    "Stoffkreisläufe in Natur und Technik",
    "Elektrochemische Vorgänge"], "S. 32 f.")
add("Chemie", "Blick hinter die Kulissen – Aufbau von Stoffen und chemische Bindung", C1, [
    "Teilchenmodell zur Deutung von Phänomenen"], "S. 33")
add("Chemie", "Blick hinter die Kulissen – Aufbau von Stoffen und chemische Bindung", C910, [
    "Differenziertes Atommodell",
    "Aufbau und Reaktionen von Atomen, Molekülen und Ionen",
    "Ionen- und Elektronenpaarbindung, Lewisschreibweise"], "S. 33")
add("Chemie", "Magie des Kohlenstoffs – Organische Verbindungen", C1, [
    "Eigenschaften ausgewählter organischer Stoffe"], "S. 34")
add("Chemie", "Magie des Kohlenstoffs – Organische Verbindungen", C910, [
    "Eigenschaften organischer Stoffe mittels Struktur und funktioneller Gruppen",
    "Systematik anhand von Stoffklassen",
    "Gewinnung, Verwendung und Recycling organischer Stoffe"], "S. 34")

# Physik Kap. 7.2
add("Physik", "Haus der Naturwissenschaften", P1, [
    "Körper und deren Eigenschaften", "Physikalische Größen und ihre Messung"], "S. 29")
add("Physik", "Haus der Naturwissenschaften", P910, [
    "Besonderheiten und Gemeinsamkeiten der Physik, Chemie und Biologie",
    "Historische und aktuelle Erkenntniswege der Physik"], "S. 29")
add("Physik", "Erweiterung der Sinne", P1, [
    "Wahrnehmung der Umgebung mit den Sinnesorganen",
    "Sender-Empfänger-Modell",
    "Schatten als Abwesenheit von Licht",
    "Verhalten von Licht an Grenzflächen",
    "Astronomische Phänomene durch Konstellationen von Sonne, Erde, Mond"], "S. 30")
add("Physik", "Erweiterung der Sinne", P910, [
    "Schall, Licht und ihre Ausbreitung",
    "Optische Phänomene, optische Abbildungen",
    "Auswirkungen von Lärm auf die Gesundheit (Bewertung)"], "S. 30")
add("Physik", "Energie in Umwelt und Technik", P1, [
    "Anschaulicher Energiebegriff", "Energietransport",
    "Energiestrom in die Umgebung als Entwertung von Energie"], "S. 31")
add("Physik", "Energie in Umwelt und Technik", P910, [
    "Energie als quantifizierbare Größe",
    "Energieformen und ihre Umwandlung",
    "Prinzip der Energieerhaltung"], "S. 31")
add("Physik", "Elektrizität im Alltag", P1, [
    "Elektrischer Strom als Transportform von Energie",
    "Elemente des elektrischen Stromkreises",
    "Gefahren beim Umgang mit Elektrizität im Alltag"], "S. 32")
add("Physik", "Elektrizität im Alltag", P910, [
    "Einfluss von Widerständen auf die Stromstärke",
    "Stromkreise als Systeme",
    "Elektrostatische Phänomene"], "S. 32")
add("Physik", "Wettererscheinungen und Klima", P1, [
    "Temperatur und deren Messung",
    "Modelle des Aufbaus der Materie",
    "Aggregatzustände und deren Übergänge",
    "Stoffe bei Temperaturänderung",
    "Anomalie des Wassers und seine Bedeutung für das irdische Leben",
    "Druck als 'Gepresstsein' der Materie"], "S. 33")
add("Physik", "Wettererscheinungen und Klima", P910, [
    "Übertragung thermischer Energie",
    "Druck als physikalische Zustandsgröße, Druck- und Temperaturunterschiede",
    "Einfluss des Menschen auf das Klima und Folgen (Bewertung)"], "S. 33")
add("Physik", "Fortbewegung und Mobilität", P1, ["Weg, Zeit und Geschwindigkeit"], "S. 34")
add("Physik", "Fortbewegung und Mobilität", P910, [
    "Wechselwirkung von Körpern, Trägheit, Wirkungen von Kräften",
    "Menschliche und technische Leistungen und deren Vergleich",
    "Trägheit und Risiken im Straßenverkehr (Bewertung)"], "S. 34")
add("Physik", "Technik im Dienst des Menschen", P1, ["Magnetismus"], "S. 35")
add("Physik", "Technik im Dienst des Menschen", P910, [
    "Kraft wandelnde Systeme", "Phänomen Auftrieb",
    "Magnetische Wirkung des elektrischen Stroms"], "S. 35")
add("Physik", "Zukunftssichere Energieversorgung", P1, [
    "Regenerative und erschöpfbare Energien"], "S. 36")
add("Physik", "Zukunftssichere Energieversorgung", P910, [
    "Umwandlung verschiedener Energieformen in elektrische Energie",
    "Großenergieanlagen, Speicherung und Transport von Energie, Energieversorgungsnetze",
    "Zentrale und dezentrale Energieversorgung, globale Energieproblematik (Bewertung)"], "S. 36")
add("Physik", "Physik in der Verantwortung", P1, [
    "Verantwortung gegenüber der Umwelt",
    "Rolle der Physik bei Umwelt- und Naturereignissen"], "S. 37")
add("Physik", "Physik in der Verantwortung", P910, [
    "Radioaktive Zerfallsprozesse, Auswirkungen verschiedener Strahlungsarten",
    "Konsequenzen der Nutzung physikalischer Forschungsergebnisse"], "S. 37")

# Erdkunde (Stichworte aus Inhaltsfeldbeschreibung Kap. 6)
add("Erdkunde", "Umwelt-Gesellschaft-Beziehungen und globale Probleme", OHNE, [
    "Tourismus, Migration, Standortverlagerungen, Strukturwandel, wirtschaftliche Globalisierung",
    "Naturgeographische Phänomene, die zur Gefahr für den Menschen werden können",
    "Syndrome: Ressourcensicherung, Umweltgefährdung, globale Disparitäten",
    "Prinzipien der Nachhaltigkeit"], "S. 24 f.")
add("Erdkunde", "Natur/Umwelt", OHNE, [
    "Geofaktoren: geologische Gegebenheiten, Oberflächenformen, Klima, Boden, Vegetation"], "S. 25")
add("Erdkunde", "Mensch/Gesellschaft", OHNE, [
    "Demographische Entwicklung, Migration, Globalisierung, Metropolisierung, Strukturwandel, städtisches Wachstum"], "S. 25")
add("Erdkunde", "Geographie auf regionaler Ebene", OHNE, [
    "Regelhaftigkeiten und Besonderheiten bestimmter Raumausschnitte",
    "Folgen von Eingriffen des Menschen in die Umwelt"], "S. 26")
add("Erdkunde", "Erde als Planet", OHNE, [
    "Aufbau der Erde",
    "Rotation, Neigung der Erdachse, Jahreszeiten, Zeitzonen"], "S. 26")
add("Erdkunde", "Räumliches Orientierungswissen", OHNE, [
    "Kontinente, Ozeane, große Gebirgszüge, Bundesländer, europäische Städte und Flüsse",
    "Gradnetz, Klima- und Landschaftszonen, Karten, Atlanten, Pläne"], "S. 26")

# Politik und Wirtschaft (Stichworte aus Inhaltsfeldbeschreibung Kap. 6, Text teilweise abgeschnitten)
add("Politik und Wirtschaft", "Demokratie", OHNE, [
    "Politisches System der Bundesrepublik Deutschland, Grundrechte, Gewaltenteilung, Föderalismus",
    "Rolle der Medien in der Demokratie",
    "Sozialstaat, europäische Integration",
    "Demokratiefeindliche Verhaltensweisen"], "S. 25")
add("Politik und Wirtschaft", "Wirtschaft", OHNE, [
    "Soziale Marktwirtschaft, Funktionsprinzipien des Marktes",
    "Rolle als Verbraucherinnen und Verbraucher sowie künftige Erwerbstätige",
    "Organisierte Interessenwahrnehmung (Verbraucherverbände, Gewerkschaften, Unternehmerverbände)"], "S. 25 f.")
add("Politik und Wirtschaft", "Individuum und Gesellschaft", OHNE, [
    "Sozialisation, Enkulturation, Sozialstruktur, sozialer Wandel, Genderproblematik",
    "Grenzen der Toleranz gegenüber freiheits- und demokratiefeindlichen Gruppen"], "S. 26")
add("Politik und Wirtschaft", "Gesellschaft und Natur", OHNE, [
    "Spannungsfeld zwischen Ökonomie und Ökologie",
    "Nachhaltige Entwicklung, Generationenverantwortung"], "S. 26")
add("Politik und Wirtschaft", "Recht und Rechtsprechung", OHNE, [
    "Rechtssysteme und Menschenrechte",
    "Recht als Rahmen wirtschaftlichen Handelns (z. B. Eigentumsrecht, soziale und ökologische Standards)"], "S. 26")
add("Politik und Wirtschaft", "Internationale Beziehungen und Globalisierung", OHNE, [
    "Internationale politische und ökonomische Verflechtung, Globalisierung",
    "Europäischer Einigungsprozess",
    "Migration und Integration"], "S. 27")

# ---------------- Kompetenzbereiche ----------------
NW = [
    ("Erkenntnisgewinnung", "Beobachten, beschreiben, vergleichen; Planen, untersuchen, auswerten, interpretieren; Arbeiten mit Modellen"),
    ("Kommunikation", "Arbeiten mit Quellen; Kommunizieren, argumentieren; Dokumentieren, präsentieren; Verwenden von Fach- und Symbolsprache"),
    ("Bewertung", "Beurteilen von Alltagskontexten mit naturwissenschaftlichen Kenntnissen; Abwägen und bewerten von Handlungsfolgen auf Natur und Gesellschaft; Reflektieren und bewerten von Handlungsoptionen als Grundlage gesellschaftlicher Partizipation"),
    ("Nutzung fachlicher Konzepte", "Konzeptbezogenes Strukturieren von Sachverhalten; Vernetzen von Sachverhalten und Konzepten; Problemorientiertes und konzeptbezogenes Erschließen von Sachverhalten"),
]
KB = []
for f, s in [("Biologie", "S. 14"), ("Chemie", "S. 13"), ("Physik", "S. 13")]:
    for k, t in NW:
        KB.append((f, k, t, s, "In Biologie, Chemie und Physik einheitlich definiert"))
KB += [
    ("Erdkunde", "Geographische Analysekompetenz", "Umwelt-Gesellschaft-Beziehungen sowie natur- und humangeographische Systeme untersuchen", "S. 15", "Übergeordnet: raumbezogene Handlungskompetenz"),
    ("Erdkunde", "Räumliche Orientierungskompetenz", "Orientierungswissen, Orientierungsraster und Ordnungssysteme nutzen; Karten lesen und auswerten; Raumwahrnehmung reflektieren", "S. 15", ""),
    ("Erdkunde", "Geographische Methodenkompetenz", "Geographisch relevante Informationsquellen und Methoden nutzen und reflektieren", "S. 16", ""),
    ("Erdkunde", "Geographische Urteils- und Kommunikationskompetenz", "Sachverhalte beurteilen und begründet bewerten; sach- und adressatengerecht kommunizieren", "S. 16", ""),
    ("Politik und Wirtschaft", "Analysekompetenz", "fragen, unterscheiden, beschreiben, strukturieren", "S. 18", ""),
    ("Politik und Wirtschaft", "Urteilskompetenz", "überprüfen, schlussfolgern, bewerten, entscheiden", "S. 18", ""),
    ("Politik und Wirtschaft", "Handlungskompetenz", "formulieren, vertreten, sich beteiligen, umsetzen", "S. 18", ""),
    ("Politik und Wirtschaft", "Methodenkompetenz", "entwickeln, forschen, aufbereiten, präsentieren", "S. 18", ""),
]

# ---------------- Belegte Querbezüge ----------------
QB = [
    ("alle fünf", "alle Fächer", "Teil A: Kompetenzbereiche und Inhaltsfelder sollen auch über die Fächergrenzen hinaus vernetzt werden", "Kap. 1, S. 7"),
    ("Biologie, Chemie, Physik", "untereinander", "Kompetenzbereiche der drei Naturwissenschaften sind einheitlich definiert und in Teilbereiche gegliedert", "Kap. 3 (Bio S. 13 f., Ch S. 12 f., Ph S. 12 f.)"),
    ("Physik", "Erdkunde", "Bei den zentralen Konzepten der PISA-Studie (u. a. System Erde und Weltraum) bietet sich eine Zusammenarbeit mit Erdkunde an", "Kap. 3, S. 12"),
    ("Physik", "Biologie, Chemie", "Das Basiskonzept Energie findet sich auch in den Fächern Biologie und Chemie wieder", "Kap. 5, S. 18"),
    ("Physik", "Biologie, Chemie", "Inhaltlicher Schwerpunkt 'Besonderheiten und Gemeinsamkeiten der Physik, Chemie und Biologie' (Haus der Naturwissenschaften)", "Kap. 7.2, S. 29"),
    ("Biologie", "Sozial- und Geisteswissenschaften, Naturwissenschaften", "Anknüpfungspunkte zu Sozial- und Geisteswissenschaften sowie den weiteren Naturwissenschaften", "Kap. 3, S. 11"),
    ("Biologie", "sozial- und geisteswissenschaftliche Fächer", "Gesundheits-, Sexual- und Umwelterziehung sowie Bioethik; ergänzende Konzepte und Arbeitsweisen aus sozial- und geisteswissenschaftlichen Fächern", "Kap. 4, S. 19"),
    ("Biologie", "andere Fächer, Einrichtungen", "Sexualität des Menschen (5/6): Zusammenarbeit mit anderen Fächern oder Einrichtungen", "Kap. 7.1, S. 38; Kap. 7.3, S. 46"),
    ("Chemie", "andere Fächer", "Schnittstellen u. a.: Gesellschaftsrelevanz und Umweltbewusstsein, moralisches Empfinden, Teamfähigkeit, ästhetisches Empfinden, kreatives Gestalten, Formulierungsfähigkeit, räumliches Vorstellungsvermögen, Gesundheitsbewusstsein und Ernährung", "Kap. 4, S. 16"),
    ("Erdkunde", "Geschichte, Politik und Wirtschaft", "Gemeinsames gesellschaftswissenschaftliches Aufgabenfeld; Perspektiven Raum (Erdkunde), Zeit (Geschichte), Entscheidung und Gestaltung (PoWi); Themenkoordination und zeitweilig fachübergreifender Unterricht; Lernbereich Gesellschaftslehre möglich", "Kap. 3, S. 12 f."),
    ("Politik und Wirtschaft", "Erdkunde, Geschichte", "Gleicher Text wie bei Erdkunde; Abb. 1 zeigt Beispiele für Verzahnungen von Inhaltsfeldern (nur Grafik, nicht als Text auslesbar)", "Kap. 3, S. 13 f."),
    ("Politik und Wirtschaft", "andere Fächer", "Mit * markierte Standards für fächerübergreifendes Lernen, u. a. Methoden anderer Fächer nutzen (Statistik, naturwissenschaftliches Experiment)", "Kap. 6, S. 22 ff."),
    ("Politik und Wirtschaft", "Geschichte", "Handlungskompetenz: undemokratisches Verhalten erkennen und ein historisches Beispiel damit in Verbindung bringen", "Kap. 6, S. 23"),
]

# ---------------- Anknüpfungspunkte (Vorschlag) ----------------
AK = [
    ("Energie", [
        ("Physik", "Energie in Umwelt und Technik", "Anschaulicher Energiebegriff; Energieformen und ihre Umwandlung", P1 + " / " + P910),
        ("Physik", "Zukunftssichere Energieversorgung", "Regenerative und erschöpfbare Energien", P1),
        ("Chemie", "Verwandlungen – Chemische Reaktion", "Endotherme und exotherme Reaktionen", C1),
        ("Biologie", "Stoffwechsel und Regelmechanismen", "Zusammenhänge zwischen Stoff- und Energieumwandlungen", B56),
        ("Erdkunde", "Umwelt-Gesellschaft-Beziehungen und globale Probleme", "Ressourcensicherung", OHNE),
        ("Politik und Wirtschaft", "Gesellschaft und Natur", "Spannungsfeld zwischen Ökonomie und Ökologie", OHNE)]),
    ("Klima und Wetter", [
        ("Physik", "Wettererscheinungen und Klima", "Einfluss des Menschen auf das Klima und Folgen", P910),
        ("Erdkunde", "Natur/Umwelt", "Geofaktor Klima", OHNE),
        ("Biologie", "Stoffwechsel und Regelmechanismen", "Stoffkreisläufe (z. B. Kohlenstoffkreislauf)", B910),
        ("Politik und Wirtschaft", "Gesellschaft und Natur", "Nachhaltige Entwicklung, Generationenverantwortung", OHNE)]),
    ("Wasser, Luft, Boden, Stoffkreisläufe", [
        ("Chemie", "Schatzkiste der Natur – Chemie in Alltag und Technik", "Luft, Wasser, Boden; Stoffkreisläufe in Natur und Technik", C910),
        ("Chemie", "Welt der Stoffe – Identifikation und Ordnung von Stoffen", "Alltags-, Lebens- und Umweltrelevanz von Luft und Wasser", C910),
        ("Physik", "Wettererscheinungen und Klima", "Anomalie des Wassers", P1),
        ("Biologie", "Stoffwechsel und Regelmechanismen", "Stoffkreisläufe (z. B. Kohlenstoffkreislauf)", B910),
        ("Erdkunde", "Natur/Umwelt", "Geofaktor Boden", OHNE)]),
    ("Ökosysteme und Eingriffe des Menschen", [
        ("Biologie", "Wechselwirkungen in Ökosystemen", "Gefährdung von Ökosystemen durch Eingriffe des Menschen", B910),
        ("Biologie", "Stoffwechsel und Regelmechanismen", "Auswirkungen von Eingriffen des Menschen in ökologische Beziehungen", B56),
        ("Erdkunde", "Umwelt-Gesellschaft-Beziehungen und globale Probleme", "Umweltgefährdung", OHNE),
        ("Erdkunde", "Geographie auf regionaler Ebene", "Folgen von Eingriffen des Menschen in die Umwelt", OHNE),
        ("Physik", "Physik in der Verantwortung", "Verantwortung gegenüber der Umwelt", P1),
        ("Politik und Wirtschaft", "Gesellschaft und Natur", "Nachhaltige Entwicklung", OHNE)]),
    ("Sinne und Wahrnehmung", [
        ("Biologie", "Informationsfluss im Organismus und zwischen Organismen", "Sinnesorgane (Auge oder Ohr), Gesundheitsschutz", B910),
        ("Physik", "Erweiterung der Sinne", "Wahrnehmung der Umgebung mit den Sinnesorganen", P1),
        ("Physik", "Erweiterung der Sinne", "Auswirkungen von Lärm auf die Gesundheit", P910)]),
    ("Mobilität und Verkehr", [
        ("Physik", "Fortbewegung und Mobilität", "Weg, Zeit, Geschwindigkeit; Trägheit und Risiken im Straßenverkehr", P1 + " / " + P910),
        ("Chemie", "Magie des Kohlenstoffs – Organische Verbindungen", "Kohlenwasserstoffverbindungen u. a. aus Energiewirtschaft und Verkehr (Kap. 6, S. 27)", "Inhaltsfeldbeschreibung"),
        ("Politik und Wirtschaft", "Wirtschaft", "Analysekompetenz: externe Effekte bei verkehrspolitischen Fragen (Kap. 4, S. 16)", "Kompetenzbeschreibung"),
        ("Erdkunde", "Mensch/Gesellschaft", "Humangeographisches Teilsystem Verkehr (Kap. 5, S. 19)", "Konzeptbeschreibung")]),
    ("Ernährung, Gesundheit, Konsum", [
        ("Biologie", "Stoffwechsel und Regelmechanismen", "Aspekte zur ausgewogenen Ernährung", B56),
        ("Biologie", "Stoffwechsel und Regelmechanismen", "Bewertung des Konsumverhaltens im Hinblick auf Haltung und Nutzung von Lebewesen", B56),
        ("Chemie", "Magie des Kohlenstoffs – Organische Verbindungen", "Organische Stoffe aus Ernährung und Hygiene (Kap. 6, S. 27)", "Inhaltsfeldbeschreibung"),
        ("Politik und Wirtschaft", "Wirtschaft", "Rolle als Verbraucherinnen und Verbraucher", OHNE)]),
    ("Teilchen und Aufbau der Materie", [
        ("Chemie", "Blick hinter die Kulissen – Aufbau von Stoffen und chemische Bindung", "Teilchenmodell zur Deutung von Phänomenen", C1),
        ("Physik", "Wettererscheinungen und Klima", "Modelle des Aufbaus der Materie; Aggregatzustände", P1),
        ("Chemie", "Verwandlungen – Chemische Reaktion", "Aggregatzustand und Aggregatzustandsänderungen", C1),
        ("Physik", "Physik in der Verantwortung", "Radioaktive Zerfallsprozesse", P910)]),
    ("Ressourcen und Recycling", [
        ("Chemie", "Magie des Kohlenstoffs – Organische Verbindungen", "Gewinnung, Verwendung und Recycling organischer Stoffe", C910),
        ("Physik", "Zukunftssichere Energieversorgung", "Regenerative und erschöpfbare Energien", P1),
        ("Erdkunde", "Umwelt-Gesellschaft-Beziehungen und globale Probleme", "Ressourcensicherung", OHNE),
        ("Politik und Wirtschaft", "Gesellschaft und Natur", "Spannungsfeld zwischen Ökonomie und Ökologie", OHNE)]),
    ("Migration und Globalisierung", [
        ("Erdkunde", "Mensch/Gesellschaft", "Migration, Globalisierung, Metropolisierung", OHNE),
        ("Erdkunde", "Umwelt-Gesellschaft-Beziehungen und globale Probleme", "Migration, Standortverlagerungen, wirtschaftliche Globalisierung", OHNE),
        ("Politik und Wirtschaft", "Internationale Beziehungen und Globalisierung", "Globalisierung; Migration und Integration", OHNE)]),
    ("Technik, Forschung und Verantwortung", [
        ("Physik", "Physik in der Verantwortung", "Konsequenzen der Nutzung physikalischer Forschungsergebnisse", P910),
        ("Biologie", "Vielfalt, Veränderung und Abstammung von Lebewesen", "Bewertung der Eingriffe des Menschen in das Erbgut", B910),
        ("Biologie", "Fortpflanzung und Entwicklung", "Bewertung gentechnischer Veränderungen von Pflanzen und Tieren", B910),
        ("Chemie", "Verwandlungen – Chemische Reaktion", "Chancen und Grenzen bei der Herstellung von Stoffen (Bewertung, Kap. 6, S. 24)", "Inhaltsfeldbeschreibung")]),
]

HIN = [
    ("Bildungsgang", "Inhaltsfelder sind für 17 Fächer in allen drei KC-Fassungen erfasst (Hauptschule, Realschule, Gymnasium). Schwerpunkte, Kompetenzbereiche und Querbezüge gibt es bisher nur für die fünf Pilotfächer in der Gymnasialfassung."),
    ("Fächerauswahl", "Aufgenommen sind die Fächer einer IGS 5 bis 10. Latein, Griechisch, Chinesisch, Arabisch sowie alevitische, jüdische und islamische Religion fehlen noch. Informatik gibt es nur als KC für den Wahlunterricht am Gymnasium."),
    ("Moderne Fremdsprachen", "Ein gemeinsames KC für alle modernen Fremdsprachen. Die Inhaltsfelder sind drei Lebenswelten."),
    ("Kunst", "Die Zuordnung der neun Inhaltsfelder zu den drei Kernbereichen steht nur in Abb. 2 (Kap. 5)."),
    ("Religion", "Evangelische und Katholische Religion liegen in der neuen KC-Fassung von 2026 vor."),
    ("BNE", "BNE ist nach § 6 Abs. 4 HSchG ein Aufgabengebiet. Die KC von 2011 nennen BNE nicht ausdrücklich. Als Beleg zählt nur, wo das KC selbst Nachhaltigkeit nennt (Blatt 'BNE Belege'). Die SDG-Zuordnung ist ein Vorschlag."),
    ("Stufung", "Die Stufen sind nicht einheitlich: Biologie 'bis Ende 5/6', Chemie '1. Lernjahr', Physik 'nach ca. der Hälfte des Stundenkontingents', jeweils plus 'bis Ende 9/10'. Erdkunde und Politik und Wirtschaft haben im Gymnasium-KC keine Stufung. Die Zuordnung zu Jahrgängen hängt an der Stundentafel bzw. am Schulcurriculum."),
    ("Jahrgang 8", "Biologie, Chemie, Physik, Erdkunde und PoWi weisen für das Gymnasium ausdrücklich keine Kompetenzerwartungen für Jahrgang 6/8 bzw. 8 aus (jeweils Kap. 7)."),
    ("Erdkunde, PoWi", "Die Einträge im Blatt 'Schwerpunkte' sind Stichworte aus den Inhaltsfeldbeschreibungen (Kap. 6), da es keine Schwerpunkt-Tabelle gibt."),
    ("PoWi", "Im PDF ist der rechte Teil der quer gesetzten Tabellen beim Auslesen abgeschnitten. Stichworte bitte am Original prüfen."),
    ("Grafiken", "Abbildungen (z. B. Basiskonzept-Zuordnung Physik, Verzahnung Erdkunde/PoWi/Geschichte) ließen sich nicht als Text auslesen und fehlen."),
    ("Wortlaut", "Schwerpunkte sind teils gekürzt oder zusammengefasst. Für verbindliche Formulierungen gilt das Original (Seitenangabe je Zeile)."),
    ("Anknüpfungspunkte", "Das Blatt 'Anknüpfungspunkte' enthält Vorschläge auf Basis gemeinsamer Stichworte. Sie stehen so nicht im KC und sind fachlich zu prüfen."),
]

