# -*- coding: utf-8 -*-
"""LIVRABLE 2 — Cadre de Performance 2027-2028 : contenu (modèle de blocs)."""
import data as D

B = []


def add(**kw):
    B.append(kw)


def h2(t):
    add(t="h2", text=t)


def h3(t):
    add(t="h3", text=t)


def p(t, lead=False):
    add(t="p", text=t, lead=lead)


def bul(items):
    add(t="bul", items=items)


def num(items):
    add(t="num", items=items)


def table(caption, num_, header, rows, widths, font=8.5, first_bold=True,
          center=None, total=False, land=False, colors=None):
    add(t="table", caption=caption, num=num_, header=header, rows=rows,
        widths=widths, font=font, first_bold=first_bold, center=center or [],
        total=total, land=land, band=True, colors=colors)


def callout(title, text, icon="✓", fill="EAF3FB", accent="0072CE"):
    add(t="callout", title=title, text=text, icon=icon, fill=fill, accent=accent)


def note(t):
    add(t="note", text=t)


def img(key, caption=None):
    add(t="img", key=key, caption=caption)


def section(n, title, sub=""):
    add(t="section", num=n, title=title, sub=sub)


VERT, ORANGE, ROUGE = "D8EFE2", "FCE9D2", "F8D7D3"

STATUTS = ["Vert", "Vert", "Rouge", "Rouge", "Rouge", "Rouge", "Orange",
           "Vert", "Vert", "Rouge", "Orange", "Orange"]
STAT_COL = {"Vert": VERT, "Orange": ORANGE, "Rouge": ROUGE}

# ====================================================================== COUVERTURE
add(t="cover", data={
    "kicker": "PROJET MULTISECTORIEL DE NUTRITION ET DE SANTÉ (PMNS) · PROVINCE DU KWILU · RDC",
    "title": "Services de Nutrition à Assise Communautaire (NAC) dans la province du Kwilu",
    "subtitle": "Cadre de Performance 2027–2028",
    "consortium": "Consortium SANRU (chef de file) — ICHESS — FONLIV — FDSS",
    "info": [
        ("Maître d'ouvrage", "Ministère de la Santé Publique, Hygiène et Prévention (MSPHP)"),
        ("Bailleur / Unité de gestion", "Projet Multisectoriel de Nutrition et de Santé (PMNS) — UG-PDSS"),
        ("Référence du marché", "DP N° ZR-DRC-MSP-235334-CS-QCBS — Formulaire TECH-4"),
        ("Document de référence", "Plan de Suivi-Évaluation 2027-2028 (Livrable 1), sections 6 et 8"),
        ("Période couverte", "Année 1 : janvier – décembre 2027 · Année 2 : janvier – décembre 2028"),
        ("Version", "1.0 — version soumise pour validation"),
        ("Date de rédaction", "Novembre 2026"),
        ("Auteur", "Responsable S&E/HMIS du consortium, avec l'appui d'un expert senior en santé publique et suivi-évaluation"),
    ],
    "footer": "Ce cadre de performance est la déclinaison opérationnelle et synthétique du Plan de Suivi-Évaluation. "
              "Il en reprend les indicateurs et les cibles sans en modifier la teneur. Toute donnée absente de Tech-4 "
              "est signalée par la mention « [À compléter selon Tech-4] ».",
})

# ====================================================================== SOMMAIRE
add(t="toc", text="")

# ====================================================================== 01. OBJET
section("01", "Objet et mode d'emploi",
        "À quoi sert ce cadre, qui l'utilise et comment il se lit")

p("Le présent Cadre de performance est le document de pilotage du projet. Il condense, en quatre tableaux, "
  "l'information dont le chef de projet, le comité de pilotage et l'UG-PDSS ont besoin pour savoir, à tout "
  "moment, si le projet est sur la bonne voie. Il ne remplace pas le Plan de Suivi-Évaluation : il en extrait "
  "les indicateurs de plus haut niveau et les organise en instrument de décision.", lead=True)

