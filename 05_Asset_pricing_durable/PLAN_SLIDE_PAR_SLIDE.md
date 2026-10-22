# Séance 5 — Asset pricing durable : le vert a-t-il un prix ?

**Cours :** Finance verte — Master IEFM · **Durée :** 3 h (180 min) · **Support :** 37 slides
**Sources principales :** cours « Green Finance » d'Olivier David Zerbib (CREST–ENSAE, Institut Polytechnique de Paris), fichiers `/tmp/david-zerbib-finance-verte/` :
- `2.txt` — ch. 2 « Introduction to portfolio allocation and asset pricing »
- `3.txt` — ch. 3 « Sustainable asset pricing »
- `6.txt` — ch. 6 « "Green" assets »

Tout le contenu issu de ces supports est **reformulé et adapté** (jamais recopié). Les éléments construits pour la séance sont signalés « apport propre IAM ».

---

## Objectifs d'apprentissage

À l'issue de la séance, l'étudiant·e doit pouvoir :

1. Réactiver le cadre CAPM (frontière efficiente, CML, SML, bêta, estimation two-pass Fama-MacBeth) et l'utiliser comme langage commun de l'asset pricing.
2. Présenter les trois familles d'outils empiriques reliant performance environnementale et rendements (event study, analyse factorielle, approche standard sur portefeuilles triés) et leurs biais majeurs (causalité inverse, mesure, variables omises).
3. Expliquer, dans le cadre d'équilibre de Pástor–Stambaugh–Taylor (2021), comment les **préférences vertes** et le **risque climatique** abaissent tous deux le rendement attendu des actifs verts, et pourquoi il faut empiriquement les distinguer.
4. Définir le **greenium actions** et le mesurer **ex ante** (coût implicite du capital) et **ex post** (contrôle des chocs de préoccupations climatiques et de résultats) d'après Pástor–Stambaugh–Taylor (2022), en gardant la distinction rendements réalisés / rendements attendus.
5. Manipuler le **S-CAPM** de Zerbib (2022) : primes de goût et primes d'exclusion, estimation structurelle via les holdings de fonds verts, passage à la valorisation (DCF).
6. Transposer au marché obligataire : greenium des obligations vertes (Zerbib 2019), limites structurelles des green bonds et design des sustainability-linked bonds (SLB).

---

## Timing général (180 min)

| Étape | Intitulé | Slides | Durée |
|---|---|---|---|
| 0 | Introduction substantielle et plan | 1–2 | 10 min |
| 1 | Rappels : du portefeuille au CAPM (compact) | 3–6 | 17 min |
| 2 | Boîte à outils empirique : ESG et rendements | 7–12 | 26 min |
| 3 | Théorie : préférences vertes vs risque climatique (PST 2021) | 13–18 | 24 min |
| 4 | Greenium ex ante / ex post (PST 2022) et contrepoints | 19–23 | 19 min |
| 5 | Atelier notebook (activité) | 24–26 | 41 min |
| 6 | S-CAPM (Zerbib 2022) : goûts, exclusion, valorisation | 27–32 | 23 min |
| 7 | Dette verte : obligations vertes et SLB | 33–36 | 15 min |
| 8 | Synthèse finale | 37 | 5 min |
| | **Total** | **37 slides** | **180 min** |

---

## Déroulé slide par slide

### Slide 1 — Asset pricing durable : le vert a-t-il un prix ? (durée : 8 min · étape 0)

**Contenu :**
1. Accroche : en asset pricing, « payer cher » un actif, c'est accepter un rendement attendu faible. Si les investisseurs préfèrent les actifs verts, ils doivent accepter un rendement moindre : un éventuel « greenium » se lit dans les prix, pas dans les discours.
2. Tension centrale de la séance : un même constat empirique (le vert a surperformé depuis 2012) peut avoir trois origines différentes — des préférences (goûts), une couverture du risque climatique, ou de simples flux de demande — et l'on n'observe jamais que des rendements **réalisés**, jamais les rendements **attendus** qui fondent la théorie.
3. Promesse de la séance : outiller la réponse en sept étapes — rappels CAPM, outils empiriques, cadre d'équilibre (préférences vs risque climatique), mesure du greenium ex ante/ex post, atelier notebook, S-CAPM (goûts + exclusion) et dette verte.
4. Lien avec les séances précédentes : les IAM fournissent scénarios climatiques et coût social du carbone ; la question du jour est de savoir si les marchés financiers intègrent déjà ces risques et ces préférences dans les prix.

**Forme pédagogique :** exposé d'ouverture + sondage à main levée (« accepteriez-vous 1 % de rendement en moins pour un portefeuille aligné ? ») pour installer la question.

