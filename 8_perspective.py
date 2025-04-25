'''
Critique et perspectives :
ce qui aurait pû être fait avec plus de temps.

'''

import streamlit as st

st.title('Critiques et perspectives')
st.subheader(':orange[Difficultés rencontrées]')
with st.expander("🔒 Verrou scientifique principal"):
    st.markdown(""" Le principal verrou scientifique rencontré durant ce projet a été la complexité de la gestion des données audio, 
                notamment en ce qui concerne l’équilibrage des classes et la diversité des enregistrements. """)
    st.markdown("""Le signal audio est particulièrement sensible aux facteurs environnementaux, 
                tels que les bruits de fond ou les variations de lieu d’enregistrement (milieu hospitalier), 
                rendant la détection automatisée des crises épileptiques plus complexe et moins généralisable.""")
with st.expander("🔮 Prévisionnel"):
    st.markdown(""" Certaines tâches ont nécessité plus de temps que prévu, en particulier : """)
    st.markdown(""" * L’exploration des caractéristiques audio, 
                qui a demandé une phase importante d’essais et d’erreurs pour identifier les représentations temporelles
                 et fréquentielles les plus pertinentes ;""")
    st.markdown(""" * Docker, dont la configuration pour l’environnement d’exécution a été plus longue que prévu, 
                notamment pour la compatibilité avec les bibliothèques spécifiques de traitement audio et d’apprentissage profond ; """)
    st.markdown(""" * L'exploration de CuDF, envisagée pour optimiser le traitement des données via le GPU, 
                a finalement été abandonnée en raison de limitations de compatibilité et d’intégration avec les autres outils du pipeline. """)
    st.markdown("""Aussi, pour une sélection rapide de modèles classiques, nous avons initialement utilisé LazyPredict. 
                Toutefois, nous l’avons écarté pour nous diriger vers des approches plus ciblées.""")
with st.expander("📊 Jeu de données"):
    st.markdown(""" L’acquisition de données audio supplémentaires s’est révélée plus difficile que prévu :
                 à ce jour, aucune nouvelle source externe n’a pu être intégrée au projet.""")
    st.markdown(""" Le déséquilibre entre les classes (crises vs. non-crises) a constitué un obstacle récurrent. 
                L’adoption de techniques d’undersampling a permis d’atténuer cet effet, 
                mais au prix d’une réduction de la diversité des segments disponibles pour l’apprentissage. 
                Ce compromis a nécessité plusieurs ajustements et validations pour stabiliser les performances.""")
with st.expander("🤓Compétences techniques / théoriques"):
    st.markdown(""" Le projet a rapidement requis des compétences avancées en deep learning et en traitement du signal audio, 
                qui sont abordées dans la deuxième moitié de la formation. 
                Cela a nécessité de prendre de l’avance sur le programme: modélisation CNN sur spectrogrammes, 
                manipulation de bibliothèques audio, 
                ou encore compréhension des métriques propres à un contexte de déséquilibre de classes. """)
with st.expander("💻 Ressources informatiques"):
    st.markdown(""" La puissance de calcul disponible s’est parfois révélée limitée pour l’entraînement de modèles complexes 
                sur des jeux de données volumineux. Malgré l'utilisation de GPU, certaines contraintes techniques comme la gestion
                 de la mémoire ou le temps de chargement des données ont constitué des freins. Des ajustements progressifs du batch size,
                 du prétraitement et du pipeline de données ont été nécessaires pour garantir une exécution fluide.""")


st.subheader(':green[Perspectives et pistes d\'amélioration]')
st.caption("""Les résultats obtenus dans ce projet ont permis de mettre en place un pipeline prometteur 
           pour la détection des crises d’épilepsie à partir du signal vocal, 
           notamment grâce à l’utilisation de réseaux de neurones convolutifs appliqués à des segments de 2 secondes.
           Cependant, plusieurs axes d’amélioration sont encore à explorer pour renforcer la robustesse, 
           la généralisation et l’utilisabilité de ce modèle, particulièrement dans des contextes cliniques ou embarqués.""")