h2("1.1  Ce que contient ce document")
bul(["**Une matrice de performance globale** (section 02) : douze indicateurs clés, rattachés aux objectifs "
     "spécifiques et aux résultats intermédiaires de TECH-4, avec leur valeur de référence, leurs cibles "
     "annuelles, leur seuil d'alerte et leur responsable.",
     "**Un tableau de bord synthétique** (section 03) : la représentation visuelle du positionnement du projet, "
     "avec un code couleur à trois niveaux et des cibles semestrielles permettant un suivi trimestriel.",
     "**Une matrice de risques liée à la performance** (section 04) : les douze risques susceptibles de faire "
     "dévier le projet, leur probabilité, leur impact, la stratégie d'atténuation et l'indicateur d'alerte "
     "précoce associé.",
     "**Un échéancier des jalons** (section 05) : les huit trimestres de mise en œuvre, avec la cible cumulative "
     "attendue à chaque échéance et la revue prévue.",
     "**Les règles de gouvernance** (section 06) : qui met à jour le cadre, à quelle fréquence et selon quelles "
     "modalités."])

h2("1.2  Comment lire les cibles")
p("La même convention que celle du Plan de Suivi-Évaluation est appliquée, afin d'éviter toute ambiguïté sur "
  "l'origine d'un chiffre.")
table("Convention de lecture des cibles et des valeurs", "1",
      ["Marque", "Signification", "Conséquence opérationnelle"],
      [("Aucune", "Cible explicitement chiffrée dans le formulaire TECH-4",
        "La cible est opposable ; tout écart doit être expliqué en revue"),
       ("(b)", "Cible d'alignement sur la référence nationale citée dans TECH-4",
        "La cible de l'année 2 reprend la valeur nationale ; celle de l'année 1 en est le point médian"),
       ("(c)", "Donnée absente de TECH-4",
        "Cible fixée à l'atelier de cadrage de janvier 2027, sur la base de l'enquête de référence"),
       ("n.d.", "Valeur de référence non disponible dans TECH-4",
        "La référence est établie par l'enquête de référence ; aucune cible n'est annoncée avant")],
      [1.9, 7.4, 7.7], font=8.5, center=[0])

h2("1.3  Le code couleur")
p("Le tableau de bord utilise trois couleurs, définies sans ambiguïté afin d'éviter les interprétations "
  "divergentes d'une revue à l'autre.")
table("Définition du code couleur", "2",
      ["Code", "Signification", "Critère d'attribution", "Réponse attendue"],
      [("Vert", "Sur la bonne voie",
        "La valeur atteint au moins 90 % de la cible semestrielle, ou l'indicateur est déjà à 66 % ou plus de sa cible annuelle",
        "Aucune action spécifique ; l'indicateur reste sous surveillance"),
       ("Orange", "Attention requise",
        "La valeur atteint entre 60 % et 90 % de la cible semestrielle, ou la donnée n'est pas encore disponible",
        "Analyse causale en revue trimestrielle ; mesure corrective légère"),
       ("Rouge", "En retard",
        "La valeur est inférieure à 60 % de la cible semestrielle, ou l'indicateur est structurellement bloqué",
        "Plan de redressement obligatoire, avec responsable et échéance")],
      [1.9, 3.4, 7.3, 4.4], font=8.5, center=[0],
      colors={(0, 0): VERT, (1, 0): ORANGE, (2, 0): ROUGE})

h2("1.4  Articulation avec les autres documents")
p("Le cadre de performance s'articule avec trois autres documents du dispositif : le **Plan de Suivi-Évaluation** "
  "(Livrable 1), qui contient les 43 indicateurs, les fiches techniques et le calendrier de collecte ; le "
  "**rapport trimestriel de performance**, qui renseigne le tableau de bord ; et le **plan d'action de "
  "redressement**, qui traduit en décisions les indicateurs passés en orange ou en rouge.")
