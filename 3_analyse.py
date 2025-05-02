'''
Analyse des données avec figures de DataVizualization
'''
import streamlit as st

st.title('Visualisation des données')
st.subheader('Chargement et pré-traitement des données')
st.markdown("""<div style="text-align: justify"> Les fichiers audio ont été chargés à partir d'un répertoire spécifique, 
            contenant des enregistrements des patients. Un fichier CSV, nommé audio_features.csv, 
            a été utilisé pour associer chaque fichier audio à une étiquette de crise 
            (indiquant si le fichier correspond à une période de crise ou non) ainsi qu'aux informations 
            temporelles concernant le début et la fin des crises pour chaque enregistrement. 
            Le DataFrame résultant contient les colonnes suivantes : filename, Crise, crise_start, et crise_end. 
            Les labels de crise sont associés aux fichiers audio, permettant ainsi de visualiser et d'annoter 
            les moments précis des crises sur les caractéristiques extraites.</div>""", unsafe_allow_html=True)

st.subheader('Extraction des caractéristiques audio')
st.markdown("""<div style="text-align: justify"> Le script utilise la bibliothèque librosa pour extraire plusieurs caractéristiques audio pertinentes. 
            Ces caractéristiques ont été choisies pour leur capacité à capturer différents aspects du signal audio, 
            potentiellement liés aux crises épileptiques. Les caractéristiques suivantes ont été extraites pour chaque fichier audio :  
            </div>""", unsafe_allow_html=True)
st.markdown("")
with st.expander("Root Mean Square Error (RMSE)"):
    st.caption(""" L'amplitude du signal a été mesurée à l'aide de la fonction RMSE. 
               Cela permet de suivre l'évolution de l'intensité sonore au cours du temps, 
               un indicateur potentiellement pertinent pour détecter des périodes de crise.""")
with st.expander("Spectral Centroid"):
    st.caption(""" Le centroïde spectral est calculé pour déterminer la "position centrale" 
               de l'énergie dans le spectre de fréquence du signal audio. 
               Il fournit une mesure de la distribution de l'énergie, en indiquant où se concentrent 
               les fréquences dominantes. Un centroid spectral élevé est généralement associé 
               à des sons plus brillants et aigus, tandis qu'un centroid plus bas reflète des sons plus graves. 
               Cette mesure permet d'analyser la texture sonore et peut fournir des informations sur les changements 
               dans la tonalité du signal, notamment durant les crises.""")
with st.expander("Spectral Bandwidth"):
    st.caption(""" La largeur du spectre décrit combien de fréquences, au-dessus et en dessous de la fréquence centrale, 
               sont présentes dans le signal. Une largeur de spectre étroite signifie que l'énergie du signal 
               est concentrée autour d'une fréquence particulière, tandis qu'une largeur de spectre large 
               indique une plus grande diversité de fréquences dans le signal.""")
with st.expander("Spectral Rolloff"):
    st.caption(""" Le spectral rolloff mesure le point où une certaine proportion (par exemple, 85%) 
               de l'énergie spectrale est contenue dans les fréquences inférieures. 
               Cela permet d'observer la concentration des fréquences à haute énergie.""")
with st.expander("Zero Crossing Rate"):
    st.caption(""" Le taux de traversée de zéro mesure combien de fois le signal audio traverse la ligne de zéro 
               (c'est-à-dire change de signe, de positif à négatif ou vice versa) au cours du temps. 
               Un taux élevé indique que le signal oscille rapidement entre des valeurs positives et négatives, 
               ce qui peut être associé à une activité plus dynamique ou plus erratique du signal, 
               comme cela pourrait être observé pendant les crises. En revanche, 
               un taux faible suggère un signal plus stable et moins fluctuant.""")