**Source :** apport propre IAM (texte d'introduction rédigé pour la séance) ; cadrage en écho à `3.txt`, ch. 3, slide 29 (« rendements attendus vs réalisés ») et `2.txt`, ch. 2.

### Slide 2 — Plan de la séance (durée : 2 min · étape 0)

**Contenu :**
1. Étape 1 — Rappels : du portefeuille au CAPM (slides 3–6).
2. Étape 2 — Boîte à outils empirique : ESG et rendements (slides 7–12).
3. Étape 3 — Théorie : préférences vertes vs risque climatique, PST 2021 (slides 13–18).
4. Étape 4 — Greenium ex ante / ex post, PST 2022, et contrepoints (slides 19–23).
5. Étape 5 — Atelier notebook (slides 24–26, ≈ 40 min).
6. Étape 6 — S-CAPM Zerbib 2022 : goûts, exclusion, valorisation (slides 27–32).
7. Étape 7 — Dette verte : obligations vertes et SLB (slides 33–36).
8. Étape 8 — Synthèse (slide 37).

**Forme pédagogique :** lecture guidée du plan, annonce des transitions et de l'activité notebook ; contrat de séance affiché.

**Source :** apport propre IAM.

### Slide 3 — Transition : pourquoi rappeler le CAPM ? (durée : 1 min · étape 1)

**Contenu :**
1. Rappel de plan : introduction faite, on entre dans l'étape 1/8 (rappels) ; s'ensuivront outils empiriques, théorie, greenium, atelier, S-CAPM, dette verte, synthèse.
2. Objectif du bloc : remettre à plat en 15 minutes le vocabulaire qui servira toute la séance — prime de risque, bêta, alpha, coût du capital, estimation two-pass.
3. Annonce : le CAPM sera « très compact », l'effort portera ensuite sur son extension durable.

**Forme pédagogique :** transition orale rapide, plan projeté avec bloc courant surligné.

**Source :** apport propre IAM (structure) ; notions couvertes par `2.txt`, ch. 2.

### Slide 4 — De l'allocation de portefeuille à la frontière efficiente (durée : 4 min · étape 1)

**Contenu :**
1. Un actif risqué + un actif sans risque : `μ = rf + (σ/σ1)(μ1 − rf)` — l'ensemble d'opportunité est une droite dont la pente est le ratio de Sharpe, « prix de la réduction de risque ».
2. Deux puis n actifs risqués : la frontière (parabole en (μ, σ²), hyperbole en (μ, σ)) ; la diversification fait chuter le risque spécifique.
3. Ajout de l'actif sans risque : la ligne de marché des capitaux (CML) domine toutes les frontières internes ; théorème de séparation — chacun détient le portefeuille tangent combiné à l'actif sans risque.

**Forme pédagogique :** dérivation au tableau + graphique commenté ; question posée à la classe : « pourquoi, en tant qu'investisseur, vous souciez-vous du ratio de Sharpe ? ».

**Source :** `2.txt`, ch. 2, slides 2–10 (formules et figures reformulées).

### Slide 5 — Le CAPM en une équation (durée : 7 min · étape 1)

**Contenu :**
1. Hypothèses : modèle à une période, préférences moyenne-variance (utilité exponentielle, rendements gaussiens), concurrence pure, absence de frictions, information homogène et gratuite, équilibre (offre = demande).
2. Dérivation : la demande optimale `s = (1/γ)·Σ⁻¹(μ − rf·1)`, agrégée via le clearing, donne `E(ri) − rf = βi·(E(rm) − rf)` — la Security Market Line.
3. Interprétation : seul le risque **systématique** est rémunéré, car le risque idiosyncratique s'élimine par diversification ; le bêta est la mesure standardisée du risque pertinent.
4. Repère graphique : SML et bêta comme moteur de la volatilité de l'actif.

**Forme pédagogique :** dérivation guidée pas-à-pas ; question de classe : « pourquoi seul le risque systématique est-il prix dans le CAPM ? » (réponse construite collectivement).

**Source :** `2.txt`, ch. 2, slides 13–19 (reformulé).

### Slide 6 — À quoi servent les rendements attendus ? Coût du capital, alpha, estimation (durée : 5 min · étape 1)

**Contenu :**
1. Usage 1 — coût du capital et prix : le rendement attendu sert de taux d'actualisation des flux futurs (mini-exercice : flux de 10 pendant 5 ans, prime de marché 3 %, β = 1,2 → coût du capital puis prix).
2. Usage 2 — évaluation de fonds : l'alpha mesure la performance créée au-delà de la compensation du risque.
3. Estimation empirique : `ri − rf = β(rm − rf) + ε` ; procédure two-pass de Fama-MacBeth (bêta sur fenêtre glissante de 5 ans, régressions en coupe, moyenne des primes).
4. Ouverture multifactorielle : Fama-French 3 facteurs (SMB, HML) puis Carhart (MOM) — tous les risques systématiques ne se résument pas au marché.

**Forme pédagogique :** mini-exercice flash (calculatrice) + schéma de la procédure two-pass au tableau.

**Source :** `2.txt`, ch. 2, slides 20–24 (exercices et méthodes reformulés).

### Slide 7 — Transition : ESG et rendements, que mesure-t-on vraiment ? (durée : 1 min · étape 2)

**Contenu :**
1. Rappel de plan : étape 1/8 terminée, entrée dans l'étape 2/8 (outils empiriques) ; viendront ensuite théorie, greenium, atelier, S-CAPM, dette verte, synthèse.
2. Question-pont : un score environnemental explique-t-il les rendements **au-delà** du bêta du CAPM ?
3. Annonce : trois familles de méthodes, leurs biais, puis trois études fondatrices sur le coût du capital.

**Forme pédagogique :** transition orale, plan surligné, question affichée.

**Source :** apport propre IAM.

### Slide 8 — Trois familles d'études empiriques (durée : 5 min · étape 2)

**Contenu :**
1. Event study : choc exogène (ex. introduction d'une régulation) ; estimation des rendements « normaux » pré-événement, calcul des rendements anormaux `AR = R − R*`, analyse des CAR pré/post avec contre-factuels appariés.
2. Analyse factorielle : régression du facteur vert `R_GMB` sur marché, SMB, HML, MOM — l'alpha capture-t-il une prime verte autonome ?
3. Approche panel (hors standard) : effets fixes firmes et temps, `R_it = α_i + α_t + λ·β_mkt + β_GMB·EP_it + X_it + ε` — corrélation conditionnelle entre performance environnementale (EP) et rendements.

**Forme pédagogique :** exposé dialogué ; tableau comparatif rempli au tableau (question posée, données, menace principale).

**Source :** `3.txt`, ch. 3, slides 2–3 (méthodes reformulées).

### Slide 9 — L'approche asset pricing standard : portefeuilles triés et two-pass (durée : 5 min · étape 2)

**Contenu :**
1. Principe : trier les actions par « greenness » (quintiles), estimer `R_it = α_i + λ_mkt·β_mkt,i + λ_green·β_GMB,i (+ SMB, HML, MOM)` en coupe croisée.
2. Deux passes à la Fama-MacBeth : (i) bêta estimé par action sur fenêtre glissante T1, (ii) primes `λ` estimées en coupe à chaque date puis moyennées.
3. Lecture : `λ_green` est le prix du risque vert ; la comparaison des spécifications avec/sans facteurs classiques dit si le vert est un facteur propre.

**Forme pédagogique :** schéma des deux passes au tableau, en écho explicite à la slide 6.

**Source :** `3.txt`, ch. 3, slide 4 ; `2.txt`, ch. 2, slide 22 (méthode reformulée).

### Slide 10 — Pièges et limites des mesures ESG–rendements (durée : 5 min · étape 2)

**Contenu :**
1. Causalité inverse : la performance financière peut financer la performance environnementale — le sens de la flèche n'est pas garanti.
2. Erreur de mesure : indicateurs environnementaux non standardisés ; forte divergence des notateurs (corrélation moyenne ≈ 42,9 % entre six grands fournisseurs sur 2013–2017) ; agrégation « forces − faiblesses » (KLD) critiquée comme perte d'information.
3. Variables omises (engagement actionnarial, notoriété client) et difficulté d'obtenir de longues historiques.

**Forme pédagogique :** discussion dirigée : « quel biais menace quelle méthode ? » — les étudiants rattachent chaque biais à une des trois familles de la slide 8.

**Source :** `3.txt`, ch. 3, slides 5 et 22 (reformulé).

### Slide 11 — Environnement et coût du capital : trois preuves fondatrices (durée : 6 min · étape 2)

**Contenu :**
1. Sharfman & Fernando (2008) : une meilleure gestion du risque environnemental s'accompagne d'un WACC plus faible (S&P 500 ; indicateur construit par ACP sur données TRI et KLD ; contrôles industrie, taille, levier).
2. El Ghoul et al. (2011) : la dimension environnementale de la RSE réduit le coût des fonds propres **implicite** (moyenne de quatre modèles : Claus-Thomas, Gebhardt, Ohlson-Juettner-Nauroth, Easton) ; robustesse aux biais d'optimisme des analystes et à l'endogénéité (variables instrumentales).
3. Chava (2014) : le coût implicite du capital augmente avec les « concerns » environnementales (déchets dangereux, émissions, revenus charbon/pétrole) mais ne diminue pas avec les « strengths » ; le coût de la dette augmente avec les concerns et diminue avec les strengths.

**Forme pédagogique :** mini-présentations éclair (une étude = 2 min) ; fil rouge commun : « signal environnemental → risque perçu → taux exigé ».

**Source :** `3.txt`, ch. 3, slides 6–21 (reformulé).

### Slide 12 — « Being green » récompensé ? et le pivot critique (durée : 4 min · étape 2)

**Contenu :**
1. In, Park & Monk : intensité carbone scopes 1+2+3 rapportée au chiffre d'affaires (données Trucost) ; portefeuilles EMI (tri simple puis doubles tris valeur/croissance et taille) ; alphas 2010–2015 compris entre ≈ 2,6 % et ≈ 7 %/an selon les spécifications.
2. Mais la mesure est fragile : données environnementales critiquées (transparence, comparabilité) et variable carbone seulement partielle.
3. Pivot de la séance : différence entre rendements attendus et réalisés — les rendements réalisés sont-ils un bon proxy des rendements attendus ? → il faut un cadre d'équilibre.

**Forme pédagogique :** bascule magistrale : lecture de graphiques d'alphas, puis question écrite au tableau et laissée ouverte.

**Source :** `3.txt`, ch. 3, slides 22–29 (reformulé).

### Slide 13 — Transition : deux lectures concurrentes du même constat (durée : 1 min · étape 3)

**Contenu :**
1. Rappel de plan : étapes 1–2/8 faites ; on entre dans la théorie (étape 3/8) : PST 2021 ; puis greenium (4), atelier (5), S-CAPM (6), dette verte (7), synthèse (8).
2. Deux explications concurrentes du « vert qui rapporte » : des préférences (on aime le vert, on accepte un rendement moindre) ou un rôle d'assurance (le vert protège du risque climatique).
3. Annonce : le modèle de Pástor–Stambaugh–Taylor (2021) formalise les deux canaux.

**Forme pédagogique :** transition orale, plan surligné, dilemma affiché en une ligne.

**Source :** apport propre IAM (articulation) ; contenu à venir `3.txt`, ch. 3, slides 31–38.

### Slide 14 — PST 2021 : le cadre et la demande avec goûts (durée : 5 min · étape 3)

**Contenu :**
1. Cadre : une période, N firmes, rendements excédentaires gaussiens, et une caractéristique ESG observable `g_n` par action.
2. Utilité exponentielle enrichie d'un bénéfice **non pécuniaire** : `b_i = d_i · g` — `d_i` mesure le « goût » ESG de l'investisseur i.
3. Demande optimale `X_i = (1/a_i)·Σ⁻¹(μ + b_i)` : l'investisseur surpondère (ou sous-pondère) l'action n par rapport aux poids « CAPM » selon son goût `d_i` et le score `g_n`.

**Forme pédagogique :** construction pas-à-pas au tableau ; question intermédiaire : « que devient la demande si d_i = 0 ? » (retour au CAPM).

**Source :** `3.txt`, ch. 3, slides 31–32 (reformulé).

### Slide 15 — PST 2021 : l'équilibre, ou le prix du goût (durée : 5 min · étape 3)

**Contenu :**
1. Rendements d'équilibre : `μ = μ_m·β_m − (d̄/a)·g` — les investisseurs acceptent un rendement attendu plus faible sur les actifs qu'ils aiment (verts) et en exigent plus sur ceux qu'ils délaissent (bruns).
2. La prime de marché elle-même s'ajuste à la baisse (terme lié à `d̄·ḡ`) : le greenium est un phénomène d'équilibre, pas une anomalie à exploiter.
3. À retenir : prix = compensation du risque − valeur du goût ; un investisseur « neutre » capte un alpha si les autres ont des goûts.

**Forme pédagogique :** lecture économique ligne à ligne de l'équation ; vérification de compréhension par deux questions rapides.

**Source :** `3.txt`, ch. 3, slide 33 (reformulé).

### Slide 16 — PST 2021 : séparation à trois fonds et facteur ESG (durée : 5 min · étape 3)

**Contenu :**
1. Séparation à trois fonds : `w_i = (1 − φ_i)·w_m + φ_i·w_g` — portefeuille de marché + portefeuille vert (long vert / short brun), avec `φ_i` croissant de l'écart de goût `δ_i`.
2. Cas limite éclairant : si tous les goûts sont identiques (`δ_i = 0`), personne ne tilt et « l'industrie ESG n'existe pas » — la dispersion des préférences conditionne l'existence du greenium.
3. Le facteur ESG `f_g` (moyenne pondérée par g des rendements ajustés du marché) : une réalisation positive fait surperformer le vert et sous-performer le brun.

**Forme pédagogique :** analogie « deux fonds » (écho au théorème de séparation de la slide 4) ; quiz express sur le cas `δ_i = 0`.

**Source :** `3.txt`, ch. 3, slides 34–36 (reformulé).

### Slide 17 — PST 2021 : extension au risque climatique — goût vs assurance (durée : 4 min · étape 3)

**Contenu :**
1. Extension : l'état du climat `C̃` entre dans l'utilité ; `μ = μ_m·β_m − (d̄/a)·g + c̄·(1 − ρ_mC)·ψ`, où `ψ` est le vecteur des « climate betas » (sensibilités des rendements au climat).
2. Une action qui **couvre** le risque climatique (`ψ < 0`) a un rendement attendu plus faible — exactement comme un actif aimé pour des raisons de goût.
3. Conséquence méthodologique : deux canaux, même direction sur les prix (le vert « cher »), mais interprétations opposées (préférence vs assurance) — l'enjeu empirique est de les distinguer.

**Forme pédagogique :** mini-débat en binômes (2 min) : « comment distinguer empiriquement un goût d'une couverture de risque ? » ; mise en commun de 2 réponses.

**Source :** `3.txt`, ch. 3, slides 37–38 (reformulé).

### Slide 18 — Ce que PST 2021 prédit, et comment le tester (durée : 4 min · étape 3)

**Contenu :**
1. Prédictions testables : (i) un greenium négatif en termes de rendements **attendus** ; (ii) les actions vertes surperforment quand les préoccupations climatiques montent de façon inattendue (réalisation positive du facteur ESG) ; (iii) un effet plus fort pour les actifs couvrant le climat.
2. Tableau « prédiction → test » rempli avec la classe : mesure ex ante par coût implicite du capital ; mesure ex post par régressions contrôlant les chocs.
3. Annonce du passage à PST 2022 : mesurer enfin le greenium actions.

**Forme pédagogique :** construction collective du tableau prédiction/test au tableau.

**Source :** `3.txt`, ch. 3, slides 36–38 (prédictions) ; articulation : apport propre IAM.

### Slide 19 — Transition : greenium, deux mesures pour un prix (durée : 1 min · étape 4)

**Contenu :**
1. Rappel de plan : théorie posée (étape 3/8) ; on entre dans l'étape 4/8 — la mesure du greenium selon PST 2022 ; suivent atelier (5), S-CAPM (6), dette verte (7), synthèse (8).
2. Définition du jour : le greenium actions = l'écart de **rendement attendu** vert − brun (spread GMB).
3. Deux mesures complémentaires : ex ante (coût implicite du capital) et ex post (rendements contrôlés des chocs).

**Forme pédagogique :** transition orale, définition encadrée au tableau.

**Source :** apport propre IAM ; définition issue de `3.txt`, ch. 3, slide 42.

### Slide 20 — PST 2022 : score vert ajusté et portefeuille GMB (durée : 5 min · étape 4)

**Contenu :**
1. Score vert ajusté de l'industrie : `G_i = −(10 − Escore) × Eweight/100` (données MSCI) — un pétrolier est comparé aux pétroliers, pas aux distributeurs ; centrage par la moyenne pondérée.
2. Portefeuille GMB (long tiers supérieur de greenness, short tiers inférieur) : **+174 % de 2012 à 2020, soit ≈ 65 bps/mois**.
3. Nuance essentielle : l'alpha du GMB face aux facteurs Fama-French est significatif (le vert n'est pas un simple mix de facteurs connus), mais sa performance a été portée par les large caps, les « growth » et le momentum récent.

**Forme pédagogique :** lecture guidée du graphique GMB cumulé ; question : « un alpha significatif prouve-t-il un greenium attendu ? ».

**Source :** `3.txt`, ch. 3, slides 39–41 (reformulé).

### Slide 21 — Greenium ex ante : le coût implicite du capital (durée : 4 min · étape 4)

**Contenu :**
1. Principe : combiner prix de marché et flux prévus pour inférer, par la formule d'actualisation standard, le taux implicite de chaque action — puis comparer vert et brun.
2. Résultat PST 2022 : greenium ex ante ≈ **−12 bps/mois** — le marché anticipe un rendement plus faible sur le vert.
3. Interprétation : cohérent avec le canal des goûts (PST 2021) : on paie cher le vert en espérance ; écho direct aux mesures d'ICC d'El Ghoul et Chava (slide 11).

**Forme pédagogique :** schéma du DCF implicite au tableau ; question flash : « pourquoi ce greenium ex ante ne garantit pas une surperformance future ? ».

**Source :** `3.txt`, ch. 3, slide 42 (reformulé).

### Slide 22 — Greenium ex post : contrôler les chocs de demande (durée : 5 min · étape 4)

**Contenu :**
1. Problème : le rendement réalisé contient des chocs à espérance nulle — chocs de préoccupations climatiques et nouvelles de résultats — qui masquent l'espérance.
2. Méthode : `r_t = a + b·x_t + ε_t` avec `x_t` = chocs de préoccupations climatiques (indice MCCC d'Ardia et al. 2021 ; erreurs de prévision d'un AR(1)) et mesures de news de résultats (annonces et guidance).
3. Résultats : une fois les chocs contrôlés, le rendement attendu du GMB devient négatif **non significatif** (≈ −4 à −15 bps/mois) ; les actions vertes surperforment quand les préoccupations climatiques montent — réconciliation réalisé/attendu.

**Forme pédagogique :** lecture de tableaux de régression guidée (identifier a, b, interpréter la significativité).

**Source :** `3.txt`, ch. 3, slides 43–48 (reformulé).

### Slide 23 — Décomposition across/within et contrepoints : goûts, flux ou risque ? (durée : 4 min · étape 4)

**Contenu :**
1. Décomposition PST 2022 : l'essentiel de la performance du GMB vient de la greenness **au niveau des industries** (across), pas du positionnement intra-industrie (within).
2. Contrepoint « flux » (van der Beck, 2025) : ≈ 3 500 Md$ de flux institutionnels vers l'ESG ; 1 $ redirigé ≈ +0,7 $ de valorisation ESG ; rendement induit par les flux ≈ 1,9 %/an — la surperformance observée serait surtout un effet de demande, pas une prime attendue.
3. Contrepoint « prix » (Cheng, Jondeau, Mojon, Vayanos, 2025) : l'impact des investisseurs verts sur les prix est modeste selon les calibrations réalistes (≈ 0,2 % à 6,3 %, davantage si leur part double), et amplifié par la présence de risque climatique.

**Forme pédagogique :** débat structuré « goûts, flux ou risque ? » : vote à main levée, deux argumentaires opposés, synthèse de l'enseignant.

**Source :** `3.txt`, ch. 3, slides 49–51, 99–112 et 113–129 (reformulé).

### Slide 24 — Transition : place à l'atelier notebook (durée : 2 min · étape 5)

**Contenu :**
1. Rappel de plan : mesures du greenium vues (étape 4/8) ; place à l'atelier (étape 5/8) ; resteront S-CAPM (6), dette verte (7), synthèse (8).
2. Consignes : notebook en trois étapes — (i) bêtas et alphas CAPM, (ii) tri vert/brun et portefeuille GMB, (iii) alpha du GMB face aux facteurs et discussion réalisé/attendu.
3. Organisation : binômes, ≈ 40 min au total, jalons chronométrés, restitution courte en fin d'atelier.

**Forme pédagogique :** consignes opérationnelles projetées ; formation des binômes ; vérification que tous ont le notebook ouvert.

**Source :** apport propre IAM (notebook construit pour la séance) ; méthodes fondées sur `2.txt`, ch. 2, slides 22–24 et `3.txt`, ch. 3, slides 4 et 39–41.

### Slide 25 — Atelier notebook : estimer soi-même un « GMB » (durée : 32 min · étape 5)

**Contenu :**
1. Étape 1 (≈ 10 min) : estimer le bêta et l'alpha CAPM d'un échantillon d'actions (régression temporelle sur fenêtre glissante).
2. Étape 2 (≈ 12 min) : trier selon un score de greenness fourni, construire le portefeuille long vert / short brun, estimer son alpha face aux facteurs marché, SMB, HML, MOM.
3. Étape 3 (≈ 10 min) : interpréter — cet alpha est-il une prime attendue, un choc de demande, un artefact de mesure ? Formuler une hypothèse testable avec les chocs de préoccupations climatiques.

**Forme pédagogique :** travail en binômes sur notebook ; enseignant en tutorat circulant ; jalons affichés au tableau à 10, 22 et 32 min.

**Source :** apport propre IAM (notebook) ; méthodes : `2.txt`, ch. 2, slide 22 (two-pass) ; `3.txt`, ch. 3, slides 4 et 39–41 (tri GMB et alphas).

### Slide 26 — Mise en commun de l'atelier (durée : 7 min · étape 5)

**Contenu :**
1. Restitution de 2–3 binômes : bêtas/alphas obtenus, signe et magnitude de l'alpha du GMB.
2. Confrontation avec la littérature : +174 % pour le GMB 2012–2020 chez PST 2022, alpha significatif face à Fama-French, mais sensibilité aux chocs de préoccupations climatiques.
3. Synthèse des embûches rencontrées (mesure de la greenness, période courte, facteurs omis) — transition vers le modèle structurel.

**Forme pédagogique :** débriefing collectif au tableau ; grille récapitulative remplie en direct.

**Source :** apport propre IAM ; repères chiffrés : `3.txt`, ch. 3, slides 40–48.

### Slide 27 — Transition : du constat empirique au modèle structurel (durée : 1 min · étape 6)

**Contenu :**
1. Rappel de plan : atelier terminé (étape 5/8) ; on entre dans l'étape 6/8 — le S-CAPM de Zerbib (2022) ; resteront dette verte (7) et synthèse (8).
2. Limite des approches précédentes : elles traitent les préférences « en bloc » ; or exclusion (boycott) et intégration des goûts sont deux mécanismes distincts.
3. Annonce : un modèle qui sépare les deux canaux et permet de valoriser une entreprise.

**Forme pédagogique :** transition orale, plan surligné.

**Source :** apport propre IAM ; contenu à venir `3.txt`, ch. 3, slides 52–98.

### Slide 28 — Zerbib (2022) : motivation et contributions (durée : 4 min · étape 6)

**Contenu :**
1. La question reste ouverte : les préférences durables abaissent-elles les rendements attendus, et par quel canal — exclusion (une part d'investisseurs refuse les actifs « bruns ») ou intégration (les goûts entrent dans l'utilité) ?
2. Deux littératures séparées jusqu'ici : exclusion des « sin stocks » (Hong-Kacperczyk, Luo-Balvers) vs intégration des goûts (PST 2021, Pedersen et al.) — le S-CAPM unifie les deux dans un cadre de **segmentation partielle** et de **goûts hétérogènes**.
3. Contributions : théorie (primes de goût + primes d'exclusion, forme généralisée de la prime de Merton 1987 sur les actions négligées) ; estimation structurelle sur sin stocks (prime d'exclusion ≈ 1,5 %/an) et sur les goûts via les holdings de fonds verts (≈ 0,50 %/an entre industries vertes et brunes) ; effets croisés faibles mais significatifs.

**Forme pédagogique :** exposé dialogué ; carte des contributions (théorie / empirique) projetée et commentée.

**Source :** `3.txt`, ch. 3, slides 52–58 (reformulé).

### Slide 29 — Le S-CAPM : segmentation partielle, goûts, et l'équation d'équilibre (durée : 5 min · étape 6)

**Contenu :**
1. Deux frictions : une part `p` d'« intégrateurs » internalise un coût d'externalité environnementale `c_i` dans leur utilité ; une part `q` d'« exclueurs » ne peut détenir les actifs exclus `X` — le marché est partiellement segmenté.
2. Équation d'équilibre (proposition centrale) : `E(r_k) = β_km·E(r_mI) − p·c_mI + p·B_kI·C` (prime de goût) `+ γ·q/(1−p)·Cov(r_k, r_mX|r_I)` (prime d'exclusion de l'actif) `+ γ·q·Cov(r_k, r_mX|r_mI)` (prime de segmentation du marché).
3. Cas limites éclairants : sans exclusion (`q = 0`) → cadre type Acharya-Pedersen (2005) ; sans goûts (`c = 0`) → de Jong-de Roon (2005) ; les primes d'exclusion généralisent la prime de Merton (1987) sur les actions négligées.

**Forme pédagogique :** dérivation présentée pas-à-pas ; équation coloriée au tableau (une couleur par composante de prime).

**Source :** `3.txt`, ch. 3, slides 59–75 (reformulé).

### Slide 30 — Lire les primes : goût, exclusion-actif, exclusion-marché (durée : 4 min · étape 6)

**Contenu :**
1. Prime de goût, double effet : prime directe `p·c_i` sur l'actif (l'investisseur exige moins de rendement pour un actif « vert » à ses yeux) et ajustement de la prime de marché `−p·c_m` ; l'effet total dépend du bêta.
2. Primes d'exclusion, double effet : sur-prime des actifs exclus (les non-exclueurs exigent une compensation pour porter ce que d'autres refusent — logique « super risk premium ») et prime de segmentation qui frappe **tous** les actifs corrélés au marché exclu.
3. Le signe des primes d'exclusion n'est pas garanti actif par actif : il dépend des corrélations ; il est positif en moyenne sur le portefeuille exclu.