p("Chacun de ces documents a une fonction distincte, et le cadre de performance ne les duplique pas : il "
  "prélève dans le Plan de Suivi-Évaluation la définition de chaque indicateur, il en extrait les valeurs "
  "observées pour les confronter aux cibles, et il renvoie au rapport trimestriel le soin d'expliquer les "
  "écarts. Une valeur ne doit jamais circuler d'un document à l'autre sans être rattachée à sa source.")
table("Place de chaque document dans le dispositif de pilotage", "3",
      ["Document", "Ce qu'il apporte au cadre de performance", "Fréquence", "Producteur"],
      [["Plan de Suivi-Évaluation (Livrable 1)",
        "Les 43 indicateurs, leurs fiches techniques, les méthodes et le calendrier de collecte : il fixe "
        "la définition de calcul et la source de chaque valeur.",
        "Une fois, puis actualisé en cas de révision", "Équipe S&E"],
       ["Tableau de bord (section 03)",
        "Le positionnement des douze indicateurs clés selon le code couleur, au regard de la cible "
        "semestrielle en cours.",
        "Trimestriel", "Équipe S&E"],
       ["Rapport trimestriel de performance",
        "L'analyse causale des écarts, les mesures correctives proposées et les décisions du comité de "
        "pilotage.",
        "Trimestriel (J+25)", "Coordination du projet"],
       ["Plan d'action de redressement",
        "Les activités, responsables et échéances permettant de ramener sur trajectoire tout indicateur "
        "en rouge.",
        "À chaque indicateur rouge", "Responsable de l'indicateur"]],
      [3.9, 8.1, 2.6, 2.4], font=8.5)
callout("Une règle simple pour les revues",
        "Toute décision prise en revue doit pouvoir se lire dans l'un de ces quatre documents. Une décision "
        "qui ne s'y trouve pas n'a pas de trace, et donc pas de suite. C'est cette discipline, plus que la "
        "précision des chiffres, qui fait la valeur d'un cadre de performance.",
        icon="✓", fill="EAF3FB", accent="0072CE")

# ====================================================================== 02. MATRICE
section("02", "Matrice de performance globale",
        "Douze indicateurs clés, leurs cibles et leurs seuils d'alerte")

add(t="land_start")
h2("2.1  Matrice des indicateurs clés de performance")
p("Les douze indicateurs retenus couvrent les quatre objectifs spécifiques de TECH-4 et le résultat "
  "intermédiaire 4.5 relatif au suivi-évaluation. Ils ont été choisis parce qu'ils sont mesurables avec les "
  "instruments existants, qu'ils sont sensibles à l'action du projet à l'échelle d'un trimestre et qu'ils "
  "couvrent l'ensemble de la chaîne de résultats.", lead=True)

ROWS = []
for k in D.KPIS:
    code = k[0].split(" — ")[0]
    ROWS.append((code, k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8]))

table("Matrice de performance globale du projet (12 KPI)", "4",
      ["Objectif", "Résultat attendu", "Indicateur clé (KPI)", "Référence",
       "Cible 2027", "Cible 2028", "Seuil d'alerte", "Fréquence", "Responsable"],
      ROWS, [1.5, 4.4, 4.6, 1.9, 1.9, 1.9, 2.7, 1.9, 3.4], font=7.8,
      center=[0, 3, 4, 5, 7])


add(t="land_end")

h2("2.2  Lecture de la matrice")
p("Les indicateurs sont rattachés aux quatre objectifs spécifiques de TECH-4 : **OS1** — mise en œuvre des "
  "activités dans les sites communautaires ; **OS2** — sensibilisation aux VBG et prise en charge des "
  "victimes ; **OS3** — soutien aux structures de participation communautaire ; **OS4** — appui au système de "
  "santé pour la qualité des services de nutrition dans les FOSA. La colonne « Résultat attendu » renvoie au "
  "résultat intermédiaire (RI) correspondant.")
