# -*- coding: utf-8 -*-
"""Sections 11 à 14 du plan de suivi-évaluation."""
import design as D
import data as T

NA = T.NA

M12 = [1] * 12
Q = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]          # fin de trimestre
S = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]          # semestres
S1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]         # semestres (décalés)

ROWS_2027 = [
    ("Collecte mensuelle de routine (DHIS2, registres FOSA et CAC)", "collecte", M12, "T4"),
    ("Dénombrement et suivi individualisé (registre électronique)", "collecte", M12, "T4"),
    ("Évaluation de base : SMART, CAP, état des lieux FOSA/CAC", "evaluation",
     [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], "T4"),
    ("Atelier de validation des références et des cibles 2027", "analyse",
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], "R"),
    ("Audit initial de la qualité des données", "qualite", [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], "R"),
    ("Supervisions formatives et contrôles de premier niveau", "qualite", M12, "T4"),
    ("Monitorage amélioré pour l’action (MAA) et audits", "qualite", Q, "T4"),
    ("Third Party Monitoring ponctuel des données communautaires", "qualite",
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], "R"),
    ("Analyse trimestrielle des données et des écarts", "analyse", Q, "R"),
    ("Rapports d’avancement trimestriels à l’UG-PDSS", "rapports", Q, "T4"),
    ("Bulletins trimestriels des données de nutrition (DPS)", "rapports", Q, "T4"),
    ("Rapport d’avancement annuel 2027", "rapports", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], "T4"),
    ("Enquêtes semestrielles de satisfaction des clients", "collecte", S, "T4"),
    ("Revues semestrielles de la nutrition (province)", "revues", S, "T4"),
    ("Comité de pilotage du consortium", "revues", Q, "T4"),
    ("Évaluation à mi-parcours", "evaluation", [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], "T4"),
    ("Révision des cibles 2028", "analyse", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], "R"),
    ("Recherche opérationnelle : protocole et collecte", "capital",
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], "T4"),
    ("Documentation des bonnes pratiques et leçons apprises", "capital",
     [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], "T4"),
]

ROWS_2028 = [
    ("Collecte mensuelle de routine (DHIS2, registres FOSA et CAC)", "collecte", M12, "T4"),
    ("Dénombrement et suivi individualisé (registre électronique)", "collecte", M12, "T4"),
    ("Supervisions formatives et contrôles de premier niveau", "qualite", M12, "T4"),
    ("Monitorage amélioré pour l’action (MAA) et audits", "qualite", Q, "T4"),
    ("Audit de la qualité des données et Third Party Monitoring", "qualite",
     [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], "R"),
    ("Analyse trimestrielle des données et des écarts", "analyse", Q, "R"),
    ("Rapports d’avancement trimestriels à l’UG-PDSS", "rapports", Q, "T4"),
    ("Bulletins trimestriels des données de nutrition (DPS)", "rapports", Q, "T4"),
    ("Enquêtes semestrielles de satisfaction des clients", "collecte", S, "T4"),
    ("Revues semestrielles de la nutrition (province)", "revues", S, "T4"),
    ("Comité de pilotage du consortium", "revues", Q, "T4"),
    ("Recherche opérationnelle : finalisation et publication", "capital",
     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], "T4"),
    ("Documentation des bonnes pratiques et leçons apprises", "capital",
     [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], "T4"),
    ("Évaluation finale : SMART, CAP, revue documentaire", "evaluation",
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], "T4"),
    ("Atelier de capitalisation et revue finale", "capital",
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], "R"),
    ("Rapport annuel 2028 et rapport final du projet", "rapports",
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], "T4"),
]


