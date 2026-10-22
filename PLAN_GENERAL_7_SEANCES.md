# Finance verte — Master IEFM

## Proposition d’architecture en 7 séances de 3 heures

Le cours suit une progression unique : **comprendre les mécanismes économie-climat, construire des scénarios, valoriser les dommages, puis étudier leur transmission aux marchés et aux institutions financières**.

## Partie I — Modèles intégrés économie-climat

### 1. Les deux briques d’un IAM : économie et climat

- Bloc économique : production, capital, consommation, épargne, bien-être et actualisation.
- Bloc climatique : émissions, cycle du carbone, forçage radiatif et température.
- Matériel existant : slides, références mathématiques, notebooks étudiants/corrigés et modules Python.
- Dossier : `01_Fondations_economie_et_climat/`.

### 2. Couplage économie-climat et génération de scénarios

- Architecture de DICE et rétroactions économie-climat.
- SSP, scénarios IPCC/NGFS, BAU, politiques de transition et trajectoires net-zéro.
- Matériel existant : slides, handout DICE, notebook de scénarios et module Python.
- Dossier : `02_Couplage_IAM_et_generation_de_scenarios/`.

### 3. Coût social du carbone

- Contrôle optimal, dommage marginal, prix d’ombre et taxe carbone optimale.
- Sensibilité à l’actualisation, aux dommages et aux tipping points.
- Matériel existant : slides, handout, notebooks et complément actualisation/risques extrêmes.
- Dossier : `03_Cout_social_du_carbone/`.

## Partie II — Finance verte

### 4. Des IAM aux risques financiers

- Chaîne IAM → scénarios NGFS → variables macro-sectorielles → cash-flows/bilans → valorisation et risque → stress tests.
- Références David Zerbib : chapitres 10, 7 et 11 ; valorisation et cash-flows dans le chapitre 3.
- Dossier : `04_Des_IAM_aux_risques_financiers/`.

### 5. Asset pricing durable

- Préférences vertes, risques climatiques, greenium ex ante/ex post, S-CAPM et obligations vertes.
- Références David Zerbib : chapitres 2, 3 et 6.
- Dossier : `05_Asset_pricing_durable/`.

### 6. L’investisseur peut-il réellement avoir un impact ?

- Alignement vs impact ; exclusion, divestment, engagement, additionnalité et coût du capital.
- Mesure : empreinte, émissions évitées, notation ESG et double matérialité.
- Références David Zerbib : chapitres 4, 5, 7 et 9, avec certains instruments du chapitre 6.
- Dossier : `06_Impact_reel_de_l_investisseur/`.

### 7. Crédibilité et institutions

- Taxonomie, disclosure, labels, SFDR, greenwashing, banques centrales et transition juste.
- Conclusion critique : capacités et limites de la finance verte.
- Références David Zerbib : chapitres 6, 8, 9, 10 et 11.
- Dossier : `07_Credibilite_et_institutions/`.

## Principes de production des slides

- Introduction substantielle, puis slide **Plan** avant la première section analytique.
- Architecture générale réutilisée comme repère visuel aux transitions.
- Alternance définitions, schémas, équations, figures scientifiques, résultats empiriques, études de cas et synthèses.
- Une activité calculée ou notebook par séance.
- Style Beamer issu des supports IAM : `mystyle_diapos2.tex` et actifs associés.
- Attribution systématique des sources ; aucune reprise non citée des supports de David Zerbib.
