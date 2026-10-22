# Finance verte — Master IEFM
# Séance 4 (3 h) : Des IAM aux risques financiers

**Positionnement.** Étudiants dotés de bases de finance (DCF, CAPM, risque crédit) et de trois séances IAM (blocs économie/climat de type DICE ; scénarios SSP/RCP ; coût social du carbone). La séance construit pas à pas la chaîne : **IAM → scénarios NGFS → variables macro/sectorielles → cash-flows/bilan → valorisation et risques crédit/marché → stress tests**, en réorganisant le matériau de David Zerbib (jamais recopié) et en comblant ses lacunes quantitatives avec les acquis IAM des séances 1-3.

## Objectifs

1. Articuler la chaîne complète du modèle intégré au bilan financier, et savoir la redessiner de mémoire.
2. Lire et critiquer les hypothèses d'un scénario NGFS, en les rattachant aux SSP/RCP et aux IAM sous-jacents (acquis séance 2).
3. Traduire un choc de scénario (prix du carbone, demande sectorielle, dommages physiques) en choc de cash-flows et de bilan via un DCF conditionnel.
4. Maîtriser les preuves empiriques lien environnement–coût du capital et le débat greenium : rendements espérés vs réalisés.
5. Reconstruire l'anatomie d'un stress test climatique (top-down/bottom-up) et en énoncer les limites fondamentales (incertitude radicale, actualisation, queues épaisses).
6. Mobiliser le CSC et le débat Nordhaus/Stern (séance 3) comme grille critique des chiffrages financiers du climat.

## Rythme proposé (180 min)

| Créneau | Bloc | Slides | Durée |
|---|---|---|---|
| 0:00–0:10 | Accueil, introduction substantielle, plan, chaîne | 1–4 | 10 min |
| 0:10–0:35 | A. De l'IAM aux scénarios NGFS | 5–11 | 25 min |
| 0:35–1:00 | B. Variables macro/sectorielles → cash-flows et bilan | 12–19 | 25 min |
| 1:00–1:40 | C. Valorisation et risques crédit/marché | 20–28 | 40 min |
| 1:40–1:45 | Pause | — | 5 min |
| 1:45–2:05 | D. Stress tests et politique monétaire verte | 29–33 | 20 min |
| 2:05–2:50 | **Activité : mini stress test bottom-up (notebook)** | 34–35 | 45 min |
| 2:50–3:00 | Synthèse et ouverture | 36 | 10 min |

## Plan slide par slide (36 slides)

**Bloc d'ouverture (0:00–0:10)**

