
'''
Présentation des modèles entraînés et de leurs résultats 
Analyse du meilleur modèle sur différents fichiers existants 
'''
import streamlit as st

st.title('Modèles entraînés')
st.subheader("Intérêt du deep learning")
st.markdown("""<div style="text-align: justify"> Les résultats obtenus avec l'Isolation Forest et plus largement les algorithmes de classification, mettent en évidence 
qu'un changement de paradigme est nécessaire pour progresser vers un système de détection performant.
Le recours à des modèles de deep learning constitue une suite logique à notre démarche,
en offrant une alternative capable de dépasser les limitations structurelles des algorithmes classiques.
</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Les modèles de deep learning, et notamment les réseaux de neurones convolutifs (CNN) 
ou les architectures audio pré-entraînées comme Wav2Vec2, présentent plusieurs avantages décisifs dans ce contexte :
</div>""", unsafe_allow_html=True)
with st.expander("💻 Apprentissage automatique des caractéristiques"):
st.caption("""Contrairement aux approches classiques qui nécessitent une extraction manuelle des features 
(moyennes de bandes fréquentielles, écart-types, etc.), les réseaux de neurones profonds apprennent 
directement des représentations pertinentes à partir des données brutes. 
Cette capacité permet de capturer des patterns acoustiques complexes associés aux crises, 
sans biais lié au choix des descripteurs.""")
with st.expander("⌛ Modélisation de la dynamique temporelle"):
st.caption(""" En intégrant des fenêtres temporelles glissantes (2 secondes dans notre cas) 
et des architectures capables d'exploiter la continuité des signaux, 
les modèles profonds peuvent extraire des séquences temporelles significatives, 
là où les classifieurs classiques échouent à capturer la variabilité inter- et intra-patients.""")
with st.expander("🔊 Meilleure gestion du bruit"):
st.caption("""Les enregistrements utilisés comportent des artefacts sonores (bruits ambiants, échanges verbaux, mouvements) 
susceptibles de perturber la détection. Les modèles de deep learning, via leur capacité à filtrer 
les informations non pertinentes, se montrent plus robustes à ces perturbations, limitant les faux positifs.""")
with st.expander("👩‍⚕️Généralisation aux nouveaux patients"):
st.caption(""" Grâce à une phase de pré-entraînement sur de larges corpus audio, des modèles comme Wav2Vec2 
peuvent être fine-tunés sur des données spécifiques (épilepsie) tout en conservant une bonne 
capacité de généralisation, ce qui est crucial dans le contexte de la variabilité interindividuelle.""")

st.badge("Première approche (Undersampling + Wav2Vec)", color='violet')
st.markdown("""<div style="text-align: justify"> Nous avons d'abord appliqué un undersampling sur nos données déséquilibrées. Cela nous a permis de réduire l'écart de pondération de chaque classe, 
assurant que la classe minoritaire (crise) ait autant d'importance que la classe majoritaire (pas crise). Cela évite que le modèle privilégie la classe dominante et améliore la qualité de la classification.

Ensuite, nous avons fine-tuné Wav2vec sur des données audio et l'avons directement utilisé pour la classification.
</div>""", unsafe_allow_html=True)
st.markdown("")

st.badge("Deuxième approche (Wav2Vec + GradientBoosting)", color='violet')

st.markdown("""<div style="text-align: justify">Dans notre deuxième approche, Wav2Vec2 a servi à extraire des caractéristiques audio, mais ensuite un autre modèle a été appliqué sur ces caractéristiques pour la classification.

Nous avons opté pour un Gradient Boosting Classifier, un modèle d'ensemble basé sur une succession d'arbres de décision. Ce choix s'explique par sa capacité à capturer des relations complexes et non linéaires dans les données, ainsi que sa robustesse face aux problèmes de classification déséquilibrée, tel que celui rencontré dans notre cas (épisodes de crises épileptiques vs segments non épileptiques).
Afin d'accélérer l'exécution de cette approche, nous avons également appliqué une PCA (Analyse en Composantes Principales) sur les caractéristiques extraites par Wav2Vec2. Cela a permis de réduire la dimensionnalité des données tout en préservant l'essentiel de l'information, facilitant ainsi l'entraînement du modèle de Gradient Boosting.

</div>""", unsafe_allow_html=True)
st.markdown("")

