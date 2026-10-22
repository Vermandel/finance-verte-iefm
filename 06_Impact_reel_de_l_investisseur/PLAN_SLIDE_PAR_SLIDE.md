# Séance 6 — L'investisseur peut-il réellement avoir un impact ?

*Cours : Finance verte — Master IEFM | Durée : 3 h (180 min) | Public : étudiants disposant des bases de finance (CAPM, coût du capital) et des séances 1 à 5 (fondations économie-climat, IAM et scénarios, coût social du carbone, des IAM aux risques financiers, asset pricing durable).*

## Esprit de la séance (introduction substantielle)

La séance 6 change de question. Jusqu'ici, nous avons regardé le climat à travers le prisme de la valorisation : dommages et fonctions de réponse, scénarios IAM, coût social du carbone, transmission vers les risques financiers, puis prix des caractéristiques de durabilité dans les rendements. La question du jour est plus inconfortable : lorsqu'un investisseur « verdit » son portefeuille, que change-t-il **réellement** pour l'économie ? Les émissions physiques baissent-elles, ou seulement la composition comptable d'une liste de titres ?

Le fil rouge de la séance est la chaîne de causalité **portefeuille → économie réelle**. Nous suivrons ses maillons un à un : d'abord les stratégies d'**alignement de portefeuille** (exclusion/divestment, screening ESG), qui alignent des titres avec des valeurs ; puis l'**engagement actionnarial**, canal « voice » qui agit directement sur les décisions des entreprises ; ensuite l'**investissement à impact**, avec sa exigence d'**additionnalité**, et le **coût du capital** comme canal de transmission central, y compris via les **instruments verts** (green bonds, obligations indexées, labels) ; enfin la **mesure** : empreinte carbone, émissions évitées, alignement 2 °C, scores ESG, double matérialité. Un notebook clôt la séance : les étudiants construisent deux portefeuilles (values-aligned vs impact-oriented) et confrontent leurs métriques — l'occasion de constater qu'un portefeuille peut être parfaitement « vert » sans démontrer le moindre impact.

La réponse que la séance construit, progressivement, est nuancée : oui, l'investisseur peut avoir un impact réel, mais cet impact est **conditionnel** (canal du coût du capital modeste, additionnalité décisive, engagement généralement supérieur à l'exclusion) et **difficile à mesurer** (contrefactuel, divergences de données, métriques trompeuses). Ce constat prépare directement la séance 7 : qui garantit la crédibilité de tout cela ?

## Objectifs de la séance

1. Distinguer rigoureusement **alignement de portefeuille** (« values-aligned ») et **impact réel** (« impact-aligned »), et identifier les conditions sous lesquelles la seconde implique le premier — mais pas l'inverse.
2. Comprendre les **canaux de transmission** de l'investisseur vers l'économie réelle : exclusion/divestment, coût du capital, engagement, additionnalité, signaux marchands et non marchands.
3. Évaluer les **preuves empiriques** (prix du péché, prime d'exclusion, exit vs voice, élasticités d'émissions au coût du capital, prime verte) et leurs limites.
4. Maîtriser les **métriques d'impact** (empreinte carbone, émissions évitées, alignement 2 °C, scores ESG, double matérialité) et leurs pièges (scope 3, contrefactuel, normalisation, divergence des agences).
5. Mobiliser les acquis des séances précédentes (budget carbone, scénarios, CSC, asset pricing durable) comme **étalon** pour juger si l'impact financier observé est à la hauteur de l'enjeu climatique.
6. Savoir **construire et critiquer** une stratégie d'investissement « à impact » sur données réelles (notebook de fin de séance).

## Rythme proposé (180 min)

| Créneau | Contenu | Slides |
|---|---|---|
| 0:00–0:15 | Introduction substantielle + plan | 1–4 |
| 0:15–0:50 | Bloc 1 — Alignement vs impact ; exclusion & divestment | 5–13 |
| 0:50–1:15 | Bloc 2 — Engagement actionnarial | 14–17 |
| 1:15–1:25 | **Pause** | — |
| 1:25–2:05 | Bloc 3 — Impact investing, additionnalité, coût du capital, instruments verts | 18–27 |
| 2:05–2:20 | Bloc 4 — Mesure : empreinte, évitées, alignement, ESG, double matérialité (rythme rapide, appliqué ensuite en notebook) | 28–34 |
| 2:20–3:00 | **Activité notebook (40 min)** : lancement, manipulation, débrief, synthèse | 35–37 |

*Détail de la fenêtre notebook (2:20–3:00, 40 min) : lancement et consignes 3 min ; manipulation en binômes ≈ 28 min ; débrief collectif ≈ 6 min ; synthèse finale ≈ 3 min.*

