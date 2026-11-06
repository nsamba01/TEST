# -*- coding: utf-8 -*-
"""CADRE DE PERFORMANCE 2027–2028 — contenu du livrable 04 (PDF).

Même source de mise en page que le plan (design.Doc), donc identité visuelle
strictement identique. Toutes les données proviennent de data.py, lui-même
construit exclusivement à partir de Tech-4.
"""
import design as D
from design import Doc
import data as T

NA = T.NA

META = {
    "title": "Cadre de performance 2027–2028 — PMNS-NAC Kwilu",
    "author": "Consortium SANRU – ICHESS – FONLIV – FDSS",
    "subject": "Cadre de performance : indicateurs, références, cibles et fiches techniques",
    "header_left": "PMNS-NAC Kwilu — Cadre de performance 2027–2028",
    "header_right": "Consortium SANRU – ICHESS – FONLIV – FDSS",
    "footer_left": "DP N° ZR-DRC-MSP-235334-CS-QCBS · Tech-4",
    "footer_center": "1ᵉʳ janvier 2027 – 31 décembre 2028",
    "cover_kicker": "Cadre de performance · Indicateurs et cibles",
    "cover_title": "CADRE DE PERFORMANCE",
    "cover_year": "2027 – 2028",
    "cover_img": "figures/cover_cadre.png",
    "cover_org": ["CONSORTIUM SANRU – ICHESS – FONLIV – FDSS",
                  "Chef de file : SANRU"],
    "cover_sub": ["Projet Multisectoriel de Nutrition et de Santé — Volet Nutrition",
                  "à Assise Communautaire (PMNS-NAC), province du Kwilu, RDC"],
    "cover_projet": ["PMNS-NAC Kwilu",
                     "41 indicateurs · 14 résultats intermédiaires · 10 zones de santé"],
    "cover_source": ["Document source : Tech-4 — Description de l’approche, de la méthodologie",
                     "et du programme de travail",
                     "Demande de Propositions N° ZR-DRC-MSP-235334-CS-QCBS"],
    "cover_periode": "Période de mise en œuvre : 1ᵉʳ janvier 2027 – 31 décembre 2028",
    "cover_version": "Version 1.0 — document de travail soumis à validation",
    "cover_footer": ["Document de consultation du classeur 03_Cadre_Performance_2027_2028.xlsx.",
                     "Mêmes indicateurs, mêmes définitions et mêmes cibles que les livrables 01 et 02."],
}

NIVEAUX = [
    ("Impact", "IMP", "Impact",
     "Mesure l’effet de long terme attendu sur la population. Tech-4 identifie un objectif global et un "
     "indicateur objectivement vérifiable ; l’indicateur de contexte complète la lecture."),
    ("Effet", "EFF", "Effets",
     "Mesure les changements de comportement, d’accès ou d’utilisation attribuables au projet. "
     "C’est le niveau le plus documenté par Tech-4, qui attache une liste d’indicateurs à l’objectif spécifique 1."),
    ("Extrant", "EXT", "Extrants",
     "Mesure les biens et services effectivement produits : structures mises en place, personnes formées, "
     "équipements livrés, campagnes diffusées."),
    ("Réalisation", "REA", "Réalisations du dispositif de suivi-évaluation",
     "Mesure la performance du dispositif de suivi-évaluation lui-même (complétude, promptitude, MAA, "
     "évaluations). Ces indicateurs relèvent du résultat intermédiaire 4.5."),
]


def _formule(txt):
    """Ne conserve que la formule : numérateur et dénominateur ont leur colonne."""
    t = str(txt)
    i = t.find("Numérateur :")
    if i > 0:
        t = t[:i].rstrip(" ;,")
    return t