**Forme pédagogique :** quiz express : trois situations projetées, associer chaque situation à la prime concernée.

**Source :** `3.txt`, ch. 3, slides 71–75 (reformulé).

### Slide 31 — Estimer le S-CAPM : goûts révélés par les holdings, exclusion des sin stocks (durée : 4 min · étape 6)

**Contenu :**
1. Proxy des goûts « révélés » : écart entre l'allocation des fonds verts et les poids de marché par industrie (`c̃_i,t`), et part de marché des fonds verts `p̃` (passée de 0,02 % à 0,12 % de 2007 à 2019) — mesure qui contourne les biais des notations ESG.
2. Résultats côté goûts : prime de goût directe ≈ 0,50 %/an entre industries vertes et brunes (ex. écart pétrole vs équipement électrique ≈ 50 bps/an) ; robuste au contrôle des chocs de goûts et à la causalité inverse.
3. Résultats côté exclusion : sur 77 sin stocks, prime d'exclusion ≈ 1,5 %/an (jusqu'à ≈ 2,8 %/an selon la spécification), cohérente avec Hong-Kacperczyk ; part d'exclueurs implicite ≈ 20 % ; prime négative pour 33 des 77 titres, comme le prédit la théorie.

**Forme pédagogique :** lecture guidée de tableaux Fama-MacBeth ; questions ciblées sur la robustesse.