p("Trois constats se dégagent de la lecture de cette matrice au démarrage.")
bul(["**Cinq indicateurs partent de zéro.** Les RECO formés, les FARN, les comités locaux de lutte contre les "
     "VBG, les FOSA sans rupture d'intrants et les FOSA dotées en équipements n'ont aucune valeur de départ : "
     "le projet doit construire l'intégralité du résultat. Ces cinq indicateurs sont donc les plus exposés au "
     "risque de retard et doivent faire l'objet d'un suivi mensuel interne, indépendamment de la fréquence de "
     "reporting trimestrielle.",
     "**Trois indicateurs disposent d'un acquis mobilisable.** La couverture des villages en CAC (71 %), la "
     "proportion de CAC disposant d'un plan d'action (16 %) et le nombre de zones rapportant des cas de VBG "
     "(6 sur 10) s'appuient sur des dispositifs existants. Le projet consolide plus qu'il ne crée, ce qui "
     "autorise des cibles de fin d'année 1 plus ambitieuses.",
     "**Deux indicateurs restent sans valeur de référence.** Le taux de prise en charge des enfants MAS référés "
     "et la complétude des données DHIS2 ne sont pas documentés dans TECH-4. Ils seront renseignés par l'enquête "
     "de référence et l'audit initial de qualité des données, au plus tard en mars 2027 ; d'ici là, ils sont "
     "maintenus en orange par convention."])

callout("Règle de gestion des seuils d'alerte",
        "Un indicateur qui franchit son seuil d'alerte deux trimestres consécutifs est inscrit d'office à "
        "l'ordre du jour du comité de pilotage. Cette règle évite que les difficultés persistantes ne se "
        "dissolvent dans la routine des revues.", icon="⚠", fill="FDF1E6", accent="F4A460")

h3("Ce que cette matrice ne dit pas")
p("Douze indicateurs ne résument pas quarante-trois. La matrice retient ceux dont dépend l'atteinte des "
  "objectifs ; elle laisse de côté les indicateurs de processus, les indicateurs de qualité de service "
  "intermédiaires et les mesures désagrégées. Ces derniers restent suivis au titre du Plan de Suivi-Évaluation "
  "et n'apparaissent au tableau de bord que lorsqu'ils éclairent une décision.")
p("Elle ne fixe pas non plus de cible pour les indicateurs marqués (c) : ces cibles dépendront de la mesure de "
  "référence et seront arrêtées en atelier, puis intégrées au cadre par voie de révision. D'ici là, la "
  "matrice indique la valeur attendue en fin d'année 1 pour les indicateurs comparables, à titre de repère de "
  "lecture et non de cible contractuelle.")

# ====================================================================== 03. DASHBOARD
section("03", "Tableau de bord synthétique",
        "Positionnement visuel des indicateurs et cibles semestrielles")

h2("3.1  Positionnement au démarrage")
p("Le tableau ci-dessous présente, pour chaque indicateur, la valeur de référence confrontée à la cible de "
  "l'année 1. La longueur de la jauge mesure le chemin déjà parcouru ; le repère vertical bleu foncé marque la "
  "cible à atteindre.", lead=True)

img("dashboard", "Figure 1. Tableau de bord du projet au démarrage — écart entre la situation de référence et la cible 2027")

note("Le code couleur du graphique exprime le chemin restant à parcourir au démarrage : vert lorsque la "
     "référence couvre déjà au moins deux tiers de la cible, orange entre un tiers et deux tiers, rouge en "
     "deçà du tiers. Il est actualisé à chaque revue trimestrielle.")

h2("3.2  Cibles semestrielles et suivi trimestriel")
p("Les cibles annuelles sont ventilées en cibles semestrielles, de manière à permettre un suivi tous les trois "
  "mois. La ventilation retenue est progressive : elle tient compte du calendrier de montée en charge — les "
  "formations et les dotations se concentrent sur les deux premiers semestres, les effets sur l'usage des "
  "services apparaissent plus tardivement.")