with st.expander("MFCC (Mel-Frequency Cepstral Coefficients)"):
    st.caption(""" Les coefficients MFCC sont extraits pour représenter de manière compacte les variations spectrales du signal audio, 
               en utilisant une échelle de fréquence qui correspond mieux à la façon dont l'oreille humaine perçoit les sons. 
               Ces coefficients capturent les caractéristiques acoustiques essentielles, telles que la texture et la tonalité du signal. 
               Les MFCC sont souvent utilisés dans la reconnaissance vocale, car ils permettent de différencier efficacement 
               les différents types de sons. Dans le cadre de l'analyse des crises, ces coefficients peuvent fournir 
               des informations importantes sur les changements dans la structure du signal audio au fil du temps, 
               notamment lors des événements de crise.""")

st.subheader('Visualisation des caractéristiques audio')

st.write("""Différentes représentations du signal audio permettent de visualiser les changements acoustiques associés à une crise: """)

tab1, tab2, tab3  = st.tabs(["Tracé Audio","Distribution", "Spectrogramme"])
tab1.write("Tracé audio brut du signal temporel.")
tab1.caption("""La courbe illustre l'évolution de l'amplitude du signal sur la durée de l’enregistrement.
             Les lignes en pointillés indiquent le début (:red[rouge]) et la fin (:green[vert]) de la crise.""")
tab1.image("images/3_trace_audio.png")

tab2.write("Histogramme de distribution des amplitudes du signal audio")
tab2.caption("""Représentation de la densité des valeurs enregistrées. """)
tab2.image("images/3_distribution.png")

tab3.write("Spectrogramme")
tab3.caption("""Le graphique représente l’intensité du signal (en dB) selon le temps (x) et la fréquence (y). 
             Les couleurs plus chaudes indiquent une plus grande intensité.""")
tab3.image("images/3_spectrogramme.png")

st.markdown("")
st.markdown("""Pour chaque caractéristique extraite, des visualisations ont été générées sous forme de graphiques :""")

tab4, tab5, tab6, tab7, tab8 = st.tabs(["RMSE","Spectral Centroid", "Spectral Bandwith", "Spectral Rolloff", "Zero Crossing"])
tab4.caption("Courbe d’amplitude mesurant l’énergie locale du signal.")
tab4.image("images/3_courbe_amplitude.png")

tab5.caption("Fréquence moyenne pondérée du spectre, perçue comme la “hauteur” du son. ")
tab5.image("images/3_spectral_centroid.png")

tab6.caption(" Largeur spectrale autour du centroïde, représentant la dispersion des fréquences.")
tab6.image("images/3_spectral_bandwith.png")

tab7.caption("Fréquence sous laquelle se concentre 85% de l’énergie spectrale.")
tab7.image("images/3_rolloff.png")

tab8.caption("""Fréquence à laquelle le signal traverse l’axe zéro (changement de signe). 
             Un indicateur de la fréquence du contenu audio.""")
tab8.image("images/3_zero_crossing.png")

st.markdown("")
st.markdown("""L’ensemble des graphes montre une nette variation des caractéristiques audio entre les périodes pré-, 
            per- et post-ictales. À partir du début de crise (ligne :red[rouge]), on observe :""")            
st.markdown("""* Une **augmentation de l’amplitude du signal** (tracé audio brut et RMSE), traduisant une activité sonore plus intense.""")
st.markdown("""* Une **énergie accrue dans les hautes fréquences** sur le spectrogramme, 
            visible par l’apparition de bandes plus claires (vers le haut du spectre).""")
st.markdown("""* Une **augmentation du Spectral Centroid** et du **Spectral Bandwidth**, 
            indiquant que le spectre se déplace vers des fréquences plus élevées et devient plus étalé.""")
st.markdown("""* Le **Spectral Rolloff** augmente également, signifiant que davantage d’énergie est présente dans les hautes fréquences pendant la crise.""")
st.markdown("""Après le **retour à l'état post-ictal** (ligne :green[verte]), on constate une nouvelle hausse de certains de ces paramètres 
            et notamment une **hausse du Zero Crossing Rate**, suggérant un contenu plus fréquentiel (signaux plus oscillants) 
            puis par la suite, un retour progressif des caractéristiques à leur niveau de base, même si certaines fluctuations persistent.""")
st.markdown("""Ces observations suggèrent que l’apparition d’une crise épileptique est associée à des changements acoustiques 
            nets et détectables dans le signal audio, en particulier sur les dimensions d’énergie et de contenu fréquentiel.""")

