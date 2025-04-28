'''
Présentation des modèles entraînés et de leurs résultats 
Analyse du meilleur modèle sur différents fichiers existants 
'''
import streamlit as st

st.title('Modèles entraînés')
st.subheader("Intérêt du deep learning")
st.markdown("""<div style="text-align: justify"> Les résultats obtenus avec l’Isolation Forest mettent en évidence 
            qu’un changement de paradigme est nécessaire pour progresser vers un système de détection performant. 
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
    st.caption(""" En intégrant des fenêtres temporelles glissantes (4 secondes dans notre cas) 
               et des architectures capables d’exploiter la continuité des signaux, 
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
    
st.subheader("Première approche")
st.subheader("Deuxième approche")
st.subheader("Troisième approche")