*Réorganisation volontaire par rapport aux chapitres du cours d'Olivier David Zerbib (Green Finance, CREST–ENSAE, 2025–2026) : les chapitres 4 (pratiques « values-aligned »), 5 (impact investing), 7 (mesure de l'impact environnemental) et 9 (juste transition) sont refondus autour d'un fil rouge unique — le chaînon portefeuille → économie réelle — plutôt que suivis chapitre par chapitre ; les éléments instrumentaux du chapitre 6 (« green » assets) sont intégrés au bloc 3.*

**Conventions de sources.** « 4.txt, chap. 4, slides 21–23 » renvoie au fichier `/tmp/david-zerbib-finance-verte/4.txt`, diapositives 21 à 23 du chapitre 4 du cours d'O. David Zerbib (même convention pour 5.txt, 6.txt, 7.txt, 9.txt). « Apport propre IAM » désigne un contenu construit pour ce cours (articulation avec les séances 1–5, schémas, implémentation notebook). Toutes les formulations sont **transformées et citées**, jamais recopiées.

---

## Plan slide par slide

### Introduction (slides 1–4)

1. **Séance 6 — L'investisseur peut-il réellement avoir un impact ?**
   - Fil rouge : une stratégie d'allocation « verte » modifie-t-elle les émissions physiques de l'économie, ou seulement l'apparence du portefeuille ?
   - Position dans le cours : après les séances 1–5 (dommages, scénarios, CSC, risques financiers, asset pricing durable), on passe du modèle d'évaluation à l'action des agents financiers
   - Prérequis mobilisés : CAPM et coût du capital ; budget carbone ; trajectoires de scénarios ; prime « verte » vue en séance 5
   - *Forme : slide de titre avec schéma du fil rouge (portefeuille → économie réelle) | Source : apport propre IAM (articulation avec les séances 1–5)*

2. **L'énigme : une finance verte en explosion, des émissions hors trajectoire**
   - Marché de l'investissement responsable en forte croissance (encours mondiaux en expansion rapide depuis une décennie)
   - Revue 2020 de 230 fonds durables européens : 52 % revendiquent un impact environnemental explicite dans leur prospectus, **aucune allégation substantiée** (Heeb et al. 2023)
   - Pendant ce temps, les émissions mondiales restent au-dessus des trajectoires compatibles 2 °C/net zéro (rappel du cadrage scénarios de la séance 2)
   - *Forme : figure contrastée (croissance du marché vs trajectoire des émissions) + question ouverte à l'amphithéâtre | Source : 4.txt, chap. 4, slide 7 (« booming market ») ; 5.txt, chap. 5, slide 118 (revue des prospectus) ; apport propre IAM pour le rappel des trajectoires*

3. **La chaîne de causalité de l'impact : où peut-elle se rompre ?**
   - Schéma : préférences des investisseurs → prix des actifs → coût du capital → choix de projets et émissions des entreprises → climat
   - Trois points de rupture possibles : arbitrage par les investisseurs neutres, faible élasticité des firmes au coût du capital, contrefactuel de l'allocation (qu'aurait financé le marché sinon ?)
   - Deux familles de questions : que « contient » le portefeuille (empreinte) vs ce qu'il **fait faire** à l'économie (impact) — les confondre est le péché originel du marketing vert
   - *Forme : schéma à compléter collectivement au tableau | Source : apport propre IAM (synthèse des mécanismes de 5.txt, chap. 5, slides 17, 38 et 40)*

4. **Plan de la séance**
   - Bloc 1 — Alignement vs impact : exclusion et divestment (slides 5–13)
   - Bloc 2 — Engagement actionnarial : la « voice » (slides 14–17)
   - Bloc 3 — Impact investing, additionnalité, coût du capital, instruments verts (slides 18–27)
   - Bloc 4 — Mesurer l'impact : empreinte, évitées, alignement, ESG, double matérialité (slides 28–34) ; puis **notebook et synthèse** (slides 35–37) ; pause à ≈ 1 h 15
   - *Forme : slide de plan | Source : apport propre IAM*

### Bloc 1 — Alignement de portefeuille vs impact ; exclusion et divestment (slides 5–13, 35 min)

5. **Transition — Deux familles d'investissement responsable**
   - Rappel du plan : nous entrons dans le bloc 1 (slides 5–13)
   - **Values-aligned** : maximiser rendement financier + « valeur sociale » des titres **détenus** (utilité intrinsèque du portefeuille)
   - **Impact-aligned** : maximiser rendement financier + conséquence de l'investissement sur le **bien-être total** (welfare)
   - Point clé annoncé : l'impact-aligned implique un portefeuille aligné, la réciproque est fausse — c'est le fil rouge de la séance
   - *Forme : cours dialogué, tableau à deux colonnes au tableau | Source : 5.txt, chap. 5, slides 71–75 (Green & Roth 2025, définitions et interprétations)*

