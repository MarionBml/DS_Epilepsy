'''
Présentation des données (volumétrie, architecture, etc.)

'''
import streamlit as st

st.title('Données')
st.subheader('Présentation des données')
with st.expander("🏥 Contexte"):
    st.markdown("""Au sein de l’Hôpital Universitaire Pitié-Salpêtrière situé à Paris, 
        une initiative visant à explorer les complexités de la prise en charge de l'épilepsie est en cours. 
        Plus précisément, des patients pharmacorésistants, candidats à une chirurgie, 
        subissent des procédures méticuleuses d'implantation d'électrodes intracrâniennes. 
        Ces procédures sont planifiées pour étudier en profondeur l'activité cérébrale lors des épisodes de crise 
        afin de mieux comprendre où se situent les neurones impliqués dans la crise.""")
    st.markdown("""La phase d’observation s’étend sur deux à trois semaines et est conçue pour capter 
            une compréhension approfondie des dynamiques neurologiques des patients. Pendant cette période, 
            une surveillance continue est mise en place, où les patients et leur environnement immédiat 
            sont documentés grâce à la technologie de vidéo-encéphalographie (VEEG). 
            Cette approche permet non seulement d'analyser les crises en détail, 
            mais fournit également des ressources précieuses pour ce projet de recherche centré 
            sur la détection des crises à partir d'enregistrements audio. 
            Ces données sont la propriété du centre hospitalier. Un accord a été établi pour utiliser ces données 
            à des fins de recherche dans le cadre de notre projet.""")
with st.expander("🎙️ Caractéristiques techniques"):
    st.markdown("""Dans le cadre de ce projet, seuls l’audio des vidéos, obtenus par la technologie VEEG, 
            ont été pris en compte.   L'instrumentation utilisée pour enregistrer les vidéos 
            comprend la caméra et le microphone suivants : caméra réseau AXIS M5525–E PTZ et microphone AXIS T8351 Mk II 3,5 mm. 
            Le dispositif AXIS T8351 Mk II 3,5 mm est un microphone analogique à faible bruit, de type hémisphérique, 
            avec une qualité sonore élevée capable de capter le son dans toutes les directions.""")
    st.image("/workspaces/DS_Epilepsy/images/microphones.png","""a) caméra AXIS M5525-E PTZ avec son support d’installation au mur dans la chambre des patients   b) Microphone 3.5 mm AXIS T8351 Mk II""")
    st.markdown("""Les enregistrements vidéo-EEG ont été analysés par un neurologue qui a sélectionné 6 patients 
            pour un total d'environ 400 minutes (près de 7 heures) d'enregistrements vidéo (15 vidéos). 
            Le neurologue a ensuite annoté le moment précis où les crises se sont produites. 
            En utilisant les enregistrements vidéo des patients, les cliniciens ont une perspective contextuelle 
            de leur environnement immédiat. Certains enregistrements sonores contenaient des périodes de silence, 
            des sons de télévision ou des discours, ainsi que des voix externes lorsque d'autres personnes, 
            telles que des infirmiers, des médecins ou des soignants, parlaient à proximité de la chambre. 
            Enfin, une période ictale claire a été fournie pour chaque sujet.""")
    st.markdown("""Étant donné que cette étude vise à détecter les crises épileptiques à partir des enregistrements audio, 
            les enregistrements audio ont été extraits des vidéos des patients. Différentes fonctions de l’Audio Toolbox™ 
            de MATLAB R2023b ont été utilisées pour importer les fichiers audio. Les fichiers audio-vidéo originaux étaient au format MP4. 
            Le taux d'échantillonnage des enregistrements audio était de 32 kHz et le débit binaire de 62 2400. 
            Afin de conserver l’anonymat des données, cette étape a été réalisée par le Dr Mario Chavez.""")

st.subheader('Variables pertinentes et cible')
st.markdown("""Au regard de nos objectifs de détection des crises épileptiques à partir de données audio, 
            plusieurs variables nous semblent particulièrement pertinentes :""")