SEM = []
colors = {}
for i, k in enumerate(D.KPIS):
    SEM.append((k[2], k[3], k[9], k[10], k[11], k[12], STATUTS[i]))
    colors[(i, 6)] = STAT_COL[STATUTS[i]]

table("Cibles semestrielles et positionnement des 12 indicateurs clés", "5",
      ["Indicateur clé (KPI)", "Référence", "S1 2027", "S2 2027", "S1 2028", "S2 2028", "Statut initial"],
      SEM, [5.2, 1.8, 1.7, 1.7, 1.7, 1.7, 3.2], font=8,
      center=[1, 2, 3, 4, 5, 6], colors=colors)

p("**Statut initial** : positionnement au démarrage, calculé sur le rapport entre la valeur de référence et la "
  "cible de l'année 1 (vert : au moins deux tiers du chemin déjà parcouru ; orange : entre un tiers et deux "
  "tiers, ou donnée non encore disponible ; rouge : moins d'un tiers). Ce statut est actualisé à chaque revue "
  "trimestrielle.")

h2("3.3  Règles d'actualisation du tableau de bord")
table("Calendrier et responsabilités d'actualisation", "6",
      ["Étape", "Contenu", "Échéance", "Responsable"],
      [("Collecte", "Remontée des données des 10 ZS et des 423 FOSA, saisie et contrôle de premier niveau",
        "J+10 après la fin du trimestre", "ECZS, IT, conseillers de zone"),
       ("Consolidation", "Calcul des 12 KPI, comparaison aux cibles semestrielles, attribution du code couleur",
        "J+20", "Responsable S&E/HMIS"),
       ("Validation", "Revue de cohérence avec les audits de qualité des données et le MAA", "J+25", "Chef de projet"),
       ("Diffusion", "Transmission du tableau de bord à l'UG-PDSS et présentation en revue trimestrielle",
        "J+30", "Chef de projet"),
       ("Décision", "Plan de redressement pour les indicateurs orange et rouge", "Revue trimestrielle", "Comité de pilotage")],
      [2.6, 7.4, 3.4, 3.6], font=8.5)

p("Le délai de trente jours entre la fin du trimestre et la diffusion du tableau de bord n'est pas une marge "
  "de confort : il correspond au temps nécessaire pour que les données des 423 FOSA remontent par les IT et "
  "les BCZS, soient contrôlées, puis confrontées aux constats des audits de qualité. Un tableau de bord "
  "produit plus vite serait un tableau de bord non vérifié.")
note("Le premier exercice complet porte sur le premier trimestre 2027, avec une réserve : l'enquête de "
     "référence n'étant close qu'à la fin mars, les valeurs de référence des indicateurs marqués (b) et (c) "
     "sont renseignées avec le tableau de bord du deuxième trimestre. D'ici là, ces indicateurs figurent au "
     "tableau de bord avec la mention « en attente de vérification » et ne reçoivent pas de code couleur.")

# ====================================================================== 04. RISQUES
section("04", "Matrice de risques liée à la performance",
        "Probabilité, impact, atténuation et indicateurs d'alerte précoce")

add(t="land_start")
h2("4.1  Matrice des risques")
p("Les risques ci-dessous sont ceux qui menacent directement l'atteinte des cibles du cadre de performance. "
  "Ils sont tous documentés dans TECH-4 ou en découlent directement : rupture d'intrants depuis 2019, "
  "enclavement de la province, instabilité des RECO, faible qualité des données, sous-déclaration des VBG, "
  "aléas épidémiques et sécuritaires. Chaque risque est associé à un indicateur d'alerte précoce, distinct de "
  "l'indicateur de performance : il ne mesure pas le résultat, mais la probabilité que ce résultat ne soit pas "
  "atteint.", lead=True)

RISK_ROWS = [(r[0], r[1], r[2], r[3], r[4]) for r in D.RISKS]
rcolors = {}
for i, r in enumerate(D.RISKS):
    rcolors[(i, 1)] = {"Élevée": ROUGE, "Moyenne": ORANGE, "Faible": VERT}.get(r[1], "FFFFFF")
    rcolors[(i, 2)] = {"Majeur": ROUGE, "Modéré": ORANGE, "Mineur": VERT}.get(r[2], "FFFFFF")

