# -*- coding: utf-8 -*-
"""LIVRABLE 1 — Plan de Suivi-Évaluation 2027-2028 : contenu (modèle de blocs)."""
import data as D

B = []


def add(*args, **kw):
    B.append(dict(*args, **kw))


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


def table(caption, num_, header, rows, widths, font=9, first_bold=False,
          center=None, total=False, land=False, band=True):
    add(t="table", caption=caption, num=num_, header=header, rows=rows,
        widths=widths, font=font, first_bold=first_bold, center=center or [],
        total=total, land=land, band=band)


def callout(title, text, icon="✓", fill="EAF3FB", accent="0072CE"):
    add(t="callout", title=title, text=text, icon=icon, fill=fill, accent=accent)


def note(t):
    add(t="note", text=t)


def img(key, caption=None):
    add(t="img", key=key, caption=caption)


def section(n, title, sub=""):
    add(t="section", num=n, title=title, sub=sub)


# ====================================================================== 1. COUVERTURE
add(t="cover", data={
    "kicker": "PROJET MULTISECTORIEL DE NUTRITION ET DE SANTÉ (PMNS) · PROVINCE DU KWILU · RDC",
    "title": "Services de Nutrition à Assise Communautaire (NAC) dans la province du Kwilu",
    "subtitle": "Plan de Suivi-Évaluation 2027–2028",
    "consortium": "Consortium SANRU (chef de file) — ICHESS — FONLIV — FDSS",
    "info": [
        ("Maître d'ouvrage", "Ministère de la Santé Publique, Hygiène et Prévention (MSPHP)"),
        ("Bailleur / Unité de gestion", "Projet Multisectoriel de Nutrition et de Santé (PMNS) — UG-PDSS"),
        ("Référence du marché", "DP N° ZR-DRC-MSP-235334-CS-QCBS — Formulaire TECH-4"),
        ("Document source", "Tech-4 : approche, méthodologie et programme de travail du Consultant (base unique et exclusive)"),
        ("Période couverte", "Année 1 : janvier – décembre 2027 · Année 2 : janvier – décembre 2028"),
        ("Version", "1.0 — version soumise pour validation"),
        ("Date de rédaction", "Novembre 2026"),
        ("Auteur", "Responsable S&E/HMIS du consortium, avec l'appui d'un expert senior en santé publique et suivi-évaluation"),
    ],
    "footer": "Logo du bailleur : [à confirmer — non disponible dans Tech-4]. "
              "Document établi sur la base exclusive du formulaire TECH-4 ; toute donnée absente du document source est signalée "
              "par la mention « [À compléter selon Tech-4] ».",
})

# ====================================================================== 2. SOMMAIRE
add(t="toc", text="")

# ====================================================================== 3. ACRONYMES
section("03", "Sigles, acronymes et abréviations",
        "Vocabulaire de référence commun aux deux livrables du dispositif S&E")

p("Les sigles ci-dessous sont ceux employés dans le formulaire TECH-4 et dans le présent plan. "
  "Ils constituent le vocabulaire de référence pour l'ensemble des outils de collecte, des rapports "
  "et des échanges avec l'UG-PDSS, la DPS du Kwilu et le PRONANUT.", lead=True)

acro_rows = [(a, b) for a, b in D.ACRONYMES if a != "HCG"]
half = (len(acro_rows) + 1) // 2
rows = []
for i in range(half):
    left = acro_rows[i]
    right = acro_rows[i + half] if i + half < len(acro_rows) else ("", "")
    rows.append((left[0], left[1], right[0], right[1]))
table("Sigles et acronymes", "1",
      ["Sigle", "Signification", "Sigle", "Signification"],
      rows, [2.1, 6.4, 2.1, 6.4], font=8.5, first_bold=True)

# ====================================================================== 4. RÉSUMÉ EXÉCUTIF
section("04", "Résumé exécutif",
        "Ce qu'il faut retenir du dispositif de suivi-évaluation 2027-2028")

p("Le présent Plan de Suivi-Évaluation (S&E) couvre la mise en œuvre des services de Nutrition à Assise "
  "Communautaire (NAC) confiée au consortium SANRU-ICHESS-FONLIV-FDSS dans dix zones de santé de la province "
  "du Kwilu, sur la période 2027-2028. Il est adossé, sans exception, au formulaire TECH-4 qui constitue sa "
  "source unique et exclusive : objectifs, résultats intermédiaires, activités, cibles, zones d'intervention, "
  "populations bénéficiaires et parties prenantes y sont repris à l'identique.", lead=True)

p("**Ce que le dispositif doit mesurer.** Le projet poursuit un objectif général — s'attaquer aux principaux "
  "déterminants du retard de croissance chez les enfants de moins de deux ans — décliné en quatre objectifs "
  "spécifiques (services communautaires, VBG/EAS/HS, participation communautaire, système de santé) et "
  "quatorze résultats intermédiaires. Le plan traduit cette architecture en **43 indicateurs** répartis en "
  "trois indicateurs d'impact, dix-huit indicateurs de résultat, vingt indicateurs d'extrant et deux "
  "indicateurs de processus, chacun doté d'une définition, d'un numérateur et d'un dénominateur, d'une valeur "
  "de référence, de cibles annuelles, d'une fréquence, d'une source et d'un responsable nommé.")

p("**Comment les données seront produites.** Le dispositif articule quatre sources complémentaires : "
  "(i) la **collecte de routine** — registres des RECO, cahiers des CAC et CODESA, registres des FOSA, "
  "saisie DHIS2 ; (ii) les **enquêtes périodiques** — enquête de référence puis enquêtes SMART, CAP et de "
  "fonctionnalité des structures communautaires ; (iii) le **Monitorage Amélioré pour l'Action (MAA)** "
  "trimestriel, adossé au cadre des déterminants de la couverture de Tanahashi ; (iv) le **Third Party "
  "Monitoring** indépendant et les audits de qualité des données. Ces quatre flux convergent vers le "
  "DHIS2 comme plateforme nationale de référence, et vers la DPS du Kwilu et le PRONANUT comme destinataires "
  "institutionnels.")

p("**Comment les résultats seront utilisés.** Le plan organise huit revues trimestrielles de performance, "
  "quatre revues semestrielles de la nutrition sous l'égide du Gouverneur et du Ministre provincial de la "
  "Santé, une évaluation à mi-parcours au troisième trimestre 2027 et une évaluation finale au quatrième "
  "trimestre 2028 conduite selon les six critères du CAD de l'OCDE. Chaque revue se conclut par un plan "
  "d'action de redressement daté et attribué, dont la mise en œuvre est elle-même suivie.")

p("**Ce que coûtera le dispositif.** L'enveloppe de suivi-évaluation est fixée à **7 % du budget total du "
  "projet**, conformément à la fourchette de 5 à 10 % recommandée pour les projets financés par des bailleurs "
  "internationaux. Sa répartition détaillée par activité figure à la section 11. L'assiette monétaire reste "
  "à extraire de Tech-4, qui ne comporte aucune ligne budgétaire chiffrée : elle sera renseignée dès la "
  "notification du marché et validée par l'UG-PDSS.")

callout("Trois décisions structurantes sont attendues de la partie prenante",
        "1) Validation du présent plan et de son cadre de performance avant le démarrage de la collecte ; "
        "2) Arbitrage sur les cibles marquées (c) — à compléter dès la disponibilité de l'enquête de référence ; "
        "3) Confirmation de l'enveloppe de 7 % et de son assiette budgétaire.",
        icon="▶")

# ====================================================================== 5. INTRODUCTION
section("05", "Introduction et contexte",
        "Contexte sanitaire, justification, objectifs et périmètre du projet")

h2("5.1  Contexte sanitaire et nutritionnel de la province du Kwilu")
p("La malnutrition menace gravement la santé et le développement mondial : elle affecte une personne sur "
  "trois sur la planète. En République Démocratique du Congo, la situation demeure préoccupante malgré les "
  "efforts consentis au cours des dernières décennies. Le formulaire TECH-4 documente une situation "
  "provinciale qui situe le Kwilu systématiquement au-dessus de la moyenne nationale sur les principaux "
  "indicateurs nutritionnels.")
p("Près de la moitié des enfants de moins de cinq ans de la province souffrent d'un retard de croissance "
  "(47 % contre 42 % au niveau national), 34,8 % présentent une insuffisance pondérale, et seuls 23 % des "
  "enfants de 36 à 59 mois atteignent le développement attendu dans au moins trois domaines "
  "(lecture-calcul-physique, socio-affectif, apprentissage). Les pratiques d'alimentation du nourrisson et du "
  "jeune enfant sont en retrait : 29,2 % seulement des enfants sont initiés à l'allaitement dans l'heure "
  "suivant la naissance (46,9 % au national), 32,7 % bénéficient d'un allaitement maternel exclusif à six "
  "mois (53,5 % au national) et 18 % seulement reçoivent une alimentation de complément adéquate en qualité, "
  "quantité et fréquence.")

CTX = [
    ("Retard de croissance (enfants < 5 ans)", "47 %", "42 %", "MICS-Palu 2017-2018"),
    ("Insuffisance pondérale (enfants < 5 ans)", "34,8 %", "—", "MICS-Palu 2017-2018"),
    ("Initiation précoce à l'allaitement (< 1 h)", "29,2 %", "46,9 %", "MICS-Palu 2017-2018"),
    ("Allaitement maternel exclusif à 6 mois", "32,7 %", "53,5 %", "MICS-Palu 2017-2018"),
    ("Alimentation de complément adéquate (6–23 mois)", "18 %", "—", "MICS-Palu 2017-2018"),
    ("Femmes enceintes avec au moins 4 CPN", "24,3 %", "42,9 %", "MICS-Palu 2017-2018"),
    ("Ménages avec point de lavage des mains (eau + savon)", "18 %", "—", "MICS-Palu 2017-2018"),
    ("Accès à une source améliorée d'eau de boisson", "29 %", "—", "MICS-Palu 2017-2018"),
    ("Insécurité alimentaire sévère", "49,9 %", "43,7 %", "IPC 2021-2022"),
    ("Insécurité alimentaire modérée à sévère", "67,5 %", "65,5 %", "IPC 2021-2022"),
    ("Population vivant avec moins de 1,90 USD par jour", "93,2 %", "74,7 %", "Enquête nationale"),
    ("Malnutrition aiguë globale (dépistage RECO)", "> 8 %", "8 %", "Rapport DPS/PRONANUT 2020"),
    ("Couverture des villages en CAC", "71 %", "—", "Cartographie DPS Kwilu 2021"),
    ("CAC ayant tenu toutes leurs réunions mensuelles", "53,6 %", "—", "DHIS2 2021"),
    ("CAC disposant d'un plan d'action communautaire", "16 %", "30 %", "PSNSC 2019-2022"),
]
table("Valeurs de référence du contexte nutritionnel et sanitaire (Kwilu)",
      "2", ["Indicateur", "Kwilu", "National", "Source citée dans Tech-4"],
      CTX, [7.6, 2.4, 2.2, 4.8], font=8.5, center=[1, 2])