def build(d):
    # ==================================================================
    # K. PLANIFICATION
    # ==================================================================
    d.h1("10", "Planification des activités de suivi-évaluation 2027–2028")

    d.p("La programmation ci-après distingue sept familles d’activités : collecte des données, contrôle "
        "qualité, analyse, production des rapports, revues de performance, évaluations, et capitalisation et "
        "apprentissage. Chaque ligne porte une marque de source : <b>T4</b> lorsque la périodicité ou l’activité "
        "est directement issue de Tech-4, <b>R</b> lorsqu’il s’agit d’une proposition méthodologique soumise à "
        "validation.")

    d.h2("10.1", "Exercice 2027")
    d.figure("figures/gantt_2027.png", 1.0,
             caption="Figure 6 — Calendrier opérationnel du suivi-évaluation, exercice 2027",
             note="L’année 2027 concentre la mise en place du dispositif : évaluation de base, fixation des "
                  "valeurs de référence et des cibles, premier cycle complet de monitorage et évaluation à "
                  "mi-parcours. La colonne « Sourc. » indique l’origine de chaque échéance.")

    d.h2("10.2", "Exercice 2028")
    d.figure("figures/gantt_2028.png", 1.0,
             caption="Figure 7 — Calendrier opérationnel du suivi-évaluation, exercice 2028",
             note="L’année 2028 consolide le dispositif, conduit l’évaluation finale et organise la "
                  "capitalisation et la transmission des acquis.")

    d.h2("10.3", "Justification de la programmation")
    d.table(
        ["Activité programmée", "Justification", "Source"],
        [0.36, 0.48, 0.16],
        [["Évaluation de base au premier trimestre 2027",
          "Tech-4 prévoit une évaluation de base « immédiatement au démarrage du projet » ; l’état des lieux "
          "précède l’évaluation de base dans le document source", "Tech-4 §1.5 et §RI 4.5"],
         ["Collecte mensuelle de routine",
          "Tech-4 prévoit le rapportage mensuel des données au BCZS puis au DHIS2, et des réunions mensuelles "
          "de monitorage", "Tech-4 §RI 4.5"],
         ["MAA trimestriel",
          "Tech-4 indique que « des sessions de MAA auront lieu chaque trimestre au niveau de la communauté, "
          "des centres de santé et des zones de santé »", "Tech-4 §RI 4.5"],
         ["Revues semestrielles",
          "Tech-4 prévoit « une revue […] tous les 6 mois » sous la direction du Gouverneur", "Tech-4 §RI 4.5"],
         ["Enquêtes semestrielles de satisfaction",
          "Tech-4 prévoit des « enquêtes semestrielles de satisfaction des clients »", "Tech-4 §RI 1.3"],
         ["Rapports trimestriels et annuels",
          "Tech-4 prévoit la soumission de rapports d’avancement mensuels, trimestriels et annuels à l’UG-PDSS",
          "Tech-4 §RI 4.5"],
         ["Évaluations à mi-parcours et finale",
          "Tech-4 prévoit trois temps d’évaluation (début, mi-parcours, fin) sans en fixer le calendrier",
          "Tech-4 §RI 4.5"],
         ["Audits de qualité des données et TPM",
          "Tech-4 prévoit des audits lors des sessions de MAA et des TPM « de façon ponctuelle »",
          "Tech-4 §RI 4.5"],
         ["Recherche opérationnelle continue",
          "Tech-4 prévoit de mener des recherches opérationnelles « tout au long du processus de mise en œuvre »",
          "Tech-4 §RI 4.5"],
         ["Positionnement mensuel précis des audits et des évaluations",
          "Le mois exact n’est pas fixé par Tech-4 : la répartition proposée doit être validée",
          "<b>Recommandation</b>"]],
        size=7.6,
        caption="Tableau 21 — Traçabilité de la programmation",
        note="Cette matrice constitue la preuve de cohérence entre la programmation proposée et le document "
             "source : aucune échéance n’est présentée comme documentée lorsqu’elle ne l’est pas.")

    # ==================================================================
    # L. RISQUES
    # ==================================================================
    d.h1("11", "Gestion des risques du dispositif de suivi-évaluation")

    d.p("Deux catégories de risques sont distinguées : les <b>risques documentés</b>, identifiés par Tech-4 "
        "lui-même (qualité des données, sous-déclaration des VBG, absence de dénominateurs fiables), et les "
        "<b>risques méthodologiques</b> propres à la conduite du dispositif de suivi-évaluation, proposés par "
        "le présent plan.")

    d.table(
        ["N°", "Risque", "Nature", "Conséquence sur le dispositif", "Mesure d’atténuation proposée", "Resp."],
        [0.05, 0.21, 0.11, 0.22, 0.30, 0.11],
        [["R1", "Faible complétude et faible promptitude des données de routine",
          "Documenté — Tech-4 §RI 4.5 et PNDS 2019-2022",
          "Indicateurs non calculables ou calculés sur des données partielles",
          "Suivi hebdomadaire des structures silencieuses ; relance par les ECZS ; tableau de bord des retards ; "
          "audits trimestriels", "Resp. S&E"],
         ["R2", "Non-fiabilité des dénominateurs de population cible",
          "Documenté — Tech-4 §RI 4.5",
          "Impossibilité de calculer des taux de couverture fiables",
          "Actualisation mensuelle du dénombrement par les RECO ; validation par les ECZS ; recours aux données "
          "de dénombrement plutôt qu’aux projections", "Resp. S&E / ECZS"],
         ["R3", "Sous-déclaration des cas de VBG et incohérence entre sources",
          "Documenté — Tech-4 §OS2",
          "Sous-estimation systématique de la prise en charge",
          "Triangulation DHIS2 / sous-cluster VBG / PNSR ; analyse des écarts explicitée dans les rapports ; "
          "ligne verte et notification communautaire", "Sp. engagement communautaire"],
         ["R4", "Registres électroniques non opérationnels (réseau, équipement, appropriation)",
          "Documenté — Tech-4 prévoit un déploiement pilote sur 2 ZS",
          "Perte de la finesse du suivi individualisé",
          "Maintien du registre papier en parallèle ; déploiement progressif ; maintenance et forfaits internet "
          "prévus", "Resp. S&E / IT"],
         ["R5", "Retard ou absence de l’évaluation de base",
          "Méthodologique",
          "Absence de valeurs de référence : le cadre de performance reste incomplet",
          "Programmation dès janvier 2027 ; lancement en parallèle de l’état des lieux ; clause contractuelle "
          "de livraison", "Dir. projet"],
         ["R6", "Cibles non arbitrées par les parties prenantes",
          "Méthodologique",
          "Absence de référence pour juger de l’atteinte des résultats",
          "Atelier de validation au T1 2027 ; procédure écrite de révision ; traçabilité des décisions",
          "Dir. projet"],
         ["R7", "Rotation du personnel formé et des points focaux",
          "Documenté — Tech-4 prévoit un plaidoyer pour la stabilité des prestataires",
          "Perte de compétences et rupture de la série de données",
          "Plan de formation continue ; tutorat par les pairs ; clause de stabilité dans la convention avec la DPS",
          "Sp. Nutrition"],
         ["R8", "Multiplicité des outils et des circuits de données",
          "Méthodologique",
          "Risque de double comptage et de divergence entre DHIS2 et registres du projet",
          "Référentiel unique d’indicateurs ; règles de priorité entre sources ; réconciliation trimestrielle",
          "Resp. S&E"],
         ["R9", "Insécurité, intempéries et enclavement",
          "Documenté — Tech-4 §Objectif 1 et §RI 4.4",
          "Missions de supervision et collectes annulées ou retardées",
          "Planification souple ; collecte décentralisée par les ECZS ; recours au téléphone et aux tablettes",
          "Dir. projet"],
         ["R10", "Sur-sollicitation des acteurs de terrain (RECO, ECZS)",
          "Méthodologique",
          "Baisse de la qualité de la collecte et démobilisation",
          "Regroupement des outils ; limitation du nombre d’indicateurs ; incitation basée sur la performance prévue",
          "Sp. Nutrition"],
         ["R11", "Non-utilisation des données pour la décision",
          "Méthodologique",
          "Le dispositif produit des rapports sans effet sur la mise en œuvre",
          "Ordre du jour décisionnel fixé pour chaque instance ; suivi des décisions ; revue de la mise en œuvre "
          "des recommandations", "Dir. projet"],
         ["R12", "Décalage entre la durée prévue par Tech-4 (18 mois, échéance 2023) et la période 2027–2028",
          "Méthodologique — lié au cadrage de la mission",
          "Références et cibles historiques non transposables telles quelles",
          "Actualisation de toutes les données de référence par l’évaluation de base 2027 ; révision explicite "
          "des échéances", "Dir. projet / DPS"]],
        size=6.9, landscape=True,
        caption="Tableau 22 — Registre des risques du dispositif de suivi-évaluation",
        note="Les risques R1, R2, R3, R4, R7 et R9 sont explicitement documentés dans Tech-4 ; les autres sont "
             "des risques méthodologiques proposés par le présent plan.")

    d.h2("11.1", "Dispositif de suivi des risques")
    d.p("Le registre des risques est revu à chaque comité de pilotage trimestriel. Chaque risque fait l’objet "
        "d’un indicateur d’alerte, d’un responsable et d’une échéance de traitement. Tech-4 prévoit par ailleurs "
        "que le consortium <i>« identifiera, évaluera et documentera les risques »</i> au cours de l’évaluation "
        "de base et pendant la mise en œuvre, et qu’il mettra à jour ses plans de contingence.")

    d.h2("11.2", "Instances de revue des risques et calendrier de traitement")
    d.table(
        ["Instance", "Objet de la revue des risques", "Périodicité", "Livrable de la revue"],
        [0.24, 0.40, 0.16, 0.20],
        [["Réunion mensuelle de monitorage (CAC, CODESA)",
          "Risques opérationnels locaux : structures silencieuses, ruptures d’intrants, absentéisme des "
          "prestataires", "Mensuelle", "Plan de redressement communautaire"],
         ["Monitorage amélioré pour l’action (MAA)",
          "Goulots d’étranglement identifiés par les données ; causes et mesures correctrices",
          "Trimestrielle", "Matrice des goulots et des actions"],
         ["Comité de pilotage du consortium",
          "Revue du registre complet ; risques R1 à R12 ; décisions d’atténuation et responsables",
          "Trimestrielle", "Compte rendu et registre actualisé"],
         ["Revue semestrielle de la nutrition",
          "Risques systémiques : qualité des données, disponibilité des intrants, couverture des zones",
          "Semestrielle", "Recommandations au Gouverneur et au Ministre provincial"],
         ["Évaluation à mi-parcours et évaluation finale",
          "Réévaluation des risques, de leur gravité et de l’efficacité des mesures prises",
          "Ponctuelle", "Rapport d’évaluation"]],
        size=7.6,
        caption="Tableau 22 bis — Instances de revue des risques",
        note="Les instances et leurs périodicités sont celles que Tech-4 prévoit ; le rattachement explicite du "
             "registre des risques à chacune d’elles est une <b>proposition</b> de mise en œuvre.")

    d.h2("11.3", "Conséquences opérationnelles des risques majeurs")
    d.p("Trois risques conditionnent directement la fiabilité du cadre de performance et appellent une décision "
        "avant la première revue :")
    d.bullets([
        "<b>R2 — dénominateurs incertains.</b> Sans dénombrement validé, aucun taux de couverture ne peut être "
        "interprété. La décision attendue porte sur la méthode de dénombrement et sur la date de validation des "
        "chiffres par les ECZS.",
        "<b>R5 et R6 — absence de référence et de cibles.</b> Le cadre de performance reste inopérant tant que "
        "les valeurs de référence et les cibles ne sont pas arrêtées. La décision attendue porte sur la date de "
        "lancement de l’évaluation de base et sur la tenue de l’atelier de validation des cibles.",
        "<b>R12 — décalage temporel.</b> Les données de contexte de Tech-4 datent de 2017-2022 et l’échéance "
        "initiale était fixée à 2023. La décision attendue porte sur la confirmation écrite de la période "
        "contractuelle et sur l’actualisation de toutes les références.",
    ])
    d.p("Ces décisions sont inscrites à l’ordre du jour du premier comité de pilotage de 2027.", size=9.6)

    # ==================================================================
    # M. UTILISATION DES RÉSULTATS
    # ==================================================================
    d.h1("12", "Utilisation des résultats")

    d.p("Le dispositif n’a de valeur que par l’usage qui est fait des données. Tech-4 affirme la nécessité "
        "d’<i>« insister et introduire la culture de l’utilisation des données dans la gestion des programmes et "
        "la prise de décisions »</i>. Le tableau ci-après précise, pour chaque usage attendu, le mécanisme, "
        "l’instance et la périodicité.")

    d.table(
        ["Usage", "Mécanisme", "Instance", "Périodicité"],
        [0.19, 0.41, 0.24, 0.16],
        [["Suivre les progrès", "Comparaison systématique référence / cible / réalisation dans les rapports "
          "périodiques et le tableau de bord", "UGP, CPP", "Mensuelle et trimestrielle"],
         ["Identifier les écarts", "Analyse des écarts par zone de santé, par aire de santé et par indicateur ; "
          "classement des structures selon la performance", "ECZS, DPS", "Trimestrielle"],
         ["Améliorer les interventions", "Plans de redressement issus du MAA et du BCP ; ajustement des "
          "stratégies de mise en œuvre", "CAC, CODESA, ECZS", "Trimestrielle"],
         ["Orienter les décisions", "Décisions consignées au compte rendu de chaque instance, avec responsable "
          "et échéance", "CPP, DPS", "Trimestrielle et semestrielle"],
         ["Documenter les résultats", "Rapports d’évaluation, notes de capitalisation, publications de la "
          "recherche opérationnelle", "Consortium, DPS, ESP", "Ponctuelle"],
         ["Rendre compte aux parties prenantes", "Rapports à l’UG-PDSS ; bulletins trimestriels de la DPS ; "
          "restitutions communautaires", "UG-PDSS, communautés", "Mensuelle à annuelle"]],
        size=7.6,
        caption="Tableau 23 — Usages des résultats et instances de décision",
        note="Les instances et les périodicités reprennent celles que Tech-4 décrit ; le mécanisme "
             "« référence / cible / réalisation » et le suivi des décisions sont des propositions.")

    d.h2("12.1", "Boucle d’apprentissage")
    d.p("La boucle d’apprentissage s’organise en quatre temps : (i) la donnée est produite au niveau de la "
        "structure ; (ii) elle est analysée lors de la réunion de monitorage et du MAA ; (iii) elle est "
        "consolidée et confrontée aux autres sources lors de la revue semestrielle ; (iv) elle est transformée "
        "en décision au comité de pilotage, puis en ajustement du programme de travail. Chaque décision est "
        "tracée et son exécution est vérifiée à l’instance suivante.")

    d.h2("12.2", "Redevabilité envers les communautés")
    d.p("Tech-4 fait de la redevabilité un principe directeur : <i>« les prestataires des services devront ainsi "
        "être responsables envers les communautés qu’ils desservent »</i>. Le dispositif prévoit à cet effet "
        "trois instruments : le Bulletin de performance communautaire (BCP), le contrôle communautaire exercé "
        "par la CAC et le mécanisme de gestion des plaintes (registre de plaintes, ligne verte, comité villageois).")

    # ==================================================================
    # N. ANNEXES
    # ==================================================================
    d.h1("13", "Annexes")

    d.h2("13.1", "Annexe A — Référentiel des activités de suivi-évaluation issues de Tech-4")
    d.p("Le référentiel ci-dessous reprend les activités de suivi-évaluation que Tech-4 identifie dans son "
        "résultat intermédiaire 4.5 et dans son programme de travail (section B.1), avec le livrable et le "
        "responsable associés par le document source.")
    d.table(
        ["Code", "Activité (Tech-4)", "Livrable", "Responsable (Tech-4)"],
        [0.09, 0.48, 0.22, 0.21],
        [["5.1", "Évaluation de base de la mise en œuvre du projet", "Rapport de l’évaluation",
          "Responsable S&E / Directeur de projet"],
         ["5.2", "Monitorage amélioré pour action (MAA) avec des registres électroniques au niveau communautaire",
          "Rapport d’activité", "Responsable S&E"],
         ["5.3", "Revues semestrielles de la nutrition", "Rapport de revue", "Responsable S&E"],
         ["5.4", "Évaluations de la qualité de prise en charge de la malnutrition dans les établissements de santé",
          "Rapport d’activité", "Responsable S&E / Spécialiste en Nutrition"],
         ["5.5", "Suivi des activités communautaires dans CAC, CODESA et UCODESA", "Rapport d’activité",
          "Responsable S&E / Spécialiste en Nutrition"],
         ["5.6", "Contrôle communautaire", "Rapport des plaintes et alertes communautaires sur le projet",
          "Responsable S&E / Spécialiste en Nutrition"],
         ["5.7", "Recherche opérationnelle", "Protocole de recherche, rapport", "Responsable S&E"],
         ["5.8", "Documentation des bonnes pratiques, des innovations et des leçons apprises",
          "Rapport de la mise en œuvre du projet", "Responsable S&E"],
         ["5.9", "Évaluation finale de la mise en œuvre du projet", "Rapport de l’évaluation finale",
          "Responsable S&E / Directeur de projet"],
         ["3.1.1", "Évaluation de base de la mise en place et de la fonctionnalité des CAC et CODESA",
          "Rapport de l’évaluation de base", "Responsable S&E/HMIS"],
         ["4.4.1", "État des lieux au niveau des aires de santé (FOSA, SSC, ressources humaines, équipements, "
          "intrants, infrastructures, indicateurs de base, analyse du genre)", "Rapport des états des lieux",
          "Spécialiste en Nutrition, Resp. S&E/HMIS"],
         ["4.2.9", "Améliorer la qualité et l’utilisation des données nutritionnelles",
          "Rapport d’activité", "Spécialiste en Nutrition / Directeur"],
         ["4.3.x", "Appui aux réunions d’analyse des données (ECZS, COGE, CA, cluster, BCZS, PRONANUT, revues)",
          "Compte rendu des réunions d’analyse", "Responsable S&E"]],
        size=7.5,
        caption="Tableau 24 — Annexe A : activités de suivi-évaluation identifiées par Tech-4",
        note="Les libellés et les responsables sont ceux du document source. Le code « 4.3.x » regroupe les "
             "activités 4.3.1 à 4.3.6, dont le libellé est identique (« appui technique et financier aux "
             "réunions ») et dont seul l’objet diffère.")

    d.h2("13.2", "Annexe B — Modèle de fiche de suivi d’indicateur")
    d.p("Le modèle ci-dessous est à renseigner pour chaque indicateur et à archiver avec le registre. "
        "Il constitue la pièce justificative de la traçabilité.")
    d.table(
        ["Rubrique", "Contenu attendu"],
        [0.30, 0.70],
        [["Code et intitulé", "Identifiant unique repris du registre (section 5) et libellé complet"],
         ["Objectif et résultat de rattachement", "Objectif global, objectif spécifique et résultat intermédiaire de Tech-4"],
         ["Définition et formule", "Définition opérationnelle, numérateur, dénominateur, unité, règles d’arrondi"],
         ["Niveau de résultat", "Impact, effet, extrant ou réalisation"],
         ["Valeur de référence", "Valeur, date, source, méthode d’obtention, responsable de la validation"],
         ["Cible 2027 / Cible 2028", "Valeur, décision de fixation (référence de l’atelier), responsable"],
         ["Source de vérification", "Document ou base où la valeur est enregistrée, localisation"],
         ["Méthode et fréquence de collecte", "Instrument, échantillon, période de référence, périodicité"],
         ["Responsables", "Collecte, contrôle de premier niveau, validation, diffusion"],
         ["Désagrégations", "Sexe, âge, zone de santé, aire de santé, milieu, type de structure"],
         ["Limites et biais connus", "Sous-déclaration, dénominateur incertain, comparabilité dans le temps"],
         ["Historique des modifications", "Date, nature, justification, validation"]],
        caption="Tableau 25 — Annexe B : structure normalisée d’une fiche de suivi d’indicateur")

    d.h2("13.3", "Annexe C — Canevas du rapport d’avancement périodique")
    d.numbered([
        "Page de garde et fiche d’identification (période, zones couvertes, version, validation).",
        "Résumé d’une page : faits saillants, alertes, décisions demandées.",
        "Rappel des objectifs et des résultats attendus concernés par la période.",
        "Tableau de bord des indicateurs : référence, cible, réalisation, écart, commentaire.",
        "Avancement du programme de travail : activités réalisées, livrables, taux d’exécution.",
        "Analyse des goulots d’étranglement et des causes (cadre du MAA).",
        "Qualité des données : complétude, promptitude, cohérence, mesures correctrices.",
        "Risques et mesures d’atténuation (mise à jour du registre).",
        "Décisions prises, responsables et échéances ; suivi des décisions antérieures.",
        "Annexes : preuves documentaires, comptes rendus, listes de présence, photographies.",
    ])

    d.h2("13.4", "Annexe D — Matrice de traçabilité documentaire")
    d.p("La matrice ci-dessous relie chaque section du présent plan au passage correspondant de Tech-4, "
        "permettant une vérification indépendante de la fidélité au document source.")
    d.table(
        ["Section du plan", "Contenu", "Source dans Tech-4"],
        [0.27, 0.33, 0.40],
        [["1. Présentation générale", "Identification, contexte, objectifs, composantes, zones",
          "Page de garde ; §1.1 à §1.3 ; §B.1 ; §RI 4.4 ; tableaux des ZS"],
         ["2. Théorie du changement", "Modèle EDO, chaîne des résultats",
          "§1.5 (théorie du changement) ; cadre logique"],
         ["3. Objectifs du dispositif", "Objectifs, besoins d’information, utilisation",
          "§RI 4.5 ; §RI 4.2"],
         ["4. Approche méthodologique", "Suivi, évaluations, triangulation, qualité",
          "§RI 1.3 ; §RI 4.2 ; §RI 4.5"],
         ["5. Registre des indicateurs", "41 indicateurs, définitions, formules, cibles",
          "Cadre logique ; §B.1 « Indicateurs » ; §RI 4.2 ; §OS2 ; §OS3"],
         ["6. Organisation institutionnelle", "Acteurs, RACI, dispositif",
          "§B.2.1 (structure de mise en œuvre et personnels) ; §RI 4.5"],
         ["7. Outils", "Registres, DHIS2, BCP, questionnaires", "§RI 4.2 ; §RI 4.5 ; tableaux de dotation"],
         ["8. Assurance qualité", "Dimensions, contrôles à trois niveaux", "§RI 4.2 ; §RI 4.5"],
         ["9. Reporting", "Matrice des rapports", "§RI 4.4 ; §RI 4.5"],
         ["10. Planification", "Calendriers 2027 et 2028", "§RI 4.5 ; §B.1 (programme de travail)"],
         ["11. Risques", "Registre des risques", "§1.4.7 ; §RI 4.5"],
         ["12. Utilisation des résultats", "Usages, boucle d’apprentissage, redevabilité",
          "§1.4.6 ; §RI 4.5"]],
        size=7.6,
        caption="Tableau 26 — Annexe D : traçabilité entre le plan et le document source")

    d.h2("13.5", "Annexe E — Informations manquantes à obtenir")
    d.table(
        ["Information manquante", "Impact sur le suivi-évaluation", "Modalité d’obtention proposée"],
        [0.30, 0.34, 0.36],
        [["Valeurs de référence de tous les indicateurs", "Impossible de mesurer un progrès",
          "Évaluation de base — T1 2027"],
         ["Cibles annuelles 2027 et 2028", "Impossible de juger de l’atteinte des résultats",
          "Atelier de validation des cibles — T1 2027"],
         ["Ventilation annuelle des volumes de livrables", "Suivi d’exécution imprécis",
          "Reprogrammation détaillée avec l’UG-PDSS"],
         ["Budget du projet et clé de répartition des financements", "Suivi financier non couvert par le présent plan",
          "Documents budgétaires du consortium"],
         ["Liste des indicateurs de performance conditionnant les primes communautaires",
          "Financement basé sur la performance non mesurable", "Cellule d’achat stratégique du consortium"],
         ["Nombre exact de comités territoriaux multisectoriels à installer", "Dénominateur de l’indicateur EFF-03",
          "Arbitrage avec la DPS"],
         ["Seuils de référence pour la qualité des services et la satisfaction",
          "Comparabilité des enquêtes dans le temps", "DPS/PRONANUT"],
         ["Calendrier officiel des évaluations", "Planification des ressources", "UG-PDSS et consortium"],
         ["Durée contractuelle effective du projet", "Cadrage temporel des cibles", "Convention de subvention"]],
        caption="Tableau 27 — Annexe E : informations indispensables non disponibles dans Tech-4",
        note="Aucune de ces informations n’a été inventée : elles sont signalées comme manquantes et leur "
             "modalité d’obtention est proposée.")

    d.h2("13.6", "Annexe F — Sigles et abréviations")
    d.table(
        ["Sigle", "Signification", "Sigle", "Signification"],
        [0.11, 0.39, 0.11, 0.39],
        [["ANJE", "Alimentation du nourrisson et du jeune enfant", "MAA", "Monitorage amélioré pour l’action"],
         ["ATPE", "Aliment thérapeutique prêt à l’emploi", "MAM", "Malnutrition aiguë modérée"],
         ["BCP", "Bulletin de performance communautaire", "MAS", "Malnutrition aiguë sévère"],
         ["BCZS", "Bureau central de la zone de santé", "MILDA", "Moustiquaire imprégnée d’insecticide à longue durée d’action"],
         ["CAC", "Cellule d’animation communautaire", "MNPs", "Micronutriments en poudre"],
         ["CAP", "Connaissances, attitudes et pratiques", "NAC", "Nutrition à assise communautaire"],
         ["CODESA", "Comité de développement sanitaire", "ONG", "Organisation non gouvernementale"],
         ["CPN", "Consultation prénatale", "OS", "Objectif spécifique"],
         ["CPoN", "Consultation postnatale", "PEC", "Prise en charge"],
         ["CPSr", "Consultation préscolaire redynamisée", "PFE", "Pratiques familiales essentielles"],
         ["DHIS2", "District Health Information Software 2", "PMNS", "Projet multisectoriel de nutrition et de santé"],
         ["DPS", "Division provinciale de la santé", "PRONANUT", "Programme national de nutrition"],
         ["EAS/HS", "Exploitation et abus sexuels / harcèlement sexuel", "PTF", "Partenaire technique et financier"],
         ["ECZS", "Équipe-cadre de la zone de santé", "RECO", "Relais communautaire"],
         ["EHA", "Eau, hygiène et assainissement", "RI", "Résultat intermédiaire"],
         ["FARN", "Foyer d’apprentissage et de réhabilitation nutritionnelle", "S&E", "Suivi-évaluation"],
         ["FEFA", "Femme enceinte et femme allaitante", "SGBV", "Sexual and gender-based violence"],
         ["FOSA", "Formation sanitaire", "SMART", "Standardized Monitoring and Assessment of Relief and Transitions"],
         ["HMIS", "Health Management Information System", "SNSAP", "Système national de surveillance alimentaire et nutritionnelle"],
         ["I.O.V.", "Indicateur objectivement vérifiable", "SNIS", "Système national d’information sanitaire"],
         ["IPC", "Cadre intégré de classification de la sécurité alimentaire", "SSC", "Site de soins communautaires"],
         ["K4 / K5", "Poste clé n° 4 / n° 5 (gestionnaire financier / logistique)", "TPM", "Third Party Monitoring"],
         ["UCODESA", "Union des CODESA", "UG-PDSS", "Unité de gestion du Programme de développement du système de santé"],
         ["UNTA / UNTI", "Unité nutritionnelle thérapeutique ambulatoire / intensive", "VBG", "Violences basées sur le genre"],
         ["VAD", "Visite à domicile", "ZS", "Zone de santé"]],
        size=7.2,
        caption="Tableau 28 — Annexe F : sigles et abréviations")

    d.h2("13.7", "Annexe G — Documents de référence")
    d.bullets([
        "Tech-4 — Description de l’approche, de la méthodologie et du programme de travail, Consortium "
        "SANRU-ICHESS-FONLIV-FDSS, DP N° ZR-DRC-MSP-235334-CS-QCBS (document source unique).",
        "Cadre de performance 2027–2028 (livrable 03) — version Excel et version PDF de consultation (livrable 04).",
        "Rapport de contrôle qualité (livrable 05) — traçabilité, informations manquantes, contrôles effectués.",
        "Références citées par Tech-4 et mobilisées dans le présent plan : MICS-Palu 2017-2018 ; MICS 6 (2018) ; "
        "IPC 2021-2022 ; DHIS2 2021 ; rapport annuel PRONANUT Kwilu 2020 ; DPS Kwilu 2021 ; Plan stratégique "
        "national de santé communautaire 2019-2022 ; PNDS recadré 2019-2022.",
    ])

    return d
