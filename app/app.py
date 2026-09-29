import streamlit as st
from transformers import pipeline

# Configuration de la page
st.set_page_config(page_title="Analyse de Sentiment", page_icon="🧠", layout="centered")

st.title("🧠 Analyseur de Sentiment Client")
st.markdown("Testez l'Intelligence Artificielle en tapant un avis client ci-dessous. Le modèle (Hugging Face BERT) lira votre texte et déterminera l'émotion qui s'en dégage.")

# Chargement du modèle avec cache pour éviter de le recharger à chaque interaction
@st.cache_resource
def charger_modele():
    # Modèle multilingue (comprend très bien le français)
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

with st.spinner("Chargement de l'Intelligence Artificielle (peut prendre quelques secondes la première fois)..."):
    analyseur = charger_modele()

# Interface de saisie
texte_utilisateur = st.text_area("✍️ Entrez un avis client :", placeholder="Exemple : Le service client est vraiment exceptionnel, merci beaucoup !")

if st.button("Analyser le sentiment 🔍"):
    if texte_utilisateur.strip() == "":
        st.warning("Veuillez entrer un texte avant de lancer l'analyse.")
    else:
        # L'IA fait sa prédiction
        resultat = analyseur(texte_utilisateur)[0]
        
        # Extraction du nombre d'étoiles (ex: "5 stars" -> 5)
        etoiles = int(resultat['label'].split()[0])
        confiance = resultat['score'] * 100
        
        st.markdown("---")
        st.subheader("📊 Résultat de l'analyse")
        
        # Affichage visuel des étoiles
        st.markdown(f"**Note estimée par l'IA :** {'⭐' * etoiles}")
        
        # Classification métier
        if etoiles >= 4:
            st.success(f"🟢 **Sentiment Positif** (Confiance : {confiance:.1f}%)")
            st.write("💡 *L'IA pense que ce client est très satisfait.*")
        elif etoiles == 3:
            st.warning(f"🟡 **Sentiment Neutre** (Confiance : {confiance:.1f}%)")
            st.write("💡 *Ce client a un avis mitigé.*")
        else:
            st.error(f"🔴 **Sentiment Négatif** (Confiance : {confiance:.1f}%)")
            st.write("🚨 *Alerte : Ce client est mécontent, intervention du service client recommandée !*")