**Source :** `3.txt`, ch. 3, slides 77–94 (reformulé).

### Slide 32 — Valoriser une entreprise avec le S-CAPM (durée : 5 min · étape 6)

**Contenu :**
1. Version simplifiée pour le DCF : `E(r_i) = β_i·E(r_m) + p·c_i` (avec `c_m ≈ 0` validé empiriquement) — le coût du capital inclut le coût des externalités tel que perçu par la part `p` d'investisseurs verts.
2. Exercice chiffré : β = 1,15 ; `E(r_m)` = 0,64 % ; p = 20 % ; `c_i` = 1 % → coût du capital ≈ 0,93 % contre ≈ 0,73 % au CAPM standard ; avec des flux de 5, 10 et 15 sur trois ans, la valeur passe de ≈ 29,50 à ≈ 29,36.
3. Lecture : la valeur baisse car les investisseurs verts internalisent le coût des externalités ; en pratique, on utilise soit les goûts estimés par industrie, soit des hypothèses explicites sur p et c.

**Forme pédagogique :** exercice guidé au tableau (calculatrice) ; débriefing : que change p = 40 % ? que change c = 0 ?

**Source :** `3.txt`, ch. 3, slides 95–98 (exercice adapté).

### Slide 33 — Transition : des actions à la dette verte (durée : 1 min · étape 7)