table("Matrice de risques liée à la performance du projet", "7",
      ["Risque", "Probabilité", "Impact", "Stratégie d'atténuation", "Indicateur d'alerte précoce"],
      RISK_ROWS, [5.4, 1.8, 1.6, 9.5, 7.4], font=7.2, center=[1, 2], colors=rcolors)
add(t="land_end")

h2("4.2  Hiérarchisation et pilotage des risques")
p("Les douze risques se répartissent en trois niveaux de vigilance, qui déterminent la fréquence de suivi.")
table("Hiérarchisation des risques et fréquence de suivi", "8",
      ["Niveau de vigilance", "Risques concernés", "Fréquence de suivi", "Instance"],
      [("Critique", "Rupture d'intrants ; instabilité des RECO ; faible qualité des données ; situation sécuritaire",
        "Mensuelle", "Chef de projet et comité de pilotage"),
       ("Élevé", "Mouvement du personnel formé ; sous-déclaration des VBG ; arrêt de l'appui aux groupes de soutien ; "
        "biais de mesure et effets saisonniers", "Trimestrielle", "Revue trimestrielle de performance"),
       ("Modéré", "Épidémies ; retard de décaissement ; appropriation communautaire ; coordination multisectorielle",
        "Semestrielle", "Comité de pilotage et revues semestrielles")],
      [3.0, 8.4, 2.4, 3.2], font=8.5, center=[2],
      colors={(0, 0): ROUGE, (1, 0): ORANGE, (2, 0): VERT})

p("**Risque le plus critique : la rupture d'intrants.** TECH-4 indique qu'aucune zone de santé de la province "
  "du Kwilu n'a été approvisionnée en intrants nutritionnels depuis 2019. Ce constat justifie que le taux de "
  "FOSA sans rupture soit à la fois un indicateur de performance et l'objet d'un suivi hebdomadaire des stocks "
  "dans les 250 dépôts aménagés. Un délai de réapprovisionnement supérieur à trente jours déclenche une alerte "
  "formelle auprès de l'UG-PDSS.")

h3("Comment la matrice de risques est tenue à jour")
bul(["**Deux révisions ordinaires par an**, en janvier et en juillet, arrêtées en comité de pilotage. La "
     "probabilité et l'impact de chaque risque sont réexaminés à la lumière des observations du semestre "
     "écoulé ; un risque dont l'indicateur d'alerte précoce s'est déclenché est réévalué d'office.",
     "**Une révision à chaud** dès qu'un risque nouveau apparaît — épidémie, incident sécuritaire, suspension "
     "d'un partenaire — ou qu'un risque sort de la liste. L'ajout se fait en revue trimestrielle, avec un "
     "responsable désigné dans la séance.",
     "**Aucun risque ne sort de la matrice parce qu'il est ancien.** Il en sort lorsqu'il est traité, lorsque "
     "le contexte qui l'a fait naître a disparu, ou lorsque le projet assume explicitement de le porter sans "
     "mesure d'atténuation — décision qui est alors consignée."])
callout("Risque versus hypothèse",
        "Le risque est ce qui peut empêcher d'atteindre une cible ; l'hypothèse est ce que le projet suppose "
        "vrai pour que sa théorie du changement fonctionne. Les deux listes ne se recouvrent pas : la matrice "
        "ci-dessus ne reprend pas les hypothèses critiques du Plan de Suivi-Évaluation, qui relèvent du "
        "raisonnement d'ensemble et non du pilotage trimestriel.",
        icon="■", fill="FDF1E6", accent="F4A460")

# ====================================================================== 05. JALONS
section("05", "Échéancier des jalons de performance",
        "Cibles cumulatives et revues prévues, trimestre par trimestre")

