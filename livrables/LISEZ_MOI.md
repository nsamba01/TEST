# Livrables — NAC Kwilu 2027–2028

Préparés le 6 novembre 2026 à partir de `Tech-4 (Récupération automatique).docx`, présent dans ce dépôt.

## Documents

- `Plan_suivi_evaluation_NAC_Kwilu_2027_2028.docx` : version Word modifiable du plan de suivi-évaluation.
- `Plan_suivi_evaluation_NAC_Kwilu_2027_2028.pdf` : version PDF de diffusion (8 pages).
- `Cadre_performance_NAC_Kwilu_2027_2028.docx` : version Word modifiable du cadre de performance.
- `Cadre_performance_NAC_Kwilu_2027_2028.pdf` : version PDF de diffusion (19 pages).

Le cadre comprend 26 indicateurs avec définitions, références disponibles ou à établir, cibles 2027 et 2028, sources, fréquences, responsables et précautions de mesure.

## Statut et réserves

Ces documents constituent une proposition technique à valider avec SANRU, le consortium, la DPS/PRONANUT et l’autorité contractante selon son mandat actualisé. Ils ne sont ni un contrat ni une certification des données historiques.

Les valeurs de référence 2027 sont à établir. Les données anciennes et les incohérences du TECH-4 sont signalées. Les cibles de performance et le budget sont proposés, pas approuvés. Le budget indicatif S&E est de 144 000 USD hors provision, soit 158 400 USD avec une provision proposée de 10 %. Les coûts doivent être recalculés selon les devis, l’échantillonnage et les ressources disponibles.

Les PDF et les Word utilisent les mêmes contenus, mais des moteurs de mise en page différents : leur pagination peut varier. Les documents d’origine ne sont pas modifiés.

## Reproduction

Depuis la racine du dépôt, avec Python 3 et les dépendances `python-docx` et `reportlab` installées dans un environnement virtuel :

```sh
python scripts/generer_livrables.py
```

Le script recrée les quatre documents. Les bibliothèques et environnements virtuels ne sont pas inclus dans le dépôt.

## Vérifications effectuées

- Génération sans erreur des quatre documents.
- Ouverture et extraction textuelle des deux PDF avec `pypdf` ; aucune page quasi vide détectée.
- Ouverture des Word avec `python-docx` et vérification des tableaux.
- Contrôle du nombre d’indicateurs et des sommes du budget.

Une relecture technique et une vérification visuelle dans Word ou un lecteur PDF restent recommandées avant signature et diffusion officielle.