p("Ces déterminants se combinent : mauvaise qualité de l'alimentation, insécurité alimentaire aiguë, "
  "prévalences élevées des maladies infantiles (paludisme, diarrhée, infections respiratoires aiguës), "
  "épidémies de rougeole et de choléra, conditions d'hygiène dégradées, très faible couverture d'accès à l'eau "
  "potable, enfin effets de la situation sécuritaire. La province est par ailleurs la plus peuplée de "
  "l'ancienne province du Bandundu, avec une économie essentiellement agricole de subsistance, un élevage peu "
  "développé et des zones de production enclavées.")

h2("5.2  Justification du projet")
p("Le Kwilu fait partie des neuf provinces les plus touchées par la pauvreté : 93,2 % de la population vit "
  "avec moins de 1,90 USD par jour, contre 74,7 % au niveau national. Selon l'IPC 2021-2022, plusieurs de ses "
  "zones de santé se trouvent dans une situation nutritionnelle sérieuse. TECH-4 identifie quatre facteurs "
  "limitant l'accès, l'utilisation et la qualité des services : l'insuffisance de prestataires communautaires "
  "formés en NAC — la dernière formation date de quatre ans et n'a ciblé que la seule zone de santé de "
  "Mosango —, l'application isolée ou partielle du paquet d'interventions (PCIMA et ANJE introduites dans "
  "Kikwit Nord en 2015, Djuma en 2016, puis les autres zones en 2017-2018), l'absence d'approvisionnement en "
  "intrants nutritionnels depuis 2019, et la faiblesse des mécanismes de redevabilité communautaire.")
p("La justification du projet tient donc moins à l'identification de nouveaux besoins qu'à la nécessité de "
  "passer d'interventions dispersées à un **paquet complet et intégré** — NAC, PCIMA, ANJE, CPSr — porté "
  "simultanément par la communauté et par les formations sanitaires, dans une logique de couverture totale "
  "des 3 188 villages et des 250 aires de santé des dix zones ciblées.")

h2("5.3  Objectif général et objectifs spécifiques (verbatim TECH-4)")
callout("Objectif général (citation de TECH-4)",
        "« Contribuer efficacement à la réalisation de l'objectif général du Projet Multisectoriel de "
        "Nutrition et de Santé (PMNS) qui est celui de s'attaquer aux principaux déterminants du retard de "
        "croissance chez les enfants de moins de deux ans grâce à des actions multisectorielles, "
        "complémentaires, ciblées et fondées sur des données probantes et des pratiques éprouvées. »",
        icon="★", fill="EAF3FB", accent="0072CE")

OS = [
    ("OS1", "Assurer la mise en œuvre des activités dans les sites communautaires conformément aux objectifs "
            "établis et convenus (en termes de qualité et de couverture) pour améliorer l'accès, l'utilisation "
            "et la qualité d'un ensemble de services communautaires de nutrition et de santé."),
    ("OS2", "Sensibiliser sur les violences basées sur le genre et développer un système de prestation de "
            "services pour la prise en charge des victimes de la violence sexuelle et sexiste."),
    ("OS3", "Soutenir les structures de participation communautaire au niveau des communautés et des Zones de "
            "Santé afin d'améliorer la gestion et la mise en œuvre des services de nutrition et de santé "
            "communautaires."),
    ("OS4", "Appuyer le système de santé dans l'amélioration, l'utilisation et de la qualité des services de "
            "nutrition dans les FOSA, selon les normes et standards nationaux."),
]
table("Objectifs spécifiques du projet (libellés TECH-4)", "3",
      ["Code", "Objectif spécifique"], OS, [1.6, 15.4], font=9, first_bold=True)

h2("5.4  Périmètre, populations bénéficiaires et parties prenantes")
p("Le projet couvre **dix zones de santé** réparties dans cinq territoires et une ville : Sia (Bagata), "
  "Djuma (Bulungu), Gungu, Kingandu (Gungu), Kimputu (Idiofa), Kikwit Nord (Kikwit), Moanza, Mosango, "
  "Pay Kongila et Yasa Bonga (Masi-Manimba). La ville de Bandundu, chef-lieu de province, n'abrite aucune "
  "des dix zones mais accueille un sous-bureau du consortium pour des raisons stratégiques.")

table("Répartition géographique des zones de santé ciblées", "4",
      ["Territoire", "Zone de santé", "Aires de santé", "Villages", "CAC installées", "Ménages", "RECO attendus"],
      [(t, z, str(a), str(v), str(c), f"{m:,}".replace(",", " "), f"{r:,}".replace(",", " "))
       for (t, z, a, v, c, m, r) in D.ZS_DETAIL] +
      [("Total", "10 ZS", "250", "3 188", "2 250", "415 695", "8 314")],
      [3.0, 3.2, 2.2, 2.2, 2.4, 2.2, 2.4], font=8.5, center=[2, 3, 4, 5, 6], total=True)

p("**Populations ciblées.** Les cibles directes sont les femmes enceintes, les femmes allaitantes, les "
  "enfants de moins de cinq ans (avec une attention particulière aux moins de deux ans, dans le cadre des "
  "mille premiers jours) et les adolescents. TECH-4 étend explicitement le ciblage aux groupes qui "
  "influencent l'état nutritionnel de l'enfant : grands-mères, pères et maris, chefs traditionnels, chefs "
  "religieux, guérisseurs traditionnels, RECO et prestataires de soins.")
p("**Parties prenantes.** La mise en œuvre associe la Division Provinciale de la Santé du Kwilu et le "
  "PRONANUT, les dix équipes cadres de zone de santé et leurs bureaux centraux, les 250 CODESA et 10 UCODESA, "
  "les 3 188 CAC, les 423 formations sanitaires, l'UG-PDSS et le MSPHP, les partenaires techniques "
  "(Fonds mondial / CORDAID / FDSS, UNFPA, PNSR), les clusters Nutrition, WASH et Sécurité alimentaire, une "
  "ONG spécialisée dans la prise en charge des VBG, l'École de Santé Publique de Kinshasa, IMA World Health "
  "et Save the Children, enfin les autorités politico-administratives, coutumières et religieuses.")

h2("5.5  Objet, approche et structure du plan")
p("Le présent document constitue le plan de suivi-évaluation prévu par le résultat intermédiaire 4.5 de "
  "TECH-4, qui engage le consortium à élaborer un plan de S&E, à en assurer le suivi périodique par des "
  "revues internes, à appuyer la production et le feedback des rapports de terrain et à soumettre les "
  "rapports mensuels, trimestriels et annuels à l'UG-PDSS.")
p("Sa construction repose sur quatre partis pris méthodologiques :")
num(["**Fidélité au document source.** Aucun objectif, résultat, indicateur ou activité n'est introduit s'il "
     "ne découle pas directement de TECH-4. Les cibles chiffrées sont celles du document ; à défaut, la "
     "mention « [À compléter selon Tech-4] » est employée.",
     "**Traçabilité de chaque indicateur.** Chaque indicateur est rattaché à un objectif spécifique et à un "
     "résultat intermédiaire identifiés, ce qui permet de reconstituer le chemin entre une donnée de terrain "
     "et un engagement contractuel.",
     "**Utilité opérationnelle.** Le plan est conçu pour être utilisé par les équipes de zone et les "
     "partenaires, non pour être archivé : il privilégie des indicateurs mesurables avec les instruments "
     "existants et un calendrier de collecte compatible avec les routines du SNIS.",
     "**Redevabilité et apprentissage.** Le dispositif organise la restitution des résultats aux communautés "
     "et aux autorités, conformément au principe de redevabilité posé par TECH-4, et la capitalisation "
     "systématique des leçons apprises."])
p("Le plan s'organise en douze sections : la présente introduction ; le cadre logique (section 6) ; la "
  "théorie du changement (section 7) ; le système de suivi (section 8) ; le système d'évaluation (section 9) ; "
  "les mécanismes de redevabilité et d'apprentissage (section 10) ; le budget du S&E (section 11) ; les "
  "annexes techniques (section 12). Le **Cadre de Performance** constitue le second livrable : il en est la "
  "declinaison opérationnelle et synthétique, destinée au pilotage trimestriel.")

# ====================================================================== 6. CADRE LOGIQUE
section("06", "Cadre logique du projet",
        "Matrice de la chaîne de résultats, indicateurs, sources de vérification et hypothèses")

add(t="land_start")
h2("6.1  Matrice du cadre logique")
p("Le formulaire TECH-4 annonce un cadre logique dont la matrice n'est pas reproduite dans le corps du "
  "document. Le cadre logique ci-dessous est donc **reconstruit** à partir des objectifs spécifiques, des "
  "quatorze résultats intermédiaires et des cibles chiffrées qui y figurent. Chaque énoncé est une reprise "
  "de TECH-4 ; les indicateurs objectivement vérifiables (IOV) renvoient aux fiches de la section 8.1.", lead=True)

