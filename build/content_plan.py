# -*- coding: utf-8 -*-
"""Contenu du PLAN DE SUIVI-ÉVALUATION 2027–2028.

Toute affirmation factuelle est rattachée à Tech-4 ; les propositions
méthodologiques sont explicitement étiquetées « Recommandation à valider ».
"""
import design as D
from design import Doc
import data as T

NA = T.NA
NM = "Non renseigné dans le document source"

META = {
    "title": "Plan de suivi-évaluation 2027–2028 — PMNS-NAC Kwilu",
    "author": "Consortium SANRU – ICHESS – FONLIV – FDSS",
    "subject": "Plan de suivi-évaluation et cadre de performance 2027–2028",
    "header_left": "PMNS-NAC Kwilu — Plan de suivi-évaluation 2027–2028",
    "header_right": "Consortium SANRU – ICHESS – FONLIV – FDSS",
    "footer_left": "DP N° ZR-DRC-MSP-235334-CS-QCBS · Tech-4",
    "footer_center": "1ᵉʳ janvier 2027 – 31 décembre 2028",
    "cover_kicker": "Suivi-évaluation · Gestion axée sur les résultats",
    "cover_title": "PLAN DE SUIVI-ÉVALUATION",
    "cover_year": "2027 – 2028",
    "cover_img": "figures/cover_plan.png",
    "cover_org": ["CONSORTIUM SANRU – ICHESS – FONLIV – FDSS",
                  "Chef de file : SANRU"],
    "cover_sub": ["Projet Multisectoriel de Nutrition et de Santé — Volet Nutrition",
                  "à Assise Communautaire (PMNS-NAC), province du Kwilu, RDC"],
    "cover_projet": ["PMNS-NAC Kwilu",
                     "10 zones de santé · 250 aires de santé · 3 188 villages"],
    "cover_source": ["Document source : Tech-4 — Description de l’approche, de la méthodologie",
                     "et du programme de travail",
                     "Demande de Propositions N° ZR-DRC-MSP-235334-CS-QCBS"],
    "cover_periode": "Période de mise en œuvre : 1ᵉʳ janvier 2027 – 31 décembre 2028",
    "cover_version": "Version 1.0 — document de travail soumis à validation",
    "cover_footer": ["Élaboré exclusivement à partir du document Tech-4 du consortium. Aucune donnée, cible ou valeur de référence",
                     "n’a été ajoutée : les informations absentes de la source sont signalées « À préciser »."],
}