st.badge("Troisième approche (CNN)", color='violet')
st.markdown("""<div style="text-align: justify"> Afin d'explorer une alternative aux modèles pré-entraînés de type Wav2Vec2, 
une troisième approche basée sur un réseau neuronal convolutionnel (CNN) Keras a été mise en œuvre.
Ce choix s'inscrit dans une tendance actuelle où les CNN sont de plus en plus utilisés pour l'analyse audio, et 
a été développée pour la détection des crises épileptiques à partir de signaux audio. 

Cette méthode s'appuie sur la transformation des signaux acoustiques en spectrogrammes, 
qui constituent des représentations visuelles temps-fréquence bien adaptées à l'apprentissage profond.

L'objectif ici est d'exploiter la capacité des CNN à extraire automatiquement des motifs discriminants dans ces représentations spectrales, 
sans recourir à des embeddings préexistants. Ce choix méthodologique offre une architecture plus légère et contrôlable, 
notamment pour des cas où les ressources de calcul sont limitées ou lorsque l'on souhaite une personnalisation du modèle à un domaine spécifique.
</div>""", unsafe_allow_html=True)

st.image("images/5_pipeline.png","Pipeline global de traitement mis en oeuvre dans cette troisième approche")
st.markdown("")
st.subheader("Analyse comparative des approches et choix du modèle")
st.image("images/5_deep_synthesis.png","""Stratégies explorées dans nos recherches incluant du deep learning. Sont exclues de ce diagrammes les recherches
concernant les classifieurs puisque ces recherches n'ont pas porté leurs fruits et les méthodes de pensée & concepts ont été repris et appliqués au deep learning.""")



st.badge("Analyse comparative des approches", color='violet')
st.markdown("""<div style="text-align: justify"> L'objectif principal de ce projet était d'explorer différentes stratégies 
de classification pour la détection de crises d'épilepsie à partir d'enregistrements audio, 
en tenant compte du déséquilibre intrinsèque des données. Trois grandes familles d'approches ont été testées : </div>""", unsafe_allow_html=True)
st.markdown("* Des modèles de machine learning classiques à partir de descripteurs statistiques")
st.markdown("* Des modèles pré entraînés de type Wav2Vec2")
st.markdown("* Des réseaux de neurones convolutifs (CNN)")
st.markdown("""<div style="text-align: justify"> Chaque approche a été évaluée selon des métriques standard (précision, rappel, F1-score), 
avec un focus particulier sur la classe minoritaire correspondant aux épisodes de crise.</div>""", unsafe_allow_html=True)
st.markdown("")

with st.expander("💻 Approches par Machine Learning supervisé et non supervisé"):
st.markdown("""<div style="text-align: justify"> Une première série de pipelines a été mise en œuvre à partir de descripteurs 
statistiques simples (moyenne et écart-type glissants), suivis d'une réduction de dimensionnalité par ACP (PCA). 
Plusieurs variantes ont été comparées :
</div>""", unsafe_allow_html=True)
st.markdown("* PCA + Gradient Boosting")
st.markdown("* PCA +  Classification par centroïdes + Gradient Boosting")
st.markdown("* PCA + Isolation Forest (avec un seuil d'anomalie fixé à 5 %)")
st.markdown("""<div style="text-align: justify"> Les performances globales de ces modèles supervisés classiques se sont révélées modestes, 
en particulier pour la détection des épisodes de crise. L'approche semi-supervisée par Isolation Forest a toutefois 
montré de meilleures capacités de rappel, en identifiant efficacement certains segments audio atypiques. 
Cependant, sa dépendance à un paramétrage nécessitant une estimation a priori du taux de crises limite 
sa généralisation à des contextes réels.</div>""", unsafe_allow_html=True)
st.markdown("")