CL = [
    ("Impact",
     "Réduction du retard de croissance et de la mortalité liée à la malnutrition chez les enfants de moins de "
     "deux ans dans la province du Kwilu (objectif général du PMNS).",
     "I-01 Prévalence du retard de croissance (0–59 mois) : 47 % → tendance à la baisse\n"
     "I-02 Prévalence de l'insuffisance pondérale : 34,8 %\n"
     "I-03 Prévalence de la MAG : > 8 %",
     "Enquêtes SMART ; EDS-MICS ; DHIS2/SNSAP ; rapports PRONANUT",
     "Stabilité macro-économique et sécuritaire ; absence de choc nutritionnel majeur ; contribution attribuable au projet et non mesurée isolément"),

    ("Effet — OS1",
     "Accès, utilisation et qualité améliorés d'un ensemble de services communautaires de nutrition et de santé "
     "dans les 250 aires de santé des 10 ZS.",
     "R-01 Taux de prise en charge des MAS référés ≥ 80 %\nR-02 30 FARN fonctionnels\nP-01 8 314 RECO formés\n"
     "P-04 3 188 CAC fonctionnelles",
     "Registres communautaires ; DHIS2 ; MAA ; rapports de supervision ; enquête de référence",
     "Les communautés adhèrent aux services ; les RECO restent en poste ; les intrants sont disponibles"),

    ("Produit — RI 1.1",
     "Accès et utilisation améliorés d'un ensemble de services communautaires de nutrition et de santé grâce à la "
     "mise en œuvre des activités dans les sites communautaires des 10 ZS ciblées.",
     "P-01 RECO formés (4 956 puis 8 314)\nP-20 VAD réalisées\nX-01 Villages couverts par une CAC : 71 % → 100 %",
     "Fiches de présence ; cahiers RECO ; tablettes ODK ; DHIS2",
     "Les villages restent accessibles ; les RECO disposent de vélos et d'outils"),

    ("Produit — RI 1.2",
     "Mise en place et documentation des approches innovantes pour renforcer la lutte durable contre la "
     "malnutrition aiguë (PB-Famille, FARN, modèle IMA/SANRU).",
     "R-02 30 FARN opérationnels dans 30 villages (Yasa Bonga, Kingandu)\nR-05 Alimentation de complément adéquate",
     "Rapports FARN ; fiches de suivi anthropométrique ; documentation des innovations",
     "Les aliments locaux 4 étoiles sont disponibles ; les mères adhèrent aux démonstrations culinaires"),

    ("Produit — RI 1.3",
     "Qualité améliorée de l'ensemble des services communautaires : prestataires formés, sites dotés, stocks "
     "disponibles, mesures de prévention des infections appliquées.",
     "P-06 423 FOSA dotées\nR-14 FOSA sans rupture d'intrants\nP-16 supervisions et accompagnements (4 020/an)",
     "Bons de livraison ; fiches de stock ; rapports de supervision formative ; MAA",
     "La chaîne d'approvisionnement fonctionne ; les superviseurs sont recrutés à temps"),

    ("Effet — OS2",
     "Communautés sensibilisées et système de prestation de services de prise en charge des survivantes de "
     "violences sexuelles et sexistes renforcé dans les 10 ZS.",
     "R-10 Survivantes avec PEC holistique : 1,9 % → ≥ 50 %\nR-11 10 ZS rapportant des cas VBG\nP-13 10 comités locaux actifs",
     "DHIS2 ; registres VBG ; rapports de l'ONG spécialisée ; sous-cluster VBG",
     "Les survivantes osent dénoncer ; la confidentialité est garantie ; les kits PEP sont disponibles"),

    ("Produit — RI 2.1",
     "Comités locaux de lutte contre les VBG/EAS/HS mis en place et actifs dans les 10 ZS.",
     "P-13 Nombre de comités actifs (10)\nNombre de réunions trimestrielles tenues",
     "PV de réunion ; arrêtés de mise en place ; rapports de comités",
     "Les autorités politico-administratives soutiennent les comités"),

    ("Produit — RI 2.2",
     "Communautés sensibilisées et engagées dans la lutte contre les VBG.",
     "P-11 2 500 jeunes pairs-éducateurs formés\nNombre de séances de sensibilisation et d'émissions radio",
     "Rapports d'activité ; rapports de monitorage des radios ; enquête CAP",
     "Les normes sociales évoluent ; les leaders sont engagés"),

    ("Produit — RI 2.3",
     "Système de prestation de services de prise en charge des survivantes de violences sexuelles renforcé.",
     "P-12 60 formateurs et prestataires formés\nP-14 6 FOSA dotées en kits PEP\nSystème de référencement fonctionnel dans chaque ZS",
     "Rapports de formation ; fiches de stock PEP ; fiches de référencement",
     "Le référencement est rapide et sécurisé ; les ONG partenaires assurent les volets psychosocial et juridique"),

    ("Effet — OS3",
     "Structures de participation communautaire (CAC, CODESA, UCODESA) organisées, fonctionnelles et dotées d'un "
     "leadership local renforcé dans les 10 ZS.",
     "P-04 3 188 CAC\nP-05 250 CODESA et 10 UCODESA\nR-12 CAC tenant leurs réunions mensuelles\nR-13 CAC avec plan d'action",
     "Cartographie DPS ; DHIS2 ; plans d'action communautaires ; BCP",
     "Les chefs de village exercent leur leadership ; les indemnités de performance sont payées"),

    ("Produit — RI 3.1",
     "Organisation et fonctionnement des structures de participation communautaire renforcés.",
     "R-12 Proportion de CAC fonctionnelles\nTaux de tenue des réunions de monitorage (CAC, CODESA, UCODESA)",
     "Canevas de monitorage ; rapports CODESA ; MAA",
     "Les membres des CAC sont disponibles et formés"),

    ("Produit — RI 3.2",
     "Leadership et capacités managériales locales des structures de participation communautaire renforcés.",
     "R-13 CAC disposant d'un plan d'action : 16 % → 30 %\nNombre de sessions de renforcement des capacités",
     "Plans d'action communautaires ; rapports de formation ; BCP",
     "Les plans sont réellement mis en œuvre et suivis"),

    ("Produit — RI 3.3",
     "Coordination, collaboration multisectorielle et mécanismes de suivi des interventions renforcés.",
     "Nombre de réunions de cadre de concertation tenues\nP-17 40 sessions de MAA par an",
     "Comptes rendus de réunion ; rapports de revues ; bulletins trimestriels",
     "Les partenaires participent régulièrement ; les décisions sont suivies d'effet"),

    ("Effet — OS4",
     "Offre, utilisation et qualité des services de nutrition améliorées dans les 423 formations sanitaires des "
     "10 ZS, conformément aux normes et standards nationaux.",
     "R-15 FOSA avec personnel formé PCIMA : 27 % → 100 %\nR-06 Femmes avec ≥ 4 CPN : 24,3 % → 42,9 %\nR-16 Taux de fréquentation CPSr",
     "DHIS2 ; registres FOSA ; MAA ; évaluations de qualité des soins",
     "Les prestataires restent en poste ; les FOSA appliquent la tarification forfaitaire"),

    ("Produit — RI 4.1",
     "Offre et utilisation des services de nutrition dans les 423 FOSA des 10 ZS améliorées (PCIMA, CPSr, "
     "CPN/CPoN, ANJE).",
     "P-06 423 FOSA dotées\nP-19 5 076 démonstrations culinaires/an\nR-07 100 % des femmes avec ≥ 90 comprimés FAF",
     "Registres UNTA/UNTI, CPSr et CPN ; DHIS2 ; rapports de supervision",
     "Les intrants sont disponibles en continu ; les femmes fréquentent les services"),

    ("Produit — RI 4.2",
     "Qualité des services de nutrition dans les 423 FOSA améliorée (compétences, infrastructures, gestion des "
     "intrants).",
     "P-02 846 prestataires formés\nP-07 10 UNTI réhabilitées et 250 dépôts aménagés\nR-14 FOSA sans rupture",
     "Rapports de formation ; PV de réception des travaux ; fiches de stock",
     "Les travaux sont réalisés dans les délais ; les marchés sont passés à temps"),

    ("Produit — RI 4.3",
     "Suivi et coordination des interventions nutritionnelles à tous les niveaux du système de santé renforcés.",
     "P-18 20 sites sentinelles fonctionnels\nNombre de revues provinciales et zonales tenues",
     "Bulletins SNSAP ; rapports de revues ; comptes rendus de cluster",
     "Les données circulent de la périphérie vers la province"),

    ("Produit — RI 4.4",
     "Mise en œuvre des activités de nutrition dans les 10 ZS de la province du Kwilu assurée (bureaux, "
     "personnel, logistique).",
     "Taux d'exécution du plan de travail annuel\nTaux de couverture des 10 ZS par les visites de coordination (180/an)",
     "Rapports d'avancement ; plan de travail annuel ; rapports de mission",
     "Le financement est décaissé à temps"),

    ("Produit — RI 4.5",
     "Système de suivi-évaluation, de redevabilité et d'apprentissage des activités de nutrition dans les 10 ZS "
     "assuré.",
     "X-02 100 % des rapports périodiques transmis à temps\nP-17 40 sessions de MAA/an\n43 indicateurs renseignés",
     "Plan de S&E ; rapports mensuels, trimestriels et annuels ; rapports d'évaluation",
     "Les équipes S&E sont dotées ; les partenaires transmettent leurs données"),
]

table("Cadre logique du projet — matrice reconstruite à partir de TECH-4", "5",
      ["Niveau d'intervention", "Énoncé (TECH-4)", "Indicateurs objectivement vérifiables",
       "Sources de vérification", "Hypothèses / Risques"],
      CL, [3.3, 7.6, 6.4, 4.5, 3.9], font=8, first_bold=True)

add(t="land_end")

h2("6.2  Lecture du cadre logique")
p("La matrice se lit de bas en haut : les produits (quatorze résultats intermédiaires) conditionnent les "
  "quatre effets (objectifs spécifiques), qui concourent ensemble à l'impact. Trois points méritent "
  "l'attention du lecteur.")
bul(["**L'impact n'est pas mesuré en attribution mais en contribution.** TECH-4 précise que l'impact du projet "
     "ne sera pas analysé au cours de l'évaluation finale, une étude plus approfondie étant nécessaire. Les "
     "indicateurs d'impact sont donc suivis en tendance, à partir des enquêtes SMART et du SNSAP, et non "
     "rattachés à une cible contractuelle.",
     "**Deux niveaux d'effets sont mesurés simultanément.** L'objectif spécifique 1 (services communautaires) "
     "et l'objectif spécifique 4 (formations sanitaires) portent la même ambition de couverture ; leur "
     "enchaînement — la communauté dépiste et réfère, la FOSA confirme et traite — constitue le principal "
     "mécanisme causal du projet et doit être suivi comme tel.",
     "**Les hypothèses sont vérifiables.** Chaque hypothèse de la colonne de droite correspond à un risque "
     "documenté dans la matrice de risques du Cadre de performance, avec un indicateur d'alerte précoce "
     "associé."])

p("**Ce que le cadre logique permet de décider.** La matrice n'est pas un document d'archive : elle sert de "
  "grille de lecture à trois moments du cycle de gestion. En **revue trimestrielle**, elle permet de "
  "distinguer un retard de produit — une formation non réalisée, une dotation non livrée — d'un retard "
  "d'effet, qui se manifeste plus tard et relève d'une autre réponse. En **évaluation à mi-parcours**, elle "
  "fournit la trame des questions évaluatives : chaque hypothèse de la dernière colonne devient une question "
  "à tester sur le terrain. En **évaluation finale**, elle constitue la référence pour apprécier l'efficacité, "
  "puisque chaque énoncé de résultat y est associé à des indicateurs et à des sources de vérification "
  "explicitement identifiés.")
