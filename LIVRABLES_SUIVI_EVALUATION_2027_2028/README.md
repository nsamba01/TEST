# Livrables — Plan de suivi-évaluation et cadre de performance 2027–2028

**Projet Multisectoriel de Nutrition et de Santé — volet Nutrition à Assise Communautaire (PMNS-NAC)**
Province du Kwilu, République démocratique du Congo
Consortium SANRU – ICHESS – FONLIV – FDSS (chef de file : SANRU)
Demande de Propositions N° ZR-DRC-MSP-235334-CS-QCBS

Période couverte : **1ᵉʳ janvier 2027 – 31 décembre 2028** (année 1 : 2027, année 2 : 2028).

---

## Fichiers

| Fichier | Format | Contenu |
|---|---|---|
| `01_Plan_Suivi_Evaluation_2027_2028.docx` | Word | Plan de suivi-évaluation complet, 13 sections, 28 tableaux, 7 figures, 2 calendriers |
| `02_Plan_Suivi_Evaluation_2027_2028.pdf` | PDF, 48 p. | Version de diffusion du même plan — mise en page identique |
| `03_Cadre_Performance_2027_2028.xlsx` | Excel, 7 onglets | Cadre de performance, 41 indicateurs, en-têtes filtrés et volets figés |
| `04_Cadre_Performance_2027_2028.pdf` | PDF, 63 p. | Tableau 14 colonnes + 41 fiches techniques |
| `05_Rapport_Controle_Qualite.docx` | Word, 16 p. | Traçabilité, informations manquantes, incohérences, contrôles effectués |

---

## Règle de fidélité documentaire

Le formulaire **Tech-4** est la source unique. Aucun objectif, résultat, indicateur, volume, montant, valeur de
référence, cible ou mécanisme institutionnel n'a été ajouté.

- **Valeurs en caractères normaux** : information explicitement présente dans Tech-4.
- **« À préciser » (rouge)** : information absente du document source. Tech-4 ne fournit **aucune valeur de
  référence propre au projet** pour les 14 résultats intermédiaires et **aucune cible annuelle** : les 82 cellules
  « Cible 2027 » / « Cible 2028 » portent donc cette mention.
- **« Cible globale Tech-4 »** : volume fixé par Tech-4 pour toute la durée du projet (3 188 CAC, 8 314 RECO,
  423 FOSA, 10 ZS, 190 SSC…). Ce n'est pas une cible annuelle et il n'est jamais reporté dans une colonne
  annuelle.
- **« Recommandation à valider »** : proposition méthodologique du consultant, qui n'engage pas le projet.

## Traçabilité

Chaque indicateur porte son code (`IMP-01`, `EFF-01`… `REA-04`) et sa source dans Tech-4. Le registre des
indicateurs est la source unique des quatre autres documents : les codes, intitulés, définitions, formules et
cibles sont identiques dans le plan, le cadre PDF et le classeur Excel (contrôle automatisé).

## Reproduire les livrables

```bash
cd build
python3 figures.py      # 9 figures + 3 couvertures
python3 build_all.py    # les 5 livrables dans ce dossier
python3 verify.py       # 30 contrôles — attendu : CONFORME
```

`build/design.py` est l'unique source de mise en page : le PDF (reportlab) et le Word (python-docx) en sont
deux rendus, d'où une identité graphique identique par construction.
