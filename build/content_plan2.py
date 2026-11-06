# -*- coding: utf-8 -*-
"""Sections 6 à 13 du plan de suivi-évaluation."""
import design as D
import data as T

NA = T.NA
NM = "Non renseigné dans le document source"


SHORT_RI = {
    "Objectif global (niveau impact) — Tech-4, cadre logique du projet": "Objectif global — niveau impact",
    "Indicateur de contexte (impact attendu à long terme) — proposition à valider":
        "Indicateur de contexte (proposition)",
    "Objectif global — I.O.V. du cadre logique Tech-4": "Objectif global — I.O.V.",
}


def ri(resultat):
    """Libellé court d'un résultat intermédiaire pour les tableaux matriciels."""
    if resultat in SHORT_RI:
        return SHORT_RI[resultat]
    if " — " in resultat:
        head, tail = resultat.split(" — ", 1)
        for a, b in ((" grâce à la mise en œuvre des activités", ""),
                     (" dans les sites communautaires", ""),
                     (" des 10 ZS", ""), (" dans les 10 ZS", ""),
                     ("d’un ensemble de services", "des services")):
            tail = tail.replace(a, b)
        return head + " — " + tail
    return resultat


def _statut(v, s):
    if s == "T4":
        return v
    if s == "NA":
        return '<font color="#%s"><i>%s</i></font>' % (D.RED, NA)
    return '<font color="#%s"><i>%s</i></font>' % (D.GOLD, v)