p("Deux précautions d'usage méritent d'être rappelées. D'une part, la colonne des hypothèses ne se lit pas "
  "comme une liste de vœux : chaque hypothèse est associée à un risque documenté et à un indicateur d'alerte "
  "précoce, ce qui permet de savoir *quand* l'hypothèse cesse de tenir. D'autre part, le cadre logique ne dit "
  "rien des délais : c'est le chronogramme de la section 8.2 qui porte la dimension temporelle, et les deux "
  "documents doivent être lus ensemble lors des revues.")

# ====================================================================== 7. THÉORIE DU CHANGEMENT
section("07", "Théorie du changement",
        "Du modèle EDO de TECH-4 à la chaîne de résultats du projet")

h2("7.1  Le fondement : le modèle Environnement – Demande – Offre")
p("TECH-4 inscrit explicitement sa théorie du changement dans le **modèle EDO**. Ce modèle représente de "
  "manière égale, équivalente et interdépendante trois domaines : l'**Offre** de services, la génération de "
  "la **Demande** et l'**Environnement favorable**. Son postulat est qu'aucun de ces domaines ne peut, à lui "
  "seul, produire un changement durable de l'état nutritionnel : c'est leur combinaison qui le permet.")
p("La traduction opérationnelle de ce modèle dans le projet est la suivante : l'Offre est portée par les "
  "3 188 CAC, les 190 sites de soins communautaires et les 423 formations sanitaires ; la Demande est générée "
  "par la communication pour le changement social et de comportement, les visites à domicile, les groupes de "
  "soutien à l'ANJE et les démonstrations culinaires ; l'Environnement favorable repose sur les structures de "
  "participation communautaire (CAC, CODESA, UCODESA), la coordination multisectorielle, les mécanismes de "
  "redevabilité et la gestion des risques, y compris les VBG.")

img("toc", "Figure 1. Théorie du changement du projet — chaîne Intrants → Activités → Extrants → Résultats → Impact, "
           "adossée au modèle EDO de TECH-4")

h2("7.2  Chaîne de résultats")
p("**Intrants.** Le projet mobilise le financement du PMNS via l'UG-PDSS, le consortium SANRU-ICHESS-FONLIV-FDSS, "
  "63 superviseurs nutritionnistes et 33 personnels d'appui, les intrants nutritionnels (vitamine A, "
  "Mébendazole, fer et acide folique, SRO-Zinc, suppléments multi-micronutriments), les équipements de mesure "
  "(MUAC, balances, toises), les tablettes et les outils de gestion.")
p("**Activités.** TECH-4 organise l'essentiel autour de la formation (8 314 RECO, 846 prestataires de FOSA, "
  "60 cadres d'ECZS, 30 formateurs et 30 prestataires en prise en charge des VBG, 2 500 jeunes "
  "pairs-éducateurs), de la dotation et de l'approvisionnement des 3 188 CAC, 190 sites de soins communautaires "
  "et 423 formations sanitaires, des activités de promotion et de prévention (VAD, CPSr, ANJE/PFE, "
  "démonstrations culinaires, supplémentation, déparasitage), du monitorage et de la supervision.")
p("**Extrants.** Les extrants attendus sont fonctionnels : des CAC et des CODESA qui fonctionnent, des "
  "formations sanitaires qui offrent le paquet nutritionnel complet, trente FARN opérationnels, dix comités "
  "locaux de lutte contre les VBG actifs, des données DHIS2 complètes et promptes.")
p("**Résultats.** Les quatre résultats attendus correspondent aux quatre objectifs spécifiques : accès, "
  "utilisation et qualité des services communautaires améliorés ; système de prise en charge des survivantes "
  "renforcé ; structures de participation communautaire performantes ; système de santé offrant des services "
  "de nutrition de qualité.")
p("**Impact.** La réduction du retard de croissance chez l'enfant de moins de deux ans, la réduction de la "
  "morbidité et de la mortalité liées à la malnutrition et, en dernière instance, la préservation du capital "
  "humain de la province.")

h2("7.3  Chemin critique et hypothèses")
p("La théorie du changement n'est valide que si quatre conditions se tiennent. Le plan de S&E les traite "
  "comme des hypothèses à tester, chacune dotée d'un indicateur d'alerte précoce dans le Cadre de performance.")
bul(["**Condition de disponibilité.** Les intrants doivent être présents en continu. TECH-4 signale qu'aucune "
     "zone de santé du Kwilu n'a été approvisionnée en intrants nutritionnels depuis 2019 ; la rupture de "
     "stock est donc le risque numéro un, et sa surveillance un indicateur de processus prioritaire.",
     "**Condition de compétence et de stabilité.** Les compétences acquises lors des formations ne produisent "
     "d'effet que si les prestataires restent en poste. TECH-4 prévoit à cet effet une clause de stabilité de "
     "deux ans négociée dans la convention entre la DPS et le PMNS.",
     "**Condition d'adhésion communautaire.** L'utilisation des services dépend de la confiance des ménages et "
     "du statut accordé aux femmes. Les normes sociales, les interdits alimentaires et le faible pouvoir de "
     "décision des femmes sont identifiés par TECH-4 comme des déterminants majeurs.",
     "**Condition de qualité de la donnée.** Un dispositif de mesure ne vaut que par la fiabilité de ses "
     "données. TECH-4 documente une qualité de données non optimale en termes de complétude, de promptitude et "
     "de cohérence, et cinq zones de santé restées « silencieuses » en 2021."])

h2("7.4  Implications pour le dispositif de suivi-évaluation")
p("Trois conséquences découlent de cette théorie du changement pour le plan de S&E. Premièrement, le "
  "dispositif doit mesurer **les trois domaines du modèle EDO** et pas seulement l'offre de services : d'où "
  "l'inclusion d'indicateurs de demande (allaitement, alimentation de complément, fréquentation des services) "
  "et d'environnement favorable (fonctionnalité des CAC, plans d'action communautaires, comités VBG). "
  "Deuxièmement, il doit mesurer **le lien** entre communauté et formation sanitaire — le taux de prise en "
  "charge effective des enfants référés en est l'indicateur pivot. Troisièmement, il doit produire une "
  "**information utilisable localement** : c'est la raison d'être du MAA trimestriel et des Bulletins de "
  "Performance Communautaire.")

# ====================================================================== 8. SYSTÈME DE SUIVI
section("08", "Système de suivi",
        "Indicateurs, calendrier de collecte, outils, flux de données et système d'information")

add(t="land_start")
h2("8.1  Indicateurs de performance")
p("La matrice ci-dessous constitue le cœur opérationnel du plan. Elle comporte **43 indicateurs** répartis "
  "selon quatre niveaux : impact (3), résultat (18), extrant (20) et processus (2). Chaque indicateur est "
  "rattaché à un objectif spécifique et à un résultat intermédiaire de TECH-4.", lead=True)

callout("Convention de lecture des cibles",
        "Aucune cible n'est indiquée sans mention de son origine. Une cible **sans marque** est une cible "
        "explicitement chiffrée dans TECH-4. Une cible suivie de **(b)** est une cible d'alignement sur la "
        "référence nationale citée dans TECH-4 : la cible de l'année 2 reprend la valeur nationale, celle de "
        "l'année 1 correspond au point médian entre la référence provinciale et cette valeur. Une cible suivie "
        "de **(c)**, ou la mention « [À compléter selon Tech-4] », signale une donnée absente du document "
        "source : elle sera fixée lors de l'atelier de cadrage de janvier 2027, sur la base de l'enquête de "
        "référence.", icon="⚠", fill="FDF1E6", accent="F4A460")

ROWS = []
for r in D.INDICATORS:
    ROWS.append((r[0], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11]))

table("Matrice des indicateurs de performance du projet (43 indicateurs)", "6",
      ["N°", "Indicateur", "Type", "Définition", "Numérateur / Dénominateur",
       "Valeur de référence", "Cible Y1 (2027)", "Cible Y2 (2028)", "Fréquence", "Source de données", "Responsable"],
      ROWS,
      [0.9, 4.2, 1.6, 4.7, 3.4, 2.3, 1.9, 1.9, 1.9, 2.2, 2.5],
      font=7.5, center=[0, 2, 6, 7, 8], band=True)

add(t="land_end")

note("Les cellules marquées (b) renvoient à la convention d'alignement sur la référence nationale ; "
     "les cellules marquées (c) et les mentions « [À compléter selon Tech-4] » signalent une donnée absente du "
     "document source. Le détail des 43 indicateurs — y compris les indicateurs de produit non repris ici pour "
     "raison de lisibilité — figure dans la base de données de suivi du consortium, dont la structure est "
     "décrite à la section 8.5.")

h3("8.1.2  Règles de désagrégation")
p("Toutes les données de routine sont désagrégées selon quatre dimensions : le **sexe**, l'**âge** (0–5 mois, "
  "6–23 mois, 24–59 mois, 5–14 ans, 15–19 ans, 20–49 ans), la **zone de santé** et, lorsque la donnée le "
  "permet, l'**aire de santé**. Cette désagrégation est une exigence du principe d'équité posé par TECH-4 et "
  "une condition de l'analyse des inégalités prévue par l'évaluation à mi-parcours.")

h3("8.1.3  Répartition par niveau et par objectif")
NIV = [
    ("Impact", "3", "Objectif général du PMNS", "I-01 à I-03", "Annuelle"),
    ("Résultat", "18", "OS1 (6) — OS2 (3) — OS3 (3) — OS4 (6)", "R-01 à R-17", "Trimestrielle"),
    ("Extrant", "20", "RI 1.1 à 4.5", "P-01 à P-20", "Trimestrielle"),
    ("Processus", "2", "RI 4.5 et pilotage", "X-01 à X-03", "Mensuelle"),
]
table("Répartition des indicateurs par niveau", "7",
      ["Niveau", "Nombre", "Rattachement", "Plage de codes", "Fréquence dominante"],
      NIV, [3.0, 2.0, 6.2, 3.0, 2.8], font=9, center=[1], total=False)

h2("8.2  Calendrier de collecte des données")
p("Le calendrier ci-dessous couvre les 24 mois de mise en œuvre. Il articule la collecte continue (routine "
  "communautaire et FOSA), les opérations d'assurance qualité (MAA, audits, TPM, supervisions), les temps "
  "d'analyse et de redevabilité (revues, bulletins) et les trois moments d'évaluation — référence, "
  "mi-parcours, finale.")
