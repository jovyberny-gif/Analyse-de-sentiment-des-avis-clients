import pandas as pd
import numpy as np
import random

def generate_reviews():
    avis_positifs = [
        "Super produit, la qualité est au rendez-vous. Je recommande !",
        "Livraison très rapide et article conforme à la description.",
        "Excellent rapport qualité-prix, je suis ravi de mon achat.",
        "Le service client a été génial pour résoudre mon problème.",
        "Parfait, rien à redire. Fonctionne comme prévu.",
        "Très bel emballage, produit robuste. J'adore.",
        "Je l'utilise tous les jours, c'est devenu indispensable.",
        "Mieux que ce que j'espérais. 5 étoiles."
    ]
    
    avis_neutres = [
        "Produit correct, fait le job mais sans plus.",
        "Conforme aux attentes, ni bon ni mauvais.",
        "C'est OK pour le prix, mais la finition pourrait être mieux.",
        "L'article est arrivé avec un peu de retard mais il est intact.",
        "Pas mal, à voir sur le long terme comment ça vieillit."
    ]
    
    avis_negatifs = [
        "Très déçu, l'article s'est cassé après deux utilisations.",
        "Le service client est catastrophique, impossible de les joindre.",
        "La livraison a pris un mois et le colis était abîmé.",
        "La batterie ne tient pas du tout, c'est de l'arnaque.",
        "Je demande un remboursement, la qualité est médiocre.",
        "Ne fonctionne pas, très mauvais achat.",
        "Le produit reçu ne correspond pas à la photo du site."
    ]
    
    data = []
    
    for _ in range(300):
        data.append({"Texte": random.choice(avis_positifs), "Sentiment_Reel": "Positif", "Note": random.randint(4, 5)})
    
    for _ in range(150):
        data.append({"Texte": random.choice(avis_neutres), "Sentiment_Reel": "Neutre", "Note": 3})
        
    for _ in range(250):
        data.append({"Texte": random.choice(avis_negatifs), "Sentiment_Reel": "Negatif", "Note": random.randint(1, 2)})
        
    random.shuffle(data)
    
    df = pd.DataFrame(data)
    df.to_csv('data/avis_clients.csv', index=False, encoding='utf-8')
    print("Dataset de 700 avis généré avec succès dans data/avis_clients.csv")

if __name__ == "__main__":
    random.seed(42)
    generate_reviews()
