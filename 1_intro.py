'''
Présentation du sujet, du problème et des enjeux

'''
import streamlit as st

st.markdown("""

L’épilepsie est une affection neurologique chronique qui affecte près de 50 millions de personnes dans le monde. Parmi elles, un tiers souffre d’épilepsie pharmaco-résistante, c’est-à-dire que les traitements médicamenteux ne permettent pas de contrôler les crises. Ces patients nécessitent une surveillance attentive de la fréquence et de la sévérité de leurs crises afin d’ajuster les traitements et d’anticiper les risques, mais les outils actuellement disponibles sont souvent intrusifs, coûteux, ou peu pratiques pour une utilisation en continu dans la vie quotidienne.

Dans ce contexte, les enregistrements audio apparaissent comme une voie prometteuse pour le développement de solutions de détection non invasives, discrètes et accessibles. Certaines crises épileptiques s’accompagnent en effet de manifestations sonores caractéristiques – gémissements, vocalisations, bruits moteurs – qui peuvent potentiellement être exploitées pour repérer automatiquement leur survenue. L’analyse de ces signaux via des méthodes d’apprentissage automatique pourrait ainsi contribuer à améliorer le suivi des patients et à renforcer leur sécurité.

Ce projet s’inscrit dans une démarche exploratoire visant à évaluer la pertinence de cette approche à partir de données réelles. À travers le développement d’un prototype interactif, cette application Streamlit permet de tester différentes étapes du pipeline de détection : segmentation audio, extraction de caractéristiques, entraînement de modèles et évaluation des performances. Elle constitue une première étape vers des systèmes d’alerte intelligents basés sur l’analyse audio.

---

### Objectifs

- **Explorer la faisabilité de la détection des crises épileptiques à partir d’enregistrements audio**, en analysant si les caractéristiques sonores peuvent être exploitées à des fins de classification.
  
- **Développer un système de détection basé sur l’apprentissage automatique**, capable de distinguer les périodes de crise des périodes intercritiques à partir de signaux audio, avec pour ambition une solution confortable, non invasive et facilement intégrable.
  
- **Poser les bases pour de futurs développements**, en identifiant les limites, en évaluant les performances actuelles, et en ouvrant la voie à des améliorations ultérieures dans un objectif de déploiement en conditions réelles.
""")