table("Les trois cycles de collecte et leurs responsabilités", "8",
      ["Cycle", "Périodicité", "Sources et instruments", "Responsable"],
      [["Collecte de routine", "Mensuelle et trimestrielle",
        "Registres RECO et FOSA, fiches de VAD, tablette ODK, DHIS2 ; consolidation par les IT et les BCZS",
        "RECO, prestataires FOSA, ECZS"],
       ["Assurance qualité", "Trimestrielle (MAA), semestrielle (audits), annuelle (TPM)",
        "Grilles de monitorage amélioré pour action, audits de complétude et de cohérence, visites TPM",
        "Responsable S&E/HMIS, conseillers de zone"],
       ["Évaluation", "Trois temps : référence (T1 2027), mi-parcours (T3 2027), finale (T4 2028)",
        "Enquêtes SMART et CAP, évaluations thématiques, évaluation finale externe",
        "Équipe S&E, évaluateurs externes"]],
      [3.0, 4.2, 6.6, 3.2], font=8.0)
p("Les trois cycles ne se substituent pas les uns aux autres : la routine fournit la mesure continue, "
  "l'assurance qualité en établit la fiabilité, l'évaluation en produit le jugement. Un indicateur dont la "
  "valeur de routine n'a pas été auditée reste une donnée déclarative ; c'est pourquoi le rapport trimestriel "
  "distingue toujours les valeurs vérifiées des valeurs provisoires.")

img("gantt", "Figure 2. Chronogramme du suivi-évaluation sur 24 mois (janvier 2027 – décembre 2028)")

p("**Points de rendez-vous non négociables.** L'enquête de référence doit être achevée au plus tard à la fin "
  "mars 2027, faute de quoi les cibles ne pourront pas être validées avant le premier trimestre plein. "
  "L'évaluation à mi-parcours se déroule sur le troisième trimestre 2027 et son rapport est disponible en "
  "octobre 2027, à temps pour l'arbitrage budgétaire de l'année 2. L'évaluation finale s'achève avec le "
  "rapport final en décembre 2028.")

h2("8.3  Outils et méthodes de collecte")
p("TECH-4 prévoit un dispositif de collecte à quatre étages. Le plan en précise les instruments et les "
  "responsabilités.")
OUTILS = [
    ("Collecte de routine communautaire",
     "Cahier du RECO, registre de VAD, registre de dénombrement, fiche de référence, tablettes électroniques (ODK)",
     "RECO, supervisé par les AC et les IT",
     "Mensuelle",
     "3 188 CAC, 8 314 RECO"),
    ("Collecte de routine en formation sanitaire",
     "Registres UNTA/UNTI, fiche de croissance CPSr, registre CPSr, registre CPN, fiches de stock",
     "Prestataires, IT, nutritionnistes des BCZS",
     "Mensuelle",
     "423 FOSA"),
    ("Monitorage Amélioré pour l'Action",
     "Canevas MAA adossé au cadre de Tanahashi (disponibilité, accessibilité, utilisation, qualité)",
     "ECZS, AC du consortium, communautés",
     "Trimestrielle",
     "10 ZS, 250 AS"),
    ("Enquêtes périodiques",
     "Questionnaires SMART, CAP, fonctionnalité des structures communautaires, qualité des services",
     "Équipe S&E, enquêteurs formés, ESP Kinshasa",
     "Référence, mi-parcours, finale",
     "Échantillon représentatif par ZS"),
    ("Third Party Monitoring",
     "Grille d'audit indépendante, vérification croisée des données RECO et des enquêtes ad hoc",
     "Opérateur indépendant",
     "Semestrielle",
     "Échantillon aléatoire de villages et de FOSA"),
    ("Audits de qualité des données",
     "Grille de vérification complétude / promptitude / cohérence appliquée au DHIS2",
     "Resp. S&E/HMIS, responsable IT",
     "Trimestrielle",
     "10 ZS, 42 FOSA connectées"),
    ("Supervision formative",
     "Canevas de supervision NAC et FOSA, formulaire d'observation de VAD, formulaire d'évaluation de cas, spot check ménages",
     "Superviseurs nutritionnistes (63), ECZS, DPS/PRONANUT",
     "Mensuelle / trimestrielle",
     "4 020 missions par an"),
    ("Contrôle communautaire",
     "Bulletin de Performance Communautaire (BCP), registre de plaintes",
     "CAC, CODESA, communautés",
     "Trimestrielle",
     "3 188 villages"),
    ("Évaluations de la qualité des soins",
     "Grille « Quality Health Scaling », auto-évaluation des centres nutritionnels",
     "DPS, ECZS, consortium",
     "Semestrielle",
     "423 FOSA, 10 UNTI"),
]
table("Outils et méthodes de collecte", "9",
      ["Dispositif", "Instruments", "Acteurs", "Périodicité", "Couverture"],
      OUTILS, [3.4, 6.2, 3.6, 1.9, 1.9], font=8, first_bold=True)

callout("Règle des trois sources",
        "Aucun indicateur de résultat n'est renseigné à partir d'une source unique. Le principe retenu est la "
        "triangulation : donnée de routine (DHIS2) + observation directe (MAA, supervision) + mesure "
        "indépendante (enquête ou TPM). Un écart supérieur à 10 points de pourcentage entre deux sources "
        "déclenche une vérification documentée.", icon="●")

h2("8.4  Flux de données et reporting")
p("Le flux de données du projet suit la pyramide sanitaire de la RDC. Il est représenté ci-dessous, de la "
  "communauté vers le niveau national, avec la boucle de rétroaction qui conditionne l'utilisation des "
  "données sur le terrain.")

img("flux", "Figure 3. Flux de données et circuit de reporting, du RECO au niveau national")

FLUX = [
    ("RECO", "Fiche de VAD, registre de dénombrement", "CAC / CODESA", "Mensuelle", "Exhaustivité des ménages suivis"),
    ("CAC / CODESA / UCODESA", "Canevas de compilation, BCP", "IT / BCZS", "Mensuelle", "Tenue des réunions de monitorage"),
    ("IT / BCZS / ECZS", "Canevas standardisés, DHIS2", "DPS / PRONANUT", "Mensuelle", "Complétude et promptitude"),
    ("DPS / PRONANUT", "Bulletins, rapports consolidés", "SNIS / DHIS2 national", "Mensuelle", "Cohérence inter-zonale"),
    ("Responsable S&E/HMIS", "Rapport mensuel, trimestriel, annuel", "Chef de projet → UG-PDSS", "Mensuelle à annuelle", "Respect des échéances contractuelles"),
    ("UG-PDSS / MSPHP", "Rapports de performance", "Bailleur et comité de pilotage", "Trimestrielle", "Atteinte des cibles"),
]
table("Responsabilités dans le flux de données", "10",
      ["Émetteur", "Objet transmis", "Destinataire", "Fréquence", "Point de contrôle qualité"],
      FLUX, [3.2, 4.4, 3.8, 2.4, 3.2], font=8, first_bold=True)

p("**Boucle de rétroaction.** TECH-4 insiste sur l'utilisation des données comme outil de gestion. Le plan "
  "institue trois retours systématiques : un feedback trimestriel écrit du Responsable S&E/HMIS vers chaque "
  "ECZS et chaque CAC, la restitution des Bulletins de Performance Communautaire aux assemblées villageoises, "
  "et la validation en revue de performance des plans de redressement issus du MAA.")

h2("8.5  Système d'information sanitaire")
p("**DHIS2 comme plateforme de référence.** Le Système National d'Information Sanitaire de la RDC est bâti sur "
  "DHIS2 jusqu'au niveau de la zone de santé. TECH-4 relève toutefois que peu d'établissements y sont "
  "directement connectés, que la qualité des données n'est pas optimale et que la plateforme reste limitée au "
  "secteur public. Le projet agit sur ces trois limites : il dote 42 FOSA des aires de santé de Kikwit Nord et "
  "de Mosango d'un kit informatique, d'un kit solaire et d'un accès internet ; il forme les infirmiers "
  "titulaires au DHIS2 en milieu de travail ; il appuie les audits de qualité des données lors des sessions "
  "de MAA.")
p("**Intégration des données communautaires.** TECH-4 identifie comme innovation l'intégration des données des "
  "activités communautaires dans DHIS 2.0, processus en cours au niveau national avec l'appui de SANRU. Le "
  "plan de S&E accompagne cette intégration : les indicateurs communautaires retenus (VAD, dépistage, "
  "référencement, supplémentation) sont définis de manière compatible avec les métadonnées nationales afin de "
  "pouvoir être saisis dans DHIS2 sans retraitement.")
p("**SNSAP.** Le Système National de Surveillance Alimentaire et d'Alerte Précoce repose sur deux sites "
  "sentinelles par zone de santé, soit vingt sites pour les dix zones du projet. TECH-4 constate un "
  "dysfonctionnement de la transmission téléphonique faute de ressources et prévoit un forfait de crédit de "
  "20 USD par mois et par zone de santé. Le plan suit la fonctionnalité de ces vingt sites comme indicateur "
  "d'extrant (P-18).")
p("**Dispositif numérique de terrain.** Les RECO organisés en CAC reçoivent des tablettes électroniques pour le "
  "dénombrement de la population, la prestation de services communautaires et le suivi actif, longitudinal et "
  "personnalisé. Ce dispositif permet la surveillance à base communautaire digitalisée prévue par TECH-4 et "
  "alimente directement la base de suivi du consortium.")

h3("8.5.2  Architecture de la base de données de suivi")
p("La base de suivi du consortium comporte cinq tables : (i) **référentiel** — zones de santé, aires de santé, "
  "villages, structures ; (ii) **indicateurs** — code, définition, unité, sens de progression, cibles "
  "annuelles et semestrielles ; (iii) **mesures** — valeur, période, désagrégation, source, date de saisie ; "
  "(iv) **qualité** — statut de vérification, écart entre sources, observations d'audit ; "
  "(v) **actions** — plan de redressement issu des revues. Cette architecture permet de produire "
  "automatiquement le tableau de bord du Cadre de performance.")

h3("8.5.3  Contrôle de la qualité des données")
DQA = [
    ("Complétude", "Proportion de rapports attendus effectivement saisis", "≥ 90 %", "Mensuelle", "DHIS2, registre de transmission"),
    ("Promptitude", "Proportion de rapports saisis dans les délais", "≥ 90 %", "Mensuelle", "Horodatage DHIS2"),
    ("Cohérence", "Absence d'écarts internes entre numérateur et dénominateur ou entre périodes", "≤ 5 % d'écarts", "Trimestrielle", "Audit de cohérence"),
    ("Exactitude", "Concordance entre la donnée rapportée et la source primaire", "≥ 90 %", "Semestrielle", "TPM, vérification inopinée"),
    ("Actualité", "Délai entre la fin de la période et la disponibilité de la donnée", "≤ 30 jours", "Mensuelle", "DHIS2"),
]
table("Dimensions de la qualité des données et seuils retenus", "11",
      ["Dimension", "Définition opérationnelle", "Seuil", "Fréquence", "Outil de vérification"],
      DQA, [2.4, 6.4, 2.0, 2.3, 3.9], font=8.5, first_bold=True)