st.subheader('Classification du problème')
st.markdown("""<div style="text-align: justify"> Le projet s'inscrit dans une démarche de classification binaire visant à distinguer 
            deux classes : "crise" et "non-crise". Ces classes correspondent aux différents états cérébraux observés 
            dans les données audio d'électroencéphalogrammes (EEG) des patients épileptiques. 
            Le défi consiste à classifier les périodes enregistrées en fonction de la présence ou de l'absence d'une crise épileptique, 
            en utilisant des caractéristiques temporelles et spectrales extraites des signaux audio.
            </div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> D’un point de vue statistique, la détection binaire consiste à classer 
            les observations dans l’une des deux catégories définies, représentant généralement la présence ou l'absence 
            d’un événement particulier. Dans ce contexte, un modèle est entraîné à différencier deux classes distinctes. 
            Dans notre cas, ces classes correspondent aux états "crise" et "non-crise". Le modèle apprend des caractéristiques 
            discriminantes, telles que celles observées dans les signaux EEG, et est ensuite capable d’attribuer des nouvelles 
            instances à l’une des deux classes selon les schémas appris.
            </div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Ce projet repose également sur la détection d'anomalies, 
            où les crises épileptiques sont des événements rares et significatifs dans les données. 
            Contrairement aux approches traditionnelles où les modèles sont formés sur des données représentant 
            à la fois des événements normaux et anormaux, la détection d'anomalies se concentre sur des événements rares, 
            que le modèle apprend à reconnaître en se basant uniquement sur des instances normales. 
            Cela permet de mieux identifier les événements critiques, comme les crises épileptiques, 
            qui sont significativement différents des périodes "non-crise".  
            </div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> La détection d’anomalies se distingue ainsi de la classification binaire 
            classique en ce qu’elle repose sur l'identification de comportements inhabituels dans un contexte 
            où les données normales dominent. L’objectif est de développer un modèle capable de détecter ces anomalies 
            rares mais importantes, ce qui est crucial pour la prise de décision dans des domaines tels que les soins de santé.  
            </div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Pour évaluer la performance des modèles, 
            plusieurs métriques de classification binaire sont utilisées, notamment :  
            </div>""", unsafe_allow_html=True)
st.markdown("")
with st.expander("Précision (Accuracy)"):
    st.caption(""" Proportion d'exemples correctement classifiés, 
               bien qu’elle soit moins informative dans des contextes de classes déséquilibrées comme ici.""")
with st.expander("Précision (Precision) et Rappel (Recall)"):
    st.caption(""" Ces métriques sont essentielles pour évaluer la détection des crises, un événement rare. 
               La précision mesure la proportion de crises correctement identifiées parmi toutes les prédictions positives, 
               tandis que le rappel évalue la capacité du modèle à détecter toutes les crises présentes.""")
with st.expander("F1-Score"):
    st.caption(""" Un compromis entre la précision et le rappel, particulièrement utile lorsque les classes sont déséquilibrées.""")
st.markdown("""<div style="text-align: justify"> En plus de ces métriques, 
            plusieurs autres outils d’évaluation sont utilisés pour mesurer la performance du modèle :  
            </div>""", unsafe_allow_html=True)
st.markdown("")
with st.expander("Matrice de confusion"):
    st.caption(""" Permet d’analyser les erreurs du modèle en affichant les vrais positifs, faux positifs, 
               vrais négatifs et faux négatifs.""")
with st.expander("AUC-ROC"):
    st.caption(""" Indicateur de la capacité du modèle à séparer les classes, 
               un AUC proche de 1 montrant une bonne séparation.""")
with st.expander("Courbe de précision-rappel"):
    st.caption(""" Permet d’évaluer la performance du modèle en fonction des seuils de classification, 
               en mettant particulièrement l’accent sur la détection des crises.""")
st.markdown("""<div style="text-align: justify"> Ces différentes métriques et analyses permettent 
            une évaluation complète de la capacité du modèle à détecter les crises épileptiques dans les données EEG.  
            </div>""", unsafe_allow_html=True)
st.markdown("")