6. **Qui pratique quoi ? Assureurs, gérants, banques**
   - Assureurs : le climat frappe leur métier (IARD, santé) **et** leurs investissements ; intégration environnementale dans l'allocation d'actifs stratégique
   - Gérants d'actifs : marché en croissance, mais moins de 25 % des encours couverts par des politiques d'exclusion du charbon — frein principal : les fonds passifs répliquent des indices standards (ex. BlackRock ≈ 5 000 Md$ en passif)
   - Nuance : rien n'oblige un fonds indiciel à répliquer exactement son benchmark — fonds et indices peuvent évoluer (Reclaim Finance)
   - Banques : deux vecteurs d'impact (portefeuille de prêts et activités de marché) ; politiques sectorielles, critères transverses, Principes de l'Équateur
   - *Forme : exposé illustré par la cartographie des acteurs | Source : 4.txt, chap. 4, slides 2–7, 12–13, 14–19*

7. **La boîte à outils « values-aligned »**
   - Outil 1 : **exclusion/divestment** — sortir certains titres du portefeuille
   - Outil 2 : **screening ESG** — best-in-class, best-in-universe, best-effort ; appartenance à des indices « durables » (FTSE4Good, DJSI) ; recours aux agences de notation extra-financière
   - Illustration séance 5 : décarboner un portefeuille en minimisant l'erreur de suivi (Andersson et al. 2016) — un alignement « indolore » financièrement… qui ne dit rien de l'impact réel
   - Annonce : ces outils alignent le portefeuille avec des **valeurs** ; leur effet sur l'économie réelle est l'objet des slides suivantes
   - *Forme : cours dialogué | Source : 4.txt, chap. 4, slides 21–22 et 44 ; slides 8–11 (Andersson et al. 2016)*

