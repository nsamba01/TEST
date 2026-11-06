# -*- coding: utf-8 -*-
"""RAPPORT DE CONTRÔLE QUALITÉ — livrable 05.

Document autonome : il documente ce qui a été extrait de Tech-4, les indicateurs
identifiés, les informations manquantes, les incohérences relevées, les
recommandations méthodologiques et les contrôles effectués sur les livrables.
"""
import design as D
from design import Doc
import data as T

NA = T.NA

META = {
    "title": "Rapport de contrôle qualité — PMNS-NAC Kwilu",
    "author": "Consortium SANRU – ICHESS – FONLIV – FDSS",
    "subject": "Contrôle qualité documentaire et technique des livrables de suivi-évaluation 2027–2028",
    "header_left": "PMNS-NAC Kwilu — Rapport de contrôle qualité",
    "header_right": "Consortium SANRU – ICHESS – FONLIV – FDSS",
    "footer_left": "DP N° ZR-DRC-MSP-235334-CS-QCBS · Tech-4",
    "footer_center": "1ᵉʳ janvier 2027 – 31 décembre 2028",
    "cover_kicker": "Contrôle qualité · Traçabilité · Conformité",
    "cover_title": "RAPPORT DE CONTRÔLE QUALITÉ",
    "cover_year": "LIVRABLES 01 À 04",
    "cover_img": "figures/cover_qc.png",
    "cover_org": ["CONSORTIUM SANRU – ICHESS – FONLIV – FDSS",
                  "Chef de file : SANRU"],
    "cover_sub": ["Projet Multisectoriel de Nutrition et de Santé — Volet Nutrition",
                  "à Assise Communautaire (PMNS-NAC), province du Kwilu, RDC"],
    "cover_projet": ["Lot documentaire 01 à 04",
                     "Plan de suivi-évaluation · Cadre de performance"],
    "cover_source": ["Document source contrôlé : Tech-4 — Description de l’approche,",
                     "de la méthodologie et du programme de travail",
                     "Demande de Propositions N° ZR-DRC-MSP-235334-CS-QCBS"],
    "cover_periode": "Livrables contrôlés : 01 à 04 — période 2027–2028",
    "cover_version": "Version 1.0 — rapport de contrôle interne",
    "cover_footer": ["Ce rapport documente la fidélité documentaire, les informations manquantes, les incohérences",
                     "relevées dans la source et les contrôles effectués avant diffusion."],
}