def _court(txt, n=118):
    """Réduit un texte de référence à sa valeur principale, sans la déformer."""
    t = str(txt)
    if len(t) <= n:
        return t
    cut = max(t.rfind("; ", 0, n), t.rfind(". ", 0, n), t.rfind(" — ", 0, n))
    if cut < n * 0.45:
        cut = t.rfind(" ", 0, n)
    return t[:cut].rstrip(" ,;:.") + " […]"


def _v(v, statut):
    if statut == "T4":
        return str(v)
    return '<font color="#%s"><i>%s</i></font>' % (D.RED, v)


def build():
    d = Doc(META)

    # ==================================================================
    # 1. OBJET ET PÉRIMÈTRE
    # ==================================================================
    d.h1("", "Objet, périmètre et conventions de lecture")

    d.lead("Ce cadre de performance traduit en indicateurs mesurables les objectifs, résultats intermédiaires et "
           "activités du formulaire TECH-4 du consortium SANRU-ICHESS-FONLIV-FDSS. Il ne crée aucun indicateur "
           "qui ne découle du document source et signale explicitement les grandeurs que Tech-4 ne fournit pas.")

    d.kpis([("41", "indicateurs"), ("14", "résultats intermédiaires"), ("4", "niveaux de résultat"),
            ("10", "zones de santé")])

    d.h2("1", "Objet du cadre de performance")
    d.p("Le cadre de performance est l’instrument de pilotage qui permet de répondre à trois questions à chaque "
        "revue : <b>où en est-on par rapport à la situation de départ</b>, <b>où en est-on par rapport à la "
        "cible</b>, et <b>pourquoi l’écart existe-t-il</b>. Il sert de référence commune au consortium, à la "
        "Division provinciale de la santé du Kwilu, au PRONANUT et à l’Unité de gestion du Programme de "
        "développement du système de santé (UG-PDSS).")

    d.h2("2", "Périmètre")
    d.table(
        ["Élément", "Périmètre retenu", "Source"],
        [0.22, 0.54, 0.24],
        [["Période", "Année 1 : 1ᵉʳ janvier – 31 décembre 2027 ; année 2 : 1ᵉʳ janvier – 31 décembre 2028",
          "Cadrage de la mission"],
         ["Zones", "10 zones de santé : Djuma, Gungu, Kikwit Nord, Kimputu, Kingandu, Moanza, Mosango, "
                   "Pay Kongila, Sia, Yasa Bonga", "Tech-4 §1.6 et tableau des ZS"],
         ["Structures", "423 FOSA (413 CS/UNTA et 10 HGR/UNTI), 190 sites de soins communautaires, "
                        "3 188 CAC, 250 CODESA, 10 UCODESA", "Tech-4, programme de travail"],
         ["Niveaux de résultat", "Impact, effet, extrant, réalisation", "Cadre logique Tech-4"],
         ["Source unique", "Tech-4 — aucun autre document n’est mobilisé pour fixer un indicateur ou une cible",
          "Cadrage de la mission"],
         ["Documents liés", "Plan de suivi-évaluation (livrables 01 et 02) ; classeur Excel (livrable 03) ; "
                            "rapport de contrôle qualité (livrable 05)", "Présent lot"]],
        size=8.0,
        caption="Tableau 1 — Périmètre du cadre de performance")

    d.h2("3", "Conventions de lecture")
    d.callout("Trois conventions à retenir",
              "<b>1. Les valeurs en caractères normaux sont documentées</b> par Tech-4 et peuvent être citées "
              "telles quelles.<br/>"
              "<b>2. Les mentions « À préciser » en rouge signalent une information absente du document "
              "source</b> : elles ne sont jamais remplacées par une estimation.<br/>"
              "<b>3. La « cible globale » est un volume fixé par Tech-4 pour toute la durée du projet</b> ; elle "
              "n’est pas une cible annuelle et n’est donc jamais reportée dans les colonnes 2027 ou 2028.",
              tone="grey")

    d.p("Tech-4 ne comporte ni valeur de référence propre au projet pour les quatorze résultats intermédiaires, "
        "ni cible annuelle. Les colonnes « Cible 2027 » et « Cible 2028 » sont donc renseignées « À préciser » "
        "pour la quasi-totalité des indicateurs. Les seules grandeurs chiffrées disponibles sont des volumes de "
        "livrables et quelques objectifs de performance ponctuels (au moins 80 % des enfants atteints de MAS "
        "référés et pris en charge ; 80 % des femmes réalisant la CPN à la 16ᵉ semaine). Ces grandeurs sont "
        "restituées dans une colonne dédiée, sans être transformées en cibles annuelles.")

    d.h2("4", "Répartition des indicateurs")
    d.figure("figures/fig_repartition.png", 1.0,
             caption="Figure 1 — Répartition des indicateurs par niveau de résultat",
             note="41 indicateurs : 2 d’impact, 19 d’effet, 16 d’extrant et 4 de réalisation du dispositif de "
                  "suivi-évaluation.")
    from collections import Counter
    c = Counter(i["niveau"] for i in T.INDICATEURS)
    rows = []
    for lvl, pre, titre, desc in NIVEAUX:
        codes = [i["code"] for i in T.INDICATEURS if i["niveau"] == lvl]
        rows.append([lvl, "%s (%d)" % (pre, c.get(lvl, 0)), ", ".join(codes)])
    rows.append(["<b>Total</b>", "<b>%d</b>" % len(T.INDICATEURS), ""])
    d.table(["Niveau", "Préfixe (nombre)", "Codes des indicateurs"],
            [0.16, 0.20, 0.64], rows, size=7.8,
            caption="Tableau 2 — Codes et dénombrement des indicateurs",
            note="Les codes sont la clé d’identification commune au plan (livrable 02), au présent cadre et au "
                 "classeur Excel (livrable 03).")

    d.h2("5", "Structure du document")
    d.table(
        ["Section", "Contenu"],
        [0.28, 0.72],
        [["6", "Tableau principal du cadre de performance (14 colonnes, lecture paysage)"],
         ["7", "Suivi annuel de la performance — grille de saisie des réalisations 2027 et 2028"],
         ["8", "Fiches techniques des 41 indicateurs"],
         ["9", "Notes méthodologiques, limites et points à valider"]],
        caption="Tableau 3 — Plan du cadre de performance")

    # ==================================================================
    # 6. TABLEAU PRINCIPAL
    # ==================================================================
    d.h1("6", "Tableau principal du cadre de performance")

    d.p("Le tableau ci-après présente les quatorze colonnes du cadre de performance, dans l’ordre demandé. "
        "Les indicateurs y sont classés par niveau de résultat, de l’impact vers la réalisation. En raison de sa "
        "largeur, il est présenté en format paysage sur les pages suivantes.", size=9.6)

    cols = ["Niveau de résultat", "Objectif / résultat attendu", "Indicateur", "Définition", "Mode de calcul",
            "Unité", "Situation de référence", "Cible 2027", "Cible 2028", "Source de vérification",
            "Méthode de collecte", "Fréquence", "Responsable", "Hypothèses et risques"]
    widths = [0.055, 0.075, 0.088, 0.091, 0.086, 0.060, 0.080, 0.042, 0.042, 0.064, 0.072, 0.064, 0.081, 0.080]
    tot = sum(widths)
    widths = [w / tot for w in widths]
    order = ["Impact", "Effet", "Extrant", "Réalisation"]
    rows = []
    for lvl in order:
        for i in T.INDICATEURS:
            if i["niveau"] != lvl:
                continue
            obj = "%s — %s" % (i["obj_c"], i["resultat"].replace("Objectif global — ", "").replace("Objectif global (niveau impact) — ", ""))
            hyp = i.get("hypotheses") or NA
            rows.append([
                "<b>%s</b>" % lvl,
                obj,
                "<b>%s</b> — %s" % (i["code"], i["intitule"]),
                i["definition"],
                _formule(i["formule"]),
                i["unite"],
                _v(_court(i["ref"]), i["statut_ref"]),
                _v(i["c27"], i["statut_27"]),
                _v(i["c28"], i["statut_28"]),
                i["sv"],
                i["methode"],
                i["frequence"].split(" (")[0],
                i["r_collecte"],
                hyp,
            ])
    d.table(cols, widths, rows, size=6.0, landscape=True,
            caption="Tableau 4 — Cadre de performance 2027–2028 : les 14 colonnes du dispositif",
            note="Les cibles 2027 et 2028 sont « À préciser » pour l’ensemble des indicateurs : Tech-4 ne fixe "
                 "aucune cible annuelle. Le détail de la procédure de fixation figure à la section 9. "
                 "Les volumes fixés par Tech-4 pour toute la durée du projet sont documentés dans les fiches "
                 "techniques (section 8), colonne « Cible globale Tech-4 ».")

    # ==================================================================
    # 7. SUIVI ANNUEL
    # ==================================================================
    d.h1("7", "Suivi annuel de la performance")

    d.p("La grille ci-après est l’instrument de saisie annuel. <b>Les colonnes « Réalisation 2027 » et "
        "« Réalisation 2028 » sont volontairement laissées vides</b> : elles seront renseignées à partir des "
        "données effectivement collectées. <b>Aucun taux d’atteinte n’est calculé</b> à ce stade, puisque les "
        "cibles annuelles ne sont pas encore arrêtées.")

    d.callout("Règle de calcul des écarts",
              "Lorsque les cibles annuelles auront été validées (atelier du premier trimestre 2027), le taux "
              "d’atteinte sera calculé comme suit : <b>réalisation ÷ cible × 100</b> pour les indicateurs de "
              "volume et de pourcentage à sens croissant. Pour les indicateurs dont la baisse constitue "
              "l’objectif (prévalence du retard de croissance, insuffisance pondérale), le taux sera calculé "
              "sur la base de la réduction attendue : <b>(référence − réalisation) ÷ (référence − cible) × 100</b>. "
              "Cette règle est une <b>recommandation</b> ; elle devra être confirmée avec la DPS/PRONANUT.",
              tone="gold")

    cols2 = ["Code", "Indicateur", "Unité", "Référence", "Cible 2027", "Réalisation 2027", "Cible 2028",
             "Réalisation 2028", "Écart et commentaire"]
    w2 = [0.045, 0.185, 0.052, 0.100, 0.050, 0.062, 0.050, 0.062, 0.394]
    rows2 = []
    for i in T.INDICATEURS:
        rows2.append([i["code"], i["intitule"], i["unite"],
                      _v(i["ref"], i["statut_ref"]),
                      _v(i["c27"], i["statut_27"]), "",
                      _v(i["c28"], i["statut_28"]), "", ""])
    d.table(cols2, w2, rows2, size=6.1, landscape=True,
            caption="Tableau 5 — Grille de suivi annuel de la performance (réalisations à renseigner)",
            note="Colonnes « Réalisation » volontairement vides. Aucun taux d’atteinte n’est calculé dans ce "
                 "document. La grille est reprise à l’identique dans le classeur Excel (livrable 03), "
                 "onglet « Suivi annuel ».")

    # ==================================================================
    # 8. FICHES TECHNIQUES
    # ==================================================================
    d.h1("8", "Fiches techniques des indicateurs")

    d.p("Une fiche est établie pour chacun des 41 indicateurs. Elle reprend les rubriques convenues : code, "
        "intitulé, définition, justification, niveau, unité, numérateur, dénominateur, formule, désagrégations, "
        "référence, cibles 2027 et 2028, source de vérification, méthode de collecte, fréquence, responsabilités "
        "et limites. La rubrique « Cible globale Tech-4 » restitue, lorsqu’il existe, le volume fixé par le "
        "document source pour l’ensemble de la durée du projet.")

    d.callout("Avertissement",
              "Les fiches ne contiennent aucune valeur de référence ni aucune cible annuelle inventée. La "
              "rubrique « Situation de référence » cite, lorsqu’elle existe, la donnée de contexte que Tech-4 "
              "documente (prévalences provinciales, couvertures nationales) en précisant sa source ; à défaut, "
              "elle indique « À préciser ».", tone="red")

    for n, i in enumerate(T.INDICATEURS, 1):
        cible_g = i.get("cible_globale") or ('<font color="#%s"><i>%s</i></font>' % (D.RED, NA))
        cibles = "2027 : %s<br/>2028 : %s" % (_v(i["c27"], i["statut_27"]), _v(i["c28"], i["statut_28"]))
        resp = "Collecte : %s<br/>Validation : %s" % (i["r_collecte"], i["r_valid"])
        rows = [
            ["Intitulé", "<b>%s</b>" % i["intitule"]],
            ["Niveau de résultat", "%s &nbsp;·&nbsp; %s" % (i["niveau"], i.get("type_val", ""))],
            ["Objectif de rattachement", i["objectif"]],
            ["Résultat attendu", i["resultat"]],
            ["Définition", i["definition"]],
            ["Justification", i["justification"]],
            ["Unité", i["unite"]],
            ["Numérateur", i["numerateur"]],
            ["Dénominateur", i["denominateur"]],
            ["Formule", "<b>%s</b>" % _formule(i["formule"])],
            ["Désagrégations", i["desagr"]],
            ["Situation de référence", "%s<br/><font color='#%s' size='6.4'>Source : %s</font>"
             % (_v(i["ref"], i["statut_ref"]), D.GREY_MID, i["src"])],
            ["Cibles 2027 et 2028", cibles],
            ["Cible globale Tech-4", cible_g],
            ["Source de vérification", i["sv"]],
            ["Méthode de collecte", i["methode"]],
            ["Fréquence", i["frequence"]],
            ["Responsabilités", resp],
            ["Limites et biais connus", i["limites"]],
        ]
        d.table(["Rubrique", "Contenu"], [0.20, 0.80], rows,
                size=7.4, repeat_head=True, zebra=True, vcenter=False,
                caption="Fiche %d — <b>%s</b> · %s" % (n, i["code"], i["intitule"]),
                tag="keep")

    # ==================================================================
    # 9. NOTES MÉTHODOLOGIQUES
    # ==================================================================
    d.h1("9", "Notes méthodologiques, limites et points à valider")

    d.h2("1", "Ce que Tech-4 documente et ce qu’il ne documente pas")
    d.table(
        ["Élément", "Statut dans Tech-4", "Conséquence pour le cadre de performance"],
        [0.26, 0.30, 0.44],
        [["Objectif général et objectifs spécifiques", "Documentés et libellés",
          "Repris sans modification"],
         ["Résultats intermédiaires (14)", "Documentés et libellés",
          "Repris sans modification, y compris les libellés les plus longs"],
         ["Indicateurs de l’objectif spécifique 1", "Liste documentée",
          "Repris tels quels ; ils constituent l’essentiel des indicateurs d’effet"],
         ["Indicateurs des objectifs spécifiques 2, 3 et 4",
          "Partiellement documentés : Tech-4 décrit les activités sans toujours nommer l’indicateur",
          "Indicateurs dérivés du libellé des résultats et des activités, signalés comme tels"],
         ["Volumes de livrables", "Documentés (structures, personnes, équipements, campagnes)",
          "Restitués en « cible globale », non ventilés par année"],
         ["Valeurs de référence", "Absentes pour les résultats intermédiaires ; quelques prévalences "
          "provinciales citées comme contexte", "Colonne « référence » renseignée ou marquée « À préciser »"],
         ["Cibles annuelles", "Absentes", "« À préciser » pour les 41 indicateurs"],
         ["Fréquences de collecte", "Partiellement documentées (mensuel, trimestriel, semestriel, ponctuel)",
          "Reprises lorsqu’elles sont citées ; propositions signalées"],
         ["Circuit de validation des données", "Non formalisé au-delà du rôle du responsable S&E/HMIS",
          "Proposé et signalé comme recommandation"],
         ["Désagrégations", "Explicites pour les VBG (zone de santé, sexe, âge) ; implicites ailleurs",
          "Standardisées par proposition"]],
        size=7.5,
        caption="Tableau 6 — Statut documentaire des éléments du cadre de performance")

    d.h2("2", "Limites du cadre de performance")
    d.bullets([
        "<b>Absence de cibles annuelles.</b> Le cadre ne permet pas, en l’état, de juger de l’atteinte des "
        "résultats. Il devient opérationnel dès que les cibles 2027 et 2028 sont arrêtées.",
        "<b>Hétérogénéité de la précision des indicateurs.</b> Les indicateurs de l’objectif spécifique 1 sont "
        "définis par Tech-4 avec leur libellé exact ; ceux des objectifs 2 à 4 sont reconstitués à partir des "
        "activités décrites et comportent une part d’interprétation, signalée dans la rubrique « justification ».",
        "<b>Dénominateurs incertains.</b> Plusieurs indicateurs reposent sur des dénominateurs que Tech-4 ne "
        "chiffre pas (nombre d’entités administratives, nombre d’écoles éligibles, nombre de couples "
        "éducateurs attendus). Ils sont identifiés dans la rubrique « limites ».",
        "<b>Double cible sur les relais communautaires.</b> Tech-4 mentionne 8 314 RECO à couvrir et "
        "4 956 RECO à doter de téléphones ; le cadre retient les deux grandeurs en les distinguant.",
        "<b>Décalage temporel.</b> Tech-4 fixe l’échéance des objectifs au 31 décembre 2023 ; la période "
        "2027–2028 constitue une reprogrammation, sans modification des libellés.",
    ])

    d.h2("3", "Points à valider avant la première revue")
    d.table(
        ["N°", "Point à valider", "Instance de validation", "Échéance proposée"],
        [0.05, 0.47, 0.28, 0.20],
        [["1", "Valeurs de référence des 41 indicateurs", "DPS/PRONANUT et consortium", "Fin T1 2027"],
         ["2", "Cibles 2027 et 2028", "Atelier de validation des cibles", "T1 2027"],
         ["3", "Dénombrements servant de dénominateur", "ECZS et DPS", "T1 2027"],
         ["4", "Indicateurs de performance conditionnant les primes communautaires",
          "Cellule d’achat stratégique", "T1 2027"],
         ["5", "Seuils de qualité des services et de satisfaction", "DPS/PRONANUT", "T2 2027"],
         ["6", "Circuit de validation des données à trois niveaux", "Comité de pilotage", "T1 2027"],
         ["7", "Désagrégations minimales obligatoires", "Comité de pilotage", "T1 2027"],
         ["8", "Règle de calcul des taux d’atteinte pour les indicateurs à sens décroissant",
          "DPS/PRONANUT", "T1 2027"]],
        size=7.8,
        caption="Tableau 7 — Points à valider avant la première revue de performance",
        note="Ces points sont repris dans le rapport de contrôle qualité (livrable 05) et dans l’annexe E du "
             "plan de suivi-évaluation (livrable 02).")

    d.h2("4", "Cohérence avec les autres livrables")
    d.p("Le présent cadre est strictement aligné sur le plan de suivi-évaluation et sur le classeur Excel : "
        "mêmes codes, mêmes intitulés, mêmes définitions, mêmes formules, mêmes références et mêmes cibles. "
        "Les trois documents sont produits à partir du même module de données, ce qui exclut toute divergence "
        "de valeur. Le rapport de contrôle qualité (livrable 05) documente la vérification effectuée.")

    return d