def build_matrix(d):
    d.h1("5", "Dispositif de suivi des indicateurs",
         page_break=True)
    d.p("Le registre ci-après recense l’ensemble des indicateurs mobilisables à partir de Tech-4. Il constitue "
        "la base du cadre de performance (livrable 03). Chaque indicateur est rattaché à un objectif et à un "
        "résultat intermédiaire, et sa traçabilité documentaire est indiquée en dernière colonne.")

    d.callout("Comment lire les valeurs",
              "<b>Valeurs en caractères normaux</b> : information explicitement présente dans Tech-4.<br/>"
              "<b>« À préciser » en rouge</b> : information absente du document source — elle sera produite par "
              "l’évaluation de base ou arrêtée lors de l’atelier de validation des cibles.<br/>"
              "<b>« Cible globale »</b> : volume fixé par Tech-4 pour l’ensemble de la durée du projet, sans "
              "ventilation annuelle.", tone="grey")

    d.p("<b>Avertissement sur les cibles annuelles.</b> Tech-4 ne comporte aucune cible annuelle. Les colonnes "
        "« Cible 2027 » et « Cible 2028 » sont donc systématiquement renseignées « À préciser ». Le report de "
        "la « cible globale » dans l’une ou l’autre année constituerait une construction non documentée : elle "
        "n’est pas effectuée ici. La procédure d’arbitrage est décrite en section 5.3.")

    d.h2("5.1", "Registre des indicateurs — vue matricielle")
    d.p("Le tableau ci-après présente les 14 colonnes demandées. En raison de sa largeur, il est présenté en "
        "format paysage et décomposé en trois vues complémentaires (identification, mesure, gouvernance) afin "
        "de rester parfaitement lisible.", size=9.4)

    # ---- Vue 1
    rows = []
    for i in T.INDICATEURS:
        rows.append([i["code"], i["obj_c"], ri(i["resultat"]), i["intitule"], i["definition"]])
    d.table(["Code", "Objectif", "Résultat attendu", "Indicateur", "Définition"],
            [0.052, 0.046, 0.245, 0.218, 0.439], rows,
            size=6.5, landscape=True,
            caption="Tableau 10 — Registre des indicateurs (vue 1/3) : identification et définition",
            note="Objectifs : OG = objectif global ; OS1 à OS4 = objectifs spécifiques ; OS5 = RI 4.5 "
                 "(suivi-évaluation, redevabilité et apprentissage). Les libellés des résultats intermédiaires "
                 "sont ceux de Tech-4.")

    # ---- Vue 2
    rows = []
    for i in T.INDICATEURS:
        rows.append([i["code"], i["intitule"],
                     "<b>Formule :</b> " + i["formule"].split("Numérateur :")[0].rstrip(" ;,") +
                     "<br/><b>Numérateur :</b> " + str(i["numerateur"]) +
                     "<br/><b>Dénominateur :</b> " + str(i["denominateur"]),
                     i["unite"],
                     _statut(i["ref"], i["statut_ref"]),
                     _statut(i["c27"], i["statut_27"]),
                     _statut(i["c28"], i["statut_28"]),
                     i.get("cible_globale") or ('<font color="#%s"><i>%s</i></font>' % (D.RED, NA))])
    d.table(["Code", "Indicateur", "Méthode de calcul", "Unité", "Valeur de référence",
             "Cible 2027", "Cible 2028", "Cible globale Tech-4"],
            [0.045, 0.152, 0.300, 0.072, 0.152, 0.080, 0.080, 0.119], rows,
            size=6.4, landscape=True,
            caption="Tableau 11 — Registre des indicateurs (vue 2/3) : mesure, référence et cibles",
            note="Aucune cible annuelle n’est documentée dans Tech-4. La colonne « Cible globale Tech-4 » "
                 "reproduit, lorsqu’il existe, le volume fixé par le document source pour l’ensemble de la "
                 "durée du projet.")

    # ---- Vue 3
    rows = []
    for i in T.INDICATEURS:
        rows.append([i["code"], i["intitule"], i["sv"], i["methode"], i["frequence"],
                     i["r_collecte"], i["r_valid"]])
    d.table(["Code", "Indicateur", "Source de vérification", "Méthode de collecte", "Fréquence",
             "Responsable de collecte", "Responsable de validation"],
            [0.045, 0.182, 0.203, 0.190, 0.132, 0.110, 0.138], rows,
            size=6.4, landscape=True,
            caption="Tableau 12 — Registre des indicateurs (vue 3/3) : sources, méthodes et responsabilités",
            note="Les responsabilités indiquées correspondent aux postes prévus par Tech-4 (section B.1 et "
                 "tableau des personnels). La validation finale par le Directeur de projet et la validation "
                 "technique par la DPS/PRONANUT sont une <b>recommandation</b> : Tech-4 ne formalise pas "
                 "explicitement ce circuit de validation.")

    # ---- 6.2 à 6.6
    d.h2("5.2", "Indicateurs par objectif et par niveau de résultat")
    from collections import Counter, OrderedDict
    cnt = OrderedDict()
    for lvl in ("Impact", "Effet", "Extrant", "Réalisation"):
        cnt[lvl] = sum(1 for i in T.INDICATEURS if i["niveau"] == lvl)
    d.figure("figures/fig_repartition.png", 1.0,
             caption="Figure 4 — Répartition des indicateurs par niveau de résultat",
             note="La prépondérance des indicateurs d’effets s’explique par la liste d’indicateurs que Tech-4 "
                  "attache explicitement à l’objectif spécifique 1.")

    rows = [["Objectif", "Intitulé", "Impact", "Effet", "Extrant", "Réalisation", "Total"]]
    labels = {"OG": "Objectif global", "OS1": "OS1 — Sites communautaires",
              "OS2": "OS2 — VBG", "OS3": "OS3 — Participation communautaire",
              "OS4": "OS4 — Système de santé", "OS5": "OS5 — Suivi-évaluation"}
    tot = {"Impact": 0, "Effet": 0, "Extrant": 0, "Réalisation": 0}
    for code in ["OG", "OS1", "OS2", "OS3", "OS4", "OS5"]:
        sub = [i for i in T.INDICATEURS if i["obj_c"] == code]
        c = Counter(i["niveau"] for i in sub)
        for k in tot:
            tot[k] += c.get(k, 0)
        rows.append([code, labels[code], str(c.get("Impact", 0)), str(c.get("Effet", 0)),
                     str(c.get("Extrant", 0)), str(c.get("Réalisation", 0)), str(len(sub))])
    rows.append(["<b>Total</b>", "", "<b>%d</b>" % tot["Impact"], "<b>%d</b>" % tot["Effet"],
                 "<b>%d</b>" % tot["Extrant"], "<b>%d</b>" % tot["Réalisation"],
                 "<b>%d</b>" % len(T.INDICATEURS)])
    d.table(["Objectif", "Intitulé", "Impact", "Effet", "Extrant", "Réalisation", "Total"],
            [0.10, 0.40, 0.09, 0.09, 0.10, 0.11, 0.11], rows,
            align=["l", "l", "c", "c", "c", "c", "c"],
            caption="Tableau 13 — Couverture du cadre de performance par objectif",
            note="Chaque objectif de Tech-4 est couvert par au moins un indicateur d’effet ou d’extrant.")

    d.h2("5.3", "Procédure de fixation des valeurs de référence et des cibles")
    d.p("Tech-4 ne permet pas de renseigner les valeurs de référence ni les cibles annuelles. La procédure "
        "suivante est proposée pour combler cette lacune de manière traçable et concertée.")
    d.table(
        ["Étape", "Contenu", "Responsable proposé", "Échéance proposée"],
        [0.07, 0.47, 0.26, 0.20],
        [["1", "Établir les valeurs de référence de tous les indicateurs au moyen de l’évaluation de base "
              "(enquêtes SMART, CAP, état des lieux des FOSA, évaluation de la fonctionnalité des CAC)",
          "Responsable S&E/HMIS, avec la DPS/PRONANUT", "T1 2027"],
         ["2", "Consolider les valeurs de référence dans une fiche de référence unique, validée par le "
               "Directeur de projet et endossée par la DPS", "Responsable S&E/HMIS", "Fin T1 2027"],
         ["3", "Fixer les cibles 2027 et 2028 lors d’un atelier de validation réunissant le consortium, la "
               "DPS/PRONANUT, les ECZS et l’UG-PDSS", "Directeur de projet", "T1 2027"],
         ["4", "Reporter les cibles dans le cadre de performance (livrable 03) et les notifier officiellement",
          "Responsable S&E/HMIS", "T2 2027"],
         ["5", "Réviser les cibles 2028 à l’issue de l’évaluation à mi-parcours, selon une procédure écrite "
               "de révision", "Comité de pilotage", "T4 2027"]],
        caption="Tableau 14 — Procédure proposée de fixation des références et des cibles",
        note="<b>Recommandation à valider</b> : cette procédure n’est pas décrite dans Tech-4. Elle respecte "
             "en revanche les principes du document source (recours à l’évaluation de base, validation par la "
             "DPS et le PRONANUT, revues semestrielles).")

    d.h2("5.4", "Désagrégations retenues")
    d.p("Les désagrégations minimales proposées sont : le sexe, le groupe d’âge (0-23 mois, 24-59 mois, "
        "5-17 ans, 18-59 ans, 60 ans et plus), la zone de santé, l’aire de santé, le milieu (urbain/rural), "
        "le type de formation sanitaire (CS/HGR) et, pour les indicateurs communautaires, le statut de la "
        "structure (CAC/CODESA/UCODESA). Tech-4 impose par ailleurs trois désagrégations explicites : la "
        "zone de santé, le sexe et l’âge pour les cas de VBG, et le statut UNTA/UNTI pour la prise en charge.")

    d.h2("5.5", "Indicateurs non retenus et justification")
    d.p("Certains indicateurs évoqués dans Tech-4 n’ont pas été retenus comme indicateurs de performance, "
        "faute de définition ou de possibilité de mesure dans le dispositif :")
    d.bullets([
        "<b>« % de CAC, CODESA et UCODESA dont les performances […] atteignent 80 % »</b> (cadre logique) : "
        "la liste des performances contractuelles n’est pas fournie par Tech-4 ; l’indicateur EXT-02 mesure la "
        "fonctionnalité sans ce seuil, qui reste à définir.",
        "<b>Indicateurs du SNSAP</b> : Tech-4 prévoit le renforcement du système de surveillance nutritionnelle "
        "et de sécurité alimentaire dans les sites sentinelles, sans en définir les indicateurs.",
        "<b>Indicateurs de la recherche opérationnelle</b> : les questions de recherche ne sont pas encore "
        "sélectionnées ; elles feront l’objet d’un protocole distinct.",
    ])

    d.h2("5.6", "Cohérence entre les livrables")
    d.p("Le registre ci-dessus est la source unique du cadre de performance (livrable 03) et des fiches "
        "techniques du livrable 04. Toute modification d’un indicateur doit être répercutée dans les trois "
        "livrables ; la colonne « Code » sert de clé de correspondance et permet une vérification automatique "
        "de cohérence, réalisée lors du contrôle qualité (livrable 05).")