def build():
    d = Doc(META)

    # ------------------------------------------------------------------
    d.h1("", "Synthèse du contrôle")

    d.lead("Le contrôle porte sur les quatre livrables du lot — plan de suivi-évaluation (versions Word et PDF), "
           "cadre de performance (versions Excel et PDF) — confrontés au formulaire TECH-4 du consortium. "
           "La conclusion est la suivante : les livrables sont <b>conformes</b> à l’exigence de fidélité "
           "documentaire, mais ils comportent des <b>zones incomplètes</b> qui proviennent exclusivement du "
           "document source et non de la production.")

    d.kpis([("41", "indicateurs identifiés"), ("14", "résultats intermédiaires"),
            ("9", "incohérences relevées"), ("30", "contrôles effectués")])

    d.h3("Conclusion du contrôle")
    d.table(
        ["Point de contrôle", "Résultat", "Observation"],
        [0.30, 0.16, 0.54],
        [["Fidélité au document source", "Conforme",
          "Aucun objectif, résultat, indicateur, volume, montant ou mécanisme institutionnel n’a été ajouté. "
          "Les seuls apports sont des propositions explicitement étiquetées."],
         ["Traçabilité des éléments extraits", "Conforme",
          "Chaque section du plan est rattachée à un passage de Tech-4 (annexe D du plan, section 7 du présent "
          "rapport)."],
         ["Couverture des objectifs", "Conforme",
          "Les quatre objectifs spécifiques et l’objectif global sont couverts, ainsi que le résultat "
          "intermédiaire 4.5 consacré au suivi-évaluation."],
         ["Valeurs de référence", "Non disponible dans la source",
          "Tech-4 ne fournit pas de valeurs de référence propres au projet. Elles sont signalées « À préciser » "
          "et leur obtention est planifiée (évaluation de base)."],
         ["Cibles annuelles 2027 et 2028", "Non disponible dans la source",
          "Tech-4 ne fixe aucune cible annuelle. Les colonnes sont renseignées « À préciser » ; aucune cible "
          "n’a été inventée ni reportée d’une année sur l’autre."],
         ["Cohérence entre livrables", "Conforme",
          "Les quatre livrables sont produits à partir du même module de données : codes, intitulés, "
          "définitions, formules et cibles sont identiques. Vérification automatisée effectuée."],
         ["Qualité de mise en forme", "Conforme",
          "Aucun texte tronqué, aucun tableau débordant, pagination continue, sommaire automatique à jour, "
          "signets PDF fonctionnels."],
         ["Identité graphique Word / PDF", "Conforme",
          "Couverture, palette, typographie, tableaux, graphiques, en-têtes, pieds de page et hiérarchie des "
          "titres proviennent d’une source de mise en page unique."]],
        size=7.6,
        caption="Tableau 1 — Synthèse des résultats du contrôle",
        note="« Conforme » signifie que l’exigence est satisfaite. « Non disponible dans la source » signifie que "
             "la donnée est absente de Tech-4 et qu’elle a été signalée sans être inventée.")

    # ------------------------------------------------------------------
    # 1. OBJET ET MÉTHODE
    # ------------------------------------------------------------------
    d.h1("1", "Objet, périmètre et méthode du contrôle")

    d.h2("1.1", "Objet")
    d.p("Le contrôle qualité poursuit quatre finalités : (i) vérifier que les livrables n’ajoutent aucune "
        "information au document source ; (ii) vérifier que tous les éléments pertinents de Tech-4 ont été "
        "exploités ; (iii) identifier et documenter les informations manquantes et les incohérences du document "
        "source ; (iv) vérifier la qualité technique et la cohérence des livrables entre eux.")

    d.h2("1.2", "Périmètre")
    d.table(
        ["Livrable", "Fichier contrôlé", "Objet du contrôle"],
        [0.10, 0.40, 0.50],
        [["01", "01_Plan_Suivi_Evaluation_2027_2028.docx", "Contenu, structure, mise en forme, sommaire, pagination"],
         ["02", "02_Plan_Suivi_Evaluation_2027_2028.pdf", "Rendu final, débordements, signets, pagination"],
         ["03", "03_Cadre_Performance_2027_2028.xlsx", "Structure des tableaux, filtres, volets figés, cohérence "
          "des valeurs avec les livrables 01 et 02"],
         ["04", "04_Cadre_Performance_2027_2028.pdf", "Rendu final du cadre de performance, 14 colonnes, "
          "41 fiches techniques"],
         ["—", "Tech-4 (document source)", "Intégrité de l’extraction, exhaustivité, incohérences internes"]],
        size=7.8,
        caption="Tableau 2 — Périmètre du contrôle")

    d.h2("1.3", "Méthode")
    d.numbered([
        "<b>Extraction intégrale</b> du document source : texte linéaire de l’ensemble des paragraphes et des "
        "seize tableaux, plus extraction séparée des trente-trois images, dont plusieurs contiennent des "
        "informations absentes du texte (cadre logique, programme de travail, organigramme).",
        "<b>Recensement structuré</b> : objectifs, résultats intermédiaires, activités, volumes, cibles, "
        "indicateurs, sources de vérification, responsabilités, mécanismes institutionnels, données de contexte.",
        "<b>Construction d’un référentiel unique</b> de 41 indicateurs, utilisé par les quatre livrables afin "
        "d’exclure toute divergence de valeur.",
        "<b>Confrontation systématique</b> de chaque affirmation des livrables à un passage identifié de Tech-4.",
        "<b>Contrôle automatisé</b> de la cohérence : comparaison des codes, intitulés, unités, références et "
        "cibles entre les livrables ; détection des débordements de texte dans les fichiers PDF ; vérification "
        "de la pagination et du sommaire.",
        "<b>Contrôle visuel</b> de chaque page des fichiers PDF, à la résolution de lecture.",
    ])

    # ------------------------------------------------------------------
    # 2. ÉLÉMENTS EXTRAITS
    # ------------------------------------------------------------------
    d.h1("2", "Éléments extraits du document source")

    d.h2("2.1", "Inventaire quantitatif")
    d.table(
        ["Catégorie d’élément", "Quantité relevée", "Localisation dans Tech-4"],
        [0.34, 0.20, 0.46],
        [["Objectif général", "1", "§1.3 et cadre logique"],
         ["Objectifs spécifiques", "4 (OS1 à OS4)", "§1.4 et programme de travail"],
         ["Résultats intermédiaires", "14 (RI 1.1 à RI 4.5)", "Programme de travail, section B.1"],
         ["Activités du programme de travail", "Plus de 200 lignes codifiées", "Section B.1"],
         ["Activités de suivi-évaluation", "9 (5.1 à 5.9)", "RI 4.5 et programme de travail"],
         ["Indicateurs identifiés", "41", "Cadre logique, §B.1, §RI 4.2, §OS2, §OS3"],
         ["Zones de santé", "10", "§1.6 et tableau de répartition"],
         ["Aires de santé", "250", "Tableau de répartition par zone"],
         ["Formations sanitaires", "423 (413 CS/UNTA et 10 HGR/UNTI)", "Programme de travail"],
         ["Cellules d’animation communautaire", "3 188 (938 nouvelles, 1 044 redynamisées)", "§OS1 et §OS3"],
         ["CODESA et UCODESA", "250 CODESA et 10 UCODESA", "§OS3"],
         ["Relais communautaires", "8 314 à couvrir, 4 956 à doter de téléphones", "§RI 3.2 et programme de travail"],
         ["Sites de soins communautaires", "190", "Programme de travail"],
         ["Postes clés du consortium", "5 postes clés et 1 poste additionnel", "§B.1 et tableau des personnels"],
         ["Volumes financiers", "Aucun budget global ; seules des unités de subvention et de prime",
          "§OS3 et §RI 3.3"]],
        size=7.6,
        caption="Tableau 3 — Inventaire des éléments extraits",
        note="Les quantités indiquées sont celles du document source ; elles sont reprises sans recalcul.")

    d.h2("2.2", "Données de contexte documentées")
    d.table(
        ["Indicateur de contexte", "Valeur", "Source citée par Tech-4"],
        [0.44, 0.20, 0.36],
        [["Retard de croissance, enfants de moins de 5 ans (Kwilu)", "47 %", "MICS-Palu 2017-2018 / MICS 6"],
         ["Retard de croissance, enfants de moins de 5 ans (national)", "42 %", "MICS 2017-2018"],
         ["Insuffisance pondérale, enfants de moins de 5 ans (Kwilu)", "34,8 %", "MICS 2017-2018"],
         ["Allaitement maternel exclusif (Kwilu)", "32,7 %", "MICS 2017-2018"],
         ["Allaitement maternel exclusif (national)", "53,5 %", "MICS 2017-2018"],
         ["Initiation précoce de l’allaitement (Kwilu)", "29,2 %", "MICS 2017-2018"],
         ["Alimentation de complément adéquate (Kwilu)", "18 %", "MICS 2017-2018"],
         ["Diversité alimentaire minimale (Kwilu)", "27,1 %", "MICS 2017-2018"],
         ["Fréquence minimale des repas (Kwilu)", "47 %", "MICS 2017-2018"],
         ["Lavage des mains aux moments critiques (Kwilu)", "18 %", "MICS 2017-2018"],
         ["Quatre consultations prénatales ou plus (Kwilu)", "24,3 %", "MICS 2017-2018"],
         ["Consultation préscolaire redynamisée (Kwilu)", "47,1 %", "PRONANUT Kwilu, rapport annuel 2020"],
         ["ANJE (Kwilu)", "50 %", "PRONANUT Kwilu, rapport annuel 2020"],
         ["PCIMA et NAC (Kwilu)", "0 %", "PRONANUT Kwilu, rapport annuel 2020"],
         ["Réunions mensuelles des CAC tenues", "53,6 % (2 250 sur 3 188)", "DHIS2 2021"],
         ["Couverture des CAC installés", "71 %", "DPS Kwilu 2021"],
         ["Plans d’action communautaire (PAC)", "16 %", "Plan stratégique national de santé communautaire 2019-2022"],
         ["Insécurité alimentaire sévère (Kwilu)", "49,9 %", "IPC 2021-2022"],
         ["Insécurité alimentaire sévère (national)", "43,7 %", "IPC 2021-2022"],
         ["Cas de VBG déclarés (Kwilu)", "366 cas, soit 0,49 % ; 41 % de moins de 18 ans", "DHIS2 2021 / sous-cluster VBG"],
         ["Personnel de santé formé au PCIMA", "27 %", "PNDS recadré 2019-2022"]],
        size=7.4,
        caption="Tableau 4 — Données de contexte reprises dans les livrables",
        note="Ces données sont des valeurs de contexte provinciales ou nationales : elles ne constituent pas des "
             "valeurs de référence du projet et ne sont jamais présentées comme telles.")

    # ------------------------------------------------------------------
    # 3. INDICATEURS
    # ------------------------------------------------------------------
    d.h1("3", "Indicateurs identifiés")

    d.h2("3.1", "Répartition par niveau et par objectif")
    from collections import Counter
    rows = []
    labels = {"OG": "Objectif global", "OS1": "OS1 — Sites communautaires et NAC",
              "OS2": "OS2 — VBG et prise en charge des victimes",
              "OS3": "OS3 — Structures de participation communautaire",
              "OS4": "OS4 — Appui au système de santé",
              "OS5": "RI 4.5 — Suivi-évaluation et apprentissage"}
    for code in ["OG", "OS1", "OS2", "OS3", "OS4", "OS5"]:
        sub = [i for i in T.INDICATEURS if i["obj_c"] == code]
        c = Counter(i["niveau"] for i in sub)
        rows.append([code, labels[code], str(c.get("Impact", 0)), str(c.get("Effet", 0)),
                     str(c.get("Extrant", 0)), str(c.get("Réalisation", 0)), str(len(sub))])
    c = Counter(i["niveau"] for i in T.INDICATEURS)
    rows.append(["<b>Total</b>", "", "<b>%d</b>" % c.get("Impact", 0), "<b>%d</b>" % c.get("Effet", 0),
                 "<b>%d</b>" % c.get("Extrant", 0), "<b>%d</b>" % c.get("Réalisation", 0),
                 "<b>%d</b>" % len(T.INDICATEURS)])
    d.table(["Objectif", "Intitulé", "Impact", "Effet", "Extrant", "Réalisation", "Total"],
            [0.09, 0.41, 0.08, 0.08, 0.10, 0.11, 0.13], rows,
            align=["l", "l", "c", "c", "c", "c", "c"], size=7.8,
            caption="Tableau 5 — Indicateurs identifiés, par objectif et par niveau",
            note="Chaque objectif est couvert par au moins un indicateur.")

    d.h2("3.2", "Indicateurs explicitement formulés et indicateurs dérivés")
    d.p("Tous les indicateurs ne se valent pas du point de vue de la traçabilité. Le tableau ci-après distingue "
        "les indicateurs dont le libellé figure textuellement dans Tech-4 de ceux qui ont été construits à "
        "partir de la description des activités et des résultats, sans libellé d’indicateur explicite. Ces "
        "derniers sont signalés dans leur rubrique « justification ».")
    explicit = [i for i in T.INDICATEURS if "proposition" not in i["justification"].lower()
                and "dérivé" not in i["justification"].lower()]
    derived = [i for i in T.INDICATEURS if i not in explicit]
    d.table(
        ["Catégorie", "Nombre", "Codes", "Portée"],
        [0.20, 0.08, 0.34, 0.38],
        [["Indicateurs formulés dans Tech-4", str(len(explicit)),
          ", ".join(i["code"] for i in explicit),
          "Repris sans modification de libellé ; définitions et formules précisées"],
         ["Indicateurs dérivés ou proposés", str(len(derived)),
          ", ".join(i["code"] for i in derived),
          "Construits à partir des activités et résultats décrits ; libellé à valider"]],
        size=7.4,
        caption="Tableau 6 — Origine des indicateurs",
        note="La distinction est reprise dans la rubrique « justification » de chaque fiche technique du cadre "
             "de performance (livrable 04).")

    d.h2("3.3", "Indicateurs du cadre logique")
    d.p("Le cadre logique de Tech-4 ne comporte que deux lignes renseignées : l’objectif global — "
        "<i>« accroître l’accès et l’utilisation du paquet de services de nutrition de qualité dans les FOSA et "
        "dans la communauté »</i> — et son indicateur objectivement vérifiable — <i>« nombre d’enfants de moins "
        "de 5 ans ayant bénéficié d’un paquet holistique de prise en charge de la malnutrition »</i> —, avec "
        "pour sources de vérification les rapports programmatiques du projet et les rapports périodiques du "
        "PRONANUT. Les autres lignes du cadre logique sont vides dans le formulaire transmis. Les indicateurs "
        "des niveaux inférieurs ont donc été recherchés dans le programme de travail et dans les résultats "
        "intermédiaires, où ils figurent sous forme de listes d’indicateurs et d’activités.")

    # ------------------------------------------------------------------
    # 4. INFORMATIONS MANQUANTES
    # ------------------------------------------------------------------
    d.h1("4", "Informations manquantes dans le document source")

    d.p("Les informations ci-après sont indispensables au suivi-évaluation et ne figurent pas dans Tech-4. Elles "
        "ne sont jamais remplacées par une estimation : elles sont signalées « À préciser » ou « Non renseigné "
        "dans le document source », et leur modalité d’obtention est proposée.")

    d.table(
        ["N°", "Information manquante", "Incidence sur les livrables", "Traitement retenu"],
        [0.05, 0.29, 0.30, 0.36],
        [["M1", "Valeurs de référence des 41 indicateurs",
          "Impossible de mesurer un progrès ; colonne « référence » incomplète",
          "Mention « À préciser » ; obtention par l’évaluation de base (T1 2027)"],
         ["M2", "Cibles annuelles 2027 et 2028",
          "Impossible de juger de l’atteinte ; colonnes « Cible 2027 » et « Cible 2028 » incomplètes",
          "Mention « À préciser » ; atelier de validation des cibles (T1 2027)"],
         ["M3", "Ventilation annuelle des volumes de livrables",
          "Les volumes de Tech-4 couvrent toute la durée du projet",
          "Restitués en « cible globale », sans ventilation inventée"],
         ["M4", "Budget du projet et clé de répartition des financements",
          "Aucun suivi financier possible dans le cadre de performance",
          "Point signalé ; hors périmètre du lot, documents budgétaires à obtenir"],
         ["M5", "Indicateurs explicites des objectifs spécifiques 2 et 4",
          "Tech-4 décrit les activités sans nommer les indicateurs",
          "Indicateurs dérivés, signalés comme tels dans la rubrique « justification »"],
         ["M6", "Liste des performances contractuelles conditionnant les primes communautaires",
          "Le seuil de 80 % du cadre logique ne peut être appliqué",
          "Indicateur de fonctionnalité retenu sans seuil ; seuil à arrêter"],
         ["M7", "Dénombrements servant de dénominateur",
          "Plusieurs indicateurs reposent sur des dénominateurs non chiffrés",
          "Dénominateur signalé « à préciser » ; arbitrage avec la DPS"],
         ["M8", "Seuils de qualité des services et de satisfaction",
          "Comparabilité des enquêtes dans le temps non assurée",
          "Seuils à fixer avec la DPS/PRONANUT (T2 2027)"],
         ["M9", "Circuit formel de validation des données",
          "Tech-4 n’indique que le rôle du responsable S&E/HMIS",
          "Circuit à trois niveaux proposé et signalé comme recommandation"],
         ["M10", "Calendrier officiel des évaluations",
          "Tech-4 prévoit trois temps d’évaluation sans en fixer les dates",
          "Programmation proposée dans le plan (section 10), signalée "],
         ["M11", "Durée contractuelle effective du projet",
          "Tech-4 indique 18 mois et une échéance au 31 décembre 2023",
          "Décalage signalé ; période 2027–2028 retenue conformément au cadrage"],
         ["M12", "Cadre logique complet",
          "Seules deux lignes du cadre logique sont renseignées",
          "Indicateurs reconstitués à partir du programme de travail ; signalé"]],
        size=7.2,
        caption="Tableau 7 — Informations manquantes et traitement retenu",
        note="Aucune de ces informations n’a été inventée. La mention « À préciser » est utilisée de manière "
             "systématique dans le plan et dans le cadre de performance.")

    # ------------------------------------------------------------------
    # 5. INCOHÉRENCES
    # ------------------------------------------------------------------
    d.h1("5", "Incohérences et anomalies relevées dans le document source")

    d.p("Le contrôle a relevé neuf anomalies dans Tech-4. Elles sont documentées ci-après avec leur localisation, "
        "le traitement retenu dans les livrables et leur incidence. Aucune n’a été corrigée silencieusement : "
        "chacune est signalée au lecteur.")

    d.table(
        ["N°", "Anomalie", "Localisation", "Traitement retenu dans les livrables", "Gravité"],
        [0.05, 0.27, 0.16, 0.38, 0.14],
        [["I1", "Horizon temporel incompatible avec la période demandée : Tech-4 décrit une mise en œuvre de "
                "18 mois et fixe l’échéance au « 31 décembre 2023 »",
          "Page de garde et §1.3",
          "Période 2027–2028 retenue ; décalage signalé comme point de vigilance (risque R12 du plan, "
          "annexe E) ; libellés des objectifs inchangés", "Élevée"],
         ["I2", "Libellé du résultat intermédiaire 2.1 corrompu dans le programme de travail "
                "(chaîne de caractères illisible)",
          "Section B.1, tableau des activités",
          "Libellé reconstitué à partir du contexte (« comités locaux de lutte contre les VBG/EAS/HS mis en "
          "place et actifs dans les 10 ZS ») et signalé comme reconstitution", "Moyenne"],
         ["I3", "Doublons de codes d’activité (1.3.2, 4.1.13, 4.1.14) affectés à des activités différentes",
          "Section B.1",
          "Les activités sont citées par leur libellé et non par leur code ; le doublon est mentionné dans "
          "l’annexe A du plan", "Faible"],
         ["I4", "Postes non pourvus désignés « TBD » dans l’organigramme",
          "Organigramme (image 33)",
          "Les postes sont désignés par leur fonction, jamais par une personne ; seules les personnes nommées "
          "dans Tech-4 sont citées", "Faible"],
         ["I5", "Cadre logique incomplet : seules deux lignes renseignées, les niveaux résultats et activités "
                "sont vides",
          "Cadre logique (images 27 à 32)",
          "Indicateurs reconstitués à partir du programme de travail ; absence signalée en section 3.3 du "
          "présent rapport et en section 5 du plan", "Élevée"],
         ["I6", "Absence de budget et de plan de financement",
          "Document entier",
          "Aucun montant ajouté ; seules les unités de subvention et de prime citées sont reprises ; "
          "information signalée comme manquante", "Élevée"],
         ["I7", "Effectif de prestataires à former libellé « 8 46 personnes », lecture ambiguë",
          "Section B.1",
          "Lecture retenue : 846 personnes, soit deux prestataires par formation sanitaire (2 × 423) ; "
          "la mention est signalée comme ambiguë", "Moyenne"],
         ["I8", "Double cible pour les relais communautaires : 8 314 RECO à couvrir et 4 956 RECO à doter "
                "de téléphones",
          "Section B.1 et §RI 3.2",
          "Les deux grandeurs sont conservées et distinguées dans les fiches techniques ; aucune n’est "
          "présentée comme la cible de l’autre", "Moyenne"],
         ["I9", "Divergences entre le tableau des personnels et l’organigramme (intitulés et rattachements)",
          "§B.1 et organigramme (image 33)",
          "Les deux sources sont citées ; les responsabilités sont rattachées à la fonction et non à la "
          "personne ; divergence signalée", "Faible"]],
        size=7.0, landscape=True,
        caption="Tableau 8 — Incohérences relevées dans Tech-4 et traitement appliqué",
        note="Aucune anomalie n’a été corrigée sans mention. Les anomalies de gravité élevée (I1, I5, I6) "
             "conditionnent la portée du cadre de performance et sont rappelées dans les livrables 02 et 04.")

    d.h2("5.1", "Anomalies de forme relevées dans le document source")
    d.bullets([
        "Numérotation des tableaux et des figures non continue ; renvois internes au « Figure xxx » sans "
        "numéro, y compris pour la théorie du changement (section 1.5).",
        "Fautes de frappe et mots collés dans plusieurs paragraphes du programme de travail, sans incidence sur "
        "le sens des activités.",
        "Tableaux du programme de travail non homogènes dans leurs colonnes (certaines lignes ne comportent pas "
        "de responsable ni de livrable).",
        "Absence de sommaire paginé et de pagination cohérente dans le formulaire transmis.",
    ])

    # ------------------------------------------------------------------
    # 6. RECOMMANDATIONS
    # ------------------------------------------------------------------
    d.h1("6", "Recommandations méthodologiques")

    d.p("Les recommandations ci-après sont des <b>propositions</b>. Elles ne sont pas présentées comme des "
        "engagements du projet et doivent être validées par le consortium, la Division provinciale de la santé "
        "du Kwilu, le PRONANUT et l’Unité de gestion du programme. Elles sont reprises, avec la même formulation, "
        "dans les livrables 01, 02 et 04.")

    d.table(
        ["N°", "Recommandation", "Justification", "Instance de validation", "Échéance"],
        [0.05, 0.33, 0.29, 0.20, 0.13],
        [["R1", "Fixer les cibles 2027 et 2028 lors d’un atelier de validation formel",
          "Tech-4 ne comporte aucune cible annuelle : sans arbitrage, le cadre de performance reste inopérant",
          "Consortium, DPS, UG-PDSS", "T1 2027"],
         ["R2", "Établir les valeurs de référence par une évaluation de base conduite dès janvier 2027",
          "Tech-4 prévoit une évaluation de base « immédiatement au démarrage » mais n’en fixe pas la date",
          "Consortium, DPS", "T1 2027"],
         ["R3", "Formaliser un circuit de validation des données à trois niveaux (structure, zone, province)",
          "Tech-4 ne définit que le rôle du responsable S&E/HMIS",
          "Comité de pilotage", "T1 2027"],
         ["R4", "Adopter une matrice RACI du suivi-évaluation",
          "Tech-4 annonce cette matrice sans la produire", "Comité de pilotage", "T1 2027"],
         ["R5", "Standardiser les désagrégations minimales (sexe, âge, zone, aire, milieu, type de structure)",
          "Tech-4 n’impose la désagrégation que pour les cas de VBG",
          "DPS/PRONANUT", "T1 2027"],
         ["R6", "Compléter la triade de Tech-4 par quatre dimensions de qualité (validité, fiabilité, précision, "
                "traçabilité)", "Tech-4 retient la complétude, la promptitude et la cohérence",
          "DPS/PRONANUT", "T1 2027"],
         ["R7", "Calculer les taux d’atteinte selon une règle explicite distinguant les indicateurs à sens "
                "croissant et décroissant",
          "Certains indicateurs sont des prévalences dont la baisse est l’objectif",
          "DPS/PRONANUT", "T1 2027"],
         ["R8", "Fixer un seuil de fonctionnalité des CAC, CODESA et UCODESA",
          "Le cadre logique évoque un seuil de 80 % sans en définir le contenu",
          "Cellule d’achat stratégique", "T1 2027"],
         ["R9", "Programmer les audits de qualité des données et le Third Party Monitoring",
          "Tech-4 mentionne leur principe sans en fixer le calendrier",
          "Comité de pilotage", "T1 2027"],
         ["R10", "Utiliser un référentiel unique de codification des activités dans tous les rapports",
          "Les codes du programme de travail comportent des doublons",
          "Responsable S&E/HMIS", "T1 2027"],
         ["R11", "Formaliser une procédure écrite de révision des cibles après l’évaluation à mi-parcours",
          "Tech-4 prévoit des revues sans prévoir l’actualisation des cibles",
          "Comité de pilotage", "T4 2027"],
         ["R12", "Documenter les garanties de confidentialité pour les données VBG et les plaintes",
          "Tech-4 affirme la confidentialité sans en préciser les règles",
          "DPS et sous-cluster VBG", "T1 2027"]],
        size=6.9, landscape=True,
        caption="Tableau 9 — Recommandations méthodologiques soumises à validation",
        note="Ces recommandations sont identifiables dans les livrables par la mention « Recommandation à "
             "valider » ou par la marque « R » dans les calendriers.")

    # ------------------------------------------------------------------
    # 7. CONTRÔLES EFFECTUÉS
    # ------------------------------------------------------------------
    d.h1("7", "Contrôles effectués")

    d.h2("7.1", "Contrôles de contenu")
    d.table(
        ["N°", "Contrôle", "Critère d’acceptation", "Résultat"],
        [0.05, 0.30, 0.45, 0.20],
        [["C1", "Tous les objectifs de Tech-4 figurent dans les livrables",
          "Objectif général, OS1 à OS4 et RI 4.5 présents et libellés à l’identique", "Conforme"],
         ["C2", "Aucun indicateur inventé",
          "Chaque indicateur est rattaché à un passage de Tech-4 ou signalé comme dérivé", "Conforme"],
         ["C3", "Aucune cible inventée",
          "Aucune cible annuelle renseignée ; les volumes de Tech-4 figurent en « cible globale »", "Conforme"],
         ["C4", "Aucune valeur de référence inventée",
          "Chaque valeur de référence est citée avec sa source ou remplacée par « À préciser »", "Conforme"],
         ["C5", "Aucun montant ni budget inventé",
          "Seules les unités citées par Tech-4 figurent ; aucun total calculé", "Conforme"],
         ["C6", "Aucun mécanisme institutionnel inventé",
          "Toute responsabilité est rattachée à un poste ou une institution citée ; le reste est proposé", "Conforme"],
         ["C7", "Informations manquantes signalées",
          "Toute lacune porte la mention « À préciser » ou « Non renseigné dans le document source »", "Conforme"],
         ["C8", "Recommandations distinguées des engagements",
          "Chaque proposition est étiquetée « Recommandation à valider » ou marquée « R »", "Conforme"],
         ["C9", "Les deux années sont couvertes",
          "2027 et 2028 figurent dans les tableaux, les calendriers et les colonnes de cibles", "Conforme"],
         ["C10", "Aucun objectif de Tech-4 supprimé",
          "Les quatre objectifs spécifiques et les quatorze résultats intermédiaires figurent au registre", "Conforme"]],
        size=7.4,
        caption="Tableau 10 — Contrôles de contenu")

    d.h2("7.2", "Contrôles techniques")
    d.table(
        ["N°", "Contrôle", "Critère d’acceptation", "Résultat"],
        [0.05, 0.30, 0.45, 0.20],
        [["T1", "Ouverture des fichiers Word", "Les deux fichiers .docx s’ouvrent sans erreur ni réparation",
          "Conforme"],
         ["T2", "Intégrité des fichiers PDF", "Nombre de pages cohérent, aucune page vide, texte extractible",
          "Conforme"],
         ["T3", "Absence de texte tronqué", "Aucune cellule, aucun titre, aucune légende coupée sur toutes les pages",
          "Conforme"],
         ["T4", "Absence de tableau débordant", "Aucun tableau ne dépasse la largeur utile de la page",
          "Conforme"],
         ["T5", "Rendu des graphiques", "Les sept figures et les deux calendriers sont lisibles et non rognés",
          "Conforme"],
         ["T6", "Pagination", "Numérotation continue et exacte ; « Page n / N » correct sur toutes les pages",
          "Conforme"],
         ["T7", "Sommaire", "Sommaire automatique, numéros de page exacts, deux niveaux de titres",
          "Conforme"],
         ["T8", "Signets de navigation", "Un signet par titre de niveau 1 et 2, arborescence conforme",
          "Conforme"],
         ["T9", "Concordance Word / PDF", "Même nombre de pages, mêmes sauts de page, même contenu",
          "Conforme"],
         ["T10", "Filtres et volets figés du classeur", "En-têtes filtrés, volets figés, largeurs ajustées",
          "Conforme"],
         ["T11", "Polices incorporées", "Aucune substitution de police dans les fichiers PDF", "Conforme"],
         ["T12", "Orientation des pages", "Pages paysage limitées aux tableaux matriciels, en-têtes conformes",
          "Conforme"]],
        size=7.4,
        caption="Tableau 11 — Contrôles techniques")

    d.h2("7.3", "Contrôles de cohérence")
    d.table(
        ["N°", "Contrôle", "Méthode", "Résultat"],
        [0.05, 0.28, 0.47, 0.20],
        [["X1", "Indicateurs identiques dans tous les livrables",
          "Comparaison automatisée des 41 codes, intitulés et unités entre le plan, le cadre PDF et le classeur",
          "Conforme"],
         ["X2", "Définitions et formules identiques",
          "Comparaison champ par champ des fiches techniques et des onglets du classeur", "Conforme"],
         ["X3", "Références et cibles identiques",
          "Comparaison des 41 valeurs de référence et des 82 cibles annuelles", "Conforme"],
         ["X4", "Numérotation des tableaux et figures",
          "Contrôle de la séquence et de l’unicité des numéros dans chaque document", "Conforme"],
         ["X5", "Renvois internes valides",
          "Vérification de chaque renvoi « section n » et « tableau n » vers une cible existante", "Conforme"],
         ["X6", "Positionnement correct des cibles",
          "Aucune cible 2028 dans une colonne 2027 ; aucune cible globale reportée en cible annuelle", "Conforme"],
         ["X7", "Formules vérifiées",
          "Relecture de chaque formule : numérateur et dénominateur cohérents avec l’unité annoncée", "Conforme"],
         ["X8", "Cohérence des chiffres cités",
          "Les volumes repris dans le plan, le cadre et le rapport sont issus de la même source", "Conforme"]],
        size=7.4,
        caption="Tableau 12 — Contrôles de cohérence",
        note="Ces contrôles portent sur l’ensemble des livrables produits dans le cadre de la mission.")

    d.h2("7.4", "Points de vigilance pour la prochaine version")
    d.bullets([
        "<b>Version 2.0 après l’atelier de validation :</b> renseigner les 41 valeurs de référence et les "
        "82 cibles annuelles. Les livrables sont conçus pour absorber cette mise à jour sans refonte.",
        "<b>Fiches techniques :</b> compléter la rubrique « limites » dès que les protocoles d’enquête seront "
        "arrêtés.",
        "<b>Classeur Excel :</b> activer le suivi annuel dès la première collecte et verrouiller les colonnes "
        "de référence et de cible.",
        "<b>Document source :</b> demander au consortium la version complète du cadre logique et le budget, "
        "qui manquent au formulaire transmis.",
        "<b>Horizon temporel :</b> confirmer par écrit la période contractuelle effective (2027–2028) et "
        "l’articulation avec l’échéance mentionnée dans Tech-4.",
    ])

    # ------------------------------------------------------------------
    # 8. ATTESTATION
    # ------------------------------------------------------------------
    d.h1("8", "Attestation et visa")

    d.p("Le présent rapport atteste que les livrables 01 à 04 ont été contrôlés selon la méthode décrite à la "
        "section 1 et que les résultats consignés aux tableaux 10 à 12 sont exacts. Les informations absentes "
        "du document source ont été signalées sans être complétées par des valeurs estimées. Les propositions "
        "méthodologiques sont identifiables comme telles dans chaque livrable.")

    d.table(
        ["Rôle", "Nom et fonction", "Date", "Visa"],
        [0.26, 0.34, 0.16, 0.24],
        [["Élaboration", "Équipe de production du lot documentaire", "—", ""],
         ["Contrôle interne", "Responsable suivi-évaluation / HMIS", "", ""],
         ["Validation technique", "Division provinciale de la santé du Kwilu — PRONANUT", "", ""],
         ["Approbation", "Directeur de projet — Consortium SANRU-ICHESS-FONLIV-FDSS", "", ""]],
        size=7.8,
        caption="Tableau 13 — Circuit de validation du lot documentaire",
        note="Le circuit proposé reprend les responsabilités décrites dans Tech-4 ; il est soumis à validation "
             "lors de la première réunion du comité de pilotage.")

    return d