8. **Anatomie d'une exclusion**
   - Exclusions **normatives** (armes prohibées, pays sous sanctions ONU/UE) vs **sectorielles** (tabac, jeux, charbon…)
   - Le point technique : les **seuils** — doivent être à la fois relatifs (% du chiffre d'affaires) et absolus ; exemple critiqué (rapports OXFAM/Les Amis de la Terre) : seuils de ≈ 50 % du CA chez certains émetteurs français alors que Glencore, 8e producteur mondial de charbon, est à 21 %
   - Conséquences d'un cadrage mou : manque de transparence, définition encore floue de « ce qui est vert », données divergentes entre fournisseurs
   - *Forme : mini-cas : les étudiants qualifient des seuils réels (transparents vs opaques) | Source : 4.txt, chap. 4, slides 23, 34–36*

9. **Divestment : dynamique et cas emblématiques**
   - Dynamique du désinvestissement des énergies fossiles : campagnes universitaires, puis institutionnels
   - Fonds souverain norvégien (mars 2019) : vente de ≈ 7,5 Md$ d'actions d'exploration-production pétrolière, sur motifs **financiers**
   - Stanford (2014) : désinvestissement charbon d'un dotation de > 20 Md$ — effet prix quasi nul, mais forte **stigmatisation** médiatique et effet d'entraînement (Rockefeller Brothers Fund, fonds norvégien)
   - Distinction à retenir : signaux **non marchands** (stigmatisation, effet de référentiel) vs effets de marché (prix, coût du capital) — les six mécanismes d'impact seront détaillés au bloc 3
   - *Forme : storytelling de cas (deux récits contrastés) | Source : 4.txt, chap. 4, slides 24–25 ; 5.txt, chap. 5, slide 14*

10. **Le paradoxe : les financements fossiles progressent**
    - Prêts et souscriptions aux énergies fossiles des grandes banques mondiales en hausse (rapports « Banking on Climate Chaos »)
    - Banques françaises : financements fossiles massifs et croissants (OXFAM 2022), y compris pendant la période des engagements « verts »
    - Décalage structurel entre **engagements affichés** et **expositions réelles** — première rencontre avec la notion d'alignement de façade
    - *Forme : lecture commentée de graphiques (étudiants extraient la tendance avant l'explication) | Source : 4.txt, chap. 4, slides 26–31*

11. **Le cas charbon français : critères et données divergents**
    - Rapports de suivi ACPR/AMF : politiques « charbon » des banques et assureurs parisiens, calendriers de sortie très hétérogènes
    - Critères d'exclusion charbon des sociétés de gestion françaises : définitions, seuils et périmètres peu comparables
    - **Données d'exposition divergentes** selon les fournisseurs : même entreprise, mesures différentes — la mesure elle-même est un enjeu ( annonce du bloc 4)
    - *Forme : analyse comparative de documents réglementaires (extraits) | Source : 4.txt, chap. 4, slides 32–35*

12. **Preuve empirique : le prix du péché (Hong & Kacperczyk 2009)**
    - Sin stocks : surperformance de ≈ 26–29 bps/mois vs comparables ; alpha de 25–30 bps/mois après SMB/HML/MOM ; ratios de valorisation 15–20 % plus bas
    - Mécanismes : actions négligées → partage des risques limité → rendements supérieurs (Merton 1987) ; risque de litige ; détention institutionnelle plus faible (21 % vs 28 %, −7 points) ; couverture analystes −15 %
    - Lecture climat : une exclusion **largement partagée** renchérit durablement le capital des firmes visées… et paye ceux qui restent — l'arbitrage limite l'effet
    - *Forme : séminaire de lecture (tableaux de résultats projetés et décodés) | Source : 4.txt, chap. 4, slides 37–43*

13. **Ce que l'exclusion fait — et ne fait pas**
    - Effet prix réel mais **amorti** : les investisseurs neutres rachètent ce que les responsables vendent ; l'ampleur dépend de la pente de la demande de titres
    - Prime d'exclusion (Zerbib 2022) : hyperbolique dans la proportion p d'investisseurs désinvestissant — l'exit devient puissant seulement quand p est grand
    - Résultat Broccardo-Hart-Zingales (2020) : si la responsabilité sociale est peu répandue, l'équilibre sans désinvestissement domine ; l'exit n'atteint l'optimum social que si « presque tous » internalisent le dommage
    - Mini-débat flash (2 × 2 min) : « Désinvestir, est-ce se laver les mains ou envoyer un signal ? »
    - *Forme : mini-débat structuré + synthèse au tableau | Source : 5.txt, chap. 5, slides 106–109*

### Bloc 2 — Engagement actionnarial (slides 14–17, 25 min)

14. **Transition — De l'exit à la voice**
    - Rappel du plan : bloc 1 terminé (exclusion/divestment) ; nous passons au bloc 2 (slides 14–17)
    - Position du PRI (UNPRI) : le désinvestissement réduit la capacité d'influencer directement la performance de durabilité des émetteurs ; l'effet financier sur les ciblées est improbable pour modifier leur comportement
    - L'engagement en chiffres : soutien moyen aux résolutions climat 23 % en 2020 (16 % en 2019) ; ≈ 40 % des résolutions retirées avant vote après promesses d'action des ciblées
    - *Forme : transition récapitulative (1 slide, 5 min) | Source : 5.txt, chap. 5, slides 92 et 98*

15. **Mécanique de l'engagement**
    - Canaux : engagement privé (dialogue, lettres), public (votes en AG, dépôt de résolutions), sièges au conseil — le mécanisme d'impact n° 4 des six mécanismes (bloc 3)
    - Échelle de la pratique : Norges Bank IM (GPFG) a soulevé des enjeux ESG dans 1 737 réunions en 2017, soit 53 % de ses réunions avec les entreprises
    - Cas chiffré : Hermes EOS × Sinopec (2014) — dialogue aboutissant à un programme de réduction du méthane, ≈ 3 Mt de CO2e évitées revendiquées en 2017
    - *Forme : exposé + un exemple chiffré commenté | Source : 5.txt, chap. 5, slides 12 et 93*

16. **Ce qui fait réussir un engagement (Dimson, Karakas & Li 2015)**
    - Données : 613 entreprises US (1999–2009, 26 % de la capitalisation CRSP), 2 152 séquences d'engagement dont 382 réussies ; deux modes : « raised awareness » vs « request for change »
    - Facteurs de succès : engagement **agressif** (au moins une demande de changement), **intensif** (répété), **expérimenté** (succès antérieur avec la cible), **focalisé** (même thème), **collaboratif** — surtout avec des investisseurs activistes (« collaborations dures »)
    - Lecture pour le futur professionnel : un engagement efficace est une stratégie construite, pas une lettre annuelle
    - *Forme : lecture guidée de résultats empiriques | Source : 5.txt, chap. 5, slides 101–105*

17. **Cas emblématiques et verdict théorique**
    - Shell (2018) : après engagement, indexation de la rémunération des dirigeants sur les objectifs climat et sortie de groupes de lobbying opposés à l'Accord de Paris
    - Engine No. 1 × ExxonMobil (2021) : 0,02 % du capital, bataille de procurations, appui des grands institutionnels et des conseillers de vote (ISS, Glass Lewis) → 2 sièges au conseil sur 10
    - Verdict théorique (Broccardo-Hart-Zingales 2020) : dès que les actionnaires internalisent *un peu* du dommage (λ > 0), la **voice** (vote) atteint la solution du planificateur bienveillant ; l'**exit** n'y parvient que dans des configurations rares (responsabilité sociale très répandue)
    - Synthèse du bloc : sur liste cotée, l'engagement est en général le canal le plus prometteur — l'exclusion garde un rôle de signal et de dernier recours
    - *Forme : double étude de cas + synthèse magistrale | Source : 5.txt, chap. 5, slides 99–100 et 106–108*

### Bloc 3 — Impact investing, additionnalité, coût du capital, instruments verts (slides 18–27, 40 min)

18. **Transition — L'investissement à impact**
    - Rappel du plan : blocs 1–2 terminés (exclusion, engagement) ; nous entrons dans le bloc 3 (slides 18–27)
    - Définition par trois piliers (French SIF) : **intentionnalité** (viser un bénéfice social/environmental mesurable), **additionnalité** (la contribution de l'investissement à l'impact), **mesure** de l'impact (avec alignement d'intérêts si la performance est rémunérée)
    - Thèmes structurés par les 17 ODD ; deux cibles types : petites entreprises vertes à faire croître, entreprises brunes à verdir
    - *Forme : transition + définition encadrée | Source : 5.txt, chap. 5, slides 2, 5 et 7*

19. **Six mécanismes d'impact**
    - 1 Financer des marchés insuffisamment approvisionnés (additionnalité directe) ; 2 fournir du capital flexible (rendement sous-marché, dette subordonnée, horizons longs) ; 3 apporter un soutien non financier (expertise, gouvernance, réseaux)
    - 4 Engagement actionnarial (vu au bloc 2) ; 5 signaux de marché via le **coût du capital** (surovertement des verts, sous-pondération des bruns) ; 6 signaux non marchands (stigmatisation, effets de classement)
    - Exemples canoniques : Impossible Foods (25 M$ de Bill Gates à un stade incertain) ; Root Capital × coopérative Musasa (Rwanda) ; Owl Ventures (ed-tech) ; ETF ESG de Vanguard ; désinvestissement charbon de Stanford
    - *Forme : tableau récapitulatif à compléter avec la classe (mécanisme ↔ exemple) | Source : 5.txt, chap. 5, slides 8–14*

20. **L'additionnalité au cœur de tout**
    - L'impact est une affaire de **changement attendu** par rapport au contrefactuel : on peut avoir de l'impact en finançant une entreprise brune qui décarbone grâce à ce financement
    - Résultat d'équilibre (Green & Roth 2025) : les investisseurs impact-aligned ne financent **pas** les projets commercialement viables (le capital commercial s'en chargerait — financer ne déplacerait que du capital) ; ils ciblent les projets non viables commercialement mais socialement précieux
    - Contre-intuitif mais logique : à profitabilité égale, ce sont les investisseurs **les plus altruistes** qui financent les projets de plus **faible** valeur sociale (condition d'accès plus facile à satisfaire)
    - Résultat normatif : certains value-aligned peuvent accroître à la fois bien-être total **et** rendement en convertissant vers l'impact ; dans l'expérience de Green & Roth, 47 % des participants se déclarant value-aligned changeaient de choix quand on leur montrait mieux faire — des impact-aligned « mal guidés »
    - *Forme : déduction guidée à partir d'un graphique d'équilibre simplifié | Source : 5.txt, chap. 5, slides 3–4, 78–79, 83 et 90*

21. **Qui sont les investisseurs ? Tester les motifs**
    - Expérience en ligne (400 participants US, choix répétés entre investissements assortis de dons caritatifs, incitations réelles)
    - Latent class logit : trois classes — investisseurs « commerciaux » (aucune disposition à payer), **value-aligned** (cèdent 0,72 $ de rendement pour 1 $ de valeur sociale détenue), **impact-aligned** (≈ 32 %, internalisent le bien-être total)
    - Auto-déclaration vs comportement révélé : recoupements partiels — la demande d'impact existe mais s'exprime souvent de manière incohérente (annonce de Heeb et al., slide 110 et suivantes)
    - *Forme : interprétation de tableau de résultats par les étudiants (que signifient les coefficients ?) | Source : 5.txt, chap. 5, slides 85–89*

22. **Le coût du capital, canal central**
    - Mécanisme théorique (Heinkel-Kraus-Zechner 2001 ; Pastor-Stambaugh-Taylor 2021 ; Broccardo et al. 2020 ; Landier-Lovo ; Oehmke-Opp ; Green-Roth) : les investisseurs durables renchérissent le capital des firmes brunes et bonifient celui des vertes → les firmes décarbonent quand le gain de financement dépasse le coût d'abattement
    - Formalisation (De Angelis-Tankov-Zerbib 2022) : prime d'externalité −α·θ(ψ) dans le rendement d'équilibre — les investisseurs verts acceptent un rendement moindre sur les actifs verts, exigent plus sur les bruns ; cohérent avec Pastor et al. 2021, Pedersen et al. 2021, Zerbib 2020
    - Conditions pour maximiser l'impact : financer ce que le marché normal ne financerait pas, mandats larges, internaliser les effets de chaîne d'approvisionnement, prioriser l'activisme actionnarial
    - *Forme : cours magistral avec une seule équation (pas de dérivation) | Source : 5.txt, chap. 5, slides 17 et 38*

23. **Quantifier l'impact : De Angelis, Tankov & Zerbib (2022)**
    - Dispositif : modèle dynamique à croyances hétérogènes (regulars vs greens) × jeu non coopératif entre firmes choisissant leurs trajectoires d'émissions ; estimation sur les actions US 2004–2018 via les holdings des fonds verts
    - Programme d'émissions d'équilibre ψ* = c/(βᶜκᶜ + αβκ) : arbitrage entre coût d'abattement et réduction du risque climatique financier perçu ; les croyances des verts pèsent surtout sur les émissions **de long terme** (β croissant), celles des firmes sur le court terme
    - Résultats chiffrés : doubler la part d'actifs gérés par les fonds verts → intensité carbone **−4,9 %** en un an ; doubler l'incertitude climatique → **+6,7 %** ; simulations calibrées : 25 % (50 %) d'AUM verts ≈ −1 % (−3 %) d'émissions par an
    - Verdict des auteurs : les investisseurs verts alignent leurs **portefeuilles** sur 2 °C mais contribuent insuffisamment à aligner **l'économie** — premier élément de réponse à la question du jour
    - *Forme : séminaire de recherche (lecture d'équation et de tableau de régression, sans démonstration) | Source : 5.txt, chap. 5, slides 15–24, 40–44 et 63–70*

24. **Amplificateurs, dissuadeurs — et la transition juste**
    - Amplifient l'impact : anticipation d'une régulation climat plus stricte (rythme de réduction ×2,2), d'innovations technologiques (×3,6), des deux (×4) ; part de richesse et sensibilité accrues des investisseurs verts ; cadres, taxonomies et labels permettant la sélectivité
    - Réduit l'impact : l'incertitude sur les risques climatiques futurs — elle érode la prime d'externalité, incite à la réallocation vers le brown ; émissions d'équilibre +0,4 % à +8,5 % selon que l'information climatique arrive tous les 1 à 20 ans
    - Recommandation des auteurs : stratégies combinant **soutien financier aux entreprises en transition** et **engagement actionnarial** — ce qui rejoint la logique de **transition juste** : distinguer activités remplaçables (à fermer/réduire) et irremplaçables (à transformer, critères : substituabilité, coût marginal d'abattement, équité d'accès)
    - *Forme : synthèse orientée décision (grille amplificateurs/dissuadeurs) | Source : 5.txt, chap. 5, slides 47, 49, 61 et 70 ; 9.txt, chap. 9, slides 7–8*

25. **Transition — Les instruments verts**
    - Rappel du plan : blocs 1–2 + cœur du bloc 3 traités ; avant la mesure, un détour par les **instruments** (fin du bloc 3, slides 25–27)
    - Définition : actif vert = titre adossé à des projets/actifs à bénéfice environnemental direct — green bonds, green project bonds (SPV), green project equity (infrastructures renouvelables, eau), bâtiments verts labellisés, fonds à guidelines vertes
    - Ordre de grandeur : émissions de green bonds 2024 ≈ 700 Md$, encours ≈ 3 400 Md$ (2–3 % de l'encours obligataire total) — significatif mais marginal
    - Logique distincte des blocs précédents : ici le canal espéré est le **financement direct** d'actifs, pas l'exclusion ni le vote
    - *Forme : transition + taxonomie rapide des instruments | Source : 6.txt, chap. 6, slides 1–6*

26. **Green bonds : cadrage et garanties de procédé**
    - Green Bond Principles (ICMA) : 4 composantes — usage des fonds (bénéfice environnemental clair, évalué et si possible quantifié), processus d'évaluation/sélection, gestion des proceeds (traçabilité), reporting annuel jusqu'à allocation totale
    - Revue externe recommandée : second party opinion, vérification, certification, notation — recommandations **volontaires**
    - Limites structurelles : le green n'a **aucune valeur légale** (pas de sanction) et **l'additionnalité n'est pas exigée** (refinancer un projet déjà vert est permis) — Ekeland & Lefournier (2019)
    - Écosystème français/européen de transparence : labels ISR et Greenfin (exclusions charbon/hydrocarbures non conventionnels, objectifs, indicateurs), classification SFDR des produits (articles 6/8/9) — de la **divulgation**, pas une garantie d'impact
    - *Forme : lecture de cadre + quiz express (4 questions vrai/faux) | Source : 6.txt, chap. 6, slides 5, 9–15, 42 et 54–58*

27. **La prime verte et son interprétation**
    - Zerbib (2019) : appariement green/convensionnelle avec contrôle de liquidité → prime verte moyenne **−2 bps** (63 % des primes négatives), significative sur EUR/USD et financières (−3 bps pour AA) ; ni un premium de risque, ni un premium de marché, négative et stable depuis mai 2016
    - Interprétation : une réduction de coût de financement de 2–3 bps est **trop faible** pour rentabiliser des projets verts coûteux → pas d'incitation financière à créer des projets additionnels (Ekeland & Lefournier)
    - Variante moderne : obligations sustainability-linked (coupon indexé à l'objectif ESG) — gain moyen 29,2 bps (Kölbel & Lambillon 2022), mais calibrages contestables : step-up moyen 26,6 bps, coût de capital encore réduit de 2,6 bps même en cas d'échec ; risques de free-riding (échéance lointaine, remboursement anticipé)
    - Question laissée ouverte pour le débrief : un instrument vert est-il un instrument d'impact ou un instrument de communication ?
    - *Forme : discussion structurée à partir de résultats empiriques | Source : 6.txt, chap. 6, slides 22–34 et 41–44*

### Bloc 4 — Mesurer l'impact : empreinte, évitées, alignement, ESG, double matérialité (slides 28–34, 15 min, rythme rapide)

28. **Transition — Mesurer l'empreinte**
    - Rappel du plan : blocs 1–3 terminés ; bloc 4 (slides 28–34) — la mesure, qui servira directement au notebook
    - Scopes 1/2/3 : émissions directes, énergie achetée, chaîne de valeur amont/aval
    - Empreinte absolue E = Σᵢ Eᵢ et intensité pondérée I = Σᵢ wᵢ·Iᵢ (formules Erafp) ; plusieurs dénominateurs possibles (revenu, valeur d'entreprise, usage) — le choix du dénominateur change le classement des portefeuilles
    - *Forme : transition + démonstration chiffrée sur 3 titres fictifs | Source : 7.txt, chap. 7, slides 2–7*

29. **Empreinte carbone : trois pièges**
    - Piège 1 — Scope 3 : souvent ignoré alors qu'il domine dans plusieurs secteurs (automobile ≈ 80 % en aval ; aluminium en amont)
    - Piège 2 — Reallocation sectorielle : une stratégie fondée sur l'empreinte exclut mécaniquement les secteurs intenses (énergie, matériaux) — c'est un choix de composition, pas de la décarbonation de l'économie ; l'intensité CO2/chiffre d'affaires peut même sélectionner des émetteurs plus carbonés
    - Piège 3 — Normalisation par l'output : au niveau pays, la métrique « émissions par $ de PIB » (PCAF) pénalise structurellement les pays à revenu faible/intermédiaire → obligations souveraines exclues ou sous-pondérées là où les besoins de financement de la transition sont maximaux (Dibley et al., Nature 2024)
    - *Forme : démonstration par contre-exemples | Source : 7.txt, chap. 7, slides 8–10*

30. **Parts vertes et brunes**
    - Green share / brown share : parts du portefeuille dans des activités éligibles (frameworks multiples ; la taxonomie UE comme référence partagée) — utiles pour piloter une trajectoire et comparer sous une définition commune
    - Limite persistante : la part verte dépend de la définition du gérant — comparabilité encore fragile hors taxonomie
    - Au-delà de la mesure : « carbon bubble » et **actifs échoués** (échec réglementaire, économique, physique) — réactivation du lien actifs-climat-risque vu en séance 4
    - *Forme : exposé illustré (exemples de parts vertes/brunes de portefeuilles) | Source : 7.txt, chap. 7, slides 11–18*

31. **Émissions évitées**
    - Principe : comparer les émissions de l'actif financé à celles d'un **scénario de référence** (baseline) — ex. éolien vs mix électrique moyen
    - Limite décisive : la baseline est discrétionnaire → comparabilité faible entre gérants ; et contrairement aux émissions réelles, les émissions évitées sont **hypothétiques** ; aucune standardisation attendue à ce stade
    - Règle d'usage recommandée : ne jamais additionner émissions réelles et évitées ; toujours publier la baseline
    - *Forme : calcul guidé sur un exemple simple (baseline haute vs basse) | Source : 7.txt, chap. 7, slides 19–22*

32. **Alignement 2 °C**
    - Méthode type SDA (sectoral decarbonization approach) : performance physique des entreprises (scopes y compris 3), trajectoires sectorielles (IEA), calcul du sur/sous-shoot cumulé d'émissions (type « Alignment Cookbook », Institut Louis Bachelier)
    - Approche **dynamique** : on évalue une trajectoire, pas un instantané — un point isolé ne dit rien de l'alignement
    - Écosystème d'engagements : Net-Zero Asset Owner Alliance (≈ 5 000 Md$ à mi-2020), frameworks IIGCC, premières banques engagées — l'alignement devient un standard d'annonce… à vérifier (annonce séance 7)
    - *Forme : exposé + décryptage d'un graphique d'alignement trajectoire | Source : 7.txt, chap. 7, slides 23–26*

33. **Scores ESG : ce qu'ils mesurent vraiment**
    - Construction : arbres de scoring (features → sous-scores → score agrégé pondéré) ; évaluations **relatives**, souvent intra-sectorielles — un « bon score » ≠ un faible impact
    - Désaccord des agences (Berg, Kölbel & Rigobon 2022) : corrélations entre agences 0,38–0,71 ; divergence due à la mesure (56 %), au périmètre (38 %), aux poids (6 %) ; suspicion de réécritures historiques de scores (Berg, Fabisik & Sautner 2021) qui change les relations ESG-rendements
    - Activités vs résultats (Serafeim 2022) : les données ESG captent surtout des **activités** (politiques, principes, cibles) et rarement des **résultats** effectifs — privilégier les métriques d'outcome
    - *Forme : analyse critique de captures de rapports d'agences (mêmes entreprises, notes différentes) | Source : 7.txt, chap. 7, slides 27–31*

34. **Métriques physiques et double matérialité**
    - Métriques physiques par usage (initiative NEC) : empreintes par unité d'usage (kWh fourni, km-passager, tonne produite), sur toute la chaîne de valeur, tous piliers environnementaux (climat, eau, biodiversité, ressources), score de −100 à +100 — bavures évitées de la normalisation monétaire
    - Wrap-up de la mesure (chap. 7) : cycle de vie complet « du berceau à la tombe », métriques **physiques** par usage, **tous** les enjeux environnementaux (pas seulement le climat)
    - **Double matérialité** : un investissement crédible atténue à la fois (i) le risque financier lié à l'environnement et (ii) l'empreinte environnementale — construction collective d'exemples et de contre-exemples
    - *Forme : co-construction en plénière (tableau exemples/contre-exemples) | Source : 7.txt, chap. 7, slides 32–41*

### Activité notebook et synthèse (slides 35–37, 40 min)

35. **Activité notebook — « Construire et critiquer une stratégie d'impact » (lancement, 3 min)**
    - Données fournies (échantillon de ~40 entreprises) : intensités carbone par scope, deux jeux de scores ESG (agences distinctes), parts vertes taxonomie, métriques d'émissions évitées avec deux baselines
    - Mission en binômes (≈ 28 min) : (1) construire un portefeuille « values-aligned » (exclusions + best-in-class) et un portefeuille « impact-oriented » (cible entreprises brunes à trajectoire de décarbonation, justification d'additionnalité) ; (2) comparer leurs métriques (empreinte, intensité, part verte) ; (3) identifier le canal d'impact invoqué par chaque stratégie (prix/CoC, engagement, financement direct) ; (4) critiquer la métrique la plus flatteuse
    - Livrable : trois réponses argumentées rédigées dans le notebook (les cellules-guides contiennent les amorces de code ; aucune manipulation avancée requise)
    - *Forme : TP guidé en binômes (consigne + amorces de code) | Source : apport propre IAM (données et implémentation) ; méthodes inspirées de 5.txt, chap. 5, slides 64–67 (spécification empirique) et 7.txt (métriques)*

36. **Débrief du notebook (≈ 6 min)**
    - Mise en commun : mêmes entreprises, métriques différentes — pourquoi les deux portefeuilles peuvent afficher des empreintes similaires tout en ayant des impacts très différents ?
    - Pièges à faire émerger : intensité ≠ absolu ; exclusion ≠ additionnalité ; désaccord ESG ; baselines des évitées ; le portefeuille « impact » est souvent **plus brown** en empreinte — c'est voulu
    - Contrepoint quantitatif : mettre les résultats en perspective avec l'élasticité estimée (doublement de la part verte → −4,9 %/an) : ordre de grandeur à la main sur le portefeuille construit
    - *Forme : discussion collective structurée (2 binômes présentent, la classe complète) | Source : apport propre IAM ; 5.txt, chap. 5, slide 69*

37. **Synthèse finale et ouverture**
    - Réponse construite à la question du jour : l'investisseur **peut** avoir un impact réel, mais (i) l'exclusion agit surtout par signal et à grande échelle ; (ii) l'engagement est en général le canal le plus efficace sur liste ; (iii) l'impact investing exige l'additionnalité — financer ce que le marché ordinaire ne financerait pas ; (iv) l'effet coût du capital est réel mais modeste (−4,9 %/an pour un doublement des encours verts) ; (v) la mesure est le maillon faible — exigez métriques physiques, outcomes et double matérialité
    - Reformulation du fil rouge par 2–3 étudiants (l'enseignant complète) : aligner son portefeuille ≠ aligner l'économie
    - Ouverture vers la séance 7 — **Crédibilité et institutions** : taxonomies, labels, régulateurs, engagements net zéro — qui garantit que les promesses d'impact sont tenues ?
    - *Forme : synthèse interactive + slide d'ouverture | Source : apport propre IAM (synthèse) ; 5.txt, chap. 5, slide 70 (recommandations finales)*

---

## Statut et règles de production

- Ce document est une **proposition de plan**, pas encore le jeu de slides final.
- Le futur deck réutilisera le système Beamer des supports des séances précédentes.
- Une slide **Plan** (slide 4) suit immédiatement l'introduction substantielle ; le plan est rappelé à chaque grande transition (slides 5, 14, 18, 28, 35).
- Les formulations et figures d'O. David Zerbib sont des sources de fond **citées et transformées**, jamais recopiées sans attribution.
- Aucune modalité d'évaluation ni règle institutionnelle n'est définie dans ce plan ; l'activité notebook est un exercice de séance dont les supports (notebook étudiant et corrigé aligné cellule par cellule) restent à produire.