def build_reste(d):
    # ==================================================================
    # G. ORGANISATION INSTITUTIONNELLE
    # ==================================================================
    d.h1("6", "Organisation institutionnelle du suivi-évaluation")

    d.h2("6.1", "Acteurs et responsabilités documentés")
    d.p("Tech-4 décrit l’organisation du consortium et identifie les fonctions chargées du suivi-évaluation. "
        "Le tableau ci-après ne retient que les responsabilités explicitement rattachées à un poste ou à une "
        "institution dans le document source.")
    d.table(
        ["Acteur", "Rôle documenté dans Tech-4", "Référence"],
        [0.24, 0.56, 0.20],
        [["Comité de pilotage du consortium (CPP)",
          "« Se réunira de manière ordinaire sur base trimestriel[le] » ; cadre de concertation des membres du "
          "groupement sur les orientations stratégiques et les performances attendues", "§B.2.1"],
         ["Directeur de projet",
          "Assure le leadership général du projet ; responsable de la validation et de la transmission des "
          "rapports", "§B.2.1 ; §B.1"],
         ["Responsable S&E / HMIS (poste clé K3)",
          "Pilotage du plan de suivi-évaluation, des revues internes, du feedback sur les rapports de terrain, "
          "des rapports d’avancement mensuels, trimestriels et annuels", "§RI 4.5 ; §B.1"],
         ["Spécialiste en Nutrition (poste clé K2)",
          "Responsable de la majorité des activités de nutrition et de leur rapportage", "§B.1"],
         ["Spécialiste des marchés publics et de la logistique (K5)",
          "Dotations, approvisionnements, bons de livraison et procès-verbaux de réception", "§B.1 ; §RI 4.2"],
         ["Gestionnaire financier (K4)",
          "Preuves de paiement, rapports financiers, appuis financiers aux structures", "§B.1 ; §RI 3.1"],
         ["Spécialiste engagement communautaire et genre",
          "Volet VBG, sensibilisation, comités locaux", "§OS2 ; §B.2"],
         ["Conseillers des ZS en NAC et en engagement communautaire (14 postes)",
          "Accompagnement de proximité des ZS, des CAC et des RECO", "§RI 4.4"],
         ["DPS Kwilu / PRONANUT",
          "Validation technique, développement des outils d’évaluation de la qualité, revues périodiques, "
          "bulletins trimestriels, audits de qualité des données", "§RI 1.3 ; §RI 4.2 ; §RI 4.5"],
         ["ECZS (équipes-cadres des zones de santé)",
          "Supervision mensuelle, formation en cascade, validation des données de la ZS", "§RI 4.2 ; §RI 4.5"],
         ["UG-PDSS",
          "Destinataire des rapports d’avancement mensuels, trimestriels et annuels ; évaluations mensuelles "
          "de vérification des performances", "§RI 4.4 ; §RI 4.5"],
         ["CAC, CODESA et UCODESA",
          "Collecte communautaire, monitorage mensuel, bulletin de performance communautaire, contrôle "
          "communautaire et gestion des plaintes", "§OS3 ; §RI 4.5"]],
        size=7.6,
        caption="Tableau 15 — Acteurs et responsabilités documentés",
        note="Les responsabilités de validation finale et de contrôle de second niveau ne sont pas formalisées "
             "dans Tech-4 au-delà de ce qui est indiqué ; elles font l’objet de la matrice RACI proposée en 7.2.")

    d.h2("6.2", "Matrice RACI proposée")
    d.callout("Recommandation à valider",
              "Tech-4 annonce une « matrice des responsabilités pour chaque objectif du projet » mais ne la "
              "reproduit pas dans le formulaire. La matrice ci-dessous est donc une <b>proposition</b> "
              "méthodologique, construite à partir des postes et des responsabilités effectivement décrits. "
              "Elle doit être validée en atelier avec la DPS/PRONANUT et l’UG-PDSS.", tone="gold")
    d.table(
        ["Activité de suivi-évaluation", "Resp.", "Approuve", "Consulté", "Informé"],
        [0.34, 0.16, 0.16, 0.17, 0.17],
        [["Élaboration et mise à jour du plan de S&E", "Resp. S&E", "Dir. projet", "DPS, UG-PDSS", "CPP"],
         ["Évaluation de base et enquêtes", "Resp. S&E", "Dir. projet", "DPS/PRONANUT", "UG-PDSS"],
         ["Collecte de routine (FOSA et communauté)", "Sp. Nutrition / Conseillers ZS", "Resp. S&E",
          "ECZS", "DPS"],
         ["Consolidation des données communautaires", "PrésiCAC / CODESA", "ECZS", "Resp. S&E", "CAC"],
         ["Contrôle de la qualité des données (MAA, audits)", "Resp. S&E", "DPS/PRONANUT", "ECZS", "CPP"],
         ["Analyse et interprétation", "Resp. S&E", "Dir. projet", "Sp. Nutrition", "CPP"],
         ["Production des rapports périodiques", "Resp. S&E", "Dir. projet", "DPS", "UG-PDSS"],
         ["Revues semestrielles de la nutrition", "DPS (présidence)", "Gouverneur", "Consortium, PTF", "UG-PDSS"],
         ["Évaluations à mi-parcours et finale", "Resp. S&E", "Dir. projet", "DPS, UG-PDSS", "CPP"],
         ["Capitalisation et recherche opérationnelle", "Resp. S&E", "Dir. projet", "ESP, DPS", "PTF"],
         ["Gestion des plaintes et redevabilité", "Sp. engagement communautaire", "Dir. projet", "CAC, CODESA",
          "Communautés"]],
        size=7.5,
        caption="Tableau 16 — Matrice RACI proposée pour le suivi-évaluation",
        note="R = responsable de l’exécution ; A = approbateur ; C = consulté ; I = informé. "
             "<b>Proposition à valider</b> — Tech-4 ne fournit pas cette matrice.")

    d.h2("6.3", "Dispositif institutionnel")
    d.figure("figures/fig_dispositif.png", 1.0,
             caption="Figure 5 — Dispositif institutionnel du suivi-évaluation",
             note="Organigramme reconstitué à partir de la structure de mise en œuvre décrite dans Tech-4 "
                  "(§B.2.1) et des fonctions de suivi-évaluation identifiées au §RI 4.5.")

    # ==================================================================
    # H. OUTILS
    # ==================================================================
    d.h1("7", "Outils de collecte et de gestion des données")

    d.p("Tech-4 mentionne un ensemble d’outils dont une partie existe déjà dans le système de santé et une "
        "autre sera développée par le projet. Le tableau distingue explicitement ces deux situations : "
        "il ne prétend pas que les outils non mentionnés existent.")

    d.table(
        ["Outil", "Statut selon Tech-4", "Usage dans le dispositif", "Support"],
        [0.24, 0.26, 0.32, 0.18],
        [["Registres de FOSA (registre curatif, registre UNTA/UNTI, fiches de suivi individuel, fiches CPS)",
          "Existant — à approvisionner (826 exemplaires par registre pour les CS, 20 pour les HGR)",
          "Collecte de routine des données cliniques et nutritionnelles", "Papier, saisi dans DHIS2"],
         ["Fiches de référence et contre-référence",
          "Existant — 20 595 fiches prévues pour les CS", "Traçabilité des orientations des cas MAS et des SVS",
          "Papier"],
         ["Registre communautaire électronique (RECO et PrésiCAC)",
          "À mettre en place — innovation du projet ; 2 738 smartphones",
          "Dénombrement, suivi individualisé des cibles, alertes nutritionnelles, synchronisation Bluetooth "
          "puis serveur", "Application mobile + serveur"],
         ["DHIS2 (SNIS)",
          "Existant — plateforme nationale jusqu’au niveau de la zone de santé",
          "Routine mensuelle, indicateurs de couverture, base des bulletins trimestriels",
          "Plateforme web"],
         ["Bulletin de performance communautaire (BCP)",
          "Existant — à systématiser", "Auto-évaluation communautaire, plan de redressement, redevabilité",
          "Formulaire papier consolidé"],
         ["Canevas et guides de supervision",
          "À développer et valider par la DPS, les ECZS et le projet",
          "Supervisions formatives mensuelles ; supervision des CAC", "Papier / tablette"],
         ["Formulaires de supervision des RECO (observation de VAD, évaluation de cas, spot check)",
          "À développer (explicitement prévu)", "Contrôle de la qualité des visites à domicile",
          "Papier / tablette"],
         ["Grille d’évaluation de la qualité des services de nutrition",
          "À développer avec le PRONANUT, à partir des outils existants du Ministère",
          "État des lieux, supervisions formatives, évaluations périodiques", "Papier / tablette"],
         ["Questionnaires d’enquête (SMART, CAP, satisfaction)",
          "À développer pour l’évaluation de base ; enquêtes de satisfaction semestrielles prévues",
          "Mesure des indicateurs de résultat et de perception", "Tablette"],
         ["Fiches de stock, bons de commande, de livraison, de réception et de sortie, RUMER, carnet d’ordonnances",
          "Existant — à approvisionner (413 lots pour les CS, 10 pour les HGR)",
          "Gestion et traçabilité des intrants nutritionnels", "Papier"],
         ["Registre des plaintes et ligne verte",
          "À mettre en place (comités de gestion des plaintes dans chaque village)",
          "Redevabilité, traitement des plaintes, protection", "Papier + ligne téléphonique"],
         ["Tableau de bord de projet",
          "Non mentionné dans Tech-4 — <b>proposition</b>",
          "Synthèse mensuelle des indicateurs pour l’UGP et le CPP", "Tableur / outil de restitution"]],
        size=7.4,
        caption="Tableau 17 — Outils de collecte et de gestion des données",
        note="La colonne « Statut selon Tech-4 » distingue strictement ce qui existe, ce qui est à approvisionner "
             "et ce qui est à développer. Le tableau de bord de projet est explicitement identifié comme une "
             "proposition non prévue par le document source.")

    d.h2("7.1", "Architecture des données")
    d.p("Les données suivent trois circuits convergent vers le responsable S&E/HMIS : un circuit clinique "
        "(FOSA → BCZS → DHIS2), un circuit communautaire (RECO → PrésiCAC → serveur du projet, avec "
        "consolidation par le CODESA et l’ECZS) et un circuit d’enquête (collecte sur tablette → contrôle "
        "qualité → base d’analyse). La convergence est assurée par un identifiant commun de zone de santé, "
        "d’aire de santé et de période.")

    d.h2("7.2", "Protection des données et éthique")
    d.p("Tech-4 prévoit la confidentialité dans le traitement des plaintes et la protection des survivants de "
        "violences sexuelles. Le dispositif de suivi-évaluation applique trois règles : agrégation des données "
        "VBG avant diffusion, anonymisation des identifiants individuels dans les rapports, et approbation du "
        "protocole de recherche opérationnelle par le comité d’éthique de l’École de Santé Publique, comme le "
        "prévoit Tech-4.")

    d.h2("7.3", "Garanties de confidentialité et responsabilités associées")
    d.table(
        ["Donnée sensible", "Règle de traitement", "Responsable", "Fondement dans Tech-4"],
        [0.20, 0.34, 0.20, 0.26],
        [["Cas de violences basées sur le genre",
          "Agrégation avant tout rapport ; aucune donnée nominative dans les rapports périodiques ; "
          "diffusion limitée aux niveaux habilités",
          "Spécialiste engagement communautaire",
          "Tech-4 §OS2 : prise en charge confidentielle et protection des survivants"],
         ["Plaintes et alertes communautaires",
          "Traitement par le comité de gestion des plaintes ; registre tenu séparément ; ligne verte "
          "comme canal alternatif", "Comité de gestion des plaintes",
          "Tech-4 §OS3 : contrôle communautaire et gestion des plaintes"],
         ["Données individuelles des bénéficiaires (registre électronique)",
          "Identifiants pseudonymisés ; accès restreint ; conservation limitée à la durée du projet et à "
          "son évaluation", "Responsable S&E / HMIS",
          "Tech-4 §RI 3.2 : registre électronique communautaire (innovation du projet)"],
         ["Données relatives aux victimes de violences sexuelles",
          "Aucune diffusion nominative ; analyse par zone de santé, sexe et âge uniquement",
          "Responsable S&E / HMIS avec la DPS",
          "Tech-4 §OS2 : désagrégation exigée par zone de santé, sexe et âge"],
         ["Recherche opérationnelle",
          "Approbation préalable par le comité d’éthique de l’École de Santé Publique",
          "Responsable S&E",
          "Tech-4 §RI 4.5 : protocoles soumis à l’approbation du comité d’éthique"]],
        size=7.5,
        caption="Tableau 17 bis — Garanties de confidentialité et responsabilités",
        note="Les règles de traitement sont une <b>proposition</b> de mise en œuvre ; elles s’appuient sur les "
             "engagements de confidentialité et de protection que Tech-4 formule explicitement.")

    # ==================================================================
    # I. ASSURANCE QUALITÉ
    # ==================================================================
    d.h1("8", "Assurance qualité des données")

    d.p("Tech-4 identifie explicitement trois dimensions — <i>« la complétude, la promptitude et la "
        "cohérence »</i> — et souligne que <i>« la qualité des données n’est pas optimale »</i> dans le "
        "système national. Le présent plan retient sept dimensions et associe à chacune un contrôle et un "
        "responsable.")

    d.table(
        ["Dimension", "Définition appliquée", "Contrôle mis en place", "Responsable", "Réf."],
        [0.145, 0.285, 0.305, 0.155, 0.110],
        [["Validité", "L’indicateur mesure bien ce qu’il prétend mesurer ; les définitions sont respectées",
          "Revue annuelle des définitions ; comparaison des formules avec le registre ; validation par la DPS",
          "Resp. S&E + DPS", "T4"],
         ["Fiabilité", "Les résultats sont stables dans le temps et entre collecteurs",
          "Double saisie sur un échantillon ; comparaison entre registre papier et registre électronique",
          "Resp. S&E", "T4"],
         ["Précision", "Les valeurs sont exactes et reproductibles",
          "Vérification inopinée de cas ; recomptage lors des supervisions ; TPM ponctuel", "ECZS + Resp. S&E", "T4"],
         ["Exhaustivité", "Toutes les structures et tous les cas attendus sont couverts",
          "Suivi du taux de rapportage par FOSA et par CAC ; relance des structures silencieuses",
          "ECZS + Resp. S&E", "T4"],
         ["Cohérence", "Les données sont concordantes entre sources et entre périodes",
          "Réconciliation DHIS2 / registres communautaires ; analyse des écarts ; MAA trimestriel",
          "Resp. S&E + DPS", "T4"],
         ["Ponctualité", "Les données sont disponibles dans les délais requis",
          "Suivi de la promptitude mensuelle ; tableau de bord des retards", "Resp. S&E", "T4"],
         ["Traçabilité", "Chaque valeur peut être rattachée à sa source primaire",
          "Codification des rapports ; archivage des preuves ; registre de versions des indicateurs",
          "Resp. S&E", "Proposition"]],
        size=7.4,
        caption="Tableau 18 — Dimensions de la qualité des données et contrôles associés",
        note="Les quatre premières dimensions et les dispositifs de contrôle sont explicitement prévus par "
             "Tech-4 (MAA, audits, TPM, supervision formative). La dimension « traçabilité » est une "
             "proposition complémentaire.")

    d.h2("8.1", "Mécanismes de contrôle et de validation à trois niveaux")
    d.table(
        ["Niveau", "Mécanisme", "Périodicité", "Preuve"],
        [0.13, 0.45, 0.20, 0.22],
        [["Premier niveau — structure",
          "Vérification de la complétude et de la cohérence du registre avant transmission ; réunion mensuelle "
          "de monitorage de la CAC et du CODESA", "Mensuelle", "Registre signé, compte rendu de réunion"],
         ["Deuxième niveau — zone de santé",
          "Supervision formative mensuelle par l’ECZS ; contrôle de la qualité des données lors du MAA "
          "trimestriel ; audits de complétude, de promptitude et d’exactitude", "Mensuelle et trimestrielle",
          "Rapport de supervision, rapport de MAA"],
         ["Troisième niveau — province",
          "Revue semestrielle de la nutrition sous la direction du Gouverneur et du Ministre provincial ; "
          "audits de la qualité des données ; Third Party Monitoring ponctuel ; bulletins trimestriels",
          "Semestrielle et ponctuelle", "Rapport de revue, bulletin trimestriel, rapport TPM"]],
        caption="Tableau 19 — Contrôles de qualité à trois niveaux",
        note="Chaque mécanisme est explicitement cité par Tech-4 (§RI 4.5).")

    d.h2("8.2", "Plan d’audit de la qualité des données")
    d.bullets([
        "<b>Audit initial</b> (T1 2027) : établir la ligne de base de la complétude, de la promptitude et de "
        "l’exactitude dans les 10 ZS, préalable indispensable à toute fixation de cible.",
        "<b>Audits trimestriels</b> intégrés aux sessions de MAA, portant sur un échantillon de FOSA et de CAC "
        "par zone de santé.",
        "<b>Third Party Monitoring ponctuel</b>, conformément à la pratique que Tech-4 attribue au FDSS depuis "
        "2018, pour confronter les données des RECO aux données d’enquêtes ad hoc.",
        "<b>Audit de clôture</b> (T4 2028), avant l’évaluation finale, pour garantir la fiabilité des données "
        "utilisées dans le rapport final.",
    ])
    d.callout("Recommandation à valider",
              "La programmation et les taux d’échantillonnage des audits ne figurent pas dans Tech-4. "
              "Le calendrier ci-dessus est une proposition cohérente avec les mécanismes prévus "
              "(MAA trimestriel, revues semestrielles, TPM), mais doit être validé et dimensionné.", tone="gold")

    # ==================================================================
    # J. REPORTING
    # ==================================================================
    d.h1("9", "Plan de reporting")

    d.p("Tech-4 prévoit expressément le suivi des <i>« rapports d’avancement mensuels, trimestriels et annuels "
        "à soumettre à l’UG-PDSS »</i>, la production de bulletins trimestriels de la DPS sur les données de "
        "nutrition, des revues semestrielles et des rapports d’évaluation. La matrice ci-dessous organise ces "
        "productions et distingue celles qui sont documentées de celles qui sont proposées.")

    d.table(
        ["Rapport", "Objet", "Contenu", "Période couverte", "Fréquence", "Destinataire", "Producteur"],
        [0.15, 0.13, 0.27, 0.10, 0.11, 0.12, 0.12],
        [["Rapport d’activité mensuel", "Suivi de l’exécution",
          "Activités réalisées, volumes, difficultés, plan du mois suivant", "Mois", "Mensuelle <b>(T4)</b>",
          "BCZS, ECZS, UGP", "Spécialiste Nutrition / Conseillers ZS"],
         ["Rapport de monitorage communautaire", "Suivi communautaire",
          "Cibles dénombrées et servies, écarts, plan de redressement", "Mois", "Mensuelle <b>(T4)</b>",
          "CODESA, ECZS", "CAC / CODESA"],
         ["Rapport d’avancement trimestriel", "Redevabilité",
          "Indicateurs, analyse des écarts, risques, exécution budgétaire", "Trimestre", "Trimestrielle <b>(T4)</b>",
          "UG-PDSS, CPP", "Resp. S&E / Dir. projet"],
         ["Bulletin trimestriel des données de nutrition", "Diffusion de l’information",
          "Indicateurs clés, niveau de mise en œuvre des activités", "Trimestre", "Trimestrielle <b>(T4)</b>",
          "DPS, ZS, PTF", "DPS avec appui du consortium"],
         ["Rapport de MAA", "Analyse des goulots d’étranglement",
          "Goulots identifiés, actions correctrices, responsables, échéances", "Trimestre", "Trimestrielle <b>(T4)</b>",
          "ECZS, DPS, communautés", "Resp. S&E"],
         ["Rapport de revue semestrielle", "Réorientation programmatique",
          "Progrès, goulots persistants, décisions, recommandations", "Semestre", "Semestrielle <b>(T4)</b>",
          "Gouverneur, Ministre provincial, PTF", "DPS"],
         ["Rapport d’avancement annuel", "Redevabilité annuelle",
          "Bilan de l’année, atteinte des cibles, perspectives", "Année", "Annuelle <b>(T4)</b>", "UG-PDSS",
          "Dir. projet"],
         ["Rapport d’évaluation de base", "Référence", "Valeurs de référence, état des lieux", "Démarrage",
          "Ponctuelle <b>(T4)</b>", "UG-PDSS, DPS, CPP", "Resp. S&E"],
         ["Rapport d’évaluation à mi-parcours", "Ajustement", "Processus, premiers effets, recommandations",
          "18 premiers mois", "Ponctuelle <b>(T4)</b>", "UG-PDSS, DPS", "Resp. S&E"],
         ["Rapport d’évaluation finale", "Redevabilité finale", "Atteinte des objectifs, pérennité, leçons",
          "Durée totale", "Ponctuelle <b>(T4)</b>", "UG-PDSS, DPS, PTF", "Resp. S&E / Dir. projet"],
         ["Rapport de recherche opérationnelle", "Apprentissage", "Protocole, résultats, publication",
          "Variable", "Ponctuelle <b>(T4)</b>", "DPS, ESP, PTF", "Resp. S&E"],
         ["Tableau de bord de projet", "Pilotage interne", "Indicateurs clés, alertes, avancement",
          "Mois et trimestre", "Mensuelle <b>(R)</b>", "UGP, CPP", "Resp. S&E"],
         ["Note de capitalisation", "Capitalisation", "Bonnes pratiques, innovations, leçons apprises",
          "Semestre", "Semestrielle <b>(R)</b>", "DPS, PTF, public", "Resp. S&E"]],
        size=6.8, landscape=True,
        caption="Tableau 20 — Matrice des rapports",
        note="<b>(T4)</b> = rapport explicitement prévu par Tech-4 ; <b>(R)</b> = production proposée, "
             "à valider. Les destinataires sont ceux que Tech-4 nomme comme parties prenantes du dispositif.")

    d.h2("9.1", "Normes de production des rapports")
    d.bullets([
        "<b>Structure normalisée</b> : rappel des objectifs, méthodologie, résultats par indicateur, analyse "
        "des écarts, risques, recommandations, annexes de preuves.",
        "<b>Traçabilité</b> : chaque donnée chiffrée est référencée à sa source et à sa période.",
        "<b>Comparabilité</b> : les tableaux reprennent systématiquement référence, cible, réalisation et écart.",
        "<b>Validation</b> : tout rapport est visé par le responsable S&E/HMIS puis approuvé par le Directeur de "
        "projet ; les rapports destinés à la DPS sont endossés par celle-ci.",
        "<b>Diffusion</b> : dépôt dans un espace partagé unique, avec numérotation et archivage.",
    ])
    d.p("Ces normes sont une <b>recommandation</b> : Tech-4 prévoit la production des rapports mais n’en "
        "normalise pas la structure.", size=9.4)

    return d