def build():
    d = Doc(META)

    # ==================================================================
    # B. RÉSUMÉ EXÉCUTIF
    # ==================================================================
    d.h1("", "Résumé exécutif")

    d.lead("Le présent plan organise, pour la période 2027–2028, le dispositif de suivi-évaluation du "
           "Projet Multisectoriel de Nutrition et de Santé – volet Nutrition à Assise Communautaire "
           "(PMNS-NAC) dans la province du Kwilu, tel que décrit dans le formulaire TECH-4 de la "
           "Demande de Propositions N° ZR-DRC-MSP-235334-CS-QCBS.")

    d.p("Le document Tech-4 constitue l’unique source de référence. Aucun objectif, résultat, indicateur, "
        "montant, volume ou mécanisme institutionnel n’a été ajouté. Lorsque l’information nécessaire au "
        "suivi-évaluation n’y figure pas — en particulier les <b>valeurs de référence</b> et les "
        "<b>cibles annuelles</b> — la mention « <b>À préciser</b> » est utilisée, et la méthode permettant de "
        "la produire est proposée et signalée comme <b>recommandation à valider</b>.")

    d.h3("Contexte du projet")
    d.p("La province du Kwilu présente une situation nutritionnelle critique, documentée dans Tech-4 : "
        "47 % d’enfants de moins de cinq ans souffrent de retard de croissance, 34,8 % d’insuffisance pondérale, "
        "la prévalence de l’insécurité alimentaire sévère atteint 49,9 % (contre 43,7 % au niveau national) et "
        "seuls 32,7 % des femmes pratiquent l’allaitement maternel exclusif jusqu’à six mois. La couverture des "
        "interventions de nutrition dans les formations sanitaires des dix zones de santé ciblées demeure faible : "
        "CPSr 47,1 %, ANJE 50 %, PCIMA et NAC 0 % (rapport annuel PRONANUT Kwilu 2020, cité par Tech-4). "
        "Aucune zone de santé de la province n’a été approvisionnée en intrants nutritionnels depuis 2019.")

    d.h3("Objectifs et résultats attendus")
    d.p("L’objectif global retenu par Tech-4 est d’<b>accroître l’accès et l’utilisation du paquet de services de "
        "nutrition de qualité dans les FOSA et dans la communauté</b>. Il se décline en quatre objectifs spécifiques "
        "— mise en œuvre des activités dans les sites communautaires (OS1), prévention et prise en charge des "
        "violences basées sur le genre (OS2), renforcement des structures de participation communautaire (OS3) et "
        "appui au système de santé dans les FOSA (OS4) — complétés par un résultat intermédiaire consacré au "
        "suivi-évaluation, à la redevabilité et à l’apprentissage (RI 4.5).")

    d.h3("Approche de suivi-évaluation retenue")
    d.p("Le dispositif articule quatre niveaux : (i) le <b>suivi de la mise en œuvre</b> à partir des rapports "
        "d’activité mensuels et du programme de travail de Tech-4 ; (ii) le <b>suivi des résultats</b> au moyen "
        "d’indicateurs d’extrants et d’effets ; (iii) le <b>suivi de la qualité</b> par les supervisions formatives, "
        "les audits de données et le Monitorage amélioré pour l’action (MAA) ; (iv) les <b>évaluations</b> "
        "— de base, à mi-parcours et finale — prévues par Tech-4. La triangulation s’appuie sur trois familles de "
        "sources : données de routine (DHIS2), registres communautaires électroniques et enquêtes périodiques.")

    d.kpis([("41", "indicateurs<br/>documentés"),
            ("14", "résultats<br/>intermédiaires"),
            ("2", "années<br/>couvertes"),
            ("10", "zones de santé<br/>suivies")])

    d.h3("Principaux outils de mesure")
    d.p("Les outils sont ceux que Tech-4 mentionne explicitement : registres de FOSA (registres UNTA/UNTI, fiches "
        "de suivi individuel, fiches CPS, fiches de référence et contre-référence), registre communautaire "
        "électronique déployé auprès des RECO et des présidents de CAC, plateforme DHIS2, canevas de supervision, "
        "bulletins de performance communautaire (BCP), enquêtes SMART et enquêtes de satisfaction semestrielles. "
        "Les outils complémentaires proposés par le présent plan sont identifiés comme tels.")

    d.callout("Avertissement méthodologique",
              "Tech-4 ne contient <b>aucune valeur de référence propre au projet</b> pour les 14 résultats "
              "intermédiaires, et <b>aucune cible annuelle</b>. Les seules cibles chiffrées disponibles sont des "
              "volumes de livrables (par exemple 3 188 CAC, 8 314 RECO, 423 FOSA, 30 FARN) et quelques objectifs de "
              "performance ponctuels (au moins 80 % des enfants MAS référés pris en charge ; 80 % des femmes "
              "réalisant la CPN à la 16ᵉ semaine). Ces cibles sont reproduites telles quelles et positionnées "
              "globalement ; leur ventilation entre 2027 et 2028 n’est <b>pas</b> documentée et doit être arbitrée "
              "lors de l’atelier de validation des cibles (recommandation).", tone="red")

    d.h3("Période couverte")
    d.p("Le plan couvre une période de deux ans : <b>année 1 (1ᵉʳ janvier – 31 décembre 2027)</b> et "
        "<b>année 2 (1ᵉʳ janvier – 31 décembre 2028)</b>. Tech-4 décrit une mise en œuvre de 18 mois et fixe "
        "l’échéance des objectifs au 31 décembre 2023 ; l’exercice 2027–2028 constitue donc une "
        "<b>reprogrammation temporelle</b> des mêmes objectifs, résultats et activités, sans modification de leur "
        "libellé ni de leur portée. Ce décalage est signalé comme point de vigilance en section 11 (risque R12) "
        "et en annexe E.")

    d.h3("Nature et portée du dispositif")
    d.p("Le dispositif retenu est un <b>suivi-évaluation de gestion axée sur les résultats</b>. Il ne se "
        "substitue pas au système national d’information sanitaire : il l’utilise comme source principale et "
        "ajoute ce que le système national ne couvre pas — le registre électronique communautaire, la mesure de "
        "la fonctionnalité des structures de participation, le suivi individualisé des bénéficiaires et "
        "l’évaluation de la qualité des services. Cette articulation est celle que Tech-4 décrit au §RI 4.5.")
    d.p("Trois principes gouvernent sa construction. <b>Premièrement, la fidélité documentaire</b> : tout "
        "objectif, résultat, indicateur, volume et mécanisme institutionnel provient de Tech-4 ; les apports du "
        "présent plan sont identifiés comme tels. <b>Deuxièmement, la séparation stricte</b> entre ce qui est "
        "documenté et ce qui est proposé — les recommandations sont signalées dans des encadrés dédiés et "
        "rappelées dans les tableaux. <b>Troisièmement, la cohérence entre livrables</b> : le registre des "
        "indicateurs de la section 5 est la source unique du cadre de performance (livrable 03) et des fiches "
        "techniques (livrable 04).")

    d.h3("Structure du document")
    d.table(
        ["Section", "Objet", "Livrable lié"],
        [0.30, 0.44, 0.26],
        [["1 à 4", "Présentation du projet, théorie du changement, objectifs du dispositif et approche "
                   "méthodologique", "—"],
         ["5", "Registre des indicateurs : 14 colonnes, définitions, formules, références et cibles", "Livrables 03 et 04"],
         ["6 à 9", "Organisation institutionnelle, outils de collecte, assurance qualité, plan de reporting", "—"],
         ["10 et 11", "Planification 2027–2028 et gestion des risques", "—"],
         ["12 et 13", "Utilisation des résultats et annexes (référentiel, canevas, traçabilité, sigles)", "Livrable 05"]],
        size=8.0,
        caption="Structure du plan de suivi-évaluation",
        note="Le rapport de contrôle qualité (livrable 05) documente la traçabilité, les informations manquantes "
             "et les contrôles effectués sur l’ensemble des livrables.")

    # ==================================================================
    # C. PRÉSENTATION GÉNÉRALE DU PROJET
    # ==================================================================
    d.h1("1", "Présentation générale du projet")

    d.h2("1.1", "Identification du projet")
    d.table(
        ["Élément", "Contenu", "Source"],
        [0.24, 0.58, 0.18],
        [["Intitulé de la mission",
          "Services de consultants (ONG) chargés de la mise en œuvre des services de nutrition "
          "à assise communautaire (NAC) dans la province du Kwilu", "Tech-4, page de garde"],
         ["Document de référence",
          "Demande de Propositions (DP) N° ZR-DRC-MSP-235334-CS-QCBS — Formulaire TECH-4 "
          "(description de l’approche, de la méthodologie et du programme de travail)", "Tech-4, page de garde"],
         ["Groupement",
          "Consortium SANRU – ICHESS – FONLIV – FDSS, chef de file : SANRU", "Tech-4, page de garde"],
         ["Bailleur / maître d’ouvrage",
          "UG-PDSS (Unité de Gestion du Programme de Développement du Système de Santé) ; "
          "évaluations mensuelles de vérification des performances et rapports transmis à l’UG-PDSS", "Tech-4, RI 4.4"],
         ["Tutelle technique",
          "Ministère de la Santé publique, hygiène et prévention (MSPHP) ; DPS Kwilu ; PRONANUT ; PNSR", "Tech-4, §RI 4.4"],
         ["Province", "Kwilu (RDC), 5 territoires (Bagata, Bulungu, Gungu, Idiofa, Masimanimba) et 2 villes (Kikwit, Bandundu)", "Tech-4, §1.1"],
         ["Zones de santé ciblées",
          "10 ZS : Djuma, Gungu, Kikwit Nord, Kimputu, Kingandu, Moanza, Mosango, Pay Kongila, "
          "Sia, Yasa Bonga", "Tech-4, Tableau « Répartition et fonctionnalité des structures communautaires »"],
         ["Aires de santé", "250 aires de santé", "Tech-4, §Objectif 1"],
         ["Villages", "3 188 villages (dont 2 250 disposant d’une CAC en 2021, soit 71 %)", "Tech-4, §OS3"],
         ["Formations sanitaires", "423 FOSA (413 centres de santé abritant les UNTA et 10 HGP abritant les UNTI)", "Tech-4, §RI 4.1"],
         ["Population cible",
          "Femmes enceintes, femmes allaitantes, enfants de 0 à 59 mois, adolescentes ; "
          "groupes d’influence (grands-mères, pères, chefs traditionnels et religieux, RECO, prestataires)", "Tech-4, §1.3"],
         ["Durée indiquée dans Tech-4",
          "18 mois ; objectifs assignés « d’ici 31 décembre 2023 »", "Tech-4, §1.3 et §RI 4.2"],
         ["Période du présent plan", "1ᵉʳ janvier 2027 – 31 décembre 2028 (deux exercices)", "Cadrage de la mission"]],
        caption="Tableau 1 — Fiche d’identification du projet",
        note="Toutes les données de ce tableau sont issues de Tech-4. La durée de 18 mois et l’échéance de 2023 "
             "y sont explicitement mentionnées ; le présent plan les prolonge sur 2027–2028 (voir section 12).")

    d.h2("1.2", "Contexte et justification")
    d.p("Tech-4 documente une situation nutritionnelle préoccupante à l’échelle nationale et provinciale. "
        "En RDC, 42 % des enfants de moins de cinq ans souffrent de retard de croissance (MICS-Palu 2017-2018) ; "
        "cette proportion atteint 52 % dans les ménages les plus pauvres contre 18 % dans les plus riches. "
        "Dans la province du Kwilu, les indicateurs sont plus dégradés encore que la moyenne nationale.")

    d.table(
        ["Indicateur de situation", "Kwilu", "National", "Source citée par Tech-4"],
        [0.40, 0.13, 0.13, 0.34],
        [["Retard de croissance, enfants &lt; 5 ans", "47 %", "42 %", "MICS-Palu 2017-2018 / MICS 6"],
         ["Insuffisance pondérale, enfants &lt; 5 ans", "34,8 %", NM, "Tech-4 §1.1"],
         ["Insécurité alimentaire sévère", "49,9 %", "43,7 %", "IPC 2021-2022"],
         ["Insécurité alimentaire modérée à sévère", "67,5 %", "65,5 %", "IPC 2021-2022"],
         ["Initiation précoce à l’allaitement", "29,2 %", "46,9 %", "MICS"],
         ["Allaitement maternel exclusif à 6 mois", "32,7 %", "53,5 %", "MICS"],
         ["Allaitement maternel continu jusqu’à 24 mois", "78,1 %", NM, "MICS"],
         ["Alimentation de complément adéquate (6-23 mois)", "18 %", NM, "Tech-4 §1.1"],
         ["Diversité alimentaire minimale", "27,1 %", NM, "MICS"],
         ["Au moins 4 CPN pendant la grossesse", "24,3 %", "42,9 %", "MICS"],
         ["Ménages avec installation de lavage des mains (eau + savon)", "18 %", NM, "MICS"],
         ["Population utilisant une source améliorée d’eau", "29 %", NM, "MICS"],
         ["Population vivant avec moins de 1,90 USD/jour", "93,2 %", "74,7 %", "Tech-4 §1.1"],
         ["Couverture en CAC (villages)", "71 % (2 250/3 188)", NM, "DPS Kwilu 2021"],
         ["CAC ayant tenu toutes les réunions mensuelles en 2021", "53,6 %", NM, "DHIS2 2021"],
         ["CAC disposant d’un plan d’action communautaire", "16 %", "30 %", "PSNSC 2019-2022"]],
        align=["l", "c", "c", "l"],
        caption="Tableau 2 — Situation de référence provinciale documentée dans Tech-4",
        note="Ces valeurs constituent le <b>contexte</b> du projet ; elles ne sont pas des cibles et ne peuvent pas "
             "être utilisées comme valeurs de référence du cadre de performance, Tech-4 ne les rattachant pas "
             "explicitement aux indicateurs du projet (voir section 6).")

    d.p("Tech-4 identifie cinq familles de causes immédiates et sous-jacentes : la mauvaise qualité de "
        "l’alimentation (pratiques ANJE inadaptées, régime peu diversifié), l’insécurité alimentaire aiguë, "
        "les maladies infantiles et épidémies (paludisme, diarrhée, rougeole, géo-helminthiases, anémie), "
        "les mauvaises conditions d’hygiène et d’accès à l’eau, enfin les effets de la situation sécuritaire et "
        "des catastrophes naturelles. Le cadre conceptuel retenu est celui de l’UNICEF, adapté au contexte du "
        "Kwilu par le consortium.")

    d.h2("1.3", "Objectif général")
    d.callout("Objectif global (Tech-4, cadre logique)",
              "<b>Accroître l’accès et l’utilisation du paquet de services de nutrition de qualité dans les "
              "FOSA et dans la communauté.</b><br/><br/>"
              "Indicateur objectivement vérifiable (I.O.V.) associé par Tech-4 : nombre d’enfants de moins de "
              "5 ans ayant bénéficié d’un paquet holistique de prise en charge de la malnutrition.", tone="navy")

    d.p("Tech-4 précise par ailleurs que l’objectif ultime du projet est de contribuer à la réduction de la "
        "mortalité et de la morbidité liées à la malnutrition chez les enfants de 6 à 59 mois et les femmes "
        "enceintes et allaitantes (FEFA) dans les 10 zones de santé de la province du Kwilu, tout en signalant "
        "que <i>« l’impact du projet ne sera pas analysé au cours de cette évaluation car ceci nécessitera une "
        "étude plus approfondie »</i>.")

    d.h2("1.4", "Objectifs spécifiques")
    d.table(
        ["Code", "Objectif spécifique", "Résultats intermédiaires associés"],
        [0.09, 0.55, 0.36],
        [["OS1", T.OS1.replace("OS1 — ", ""),
          "RI 1.1 Accès et utilisation améliorés<br/>RI 1.2 Approches innovantes documentées<br/>"
          "RI 1.3 Qualité des services communautaires améliorée"],
         ["OS2", T.OS2.replace("OS2 — ", ""),
          "RI 2.1 Comités locaux VBG mis en place et actifs<br/>RI 2.2 Communautés sensibilisées et engagées<br/>"
          "RI 2.3 Système de prise en charge des SVS renforcé"],
         ["OS3", T.OS3.replace("OS3 — ", ""),
          "RI 3.1 Organisation et fonctionnement des structures renforcés<br/>"
          "RI 3.2 Leadership et capacités managériales renforcés<br/>RI 3.3 Coordination multisectorielle renforcée"],
         ["OS4", T.OS4.replace("OS4 — ", ""),
          "RI 4.1 Offre et utilisation des services améliorées<br/>RI 4.2 Qualité des services améliorée<br/>"
          "RI 4.3 Coordination des interventions renforcée<br/>RI 4.4 Mise en œuvre assurée<br/>"
          "RI 4.5 Suivi-évaluation, redevabilité et apprentissage assurés"]],
        caption="Tableau 3 — Objectifs spécifiques et résultats intermédiaires (libellés conformes à Tech-4)",
        note="Les libellés sont reproduits sans modification de sens. Tech-4 présente le RI 4.5 comme un résultat "
             "intermédiaire de l’OS4 ; le présent plan le traite également comme le cinquième domaine "
             "programmatique, ce qui explique la codification « OS5 » utilisée dans les fiches d’indicateurs.")

    d.h2("1.5", "Principales composantes et interventions")
    d.table(
        ["Composante", "Interventions documentées dans Tech-4", "Volumes et cibles du document source"],
        [0.22, 0.45, 0.33],
        [["Nutrition à assise communautaire (NAC)",
          "Formation et équipement des prestataires communautaires ; VAD ; dépistageMUAC ; distribution de "
          "vitamine A et déparasitage ; CPSr en stratégie avancée ; promotion de l’ANJE et des PFE ; "
          "démonstrations culinaires ; BCP",
          "3 188 CAC · 8 314 RECO · 190 SSC · 150 émissions radio · 10 spots ANJE"],
         ["Approches innovantes",
          "Approche « PB Famille » ; Foyers d’Apprentissage et de Réhabilitation Nutritionnelle (FARN) ; "
          "prise en charge communautaire de la MAM avec aliments locaux (modèle IMA/SANRU) ; registre "
          "électronique ; AFASAC",
          "30 FARN dans 30 villages (ZS Bonga Yasa et Kingandu) · 2 738 smartphones · 42 AS dotées en kits informatiques"],
         ["Violences basées sur le genre",
          "Comités locaux de lutte contre les VBG/EAS/HS ; sensibilisation et engagement communautaire ; "
          "prise en charge holistique des survivants ; kits PEP ; ligne verte",
          "10 comités locaux · 30 formateurs · 30 prestataires cliniques · 2 500 pairs-éducateurs · 6 FOSA dotées en kits PEP"],
         ["Participation communautaire",
          "Mise en place et redynamisation des CAC, CODESA et UCODESA ; plans d’action communautaire ; "
          "micro-projets à impact nutritionnel ; financement basé sur la performance communautaire",
          "938 CAC à créer · 1 044 CAC à redynamiser · 250 CODESA · 10 UCODESA · subvention de 300 USD par CAC"],
         ["Services de nutrition dans les FOSA",
          "PCIMA (UNTA/UNTI) ; CPSr ; CPN et CPoN ; promotion de l’ANJE ; SDE ; EHA ; gestion des intrants ; "
          "qualité des données",
          "423 FOSA · 846 prestataires formés · 60 cadres d’ECZS · 10 UNTI réhabilitées · 250 dépôts aménagés"],
         ["Coordination et gouvernance",
          "Comité provincial et comités territoriaux multisectoriels de nutrition ; réunions trimestrielles "
          "des plateformes ; mécanismes de gestion des plaintes ; partenariat DPS/PRONANUT",
          "2 ateliers provinciaux · 1 comité provincial · comités territoriaux (nombre non chiffré)"],
         ["Suivi-évaluation et apprentissage (RI 4.5)",
          "Plan de suivi-évaluation ; MAA trimestriel ; évaluations de base, à mi-parcours et finale ; "
          "recherche opérationnelle ; documentation des bonnes pratiques ; revues semestrielles ; SNSAP",
          "3 évaluations · MAA trimestriel · 2 sites sentinelles par ZS · forfait de 20 USD/mois par ZS pour le SNSAP"]],
        size=7.5,
        caption="Tableau 4 — Composantes, interventions et volumes issus de Tech-4",
        note="Les colonnes 1 et 2 reformulent des contenus de Tech-4 sans en modifier le sens ; la colonne 3 "
             "reprend les quantités explicitement écrites dans le document source.")

    d.h2("1.6", "Zones d’intervention et population cible")
    d.p("Les dix zones de santé ciblées se répartissent sur cinq territoires et la ville de Kikwit. "
        "La ville de Bandundu, chef-lieu de la province, est excentrée et n’abrite aucune des dix zones de santé, "
        "mais le consortium y ouvre un sous-bureau pour des raisons stratégiques.")
    d.table(
        ["Territoire / Ville", "Zone de santé", "Aires de santé", "Villages", "Ménages", "CAC installées (2021)", "Couverture CAC"],
        [0.18, 0.17, 0.11, 0.11, 0.14, 0.14, 0.15],
        [["Bagata", "Sia", "22", "129", "25 751", "127", "98 %"],
         ["Bulungu", "Djuma", "35", "226", "50 652", "226", "100 %"],
         ["Idiofa", "Kimputu", "28", "237", "45 962", "232", "98 %"],
         ["Gungu", "Gungu", "31", "393", "58 219", "262", "67 %"],
         ["Gungu", "Kingandu", "20", "222", "25 320", "222", "100 %"],
         ["Kikwit", "Kikwit Nord", "25", "833", "54 506", "72", "9 %"],
         ["Masi-Manimba", "Pay Kongila", "23", "311", "35 038", "306", "98 %"],
         ["Masi-Manimba", "Moanza", "23", "275", "40 017", "273", "99 %"],
         ["Masi-Manimba", "Mosango", "18", "250", "28 247", "231", "92 %"],
         ["Masi-Manimba", "Yasa Bonga", "25", "312", "51 983", "299", "96 %"],
         ["<b>Total</b>", "<b>10 ZS</b>", "<b>250</b>", "<b>3 188</b>", "<b>415 695</b>", "<b>2 250</b>", "<b>71 %</b>"]],
        align=["l", "l", "c", "c", "c", "c", "c"],
        caption="Tableau 5 — Répartition géographique et démographique des 10 zones de santé ciblées",
        note="Source : Tech-4, Tableau « Répartition et fonctionnalité des structures communautaires par ZS, "
             "DPS Kwilu 2021 ». Le besoin en relais communautaires est estimé à 8 314 RECO sur la base d’un "
             "ratio d’au plus 50 ménages par RECO.")

    # ==================================================================
    # D. THÉORIE DU CHANGEMENT
    # ==================================================================
    d.h1("2", "Théorie du changement et logique d’intervention")

    d.h2("2.1", "Le modèle Environnement – Demande – Offre (EDO) retenu par le consortium")
    d.p("Tech-4 fonde sa théorie du changement sur le modèle EDO, qui postule que <i>« seule une approche "
        "holistique d’interventions qui se renforcent mutuellement conduira à des programmes de santé et de "
        "développement durable »</i>. Les trois domaines — Offre, Environnement favorable et Demande — sont "
        "représentés comme « de manière égale, équivalente et interdépendante ».")
    d.figure("figures/fig_edo.png", 0.78,
             caption="Figure 1 — Modèle EDO : Offre, Demande et Environnement favorable",
             note="Schéma reconstitué à partir de la description du modèle EDO dans Tech-4 (§1.5). "
                  "Tech-4 renvoie également à une figure non reproduite dans le formulaire (« Figure xxx : "
                  "Théorie de changement basée sur le modèle EDO »).")

    d.p("Le consortium précise que <i>« l’évaluation de départ « Baseline » […] pourra démontrer plus de "
        "problèmes pour l’un ou l’autre domaine par rapport aux autres »</i> et qu’il priorisera en conséquence "
        "les investissements. Ce point a une implication directe pour le suivi-évaluation : la ligne de base "
        "doit être désagrégée par domaine EDO afin de permettre cet arbitrage.")

    d.h2("2.2", "Chaîne des résultats")
    d.p("La chaîne des résultats est reconstituée ci-dessous à partir des objectifs, des résultats "
        "intermédiaires, du programme de travail et du cadre logique figurant dans Tech-4. Les volumes indiqués "
        "sont ceux du document source et non des cibles annuelles.")
    d.figure("figures/fig_theorie.png", 1.0,
             caption="Figure 2 — Chaîne des résultats : ressources → activités → extrants → effets → impact",
             note="Les liens de causalité entre extrants et effets sont ceux que Tech-4 énonce dans son cadre "
                  "logique. Les relations non explicitées dans la source sont signalées en section 2.3.")

    d.h2("2.3", "Éléments de causalité à valider")
    d.table(
        ["Élément de la logique", "Statut dans Tech-4", "Point à valider"],
        [0.30, 0.34, 0.36],
        [["Impact attendu sur le retard de croissance",
          "L’objectif général cible « les principaux déterminants du retard de croissance chez les enfants de "
          "moins de deux ans » ; le cadre logique mesure un volume de prise en charge",
          "Établir la chaîne causale explicite entre le paquet de prise en charge et la prévalence du retard de "
          "croissance, et préciser si un indicateur de prévalence est suivi"],
         ["Contribution des innovations (FARN, PB Famille)",
          "Décrites et justifiées par des expériences antérieures (ACF Côte d’Ivoire 2015, FONLIV Vanga 2015, "
          "COOPI Boko 2017) ; RI 1.2 prévoit leur documentation",
          "Définir les critères de succès des innovations et la mesure de leur effet sur la récupération des "
          "enfants MAM"],
         ["Effet du volet VBG",
          "Trois résultats intermédiaires (RI 2.1 à 2.3) et un I.O.V. de prise en charge holistique",
          "Préciser le lien attendu entre sensibilisation, notification des cas et prise en charge effective"],
         ["Financement basé sur la performance communautaire",
          "Modèle annoncé (prime de 5 USD par RECO, 10 USD/mois par CAC) sans indicateurs de performance "
          "explicitement listés",
          "Arrêter la liste des indicateurs de performance conditionnant les primes"],
         ["Durabilité",
          "Principe directeur ; appui aux groupes de soutien limité aux 9 premiers mois ; micro-projets de 300 USD",
          "Définir les indicateurs de pérennité (appropriation communautaire, maintien des CAC après le projet)"]],
        caption="Tableau 6 — Éléments de la théorie du changement à préciser",
        note="Ces points ne sont pas des lacunes du document source mais des éléments que le dispositif de "
             "suivi-évaluation doit clarifier pour être en mesure de démontrer les effets.")

    # ==================================================================
    # E. OBJECTIFS DU SYSTÈME DE SUIVI-ÉVALUATION
    # ==================================================================
    d.h1("3", "Objectifs du système de suivi-évaluation")

    d.h2("3.1", "Objectif général du dispositif")
    d.callout("Objectif général",
              "Doter le consortium et ses partenaires d’un dispositif unique de mesure, d’analyse et de "
              "redevabilité permettant de vérifier, tout au long des exercices 2027 et 2028, l’atteinte des "
              "objectifs et des résultats intermédiaires définis dans Tech-4, d’éclairer la prise de décision et "
              "de rendre compte aux communautés, à la DPS/PRONANUT et à l’UG-PDSS.", tone="navy")

    d.h2("3.2", "Objectifs spécifiques")
    d.numbered([
        "<b>Mesurer la mise en œuvre</b> : rendre compte de l’exécution du programme de travail de Tech-4 "
        "(activités, volumes de livrables, calendrier) selon une périodicité mensuelle et trimestrielle.",
        "<b>Mesurer les résultats</b> : suivre les extrants et les effets au moyen des indicateurs du cadre de "
        "performance, avec des valeurs de référence établies par l’évaluation de base.",
        "<b>Vérifier la qualité des services</b> : documenter la qualité des prestations communautaires et "
        "cliniques au moyen des outils d’évaluation développés avec le PRONANUT, des supervisions formatives et "
        "des enquêtes semestrielles de satisfaction.",
        "<b>Assurer la qualité des données</b> : appliquer la triade complétude – promptitude – cohérence "
        "retenue par Tech-4, complétée par l’exactitude, et organiser des audits réguliers.",
        "<b>Éclairer la décision</b> : produire des analyses exploitables lors des réunions de monitorage, du "
        "MAA, des revues semestrielles et des sessions du comité de pilotage.",
        "<b>Rendre compte</b> : produire les rapports mensuels, trimestriels et annuels attendus par l’UG-PDSS, "
        "ainsi que les bulletins trimestriels de la DPS sur les données de nutrition.",
        "<b>Capitaliser et apprendre</b> : documenter les bonnes pratiques, les innovations et les leçons "
        "apprises, et conduire la recherche opérationnelle prévue par Tech-4.",
    ])

    d.h2("3.3", "Besoins en information par niveau de décision")
    d.table(
        ["Niveau de décision", "Besoins d’information", "Périodicité", "Support"],
        [0.22, 0.40, 0.17, 0.21],
        [["Communauté (CAC, CODESA)",
          "Couverture des cibles, réalisation des VAD, écarts entre cibles dénombrées et cibles servies, "
          "goulots d’étranglement locaux", "Mensuelle (réunions de monitorage)", "Registre électronique, BCP, tableau de bord communautaire"],
         ["Aire de santé et centre de santé",
          "Disponibilité des intrants, réalisation des activités, qualité des prestations, référencement",
          "Mensuelle", "Registres de FOSA, fiche de supervision, DHIS2"],
         ["Zone de santé (ECZS)", "Performance des AS, fonctionnalité des CAC/CODESA, qualité des données, "
          "gestion des intrants", "Mensuelle et trimestrielle", "DHIS2, rapports des AS, MAA"],
         ["Province (DPS / PRONANUT)",
          "Couverture des interventions traces, qualité des services, coordination multisectorielle",
          "Trimestrielle et semestrielle", "Bulletins trimestriels, revues semestrielles"],
         ["Consortium (UGP)", "Avancement du programme de travail, exécution budgétaire, risques, performances",
          "Mensuelle et trimestrielle", "Rapports d’avancement, tableau de bord de projet"],
         ["Bailleur (UG-PDSS)", "Atteinte des objectifs, résultats, redevabilité", "Trimestrielle et annuelle",
          "Rapports d’avancement trimestriels et annuels"]],
        caption="Tableau 7 — Besoins en information par niveau de décision",
        note="Les périodicités reprennent celles que Tech-4 mentionne explicitement : réunions mensuelles de "
             "monitorage, supervisions mensuelles au niveau opérationnel, revues et supervisions trimestrielles "
             "aux niveaux provincial et national, revues semestrielles de la nutrition, rapports mensuels, "
             "trimestriels et annuels à l’UG-PDSS.")

    d.h2("3.4", "Utilisation des données pour la prise de décision")
    d.p("Tech-4 énonce que le dispositif doit permettre <i>« d’orienter la prise de décision basée sur des "
        "données fiables et de bonne qualité »</i> et prévoit explicitement que les résultats des évaluations "
        "alimentent les visites de supervision formative et de coaching. Le présent plan formalise quatre "
        "points d’entrée décisionnels : la réunion mensuelle de monitorage (action locale immédiate), le MAA "
        "trimestriel (suppression des goulots d’étranglement), la revue semestrielle (réorientation "
        "programmatique) et le comité de pilotage (arbitrage stratégique et budgétaire).")

    # ==================================================================
    # F. APPROCHE MÉTHODOLOGIQUE
    # ==================================================================
    d.h1("4", "Approche méthodologique")

    d.h2("4.1", "Architecture générale du dispositif")
    d.p("Le dispositif repose sur la combinaison de trois sources de données et de quatre temps de régulation. "
        "Les sources sont : (i) les <b>données de routine</b> du système national d’information sanitaire "
        "(DHIS2) alimentées par les FOSA ; (ii) les <b>registres communautaires</b>, papier puis électroniques, "
        "renseignés par les RECO et consolidés par les présidents de CAC ; (iii) les <b>enquêtes et évaluations</b> "
        "périodiques. Les temps de régulation sont le monitorage mensuel, le MAA trimestriel, la revue "
        "semestrielle et le comité de pilotage trimestriel.")
    d.figure("figures/fig_chaine.png", 1.0,
             caption="Figure 3 — Chaîne de valeur des données et dispositifs de contrôle",
             note="Les dispositifs de contrôle listés sont ceux que Tech-4 prévoit (§RI 4.2 et §RI 4.5).")

    d.h2("4.2", "Suivi de la mise en œuvre")
    d.p("Le suivi de la mise en œuvre s’appuie sur le programme de travail de Tech-4 (section B.1), qui associe "
        "à chaque activité un livrable et un responsable. Le suivi consiste à renseigner, pour chaque activité, "
        "son état d’avancement, la date de réalisation, le volume produit et la preuve documentaire. "
        "Les livrables types identifiés par Tech-4 sont : rapport d’activité, rapport de formation et liste de "
        "présence, bon de livraison et procès-verbal de réception, preuve de paiement, compte rendu de réunion, "
        "cartographie, plan d’action et rapport de supervision.")
    d.callout("Recommandation à valider",
              "Adopter un référentiel unique d’activités codé selon la nomenclature de Tech-4 "
              "(1.1.1 à 5.9) et l’utiliser dans tous les rapports d’avancement, afin de garantir la traçabilité "
              "entre le programme de travail source et le suivi d’exécution. Tech-4 ne fournit pas ce "
              "référentiel sous forme de liste exhaustive : les codes cités dans le présent plan sont ceux qui "
              "figurent lisiblement dans le document.", tone="gold")

    d.h2("4.3", "Suivi des résultats")
    d.p("Le suivi des résultats s’organise autour des 14 résultats intermédiaires et de l’objectif global, "
        "mesurés par les 41 indicateurs du cadre de performance (section 6 et livrable 03). Chaque indicateur "
        "dispose d’une fiche technique précisant sa définition, sa formule, son unité, sa source de vérification, "
        "sa méthode et sa fréquence de collecte, son responsable de collecte et son responsable de validation.")
    d.p("Deux niveaux de mesure sont distingués : le <b>suivi continu</b> (indicateurs de routine, mensuels ou "
        "trimestriels) et le <b>suivi périodique</b> (indicateurs mesurés lors des enquêtes de base, à "
        "mi-parcours et finale). Cette distinction conditionne la planification de la section 9.")

    d.h2("4.4", "Suivi des indicateurs")
    d.p("Le suivi des indicateurs obéit à cinq règles : (i) un indicateur est toujours rattaché à un résultat "
        "intermédiaire de Tech-4 ; (ii) sa formule est documentée avant la première collecte ; (iii) sa valeur "
        "de référence est établie par l’évaluation de base et validée par la DPS/PRONANUT ; (iv) toute "
        "modification de définition est tracée et justifiée ; (v) aucune cible n’est fixée sans décision "
        "formelle des parties prenantes.")

    d.h2("4.5", "Évaluations périodiques")
    d.p("Tech-4 prévoit explicitement trois temps d’évaluation : <b>au début</b> (niveaux de départ des "
        "indicateurs), <b>à mi-parcours</b> (examen des processus) et <b>à la fin</b> (atteinte des objectifs et "
        "enseignements). L’évaluation initiale combine plusieurs thématiques : enquêtes SMART à grappes "
        "multiples, évaluation de la mise en place et de la fonctionnalité des organes de participation "
        "communautaire et des sites de soins communautaires, évaluation des services de nutrition et de prise "
        "en charge des VBG dans les FOSA, et évaluation des connaissances, attitudes et pratiques des communautés.")
    d.table(
        ["Évaluation", "Objet", "Méthode prévue par Tech-4", "Positionnement 2027–2028"],
        [0.18, 0.30, 0.30, 0.22],
        [["Évaluation de base", "Établir les niveaux de départ de tous les indicateurs et l’état des lieux des "
          "structures", "Enquêtes transversales cliniques et communautaires ; SMART à grappes multiples ; "
          "évaluation de la fonctionnalité des CAC/CODESA ; CAP ; état des lieux des FOSA",
          "1ᵉʳ trimestre 2027 <i>(proposition)</i>"],
         ["Évaluation à mi-parcours", "Examiner les processus et la trajectoire vers les résultats",
          "Mêmes instruments, échantillon réduit ; revue documentaire ; entretiens avec les partenaires",
          "4ᵉ trimestre 2027 <i>(proposition)</i>"],
         ["Évaluation finale", "Mesurer l’atteinte des objectifs et tirer les enseignements",
          "Combinaison des instruments de l’évaluation de base ; critères de pertinence, d’efficacité et de "
          "pérennité", "4ᵉ trimestre 2028 <i>(proposition)</i>"],
         ["Recherche opérationnelle", "Documenter les innovations et les questions de mise en œuvre",
          "Protocole validé et approuvé par le comité d’éthique de l’École de Santé Publique ; publication",
          "Continu, avec points d’étape semestriels <i>(proposition)</i>"],
         ["Évaluations de la qualité de prise en charge", "Apprécier la qualité des soins et services de nutrition",
          "Cadre global d’évaluation de la qualité, auto-évaluation, outil « Quality Health Scaling »",
          "Trimestriel <i>(proposition)</i>"]],
        caption="Tableau 8 — Évaluations et études prévues",
        note="Tech-4 fixe les trois temps d’évaluation et leurs méthodes, mais <b>ne précise pas leur calendrier</b> "
             "au-delà de « début / mi-parcours / fin ». Le positionnement annuel proposé est donc une "
             "recommandation à valider.")

    d.h2("4.6", "Collecte quantitative et qualitative")
    d.p("La collecte quantitative s’appuie sur les registres de routine et sur les enquêtes. La collecte "
        "qualitative mobilise les focus groups, les dialogues communautaires, les entretiens avec les parties "
        "prenantes et l’observation directe lors des visites à domicile. Tech-4 prévoit expressément des focus "
        "groups réguliers <i>« pour permettre de collecter les attentes, les craintes des clientes et proposer "
        "des solutions adaptées à leurs besoins »</i>, ainsi que des formulaires de supervision dédiés "
        "(observation d’une VAD intégrée et ciblée, évaluation de cas par vérification inopinée, spot check "
        "dans les ménages).")

    d.h2("4.7", "Triangulation des informations")
    d.table(
        ["Question de mesure", "Source 1", "Source 2", "Source 3"],
        [0.34, 0.22, 0.22, 0.22],
        [["Couverture des interventions", "DHIS2 (FOSA)", "Registre électronique communautaire",
          "Enquête SMART / CAP"],
         ["Qualité des services", "Grille d’évaluation de la qualité", "Supervision formative",
          "Enquête de satisfaction"],
         ["Fonctionnalité des CAC/CODESA", "Rapports de réunions mensuelles", "Cartographie actualisée",
          "Évaluation de la fonctionnalité"],
         ["Données communautaires", "Registre du RECO", "Consolidation PrésiCAC",
          "Third Party Monitoring (TPM)"],
         ["Cas de VBG", "Registres des FOSA", "DHIS2", "Rapports du sous-cluster VBG"]],
        caption="Tableau 9 — Matrice de triangulation des sources",
        note="Les sources 1 à 3 sont toutes mentionnées par Tech-4. Le recours au TPM est explicitement prévu "
             "pour tracer « les parallélismes entre les données récoltées par les RECO [et] celles des enquêtes ad hoc ».")

    d.h2("4.8", "Assurance qualité des données")
    d.p("Tech-4 retient explicitement la <i>« triade formelle de la qualité des données à savoir : la "
        "complétude, la promptitude et la cohérence »</i>. Le présent plan la complète par l’exactitude, la "
        "validité et la traçabilité, et organise les contrôles décrits à la section 8.")

    d.h2("4.9", "Documentation et capitalisation")
    d.p("Tech-4 prévoit la documentation des bonnes pratiques, des innovations et des leçons apprises, ainsi "
        "qu’un système d’apprentissage et d’échange entre les dix zones de santé. La capitalisation s’appuiera "
        "sur les constats du MAA et des revues semestrielles, sur les rapports d’évaluation et sur les "
        "productions de la recherche opérationnelle.")

    import content_plan2
    import content_plan3
    content_plan2.build_matrix(d)
    content_plan2.build_reste(d)
    content_plan3.build(d)
    return d
