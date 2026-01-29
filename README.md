# Streamlit Project — Web Scraping Véhicules

Auteur : MHSECK — Mouhamadou Habib Seck — https://github.com/MHSECK

Application en ligne
-------------------
Ouvrez l'application Streamlit en cliquant ici : [🌐 Ouvrir l'application sur Streamlit Cloud](https://appproject-axpapmv4rb4rkwpywkyvih.streamlit.app/)

Description
-----------
Application web développée avec Streamlit pour collecter, analyser et visualiser des données de véhicules (locations, ventes, motos et scooters) extraites depuis le web. Le projet sépare la logiq[...]

Principales fonctionnalités
---------------------------
- Scraping de sites de petites annonces pour :
  - Véhicules en location
  - Véhicules en vente
  - Motos et scooters
- Nettoyage et structuration des données collectées
- Export des résultats au format CSV
- Visualisations et tableaux interactifs via Streamlit
- Conception modulaire pour faciliter l'extension et la maintenance

Technologies
------------
- Python 3.9+
- Streamlit
- pandas
- requests
- BeautifulSoup4
- matplotlib

Structure du projet
-------------------
- Donnees/                      — Dossier contenant les fichiers CSV générés par le scraping
- app.py                        — Point d’entrée de l’application Streamlit
- location_vehicule.py          — Fonctions de scraping pour les véhicules en location
- vehicule.py                   — Fonctions de scraping pour les véhicules en vente
- motos_et_scooters.py          — Fonctions de scraping pour les motos et scooters
- requirements.txt              — Dépendances Python
- README.md                     — Documentation (ce fichier)
- LICENSE                       — Licence du projet
- .gitignore                    — Fichiers à ignorer par Git

Installation et exécution (local)
---------------------------------
1. Cloner le dépôt
```bash
git clone https://github.com/MHSECK/streamlit_project.git
cd streamlit_project
```

2. Créer et activer un environnement virtuel
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Lancer l'application Streamlit
```bash
streamlit run app.py
```

Utilisation
-----------
- L'interface Streamlit vous permettra de sélectionner la catégorie (location, vente, motos/scooters), d'exécuter le scraping et d'explorer les résultats.
- Les fichiers CSV générés sont enregistrés dans le dossier `Donnees/`.
- Les fonctions de scraping sont organisées par fichier (ex. `vehicule.py` pour la vente) : vous pouvez les réutiliser ou les étendre dans d'autres scripts.

Déploiement
----------
Cette application est prête à être déployée sur Streamlit Cloud ou sur tout autre service supportant les applications Streamlit. Veillez à :
- inclure le fichier `requirements.txt`
- configurer d'éventuelles variables d'environnement si vous adaptez le scraping à des sites nécessitant des identifiants ou des clés

Bonnes pratiques et limites
---------------------------
- Respectez les conditions d'utilisation et le fichier robots.txt des sites que vous scrapez.
- Évitez les requêtes trop fréquentes : insérez des délais (sleep) entre les requêtes si nécessaire.
- Le scraping peut être sensible aux changements de structure HTML des sites cibles ; maintenir des tests et des validations régulières est recommandé.

Contribution
------------
Les contributions sont bienvenues : ouvrez une issue pour proposer une fonctionnalité ou corriger un bug, puis soumettez une pull request. Suggestions typiques :
- Ajout de nouvelles sources de données
- Amélioration des fonctions de nettoyage et d'export
- Tests unitaires et CI

Support / Contact
-----------------
- Problèmes et demandes : ouvrez une issue sur le dépôt GitHub
- Auteur : MHSECK — Mouhamadou Habib Seck
- Profil GitHub : https://github.com/MHSECK
- Application en ligne : https://appproject-axpapmv4rb4rkwpywkyvih.streamlit.app/

Licence
-------
Consultez le fichier `LICENSE` pour les détails sur la licence du projet.

Remarques finales
-----------------
Ce projet fournit une base modulaire et extensible pour le web scraping d'annonces de véhicules et leur visualisation via Streamlit. N'hésitez pas à forker, améliorer et adapter selon vos besoins [...]