with st.expander("😱 Vocalisations"):
    st.caption(""" Cris, pleurs et vocalisations stéréotypées peuvent être des indicateurs clés 
            de la présence d'une crise.""")
with st.expander("🎤 Automatismes vocaux"):
    st.caption(""" Des paroles incohérentes ou répétitives peuvent signaler un épisode de crise.""")
with st.expander("🤯 Altération de la parole"):
    st.caption(""" Une parole altérée peut être liée à la présence d’une crise 
            et constitue un autre indicateur utile.""")
with st.expander("🌬️ Modifications respiratoires"):
    st.caption(""" Halètements et apnées peuvent survenir pendant une crise, 
            ce qui les rend utiles pour la classification.""")
with st.expander("🫨 Bruits moteurs"):
    st.caption(""" Les bruits d'impact et les frottements peuvent refléter 
            des mouvements involontaires associés à certaines crises.""")
with st.expander("🛌 Interactions avec l’environnement"):
    st.caption(""" Les bruits d’objets renversés ou les mouvements involontaires peuvent fournir des indices importants.""")
st.markdown(""" La variable cible de notre analyse est la présence ou l'absence d’une crise épileptique 
            détectée à partir du signal audio.""")


st.subheader('Particularités des données')
st.markdown("""Notre jeu de données présente plusieurs caractéristiques qui influencent directement l’analyse et
            l’optimisation de notre modèle :""")
with st.expander("👋 Variabilité des sons"):
    st.caption(""" Les sons produits peuvent varier considérablement en fonction du type
             de crise et des spécificités de chaque patient, ce qui rend la classification plus complexe.""")
with st.expander("🎙️ Bruit ambiant"):
    st.caption(""" La présence de bruit de fond dans les enregistrements peut compliquer
             la détection précise des événements de crise.""")
with st.expander("📈 Exploitation des caractéristiques audio"):
    st.caption(""" L’analyse nécessite l’extraction de caractéristiques 
            spécifiques du signal, telles que les **MFCC (Mel-frequency cepstral coefficients)**, 
            le **STFT (Short-Time Fourier Transform)**, et **l’entropie spectrale**, 
            afin de rendre le signal exploitable pour l'apprentissage automatique.""")
with st.expander("❔ Manque de données"):
    st.caption(""" Bien que nous disposions d’un volume important de données, 
            certaines catégories de crises sont sous-représentées, ce qui rend l’entraînement du modèle 
            plus difficile et nécessite une attention particulière.""")


st.subheader('Limites et défis')
st.markdown("Nous sommes confrontés à plusieurs défis et limitations qui peuvent affecter la performance de nos modèles :")
with st.expander("👨🏾‍👩🏾‍👧🏾‍👦🏾 Généralisation des modèles"):
    st.caption(""" En raison des différences entre les patients et des spécificités des crises,
            il peut être difficile pour le modèle de généraliser à des situations variées.""")
with st.expander("👂🏻 Bruit de fond"):
    st.caption(""" Les bruits environnementaux, tels que des sons non liés aux crises 
            (conversations, appareils en fonctionnement, etc.), peuvent interférer avec la détection précise des crises, 
            réduisant ainsi la qualité des prédictions.""")
with st.expander("🗃️ Quantité de données"):
    st.caption(""" Certaines classes de crises, bien que présentes dans notre jeu de données,
            sont moins fréquentes, ce qui peut rendre l'entraînement du modèle moins efficace pour ces types d’événements.""")
with st.expander("🎙️ Biais dans les données"):
    st.caption(""" Étant principalement issues d’enregistrements effectués dans un environnement clinique, 
            nos données peuvent ne pas être totalement représentatives des conditions réelles rencontrées à domicile,
            ce qui pourrait affecter la capacité du modèle à prédire les crises dans d’autres contextes.""")
st.markdown("""Ces particularités et limitations guideront nos efforts dans l’optimisation du modèle afin d'améliorer
            la détection des crises, tout en tenant compte des défis posés par la variabilité des enregistrements et le bruit de fond.""")