p("Les résultats de ces contrôles ne sont pas archivés : ils sont restitués à chaque revue trimestrielle sous la "
  "forme d'une note de qualité des données par zone de santé, assortie, le cas échéant, d'un plan de "
  "redressement. Trois règles s'appliquent. Une zone dont la complétude ou la promptitude passe sous le seuil "
  "de 70 % fait l'objet d'un accompagnement rapproché du responsable S&E/HMIS. Un écart d'exactitude supérieur "
  "à 10 points entre les données de routine et le Third Party Monitoring déclenche un audit de la zone "
  "concernée. Enfin, aucun indicateur dont la donnée n'a pas été vérifiée n'est présenté comme atteint dans un "
  "rapport adressé à l'UG-PDSS : il est signalé comme « en attente de vérification », ce qui protège le "
  "consortium autant que le bailleur.")

# ====================================================================== 9. ÉVALUATION
section("09", "Système d'évaluation",
        "Évaluation à mi-parcours, évaluation finale et évaluations thématiques")

p("TECH-4 prévoit que les évaluations aient lieu à trois périodes clés : au début du programme, pour établir "
  "les niveaux de départ des indicateurs ; à mi-parcours, pour s'assurer du déroulement du processus ; à la "
  "fin, pour apprécier l'atteinte des objectifs et tirer les enseignements nécessaires. Le plan retient cette "
  "architecture et en précise les modalités.", lead=True)

h2("9.1  Évaluation à mi-parcours — troisième trimestre 2027")
p("**Objet.** L'évaluation à mi-parcours porte sur le processus de mise en œuvre et sur les premiers effets. "
  "Elle intervient après dix-huit mois environ de terrain, alors que les formations initiales sont achevées et "
  "que les formations sanitaires ont été dotées.")
h3("Objectifs")
num(["Apprécier le degré d'avancement vers les cibles de l'année 1 et expliquer les écarts observés.",
     "Évaluer la qualité de la mise en œuvre du paquet NAC (formation, dotation, supervision, approvisionnement).",
     "Vérifier la validité des hypothèses de la théorie du changement et identifier les goulots d'étranglement persistants.",
     "Formuler des recommandations opérationnelles pour l'année 2 et proposer, le cas échéant, des réorientations."])
h3("Questions évaluatives")
bul(["Les activités communautaires atteignent-elles réellement les villages les plus éloignés et les "
     "populations les plus vulnérables ?",
     "Les enfants dépistés dans la communauté sont-ils effectivement pris en charge dans les formations "
     "sanitaires ? Où se rompt la chaîne de référencement ?",
     "Les formations réalisées ont-elles produit un changement de pratique observable au niveau des prestataires ?",
     "Les structures de participation communautaire (CAC, CODESA, UCODESA) fonctionnent-elles conformément à "
     "leur mandat ?",
     "Le dispositif de suivi-évaluation produit-il des données suffisamment fiables pour piloter le projet ?",
     "Les mécanismes de prise en charge des survivantes de VBG sont-ils accessibles et confidentiels ?"])
h3("Méthodologie")
p("L'évaluation combine une **revue documentaire** (plan de travail, rapports périodiques, données DHIS2 "
  "auditées, rapports de supervision et de MAA), une **analyse quantitative** des 43 indicateurs avec "
  "comparaison référence / mi-parcours, des **enquêtes de terrain** dans un échantillon de zones de santé "
  "stratifié selon la couverture initiale en CAC (Kikwit Nord et Gungu, les plus en retard, contre Djuma et "
  "Kingandu, déjà à 100 %), des **entretiens semi-structurés** avec les ECZS, les prestataires, les CODESA et "
  "les autorités, et des **groupes de discussion** avec les mères et les RECO.")
h3("Livrables")
bul(["Note de cadrage et termes de référence détaillés (mois 6) ;",
     "Rapport provisoire présenté au comité de pilotage (mois 9) ;",
     "Rapport final d'évaluation à mi-parcours, incluant la matrice des recommandations (mois 10) ;",
     "Plan de réponse aux recommandations, validé et budgété pour l'année 2 (mois 10)."])
callout("Valeur d'usage de la mi-parcours",
        "L'évaluation à mi-parcours n'est pas un exercice de conformité : elle intervient avant l'élaboration du "
        "plan de travail de l'année 2 et doit donc produire des arbitrages utilisables immédiatement. À cet "
        "effet, le rapport sera présenté à l'UG-PDSS avant la revue budgétaire annuelle.", icon="▶")

h2("9.2  Évaluation finale — quatrième trimestre 2028")
p("**Objet.** L'évaluation finale apprécie l'atteinte des objectifs, la pertinence de la stratégie et les "
  "perspectives de durabilité. Conformément à TECH-4, elle ne traite pas de l'impact au sens strict : "
  "l'analyse de l'impact nécessiterait une étude plus approfondie que le mandat ne prévoit.")
h3("Critères d'évaluation (CAD de l'OCDE)")
OCDE = [
    ("Pertinence",
     "Les objectifs et la stratégie du projet répondent-ils aux besoins nutritionnels réels des communautés des 10 ZS ?",
     "Évolution du contexte, adéquation du paquet NAC, prise en compte du genre et des droits humains",
     "Revue documentaire, entretiens, analyse des baselines"),
    ("Cohérence",
     "Le projet s'articule-t-il correctement avec le PMNS, le PNDS, le PRONANUT, les interventions du Fonds mondial et des autres partenaires ?",
     "Alignement sur les politiques nationales, synergies, absence de duplication",
     "Entretiens institutionnels, cartographie des intervenants"),
    ("Efficacité",
     "Dans quelle mesure les résultats attendus ont-ils été atteints ?",
     "Taux d'atteinte des 43 indicateurs, effet par rapport aux cibles 2027 et 2028",
     "Analyse quantitative, enquêtes, MAA"),
    ("Efficience",
     "Les ressources ont-elles été converties en résultats de manière économique et en temps utile ?",
     "Coût unitaire par RECO formé, par FOSA dotée, par enfant traité ; délais de mise en œuvre",
     "Analyse budgétaire, revue des marchés"),
    ("Impact",
     "Quels changements plus larges le projet a-t-il contribué à produire ?",
     "Tendances du retard de croissance, de la MAG et de la mortalité ; effets non prévus",
     "SMART, SNSAP, sources secondaires — analyse de contribution"),
    ("Durabilité",
     "Les acquis peuvent-ils se maintenir après le retrait du financement ?",
     "Fonctionnalité des CAC et CODESA, plans d'action, financement basé sur la performance, appropriation par la DPS",
     "Entretiens, observation, analyse institutionnelle"),
]
table("Grille d'évaluation finale fondée sur les critères du CAD de l'OCDE", "12",
      ["Critère", "Question évaluative centrale", "Éléments examinés", "Méthode"],
      OCDE, [2.6, 6.4, 5.0, 3.0], font=8.5, first_bold=True)

h3("Livrables de l'évaluation finale")
bul(["Termes de référence de l'évaluation externe (annexe C) ;",
     "Rapport initial (méthodologie et échantillonnage) ;",
     "Rapport provisoire et séance de restitution aux parties prenantes ;",
     "Rapport final d'évaluation selon les critères OCDE-CAD ;",
     "Note de capitalisation : bonnes pratiques, innovations et leçons apprises ;",
     "Plan de durabilité et de transfert des acquis à la DPS et au PRONANUT."])

h2("9.3  Évaluations thématiques")
p("TECH-4 prévoit plusieurs exercices spécifiques qui ne relèvent pas de l'évaluation globale mais éclairent "
  "des dimensions particulières du projet. Le plan les programme comme suit.")
THEMA = [
    ("Qualité de la prise en charge de la malnutrition",
     "Grille « Quality Health Scaling », auto-évaluation des centres nutritionnels",
     "T2 2028 (puis semestriellement)",
     "DPS, ECZS, consortium",
     "Rapport de qualité des soins ; plan d'amélioration par FOSA"),
    ("Prise en charge des VBG / EAS / HS",
     "Revue de la qualité des services, accessibilité, confidentialité, délais de référencement",
     "T4 2027",
     "ONG spécialisée, sous-cluster VBG, PNSR",
     "Rapport thématique ; cartographie actualisée des intervenants"),
    ("Approche FARN et déviance positive",
     "Étude de cas dans les 30 villages de Yasa Bonga et Kingandu",
     "T3 2028",
     "Consortium, ESP Kinshasa",
     "Documentation de l'innovation ; conditions de mise à l'échelle"),
    ("Recherche opérationnelle",
     "Deux études protocolisées, soumises au comité d'éthique de l'ESP de Kinshasa",
     "M5–M11 et M14–M20",
     "Consortium, consultant recruté à cet effet",
     "Protocoles, rapports de recherche, publications"),
    ("Enquête de satisfaction des bénéficiaires",
     "Enquête annuelle, complétée par les Bulletins de Performance Communautaire",
     "T4 2027 et T4 2028",
     "Consortium, CAC",
     "Rapport de satisfaction ; plan de redressement"),
]
table("Programmation des évaluations thématiques et des études", "13",
      ["Objet", "Approche", "Échéance", "Acteurs", "Livrables"],
      THEMA, [3.6, 4.6, 2.6, 3.2, 3.0], font=8, first_bold=True)

h2("9.4  Utilisation des résultats")
p("Toute évaluation produit un plan de réponse formel : chaque recommandation est affectée à un responsable, "
  "à une échéance et à une ressource. Le suivi de ce plan devient un point permanent de l'ordre du jour des "
  "revues trimestrielles, et le taux de mise en œuvre des recommandations constitue un indicateur de "
  "processus du Cadre de performance. Une recommandation non mise en œuvre au terme de deux revues est "
  "arbitrée par le comité de pilotage.")

# ====================================================================== 10. REDEVABILITÉ
section("10", "Redevabilité et apprentissage",
        "Revues, coordination, capitalisation et gestion adaptative")

h2("10.1  Revues trimestrielles de performance")
p("Huit revues trimestrielles sont programmées sur les vingt-quatre mois. Elles réunissent le chef de projet, "
  "le Responsable S&E/HMIS, les spécialistes techniques, les conseillers de zone et, selon l'ordre du jour, "
  "les ECZS concernées. Leur format est invariable, ce qui permet la comparaison d'une revue à l'autre.")