1. **Séance 4 — Des IAM aux risques financiers**
   - Sous-titre : « Du coût social du carbone au compte de résultat d'une banque »
   - Rappel logistique : activité notebook en fin de séance (ordinateur conseillé)
   - Forme : figure (visuel d'ouverture)
   - Source : apport propre IAM (titre de séance)

2. **Introduction — Pourquoi cette séance est la charnière du cours** *(introduction substantielle)*
   - Trois séances pour quantifier l'économie du climat (trajectoires, dommages, CSC) ; mais investisseurs, banques et superviseurs raisonnent en rendements, pertes et capital : il faut traduire
   - Message clé : pas de « nouvelle finance » du climat — mêmes DCF, CAPM, PD/LGD ; ce qui change, ce sont les scénarios d'entrée, désormais produits par des IAM
   - Annonce du fil rouge : construire la chaîne lien par lien, puis la faire tourner dans un stress test
   - Prérequis mobilisés : blocs économie/climat (séance 1), scénarios SSP/RCP (séance 2), CSC et actualisation (séance 3) ; côté finance, DCF et notion de spread de crédit
   - Forme : synthèse orale + schéma de transition
   - Source : apport propre IAM (articulation avec séances 1-3)

3. **Plan de la séance** *(immédiatement après l'introduction)*
   - A. De l'IAM aux scénarios NGFS — B. De la macro aux cash-flows/bilan — C. Valorisation et risques — D. Stress tests — E. Activité + synthèse
   - Fil rouge affiché : la chaîne sera revisitée à chaque transition (curseur)
   - Forme : schéma
   - Source : apport propre IAM

4. **La chaîne complète en un schéma**
   - IAM (DICE, GCAM, REMIND…) → scénarios NGFS → variables macro/sectorielles (prix carbone, PIB, énergie, demande) → cash-flows/bilan (FCF, dépréciations) → valorisation (DCF, WACC, greenium) & risques (PD/LGD, marché) → stress tests → retour vers la politique (supervision, BC)
   - Boucle de rétroaction : la réponse politique au stress alimente les scénarios
   - Ce schéma servira de « plan-rail » avec un curseur aux transitions
   - Forme : schéma
   - Source : apport propre IAM ; familles de scénarios et canaux : 10.txt, slides 23-29

**Bloc A — De l'IAM aux scénarios NGFS (0:10–0:35)**

5. **Transition et rappel de plan — entrée dans A**
   - Rappel du plan : nous entrons en A ; suivront B, C, D, l'activité puis la synthèse
   - Question charnière : le CSC (séance 3) est un prix d'ombre « optimal » unique ; les superviseurs, eux, raisonnent en familles de scénarios contrastés — pourquoi ?
   - Annonce : on passe du modèle unique au jeu de scénarios
   - Forme : transition orale + visuel de la chaîne (curseur en A)
   - Source : apport propre IAM (articulation séance 3 → séance 4)

6. **Pourquoi les banques centrales s'en préoccupent : la macro des chocs climatiques**
   - Chocs d'offre contre chocs de demande : les chocs climatiques (sécheresses, canicules) tirent croissance et inflation en sens opposés — dilemme de politique monétaire, contrairement à la « coïncidence divine » des chocs de demande
   - Conduite typique : tolérer (« look through ») un choc passager, agir s'il persiste
   - Trois effets structurels : identification des chocs dégradée (détérioration du rapport signal/bruit), risques « fat-tailed » érodant l'espace de politique conventionnelle, persistance (migrations, chocs énergétiques)
   - Forme : exposé + discussion d'exemples (Rhin 2018)
   - Source : 10.txt, slides 2-7 (fondé sur le discours de B. Cœuré, conférence NGFS-Bundesbank-CEP, 8 nov. 2018)

7. **Deux familles de risques financiers — et les actifs échoués**
   - Risques de transition (politique, technologie, préférences) vs risques physiques (aigus/chroniques) : deux branches qui s'injectent dans les bilans
   - Actif échoué (Carbon Tracker) : stranding réglementaire, économique ou physique ; connexion à la « bulle carbone »
   - Annonce : ces familles traversent d'abord la macro, puis les entreprises (bloc B)
   - Forme : définitions + schéma à deux branches
   - Source : 7.txt, slides 16-17 ; 10.txt, slides 26-29

8. **Le NGFS et ses familles de scénarios**
   - Réseau des banques centrales et superviseurs (« Network for Greening the Financial System »), premier rapport complet avril 2019, environ 148 membres fin 2025
   - Trois familles : transition ordonnée (action immédiate conforme à Paris), transition désordonnée (NDC jusqu'en 2030, puis révision brutale du prix des émissions, CDR limité), « hot house world » (politiques actuelles seulement)
   - Logique : couvrir l'espace des politiques possibles plutôt que prédire
   - Forme : exposé + figure des familles de scénarios
   - Source : 10.txt, slides 19 et 25 (NGFS, Guide Scenario Analysis)

9. **Anatomie d'un scénario : RCP, SSP, technologies, politiques**
   - Intrants physiques et socio-économiques : concentrations de GES (RCP), contexte (SSP : PIB, population, urbanisation, coopération internationale), trajectoires technologiques (efficacité, décarbonation de l'électricité, électrification, CDR/bioénergie)
   - Politiques climatiques : timing, mécanisme (taxe, cap-and-trade, subventions, normes), certitude (graduelle vs abrupte), coordination internationale ; préférences des consommateurs
   - Reconnaissance : ce sont exactement les entrées des IAM construits en séance 2 — les scénarios NGFS sont produits par des chaînes d'IAM
   - Forme : exposé + tableau entrées/scénario ; quizz express (relier un scénario NGFS à un couple SSP-RCP)
   - Source : 10.txt, slide 23 ; apport propre IAM (rattachement aux acquis de la séance 2)

10. **Choix de conception d'un exercice de scénarios**
    - Questions préalables : quels types de risques, combien de scénarios, quelle granularité sectorielle et géographique, quel horizon (de 5 à 80 ans), quelle fréquence d'analyse
    - Quatre usages : risques de firmes financières, risque systémique, impacts macroéconomiques, bilan propre de la banque centrale ; parties prenantes associées (institutions, gouvernements, académiques, public)
    - Arbitrage central : horizon climatique long contre horizons financiers courts
    - Forme : exposé + mini-débat éclair (quel horizon pour un stress test ?)
    - Source : 10.txt, slides 21-22 et 24

11. **Ce que les scénarios ne disent pas — regard critique sur les IAM**
    - Les IAM sous-jacents héritent des axiomes néoclassiques : incertitude radicale mal traitée, prix = croyances datées, marchés incapables de refléter la rareté finie, probabilités des extrêmes incalculables (Pottier 2016 ; Svartzman, Dron, Espagne 2019)
    - Conséquence pratique : les sorties de scénarios sont des ordres de grandeur conditionnels, pas des prévisions — à garder en tête pour toute la suite
    - Transition B : il faut maintenant traduire ces variables en volumes, marges et bilans
    - Forme : discussion critique guidée
    - Source : 11.txt, slides 30-33 ; 10.txt, slide 25

**Bloc B — Variables macro/sectorielles → cash-flows et bilan (0:35–1:00)**

12. **Rappel de plan — entrée dans B**
    - Où nous en sommes : scénarios en main ; où nous allons : compte de résultat et bilan
    - Phrase-pont : « un scénario n'a d'effet financier que s'il traverse un compte de résultat »
    - Forme : transition orale + visuel de la chaîne (curseur en B)
    - Source : apport propre IAM

13. **Impacts macroéconomiques : que produit un scénario ?**
    - Court terme : niveau de PIB, chômage, inflation ; long terme : déterminants de la croissance (capital, travail, productivité globale des facteurs) et demande (consommation, investissement, dépenses publiques, termes de l'échange)
    - Canaux physiques vers l'économie réelle : personnes (productivité du travail, mortalité/morbidité), capital physique (destructions, reconstruction), capital naturel (agriculture, services écosystémiques)
    - Lecture sectorielle : les IAM des séances 1-3 fournissent prix du carbone/de l'énergie et demandes sectorielles — intrants directs des modèles d'entreprise
    - Forme : exposé + schéma des canaux
    - Source : 10.txt, slides 26-27 ; apport propre IAM (sorties sectorielles des IAM)

14. **Canaux de transition vers les entreprises**
    - Profitabilité : coûts opérationnels accrus (intrants carbone-intensifs), demande qui bascule entre biens
    - Stranding d'actifs : dépréciation des actifs devenus non viables économiquement ou réglementairement
    - Quatre canaux complémentaires : responsabilités légales (actionnaires/investisseurs), revenus des ménages (taxes carbone, prix énergie/alimentation), valeurs immobilières (rénovation énergétique exigée), coûts de financement
    - Forme : exposé + exemples par secteur
    - Source : 10.txt, slide 28

15. **Canaux physiques vers les entreprises**
    - Profitabilité : revenus entamés par dommages directs ou ruptures de chaîne d'approvisionnement
    - Ménages : revenus affectés par la disruption de l'activité et la santé ; valeurs immobilières exposées aux aléas
    - Capital naturel : rendements agricoles et pêches — bouclage direct avec le bloc climatique des IAM (séance 1)
    - Forme : exposé + carte mentale
    - Source : 10.txt, slides 26 et 29 ; apport propre IAM (rappel du bloc climat de la séance 1)

16. **Chocs physiques déjà observés : deux cas chiffrés**
    - Rhin 2018 : étiage bas → barges limitées à mi-capacité → goulets d'approvisionnement pétrolier en Allemagne malgré la baisse du brut — brouillage du diagnostic d'inflation
    - Été 2022 : chaleur et sécheresse combinées ; estimation BCE : environ +0,67 point d'inflation alimentaire annuelle et +0,34 point d'inflation globale en Europe, effets concentrés au Sud — probable sous-estimation
    - Enseignement : le « bruit » climatique dégrade l'identification macroéconomique — conséquence directe pour la conduite de la politique
    - Forme : étude de cas courte (lecture de chiffres)
    - Source : 10.txt, slides 5-6 (Cœuré 2018 ; ECB Working Paper sur réchauffement et inflation)

17. **Pont IAM → cash-flows : la recette de traduction** *(maillon quantitatif propre)*
    - Scénario → drivers d'exploitation : prix du carbone × intensité (scopes 1-2-3) = surcoût variable ; demande sectorielle × part de marché = volumes ; prix de l'énergie = marges
    - Drivers d'investissement : CAPEX de décarbonation, compensations/CDR, opex de maintenance ; hypothèses de répercussion (pass-through) aux prix de vente
    - Production du FCF conditionnel : marge × volume − coûts carbone − capex, cohérente avec les élasticités et trajectoires sectorielles issues des IAM des séances 1-3
    - Forme : démonstration pas à pas au tableau
    - Source : apport propre IAM (chaîne quantitative absente des supports de D. Zerbib, construite sur les acquis des séances 1-3 ; scopes et intensités : 7.txt, slides 2-8)

18. **Le bilan sous choc climatique**
    - Actif : dépréciations d'actifs échoués (réglementaire, économique, physique), réécritures de valeurs d'usage
    - Passif et capitaux propres : pertes absorbées par les fonds propres ; endettement nouveau pour financer la transition
    - Frontière comptable : le modèle CARE inscrit les dettes de capital naturel et humain au passif — la performance économique devient condition de la performance écologique (contre les règles IFRS actuelles)
    - Forme : exposé + schéma de bilan
    - Source : 10.txt, slide 28 (asset stranding) ; 7.txt, slide 17 ; 11.txt, slide 29 (modèle CARE) ; apport propre IAM (mécanique comptable)

19. **Mini-cas filé : une cimenterie sous deux scénarios**
    - Données stylisées : forte intensité carbone (scopes 1+2), prix du carbone croissant brutalement en scénario désordonné, demande de construction stable
    - Calcul éclair : surcoût carbone, effet volume, capex de four rotatif — puis FCF 2030 dans chaque scénario
    - Conclusion : le même actif ne vaut pas la même chose selon le scénario → il faut une mécanique de valorisation (annonce du bloc C)
    - Forme : mini-cas interactif (calcul dirigé)
    - Source : apport propre IAM (construction pédagogique ; cadre des canaux : 10.txt, slides 26-29)

**Bloc C — Valorisation et risques crédit/marché (1:00–1:40)**

20. **Rappel de plan — entrée dans C**
    - Récapitulatif : A (scénarios) → B (cash-flows/bilans) ; C commence : de la valeur au risque
    - Question directrice : le marché intègre-t-il ces chocs dans les cash-flows ou dans le taux d'actualisation ?
    - Forme : transition orale + visuel de la chaîne (curseur en C)
    - Source : apport propre IAM

21. **Rappel DCF et première preuve : gestion environnementale et WACC**
    - Réactivation : coût du capital = rendement exigé par les investisseurs, taux auquel on actualise les cash-flows futurs
    - Sharfman & Fernando (2008) : une gestion du risque environnemental mesurée (combinaison PCA du suivi des rejets TRI et des forces KLD) est associée à un WACC plus faible, à contrôles d'industrie, taille et levier (échantillon S&P 500)
    - Mécanisme : signal d'un investissement moins risqué → coût du capital moins cher → performance financière future supérieure
    - Forme : rappel de cours + lecture de résultat
    - Source : 3.txt, slides 6-9

22. **Coût des capitaux propres : El Ghoul et al. (2011)**
    - Coût des capitaux propres implicite (ICC) moyennant quatre modèles comptables (Claus-Thomas, Gebhardt, Ohlson-Juettner-Nauroth, Easton) ; champ CSR fondé sur KLD (forces − concerns), firmes américaines
    - Résultat : la dimension environnementale de la CSR réduit significativement le coût des capitaux propres
    - Appareil de robustesse à souligner : biais d'optimisme des prévisions d'analystes, lenteur de réaction, endogénéité (variables omisses, causalité inverse, variables instrumentales) — un modèle de rigueur empirique
    - Forme : exposé + lecture critique de tableaux
    - Source : 3.txt, slides 10-18

23. **Coût de la dette : Chava (2014)**
    - ICC définie comme le taux interne vérifiant P = somme des FCF actualisés ; extension au coût de la dette (spread bancaire au-dessus du LIBOR)
    - Variables KLD : concerns (déchets dangereux, émissions, revenus charbon/pétrole) contre strengths (produits de remédiation, prévention de la pollution, énergies propres)
    - Résultats asymétriques : l'ICC croît avec les concerns (sans baisser avec les strengths) ; le coût de la dette croît avec les concerns et décroît avec les strengths
    - Forme : exposé + synthèse au tableau
    - Source : 3.txt, slides 19-21

24. **DCF durable : intégrer les investisseurs verts dans le taux**
    - Forme simplifiée du S-CAPM : E(r) = β·E(rm) + p·c — le coût du capital incorpore la proportion p d'investisseurs verts et le coût des externalités environnementales c
    - Exercice chiffré : β = 1,15 ; E(rm) = 0,64 % ; p = 20 % ; c = 1 % → coût de 0,93 % contre 0,73 % en CAPM standard
    - Valorisation : FCF de 5, 10 et 15 sur trois ans → 29,5 (CAPM) contre 29,36 (S-CAPM) : les investisseurs verts internalisent un coût des externalités et déprécient l'actif carboné
    - Forme : exercice dirigé (calcul simple, corrigé au tableau)
    - Source : 3.txt, slides 95-98 (Zerbib, S-CAPM en version simplifiée à préférences hétérogènes)

25. **Greenium : rendements espérés contre rendements réalisés**
    - Théorie (Pástor, Stambaugh, Taylor 2021) : en équilibre, les goûts verts dépriment le rendement espéré des actifs verts ; extension au risque climatique (couverture contre exposition)
    - Empirique (PST 2022) : le facteur GMB a surperformé (+174 % cumulés 2012-2020, ~65 bps/mois) mais cette performance est portée par les chocs de préoccupations climatiques (indice MCCC d'Ardia et al.) et les nouvelles de résultats ; greenium ex ante ≈ −12 bps/mois ; décomposition between/within industrie
    - Piège méthodologique central : rendements réalisés ≠ rendements espérés — distinguer les nouvelles (chocs de demande) des primes attendues
    - Forme : exposé + débat structuré
    - Source : 3.txt, slides 29-51

26. **Prix et flux : ce que déplacent les encours verts**
    - van der Beck (2025) : les flux institutionnels vers l'ESG (~3 500 Md$) sont le principal moteur des performances réalisées ; 1 $ réalloué ≈ +0,7 $ de capitalisation ESG ; rendement « porté par les flux » ≈ 1,9 %/an
    - Cheng, Jondeau, Mojon, Vayanos (2025) : modèle actifs/passifs/verts ; chutes de prix des brown de ~2,75 % à ~13,6 % selon volatilité et intensité du risque climatique ; l'annonce d'exclusions fait chuter les prix immédiatement
    - Lecture pour le cours : la valorisation dépend des flux autant que des fondamentaux — prudence sur les niveaux de greenium mesurés
    - Forme : exposé + lecture guidée de figures
    - Source : 3.txt, slides 99-129

27. **Du DCF action au risque de crédit : PD, LGD et spreads** *(maillon quantitatif propre)*
    - Réactivation : spread de crédit ≈ PD × LGD ; la chaîne climatique agit sur les deux termes — PD via profitabilité et levier dégradés, LGD via valeurs de collatéral et taux de recouvrement (actifs échoués, immobilier à rénover)
    - Traduction scénario → notation : migration de rating informelle à partir des chocs de marges du bloc B ; LGD conditionnelle aux trajectoires de prix immobiliers (obligation de rénovation)
    - Production : pertes attendues EL = PD × LGD × EAD par exposition, agrégées par secteur carboné — la brique du stress test
    - Forme : démonstration structurée + exemple chiffré
    - Source : apport propre IAM (absent des supports de D. Zerbib ; canaux stranding et immobilier : 10.txt, slide 28 ; actifs échoués : 7.txt, slide 17)

28. **Mesurer l'exposition : empreinte, intensités, parts vertes/brunes**
    - Empreinte carbone du portefeuille (somme des émissions) et intensité pondérée (somme des poids × intensités), conventions Erafp ; scopes 1-2-3 et leurs pièges (automobile : l'essentiel en aval ; aluminium : en amont ; risque de normalisation par le chiffre d'affaires)
    - Parts vertes/brunes et taxonomie européenne ; émissions financées (PCAF) et biais structurel contre les pays à revenu intermédiaire (Nature 2024) — les métriques orientent le financement
    - Usage : ces métriques relient expositions et scénarios — elles préparent l'activité
    - Forme : exposé + calcul express d'intensité de portefeuille
    - Source : 7.txt, slides 2-15 (biais pays : slides 9-10)

**Bloc D — Stress tests et politique monétaire verte (1:45–2:05)**

29. **Rappel de plan — entrée dans D (après la pause)**
    - Réactivation de la chaîne : nous savons valoriser un émetteur et chiffrer une perte attendue ; reste à agréger et superviser
    - Annonce : anatomie des stress tests climatiques, résultats, outils des banques centrales, limites
    - Forme : transition orale + visuel de la chaîne (curseur en D)
    - Source : apport propre IAM

30. **Anatomie d'un stress test climatique**
    - Couverture : banques, assureurs, gestionnaires d'actifs, propriétaires d'actifs, contreparties centrales et infrastructures de marché ; risques mobilisés : crédit, marché, opérationnel, liquidité, souscription
    - Deux méthodes : top-down (le superviseur applique ses propres calculs aux données déclarées) vs bottom-up (les institutions chiffrent l'impact du scénario sur leur bilan)
    - Le scénario est repris au NGFS (familles, granularité, horizon) — boucle explicite avec le bloc A
    - Forme : exposé + schéma comparatif top-down/bottom-up
    - Source : 10.txt, slides 21-22 et 28-29

31. **Résultats emblématiques : pertes de crédit attendues**
    - Hiérarchie robuste : pertes de crédit attendues plus faibles en transition ordonnée qu'en transition désordonnée (envolée du prix du carbone), maximales en « hot house world »
    - Message de politique : agir tôt réduit le risque financier agrégé — le coût de l'inaction est financier aussi
    - Lecture comparée : hétérogénéité des périmètres et hypothèses entre exercices (figures Deutsche Bank Research)
    - Forme : lecture guidée de graphiques
    - Source : 10.txt, slides 30-31

32. **Banques centrales : de la justification aux outils**
    - Justifications : échecs publics possibles (résistance politique et sociale, instabilité financière de transition, rationnement du crédit — Campiglio 2016) ; mandat européen : soutenir les politiques générales sans préjudice de la stabilité des prix
    - Outils : intégration du climat dans la stratégie BCE (juillet 2021) ; « tilting » des achats de corporate bonds depuis octobre 2022 (émissions, cibles de réduction, transparence) ; facteur climat dans le cadre de collatéral (échéance 2026) ; constat d'un QE « neutre » biaisé vers les grands émetteurs carbonés (~730 Md$ en 2017 contre ~170 Md$ nécessaires aux objectifs climat UE)
    - Limites assumées : instrument conjoncturel, univers éligible restreint, risque de bulle verte ; pas de green TLTRO ni de financement direct des États à ce stade
    - Forme : exposé + discussion (quelle efficacité ?)
    - Source : 10.txt, slides 9-18 (Cœuré 2018 ; NGFS 2018 ; Campiglio et al. 2018 ; BCE/BIS)

33. **Limites fondamentales de la quantification financière du climat**
    - Actualisation : Nordhaus (taux élevé, ~6 %) contre Stern (~1,31 %) — éviter 100 $ de dommage dans 100 ans ne vaut pas plus que 5,4 $ pour l'un, jusqu'à 52 $ pour l'autre (acquis de la séance 3 réinvestis)
    - Queues épaisses et persistance des chocs : les extrêmes érodent l'espace de politique conventionnelle ; l'incertitude radicale et les « probabilités incalculables » des extrêmes mal traitées par les modèles
    - Durabilité faible contre forte : substituer du capital financier au capital naturel est une hypothèse, pas un théorème (BIS, « green swan ») — garde-fou pour interpréter tout chiffrage
    - Forme : synthèse critique (prépare l'activité)
    - Source : 11.txt, slides 12 et 33 ; 10.txt, slide 7 ; apport propre IAM (bouclage avec la séance 3)

**Activité — mini stress test bottom-up (2:05–2:50)**

34. **Activité notebook : votre premier stress test climatique (45 min)**
    - Consigne : sur un portefeuille stylisé de 5 à 8 émetteurs sectoriels, dérouler deux scénarios NGFS simplifiés (ordonné / désordonné) définis par prix du carbone, demande sectorielle et dommages physiques
    - Chaîne à implémenter dans le notebook : drivers → FCF par scénario (recette du slide 17) → DCF au coût du capital → PD/LGD recalculés (slide 27) → pertes attendues agrégées par secteur
    - Organisation : binômes, notebook étudiant et corrigé alignés cellule par cellule ; chaque binôme rend une figure pertes par scénario
    - Forme : atelier machine (notebook)
    - Source : apport propre IAM (chaîne construite en séance ; familles de scénarios et canaux : 10.txt, slides 25-29)

35. **Débriefing de l'activité**
    - Comparaison des pertes entre scénarios : l'ordre attendu (ordonné < désordonné) fait écho aux résultats des stress tests officiels (slide 31)
    - Sensibilités à discuter : pass-through du prix du carbone, horizon du DCF, LGD du collatéral immobilier ; erreurs fréquentes (double comptage capex/stranding, cohérence des volumes)
    - Méta-message : le chiffre dépend des hypothèses — les scénarios donnent des ordres de grandeur conditionnels, pas des vérités
    - Forme : discussion collective autour des sorties de notebooks
    - Source : apport propre IAM ; résultat ECL de référence : 10.txt, slide 31

**Synthèse (2:50–3:00)**

36. **Synthèse finale et ouverture**
    - La chaîne récapitulée de mémoire : IAM → scénarios (RCP/SSP, familles NGFS) → variables macro/sectorielles → cash-flows et bilans → valorisation (DCF, greenium, S-CAPM) et risque (PD/LGD) → stress tests → supervision et banques centrales
    - Trois idées à emporter : (i) pas de nouvelle finance, de nouveaux scénarios d'entrée ; (ii) le marché internalise par les cash-flows et par les taux — et par les flux, avec incertitude ; (iii) tout chiffrage est conditionnel à l'actualisation et aux dommages (leçon Nordhaus/Stern)
    - Ouverture séance 5 (asset pricing durable) : le S-CAPM complet, préférences et exclusion, prix des obligations vertes
    - Forme : synthèse + schéma final annoté
    - Source : apport propre IAM ; annonce fondée sur 3.txt, slides 52-98 (S-CAPM) ; boucle institutionnelle : 10.txt

---

## Statut et règles de production

- Ce document est une **proposition de plan**, pas encore le jeu de slides final.
- Le futur deck utilisera le système Beamer « mystyle_diapos2.tex » déjà employé dans les supports IAM de Polytechnique.
- Une slide **Plan** suit immédiatement l'introduction substantielle ; le plan est rappelé aux grandes transitions (slides 5, 12, 20, 29).
- Les formulations et figures de David Zerbib sont des sources de fond à citer et à réorganiser, jamais à recopier sans attribution ; les maillons quantitatifs absents de ses supports (pont IAM → FCF, PD/LGD, stress test pédagogique) sont marqués « apport propre IAM ».
- Les activités disposent d'un notebook étudiant et d'un corrigé strictement alignés cellule par cellule.