with st.expander("📈 Diversification et augmentation des données"):
    st.caption("""L'un des principaux défis réside dans la taille et le déséquilibre du jeu de données, 
               qui peuvent limiter la capacité du modèle à généraliser à de nouveaux cas cliniques. 
               L’intégration de données issues d’enregistrements réels provenant de différents contextes cliniques 
               (différents environnements sonores, langues, etc.) permettrait également de renforcer la transférabilité 
               et la fiabilité du modèle.""")
with st.expander("⏱️ Affinage de la représentation temporelle"):
    st.caption("""Le choix actuel de segments de 2 secondes a montré de bons résultats, 
               mais il pourrait être judicieux d’explorer d'autres approches temporelles. 
               L’utilisation de fenêtres adaptatives ou de modèles à mémoire longue, tels que les LSTM, 
               GRU ou transformers temporels, pourrait permettre de mieux capter les dynamiques complexes des crises, 
               dont la signature sonore peut évoluer au fil du temps. Un affinement dans le fenêtrage, 
               par exemple en utilisant un chevauchement glissant des fenêtres, 
               pourrait aussi améliorer la résolution temporelle tout en maintenant la charge computationnelle à un niveau acceptable.""")
with st.expander("⚖️ Optimisation de l’équilibrage des classes"):
    st.caption("""Le déséquilibre entre les classes reste un problème majeur pour garantir des performances optimales. 
               En plus des techniques d’undersampling classiques, des approches d’équilibrage comme le focal loss, 
               les méthodes de suréchantillonnage synthétique (par exemple, SMOTE pour les signaux audio), 
               ou encore des approches bayésiennes intégrant une incertitude sur les prédictions pourraient être explorées 
               pour améliorer la précision et la robustesse des prédictions. """)
with st.expander("📉 Optimisation des architectures et des fonctions de perte"):
    st.caption("""Les architectures neuronales utilisées jusqu'à présent sont efficaces, 
               mais il serait pertinent d’explorer d’autres architectures proposées dans la littérature, 
               notamment celles ayant montré des succès dans des tâches similaires de détection temporelle dans des signaux audio. 
               Par ailleurs, l'optimisation des fonctions de perte pourrait être affinée en se basant sur des métriques 
               supplémentaires telles que le recall, pour mieux prendre en compte les faux négatifs, 
               particulièrement critiques dans le contexte de la détection de crises.""")
with st.expander("👩🏻‍⚕️Évaluation en conditions réalistes"):
    st.caption("""Les performances actuelles ont été évaluées sur un jeu de validation provenant du même corpus
                que les données d’entraînement. Une validation croisée sur plusieurs patients ou sur un corpus indépendant
                permettrait de mieux évaluer la capacité de généralisation du modèle. 
               De plus, l’implémentation d’un pipeline temps réel, serait un élément essentiel pour permettre l’utilisation 
               de ce modèle dans des dispositifs embarqués, tels que des téléphones portables ou des dispositifs d’assistance, 
               offrant ainsi une réponse immédiate lors d'un épisode de crise.""")
with st.expander("🏥Vers une application clinique et multimodale"):
    st.caption("""À terme, cette approche pourrait s'intégrer dans un dispositif d’alerte portable et autonome, 
               voire multimodal, en combinant le signal audio avec d'autres données provenant de capteurs 
               (par exemple, vidéo, accéléromètre, électrocardiogramme). Un système de détection multimodal 
               pourrait offrir une solution plus robuste et fiable pour la gestion des crises d’épilepsie dans des contextes variés.""")
    st.caption("""Un autre axe important pour l'avenir du projet serait de développer des modèles explicables. 
               Il serait crucial que les soignants ou les utilisateurs puissent comprendre les motifs acoustiques 
               déclenchant une alerte, afin de renforcer la confiance dans l’outil et son utilisation en clinique. 
               Cette explication des décisions pourrait aussi aider à l'amélioration continue des modèles, 
               en offrant un retour d'expérience sur les alertes générées.""")