REVUE = [
    ("1. Examen du tableau de bord", "Positionnement des 12 KPI par rapport aux cibles semestrielles, code couleur vert / orange / rouge", "Resp. S&E/HMIS"),
    ("2. Analyse des goulots d'étranglement", "Résultats du MAA du trimestre, causes identifiées par domaine (disponibilité, accessibilité, utilisation, qualité)", "Conseillers de zone"),
    ("3. Qualité des données", "Complétude, promptitude, cohérence ; écarts TPM ; mesures correctives", "Resp. S&E/HMIS, IT"),
    ("4. Exécution du plan de travail", "Taux de réalisation des activités, retards, contraintes", "Chef de projet"),
    ("5. Plan de redressement", "Décisions, responsables, échéances, ressources ; suivi des décisions antérieures", "Chef de projet"),
]
table("Ordre du jour type d'une revue trimestrielle de performance", "14",
      ["Point", "Contenu", "Animation"],
      REVUE, [4.0, 9.5, 3.5], font=8.5, first_bold=True)

h2("10.2  Réunions de coordination")
p("TECH-4 prévoit plusieurs instances de coordination que le dispositif S&E alimente en données et en "
  "analyses.")
COORD = [
    ("Comité de pilotage du consortium (CPP)", "Représentants de chaque organisation membre", "Trimestrielle",
     "Orientations stratégiques, arbitrages, performance du consortium"),
    ("Cadres de concertation post-mission", "Comité de suivi de l'évaluation (DPS), consortium, partenaires", "Après chaque mission de terrain",
     "Présentation des observations et commentaires des participants"),
    ("Revues semestrielles de la nutrition", "Gouverneur, Ministre provincial de la Santé, DPS, PRONANUT, partenaires", "Semestrielle",
     "Réduction des goulots d'étranglement, couverture des interventions traceurs, mesures correctrices"),
    ("Réunions de cluster Nutrition, WASH et Sécurité alimentaire", "Partenaires sectoriels", "Mensuelle à trimestrielle",
     "Synergies, complémentarité des interventions, évitement des doublons"),
    ("Réunions de monitorage des BCZS", "ECZS, IT, AC, CODESA", "Mensuelle",
     "Analyse des données de routine, décisions locales"),
]
table("Instances de coordination et apport du dispositif S&E", "15",
      ["Instance", "Composition", "Fréquence", "Objet au regard du S&E"],
      COORD, [4.0, 4.6, 2.6, 5.8], font=8.5, first_bold=True)

h2("10.3  Capitalisation des leçons apprises")
p("TECH-4 engage le consortium à documenter les bonnes pratiques, les innovations et les leçons apprises, en "
  "se concentrant sur ce qui fonctionne, où, pourquoi et pour qui. Le plan prévoit trois vecteurs :")
bul(["**Une fiche de leçon apprise par trimestre**, alimentée par le MAA et les revues, selon un canevas "
     "unique (contexte, constat, preuve, enseignement, recommandation, condition de transférabilité).",
     "**Deux notes de capitalisation thématiques** : l'une sur l'approche FARN et la déviance positive, "
     "l'autre sur la transformation des CAC en plateformes multisectorielles.",
     "**Un bulletin trimestriel de données clés** sur la nutrition, produit avec la DPS, qui diffuse les "
     "résultats du projet et les analyses du PRONANUT."])
p("La diffusion s'adresse à trois audiences distinctes : les équipes du projet et les ECZS (notes internes), "
  "les partenaires et le bailleur (rapports et bulletins), les communautés (restitution orale en langues "
  "locales, appuyée sur les Bulletins de Performance Communautaire).")

h2("10.4  Gestion adaptative")
p("La gestion adaptative est le mécanisme par lequel les constats du suivi et de l'évaluation se traduisent en "
  "décisions. Elle repose sur quatre règles simples :")
num(["**Un seuil déclenche une décision.** Tout indicateur passé en rouge lors d'une revue fait l'objet d'une "
     "analyse causale documentée et d'une mesure corrective affectée à un responsable nommé.",
     "**Une décision a une échéance.** Aucune mesure corrective n'est adoptée sans date de revue de son "
     "exécution, inscrite à l'ordre du jour de la revue suivante.",
     "**Le plan de travail est glissant.** Les enseignements du MAA et des revues alimentent une révision "
     "semestrielle du plan de travail, sans attendre la fin de l'année.",
     "**Les réorientations majeures sont arbitrées au niveau du comité de pilotage**, sur la base d'une note "
     "technique du chef de projet appuyée par les données du S&E."])

h2("10.5  Redevabilité envers les communautés")
p("TECH-4 fait de la redevabilité un principe directeur : les prestataires doivent être responsables envers "
  "les communautés qu'ils desservent, et les communautés doivent avoir la capacité d'exiger des services de "
  "qualité. Deux instruments opérationnalisent ce principe.")
bul(["**Le Bulletin de Performance Communautaire (BCP)**, systématisé dans le fonctionnement de routine des "
     "CAC : les communautés évaluent la qualité des prestations qui leur sont offertes et établissent avec le "
     "prestataire un plan commun de redressement.",
     "**Le mécanisme de gestion des plaintes**, porté par un comité dans chaque village, adossé à la ligne "
     "verte et à un registre de plaintes, avec des garanties de confidentialité et de non-représailles. Les "
     "plaintes sensibles liées à l'exploitation et aux abus sexuels suivent une procédure spécifique, "
     "conformément aux outils de la Banque mondiale cités par TECH-4."])

# ====================================================================== 11. BUDGET
section("11", "Budget du suivi-évaluation",
        "Enveloppe, répartition par activité et règles de gestion")

p("TECH-4 ne comporte aucune ligne budgétaire chiffrée : ni le montant total du marché, ni la ventilation par "
  "composante n'y figurent. Le plan retient donc la règle de dimensionnement appliquée aux projets financés par "
  "des bailleurs internationaux — une enveloppe de suivi-évaluation représentant **7 % du budget total** — et "
  "en propose la répartition par activité.", lead=True)

callout("Assiette budgétaire : donnée manquante à Tech-4",
        "Montant total du marché et budget par composante : [À compléter selon Tech-4]. Le taux de 7 % retenu "
        "se situe dans la fourchette de 5 à 10 % recommandée ; il sera confirmé par l'UG-PDSS lors de la revue "
        "de démarrage.",
        icon="⚠", fill="FDF1E6", accent="F4A460")

h2("11.1  Enveloppe et répartition par activité")

BUD = [
    ("1", "Ressources humaines du S&E", "Responsable S&E/HMIS (100 %), chargé de données, appui du responsable IT, conseillers de zone pour la partie suivi", "28 %", "Y1 : 30 % — Y2 : 26 %"),
    ("2", "Enquête de référence", "Enquêtes SMART, CAP, fonctionnalité des structures communautaires, dénombrement actualisé", "12 %", "Y1 : 100 %"),
    ("3", "Collecte de routine et digitalisation", "Tablettes, forfaits de connectivité, impression des canevas et registres, maintenance", "10 %", "Y1 : 50 % — Y2 : 50 %"),
    ("4", "Monitorage Amélioré pour l'Action et audits de qualité des données", "Organisation de 40 sessions de MAA par an, grilles d'audit, ateliers de restitution", "8 %", "Y1 : 50 % — Y2 : 50 %"),
    ("5", "Third Party Monitoring indépendant", "Quatre missions de vérification indépendante, contrats avec un opérateur externe", "9 %", "Y1 : 45 % — Y2 : 55 %"),
    ("6", "Évaluation à mi-parcours", "Équipe d'évaluation, enquêtes de terrain, atelier de restitution", "7 %", "Y1 : 100 %"),
    ("7", "Évaluation finale externe", "Équipe d'évaluation, enquêtes, analyse selon les critères OCDE-CAD, atelier national", "9 %", "Y2 : 100 %"),
    ("8", "Évaluations thématiques et recherche opérationnelle", "Qualité des soins, VBG, FARN, deux études protocolisées et soumises au comité d'éthique", "6 %", "Y1 : 40 % — Y2 : 60 %"),
    ("9", "Revues, bulletins et rapports", "Huit revues trimestrielles, quatre revues semestrielles, bulletins trimestriels, rapports à l'UG-PDSS", "6 %", "Y1 : 50 % — Y2 : 50 %"),
    ("10", "Capitalisation et documentation", "Fiches de leçons apprises, notes de capitalisation, publication et diffusion", "3 %", "Y1 : 40 % — Y2 : 60 %"),
    ("11", "Renforcement des capacités S&E des partenaires", "Formation des ECZS et des IT à l'analyse et à l'utilisation des données", "2 %", "Y1 : 60 % — Y2 : 40 %"),
]
table("Répartition de l'enveloppe de suivi-évaluation par activité (7 % du budget du projet)", "16",
      ["N°", "Poste", "Contenu", "Part de l'enveloppe S&E", "Répartition indicative par année"],
      BUD, [1.0, 4.0, 6.6, 2.6, 2.8], font=8, center=[0, 3], total=False)

p("Les montants absolus seront obtenus en appliquant 7 % à l'assiette contractuelle : les évaluations externes "
  "représentent 16 % de l'enveloppe, les opérations de mesure 39 %, les ressources humaines 28 %.")

h2("11.2  Règles de gestion")
bul(["**Engagement budgétaire annuel.** L'enveloppe S&E est engagée par exercice, avec un taux d'exécution "
     "cible de 90 % en fin d'année ; un écart supérieur à 15 points déclenche une revue budgétaire.",
     "**Non-substituabilité.** Les crédits du S&E ne peuvent être redéployés vers les activités "
     "programmatiques qu'après autorisation écrite de l'UG-PDSS.",
     "**Traçabilité et audit.** Chaque dépense est rattachée à une activité du présent plan et à un livrable "
     "identifié (rapport, évaluation, bulletin) ; les dépenses de S&E sont auditées annuellement dans le cadre "
     "de l'audit du projet."])

# ====================================================================== 12. ANNEXES
section("12", "Annexes",
        "Fiches techniques d'indicateurs, modèles de rapports et termes de référence types")

h2("Annexe A — Fiches techniques d'indicateurs")
p("Les fiches ci-dessous détaillent, à titre de modèle, cinq indicateurs parmi les quarante-trois du plan. "
  "Chaque fiche est destinée à être reproduite pour l'ensemble des indicateurs et intégrée à la base de "
  "suivi du consortium.")