h2("5.1  Jalons trimestriels 2027-2028")
p("Les huit jalons ci-dessous constituent les points de contrôle du projet. À chaque échéance, le chef de "
  "projet atteste de l'atteinte de la cible cumulative devant le comité de pilotage ; un jalon non atteint "
  "déclenche un plan de rattrapage présenté au trimestre suivant.", lead=True)

table("Échéancier des jalons de performance (huit trimestres)", "9",
      ["Trimestre", "Jalon clé", "Cible cumulative", "Revue prévue"],
      [(m[0], m[1], m[2], m[3]) for m in D.MILESTONES],
      [1.9, 5.9, 5.6, 3.6], font=7.8, center=[0])

h2("5.2  Points de non-retour")
p("Trois échéances conditionnent la suite du projet et ne tolèrent aucun glissement.")
bul(["**Fin mars 2027 — fin de l'enquête de référence.** Sans elle, les cibles marquées (c) ne peuvent être "
     "fixées, et le projet avance sans référence mesurée. C'est la seule échéance dont le report compromet "
     "l'ensemble du dispositif de mesure.",
     "**Fin décembre 2027 — achèvement du paquet de première génération.** Les 4 956 RECO formés, les 846 "
     "prestataires formés et la couverture intégrale des 3 188 CAC doivent être acquis à cette date : l'année 2 "
     "est consacrée à l'extension et à la consolidation, non à rattraper l'année 1.",
     "**Septembre 2028 — fin des évaluations thématiques.** Passé cette date, les recommandations ne peuvent "
     "plus être mises en œuvre avant la clôture, ce qui priverait l'évaluation finale d'une partie de sa "
     "matière."])
p("Ces trois dates ne sont pas des objectifs de performance : ce sont des conditions de validité. Un jalon "
  "manqué ne se rattrape pas en accélérant la collecte les mois suivants ; il se rattrape en révisant le "
  "calendrier et en assumant la révision devant le bailleur. C'est pourquoi ils figurent ici, alors qu'ils "
  "n'apparaissent pas dans la matrice de performance.")
add(t="pagebreak")
h3("Que se passe-t-il si un point de non-retour est manqué ?")
num(["**Constat en revue.** Le jalon manqué est constaté à la première revue trimestrielle qui suit l'échéance, "
     "sur la base du même seuil de preuve que les indicateurs : un livrable déposé, une base de données "
     "clôturée, un rapport reçu.",
     "**Analyse d'impact sous quinze jours.** L'équipe S&E établit ce que le retard rend impossible : quelles "
     "cibles ne peuvent plus être tenues, quels indicateurs perdent leur référence, quelles activités de "
     "l'année 2 doivent être décalées.",
     "**Décision explicite du comité de pilotage.** Trois options sont instruites : le maintien du calendrier "
     "avec un plan de rattrapage daté, la révision des cibles concernées, ou le report assumé de l'activité à "
     "l'année suivante. Aucune option n'est retenue par défaut.",
     "**Information de l'UG-PDSS.** Toute révision touchant une cible contractuelle est notifiée par écrit et "
     "consignée dans le rapport trimestriel, avec sa justification."])
table("Options instruites en comité de pilotage lorsqu'un jalon est manqué", "10",
      ["Option", "Ce que cela implique", "Qui décide", "Trace"],
      [["Maintien du calendrier",
        "Un plan de rattrapage daté est adopté ; les activités suivantes sont resserrées sans réduction de "
        "périmètre. Option retenue lorsque le retard est inférieur à un trimestre.",
        "Comité de pilotage, sur proposition du chef de projet",
        "Plan de rattrapage annexé au rapport trimestriel"],
       ["Révision de la cible",
        "La cible annuelle concernée est ramenée à un niveau atteignable et la valeur antérieure reste "
        "documentée. Toute cible contractuelle ne peut être révisée sans accord écrit.",
        "UG-PDSS, sur demande motivée du consortium",
        "Avenant de cible et note de justification"],
       ["Report assumé à l'année 2",
        "L'activité est reprogrammée et son budget redéployé. Les indicateurs qu'elle alimente sont marqués "
        "comme non mesurables sur l'exercice en cours.",
        "Comité de pilotage et UG-PDSS",
        "Reprogrammation budgétaire et note au bailleur"]],
      [3.2, 7.3, 3.3, 3.2], font=8.0)