**Contenu :**
1. Rappel de plan : S-CAPM traité (étape 6/8) ; on entre dans l'étape 7/8 — obligations vertes et SLB ; puis synthèse (8/8).
2. Question-pont : le greenium se mesure-t-il aussi sur la dette, où le prix est un taux et non un multiple ?
3. Annonce : cadres de marché (GBP, EU GBS), greenium obligataire (Zerbib 2019), puis SLB.

**Forme pédagogique :** transition orale, plan surligné.

**Source :** apport propre IAM ; contenu à venir `6.txt`, ch. 6.

### Slide 34 — Obligations vertes : définitions, cadres de marché, ordre de grandeur (durée : 5 min · étape 7)

**Contenu :**
1. Définitions : green bond (dette d'émetteur affectée à des projets à bénéfice environnemental direct, vérifiable par un tiers) vs green project bond (émis via un SPV, remboursé uniquement par les flux du projet) ; écosystème plus large : green project equity, bâtiments verts, fonds labellisés.
2. Green Bond Principles (ICMA) : quatre composantes — usage des fonds, processus d'évaluation et de sélection, gestion des fonds, reporting — renforcées par une revue externe (second party opinion, vérification, certification, notation) ; mouvement vers un standard européen (EU GBS).
3. Ordre de grandeur : ≈ 700 Md$ émis en 2024, ≈ 3 400 Md$ d'encours, soit 2–3 % du marché obligataire mondial (Climate Bonds Initiative, SIFMA, BIS).

**Forme pédagogique :** exposé illustré ; commentaire d'un exemple d'« usage of proceeds » projeté.

**Source :** `6.txt`, ch. 6, slides 2–16 (reformulé).

### Slide 35 — Le greenium obligataire : Zerbib (2019) (durée : 5 min · étape 7)

**Contenu :**
1. Méthode : apparier chaque green bond à des obligations conventionnelles similaires (rendement synthétique par interpolation des maturités), contrôler l'écart de liquidité `ΔBA`, effet fixe par obligation : `Δỹ = p_i + β·ΔBA + ε` — la prime verte `p_i` est identifiée par différence.
2. Résultat : prime moyenne ≈ **−2 bps** (63 % des primes négatives), significative en EUR, USD et pour les financières, ≈ −3 bps pour les AA — très en dessous des −17 à −18 bps estimés par d'autres approches (Barclays ; Ehlers-Packer).
3. Propriétés et limites : la prime ne reflète pas un risque plus faible, n'est pas une prime de marché, négative et stable depuis mai 2016 ; limites structurelles des green bonds : engagement sans valeur juridique, absence d'exigence d'additionnalité, faible incitation financière à investir dans des projets verts coûteux (Ekeland-Lefournier).

**Forme pédagogique :** schéma de la méthode d'appariement au tableau ; discussion : « pourquoi −2 bps et pas −20 ? » (approche par paires vs régression globale).

**Source :** `6.txt`, ch. 6, slides 22–42 (reformulé).

### Slide 36 — Sustainability-linked bonds : lier le coupon à l'objectif (durée : 4 min · étape 7)

**Contenu :**
1. Mécanique : coupon relevé (step-up) si l'objectif de durabilité n'est pas atteint — la structure introduit une pénalité conditionnelle, là où le green bond n'engage que l'usage des fonds.
2. Chiffres (Kölbel-Lambillon 2022) : décote moyenne ≈ 29,2 bps à l'émission ; step-up moyen ≈ 26,6 bps ; même après pénalisation, le coût reste ≈ 2,6 bps en dessous du contre-factuel.
3. Conditions d'un design sain : la pénalité doit excéder le coût des efforts ; le bénéfice de l'émission doit rester inférieur à la pénalité ; l'objectif doit être additionnel et ambitieux — sinon comportements de « passager clandestin » : échéance d'évaluation lointaine, remboursement anticipé avant l'évaluation.

**Forme pédagogique :** mini-cas de calibration en plénière : « où placer le step-up ? » ; vote sur trois designs proposés.

**Source :** `6.txt`, ch. 6, slides 43–45 (reformulé).

### Slide 37 — Synthèse : le vert a-t-il un prix ? (durée : 5 min · étape 8)

**Contenu :**
1. Grille récapitulative des ordres de grandeur : greenium actions ex ante ≈ −12 bps/mois (ICC) ; ex post ≈ −4 à −15 bps/mois non significatif après contrôle des chocs ; goûts structurels ≈ 0,50 %/an entre industries vertes et brunes (S-CAPM) ; exclusion des sin stocks ≈ 1,5 %/an ; greenium obligataire ≈ −2 bps ; SLB ≈ −29 bps de décote avec step-up ≈ 27 bps.
2. Trois leçons de méthode : rendements réalisés ≠ rendements attendus ; distinguer goûts, couverture du risque climatique et flux de demande ; toute mesure de « greenness » est un proxy discutable (divergence des notateurs, comparabilité).
3. Ouvertures : la croissance des flux ESG peut éroder le greenium (van der Beck) ; l'impact de prix des investisseurs verts reste modeste mais augmente avec le risque climatique (Cheng et al.) ; du prix des actifs à l'impact réel de l'investisseur — objet de la séance suivante.

**Forme pédagogique :** synthèse interactive : la grille est remplie par les étudiants (questions ciblées), l'enseignant valide et clôt.

**Source :** synthèse de la séance ; chiffres issus de `3.txt`, ch. 3 (slides 40–51, 77–98) et `6.txt`, ch. 6 (slides 31–45), cités aux slides correspondantes.

---

## Note sur les sources

- Le déroulé s'appuie sur le cours « Green Finance » d'Olivier David Zerbib (CREST–ENSAE, Institut Polytechnique de Paris), chapitres 2, 3 et 6 (`2.txt`, `3.txt`, `6.txt` dans `/tmp/david-zerbib-finance-verte/`). Les contenus sont reformulés, restructurés et re-numérotés pour la séance ; les résultats d'auteurs (Pástor-Stambaugh-Taylor, Zerbib, Chava, El Ghoul, Sharfman-Fernando, In-Park-Monk, van der Beck, Cheng et al., Kölbel-Lambillon, Ekeland-Lefournier) sont cités avec leur numéro de slide d'origine.
- Les mentions « apport propre IAM » désignent les ajouts pédagogiques construits pour ce cours (articulations, transitions, atelier notebook, sondages et débats).
- Aucune modalité d'évaluation ni dispositif institutionnel n'est défini dans ce plan ; l'atelier notebook est une activité de séance.