FICHES = [
    ("R-01", "Taux de prise en charge des enfants MAS référés dans les UNTA/UNTI",
     "Proportion d'enfants de 6 à 59 mois référés pour malnutrition aiguë sévère qui sont admis et traités "
     "conformément au protocole national de prise en charge intégrée de la malnutrition aiguë.",
     "Enfants MAS référés et admis dans une UNTA ou une UNTI / Enfants MAS référés par les RECO ou dépistés en FOSA",
     "n.d. — à établir par l'enquête de référence", "≥ 80 % en 2027 et en 2028",
     "Registres UNTA/UNTI, fiches de référence, DHIS2, vérification lors du MAA",
     "Trimestrielle", "Spécialiste Nutrition",
     "Contrôle croisé entre le nombre de fiches de référence émises et le nombre d'admissions enregistrées ; "
     "vérification inopinée d'un échantillon de dix dossiers par FOSA et par trimestre."),
    ("R-03", "Taux d'allaitement maternel exclusif chez les enfants de 0–5 mois",
     "Proportion d'enfants de 0 à 5 mois nourris exclusivement au sein au cours des 24 heures précédant "
     "l'enquête, sans autre liquide ni aliment, à l'exception de sels de réhydratation orale, de gouttes ou "
     "de sirops de vitamines, de minéraux ou de médicaments.",
     "Enfants de 0–5 mois allaités exclusivement / Enfants de 0–5 mois vivants",
     "32,7 % (MICS-Palu 2017-2018)", "43 % en 2027 ; 53,5 % en 2028 (alignement national)",
     "Enquête CAP, enquête SMART, DHIS2 (CPoN), MAA",
     "Annuelle", "Resp. S&E/HMIS",
     "Formation des enquêteurs aux définitions standard ; supervision de 10 % des entretiens ; contrôle de "
     "cohérence avec les données de CPoN."),
    ("R-10", "Proportion de survivantes de VBG ayant bénéficié d'une prise en charge holistique",
     "Proportion de survivantes de violences basées sur le genre déclarées qui ont accédé à au moins deux des "
     "trois composantes de la prise en charge holistique : médicale, psychosociale et juridique.",
     "Survivantes ayant accédé à une PEC holistique / Survivantes déclarées et enregistrées",
     "1,9 % (troisième trimestre 2021)", "25 % en 2027 ; ≥ 50 % en 2028",
     "DHIS2, registres VBG des FOSA, rapports de l'ONG spécialisée, sous-cluster VBG",
     "Trimestrielle", "Spécialiste engagement communautaire / genre",
     "Vérification de la confidentialité des registres ; contrôle du respect du délai de 72 heures pour la "
     "prise en charge médicale ; analyse des perdus de vue."),
    ("P-01", "Nombre de RECO formés au paquet NAC",
     "Nombre cumulé de relais communautaires ayant achevé la formation initiale ou le recyclage au paquet NAC "
     "(ANJE, PCIMA, CPSr, PFE, SDE, VBG, gestion des données, gestion des déchets).",
     "RECO ayant achevé la formation avec attestation / cible totale de 8 314 RECO",
     "0 — dernière formation dans la seule ZS de Mosango, il y a quatre ans", "4 956 en 2027 ; 8 314 en 2028",
     "Fiches de présence, attestations, base de données des ressources humaines communautaires",
     "Trimestrielle", "Spécialiste Nutrition",
     "Contrôle de la concordance entre fiches de présence, attestations et paiement des perdiem ; suivi post-formation "
     "à trois mois pour vérifier les acquis."),
    ("X-03", "Taux de complétude et de promptitude des données DHIS2 des 10 zones de santé",
     "Proportion de rapports mensuels attendus effectivement saisis et validés dans DHIS2 dans le délai "
     "contractuel, pour les dix zones de santé du projet.",
     "Rapports saisis et validés à temps / Rapports mensuels attendus",
     "n.d. — cinq ZS « silencieuses » en 2021 (Kikwit Nord, Kimputu, Kingandu, Moanza, Pay Kongila, Yasa Bonga)",
     "80 % en 2027 ; ≥ 90 % en 2028",
     "DHIS2 (horodatage), registre de transmission, rapports d'audit de qualité des données",
     "Mensuelle", "Resp. S&E/HMIS",
     "Extraction mensuelle automatisée ; rappel aux zones en retard ; audit trimestriel de cohérence ; "
     "vérification croisée avec le TPM."),
]

for code, lib, defi, numden, base, cible, source, freq, resp, qa in FICHES:
    h3(f"Fiche {code} — {lib}")
    rows = [
        ("Code", code),
        ("Libellé", lib),
        ("Définition", defi),
        ("Num / Dén", numden),
        ("Valeur de référence", base),
        ("Cibles", cible),
        ("Source et outil", source),
        ("Fréquence", freq),
        ("Responsable", resp),
        ("Contrôle qualité", qa),
    ]
    table(None, None, ["Champ", "Contenu"], rows, [3.6, 13.4], font=8.5, first_bold=True)

h2("Annexe B — Modèles de rapports")
p("Trois modèles de rapports structurent la production périodique du consortium. Leur format est aligné sur "
  "les attentes de l'UG-PDSS rappelées par TECH-4 : rapports d'avancement mensuels, trimestriels et annuels.")
RAP = [
    ("Rapport mensuel d'activités", "Responsable S&E/HMIS", "Le 5 du mois suivant",
     "1. Faits saillants du mois (10 lignes maximum)\n2. Avancement des activités par résultat intermédiaire\n"
     "3. Tableau des indicateurs mensuels et taux de complétude\n4. Difficultés et goulots d'étranglement\n"
     "5. Mesures correctives et responsables\n6. Annexes : canevas de collecte, liste des sites visités"),
    ("Rapport trimestriel de performance", "Chef de projet et Responsable S&E/HMIS", "Le 15 du mois suivant le trimestre",
     "1. Synthèse de performance et code couleur des KPI\n2. Analyse par objectif spécifique\n"
     "3. Résultats du MAA et des audits de qualité des données\n4. Exécution du plan de travail et du budget\n"
     "5. Suivi des recommandations antérieures\n6. Plan de redressement du trimestre suivant"),
    ("Rapport annuel", "Chef de projet", "Le 31 janvier de l'année suivante",
     "1. Bilan de l'année au regard du cadre logique\n2. Atteinte des 43 indicateurs et comparaison aux cibles\n"
     "3. Analyse des écarts et facteurs explicatifs\n4. Leçons apprises et bonnes pratiques\n"
     "5. Exécution budgétaire\n6. Perspectives et plan de travail de l'année suivante"),
    ("Rapport d'évaluation (mi-parcours / finale)", "Équipe d'évaluation externe", "Selon termes de référence",
     "1. Résumé exécutif\n2. Contexte et objet de l'évaluation\n3. Méthodologie et limites\n"
     "4. Constats par critère ou par question évaluative\n5. Conclusions\n6. Recommandations hiérarchisées\n"
     "7. Annexes : outils, liste des personnes rencontrées, données"),
]
table("Modèles de rapports et canevas", "17",
      ["Rapport", "Émetteur", "Échéance", "Structure type"],
      RAP, [3.6, 3.4, 2.6, 7.4], font=8, first_bold=True)

h2("Annexe C — Termes de référence types")
h3("C.1  Termes de référence — évaluation à mi-parcours (T3 2027)")
TDR1 = [
    ("Contexte", "Le consortium SANRU-ICHESS-FONLIV-FDSS met en œuvre, dans dix zones de santé de la province "
                 "du Kwilu, les services de nutrition à assise communautaire du Projet Multisectoriel de "
                 "Nutrition et de Santé. L'évaluation à mi-parcours intervient après dix-huit mois de mise en œuvre."),
    ("Objet", "Apprécier le degré d'avancement vers les cibles de l'année 1, la qualité de la mise en œuvre et la "
              "validité des hypothèses de la théorie du changement, et formuler des recommandations pour l'année 2."),
    ("Questions évaluatives", "Cinq à sept questions portant sur la couverture, la qualité, la continuité "
                              "communauté–FOSA, la fonctionnalité des structures communautaires et la fiabilité du dispositif de S&E."),
    ("Méthodologie attendue", "Revue documentaire ; analyse quantitative des 43 indicateurs ; enquêtes de terrain "
                              "dans quatre zones de santé contrastées ; entretiens semi-structurés ; groupes de discussion."),
    ("Profil de l'équipe", "Chef de mission expert en santé publique et nutrition (10 ans d'expérience minimum) ; "
                           "expert en suivi-évaluation ; expert en genre et protection ; enquêteurs formés."),
    ("Durée et lieu", "45 jours calendaires, dont 20 jours de terrain dans la province du Kwilu."),
    ("Livrables", "Note de cadrage, rapport provisoire, rapport final, matrice des recommandations, présentation de restitution."),
    ("Critères d'évaluation des offres", "Compréhension du mandat (20 %), qualité de la méthodologie (30 %), "
                                         "expérience de l'équipe (30 %), offre financière (20 %)."),
]
table(None, None, ["Rubrique", "Contenu"], TDR1, [4.2, 12.8], font=8.5, first_bold=True)

h3("C.2  Termes de référence — évaluation finale (T4 2028)")
TDR2 = [
    ("Contexte", "Fin de la période de mise en œuvre du projet dans les dix zones de santé du Kwilu."),
    ("Objet", "Apprécier l'atteinte des objectifs et analyser la performance du projet selon les six critères du "
              "CAD de l'OCDE : pertinence, cohérence, efficacité, efficience, impact et durabilité."),
    ("Questions évaluatives", "Une à deux questions par critère, formulées dans la note de cadrage, avec "
                              "indication des éléments de preuve attendus."),
    ("Méthodologie attendue", "Analyse quantitative des quarante-trois indicateurs sur les deux années ; "
                              "comparaison référence / mi-parcours / finale ; enquête de terrain ; analyse "
                              "budgétaire et de coût-efficacité ; analyse institutionnelle de la durabilité."),
    ("Profil de l'équipe", "Chef de mission senior (15 ans d'expérience), expert en évaluation, expert en "
                           "analyse économique, expert en genre."),
    ("Durée et lieu", "60 jours calendaires, dont 25 jours de terrain."),
    ("Livrables", "Rapport initial, rapport provisoire, rapport final, note de capitalisation, plan de durabilité "
                  "et de transfert des acquis."),
    ("Exclusion explicite", "Conformément à TECH-4, l'évaluation finale n'analyse pas l'impact au sens strict : "
                            "elle en propose une lecture en termes de contribution, appuyée sur les tendances du "
                            "retard de croissance et de la malnutrition aiguë."),
]
table(None, None, ["Rubrique", "Contenu"], TDR2, [4.2, 12.8], font=8.5, first_bold=True)

note("Fin du Plan de Suivi-Évaluation 2027-2028. Document établi sur la base exclusive du formulaire TECH-4 "
     "(DP N° ZR-DRC-MSP-235334-CS-QCBS). Les données absentes du document source sont signalées par la mention "
     "« [À compléter selon Tech-4] ».")


def blocks():
    return B