callout("La règle des trois dates",
        "Un cadre de performance se juge autant sur ce qu'il empêche que sur ce qu'il mesure. En fixant trois "
        "échéances non négociables, le projet se donne les moyens de dire tôt ce qui ne sera pas tenu, plutôt "
        "que de le découvrir à l'évaluation finale.",
        icon="■", fill="EAF3FB", accent="0072CE")

# ====================================================================== 06. GOUVERNANCE
section("06", "Gouvernance du cadre de performance",
        "Rôles, mise à jour et articulation avec le Plan de Suivi-Évaluation")

h2("6.1  Rôles et responsabilités")
GOUV = [
    ("Responsable S&E/HMIS", "Consolide les données, calcule les KPI, attribue le code couleur, produit le tableau de bord",
     "Trimestrielle et à la demande"),
    ("Chef de projet", "Valide le tableau de bord, arbitre les mesures correctives, rend compte à l'UG-PDSS",
     "Trimestrielle"),
    ("Spécialistes techniques", "Vérifient la fiabilité des données de leur domaine et proposent les cibles techniques",
     "Mensuelle"),
    ("Conseillers de zone et ECZS", "Assurent la remontée des données et le premier contrôle de qualité",
     "Mensuelle"),
    ("Comité de pilotage du consortium", "Prend acte de la performance, arbitre les réorientations majeures",
     "Trimestrielle"),
    ("UG-PDSS", "Valide les cibles, reçoit les rapports, autorise les réorientations budgétaires",
     "Trimestrielle et annuelle"),
]
table("Rôles et responsabilités dans la mise à jour du cadre", "11",
      ["Acteur", "Responsabilité", "Fréquence d'intervention"],
      GOUV, [4.2, 9.6, 3.2], font=8.5)

h2("6.2  Règles de mise à jour")
num(["**Les indicateurs ne changent pas en cours d'année.** Un indicateur ne peut être retiré ou remplacé "
     "qu'avec l'accord écrit de l'UG-PDSS, sur proposition motivée du comité de pilotage.",
     "**Les cibles ne se révisent qu'à deux moments.** À l'issue de l'enquête de référence (mars 2027) pour les "
     "cibles marquées (c), et à l'issue de l'évaluation à mi-parcours (octobre 2027) pour un ajustement "
     "argumenté des cibles de l'année 2.",
     "**Le code couleur est calculé, non négocié.** Il résulte de l'application mécanique du critère de la "
     "section 1.3 ; un désaccord sur le statut se règle par la vérification de la donnée, non par la discussion "
     "du seuil.",
     "**Chaque version du cadre est archivée.** Les versions successives sont conservées avec leur date et le "
     "motif de la révision, ce qui permet de reconstituer l'historique de la performance du projet."])

h2("6.3  Ce que ce cadre ne remplace pas")
p("Le Cadre de performance est un instrument de pilotage, non un dispositif de preuve. Il ne contient ni les "
  "définitions complètes des indicateurs, ni les fiches techniques, ni le calendrier de collecte, ni les "
  "modalités d'évaluation : ces éléments figurent dans le Plan de Suivi-Évaluation, auquel il renvoie "
  "systématiquement. En cas de divergence entre les deux documents, le Plan de Suivi-Évaluation prévaut.")

callout("Trois décisions attendues pour rendre ce cadre opérationnel",
        "1) Validation des douze indicateurs et de leurs cibles par l'UG-PDSS ; 2) Confirmation du calendrier "
        "d'actualisation (J+10, J+20, J+25, J+30) avec les ECZS ; 3) Désignation formelle du point focal "
        "performance au sein de chaque équipe cadre de zone.",
        icon="▶")


def blocks():
    return B