with st.expander("🔊 Modèle Wav2Vec2 avec stratégies d'équilibrage"):
st.markdown("""<div style="text-align: justify"> Le modèle pré entraîné Wav2Vec2 a été testé avec des segments audio de 1 et 2 secondes, 
en appliquant une stratégie d'undersampling pour compenser le déséquilibre de classes. 
Pour des segments d'1 seconde, la précision globale atteignait 0.89, mais la détection des crises 
restait faible (F1-score = 0.36). Avec des segments de 2 secondes, le F1-score pour la classe "crise" montait à 0.54, 
suggérant une meilleure captation des dynamiques acoustiques spécifiques.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Une variante supervisée, combinant les embeddings Wav2Vec2 
à un classificateur Gradient Boosting entraîné par lot sur GPU, n'a pas permis d'amélioration significative. 
Le modèle restait très performant sur la classe majoritaire (F1-score = 0.98) mais quasiment aveugle 
aux épisodes de crise (F1-score = 0.10), illustrant la difficulté à équilibrer la classification avec cette architecture.
</div>""", unsafe_allow_html=True)
st.markdown("")

with st.expander("🧠 Réseau de Neurones Convolutif (CNN)"):
st.markdown("""<div style="text-align: justify"> L'approche par CNN s'est démarquée par des performances nettement 
plus équilibrées, et ce pour les deux durées de segments testées. Pour des segments d'1 seconde, 
le modèle atteignait un F1-score de 0.70 pour la classe "crise", avec un rappel de 0.59. 
En passant à des segments de 2 secondes, les performances s'améliorent encore (F1-score = 0.79 ; rappel = 0.72), 
traduisant une meilleure captation des motifs temporels caractéristiques des épisodes. </div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> L'analyse a également montré que des fenêtres trop longues (10 secondes) 
dégradent les performances tout en alourdissant considérablement la charge computationnelle. 
Un compromis optimal a été trouvé avec une fenêtre de 2 secondes, 
suffisante pour extraire les dynamiques pertinentes tout en restant adaptée à un traitement efficace. Cette fenêtre temporelle est d'ailleurs mise en avant dans la littérature scientifique.</div>""", unsafe_allow_html=True)
st.markdown("")

st.badge("Choix du modèle", color='green')
st.markdown("""<div style="text-align: justify"> À l'issue de cette analyse, le modèle CNN entraîné sur des segments audio 
de 2 secondes a été retenu comme la solution la plus pertinente pour la détection automatique des crises 
épileptiques à partir du signal vocal.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Les approches classiques basées sur des descripteurs statistiques, 
même enrichies de techniques comme PCA ou Isolation Forest, ont montré une sensibilité insuffisante 
à la classe minoritaire et une capacité de généralisation limitée. Les architectures Wav2Vec2 
ont offert des représentations audio riches, mais n'ont pas permis d'améliorer la détection 
des crises de manière satisfaisante, même après équilibrage ou transformation des embeddings.
</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Le modèle CNN, en revanche, s'est distingué 
par sa capacité à détecter efficacement les événements rares, avec un excellent compromis 
entre rappel, F1-score, robustesse au déséquilibre de classes et coût computationnel. 
Il constitue donc la base retenue pour les prochaines phases du projet, notamment 
en vue d'une intégration dans un système embarqué ou une application clinique.
</div>""", unsafe_allow_html=True)
st.markdown("""<div style="text-align: justify"> Il serait pertinent de tester à nouveau ses approches sur des volumes de données plus importants incluant entre autres de multiples crises pour un patient donné.
Cela permettrait de mieux évaluer la capacité de généralisation du modèle et d'optimiser ses performances sur des données réelles. 
De plus, l'intégration de techniques d'augmentation de données pourrait également être envisagée pour enrichir le jeu de données d'entraînement et améliorer la robustesse du modèle.
</div>""", unsafe_allow_html=True)
