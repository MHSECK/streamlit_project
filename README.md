
# Streamlit Project – Web Scraping Véhicules

Application web développée avec **Streamlit** permettant de **scraper, analyser et visualiser** des données de véhicules (location, vente, motos et scooters) à partir du web.

Le projet utilise **BeautifulSoup** pour le web scraping et affiche les résultats sous forme de tableaux et graphiques interactifs.

---

##  Objectifs du projet
- Scraper des données de véhicules depuis des sites web
- Séparer la logique de scraping par catégorie
- Générer des fichiers CSV à partir des données collectées
- Visualiser les données via une interface Streamlit
- Déployer facilement l’application via Streamlit Cloud

---

##  Technologies utilisées
- Python 3.9+
- Streamlit
- Pandas
- Requests
- BeautifulSoup4
- Matplotlib

---

## Structure du projet
📦 streamlit_project
┣ 📂 Donnees
┃   ┗ 📜 fichiers CSV générés par le scraping
┣ 📜 app.py                  # Application principale Streamlit
┣ 📜 location_vehicule.py    # Scraping des véhicules en location
┣ 📜 vehicule.py             # Scraping des véhicules en vente
┣ 📜 motos_et_scooters.py    # Scraping des motos et scooters
┣ 📜 requirements.txt        # Dépendances Python
┣ 📜 README.md               # Documentation
┣ 📜 LICENSE
┗ 📜 .gitignore

---

## 🧩 Description des modules
- **`location_vehicule.py`**  
  Contient les fonctions de scraping pour les véhicules en location.

- **`vehicule.py`**  
  Contient les fonctions de scraping pour les véhicules en vente.

- **`motos_et_scooters.py`**  
  Contient les fonctions de scraping pour les motos et scooters à vendre.

- **`Donnees/`**  
  Dossier contenant les fichiers CSV générés par le web scraping.

- **`app.py`**  
  Point d’entrée de l’application Streamlit.  
  Il importe les fonctions de scraping et affiche les résultats.

---

## ▶️ Exécution du projet en local

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/MHSECK/streamlit_project.git
cd streamlit_project

### 2️⃣ **Créer un environnement virtuel**
python -m venv venv

Activation :
	•	Windows
venv\Scripts\activate
 •	Linux / macOS
source venv/bin/activate

### 3️⃣ Installer les dépendances
     pip install -r requirements.txt

### 4️⃣ Lancer l’application Streamlit
     streamlit run app.py







