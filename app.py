import streamlit as st 
import pandas as pd
import time
import matplotlib.pyplot as plt
from vehicule import vehicule
from motos_et_scooters import motos
from Location_vehicule import loc_vehicule

# Menu

st.sidebar.title("Menu")
page =st.sidebar.radio("Navigation",["Accueil","Scraping","Donnée de Web Sraper","Vusialiser les données","AVIS"])


def accueil():
    st.title(" Plateforme de Web Scraping Automobile")
    st.subheader("Collecte intelligente et visualisation des annonces en ligne")
    st.markdown("""Cette application permet d’extraire automatiquement des annonces de **véhicules**,  
    **motos & scooters**, et **services de location**, à partir du site **https://dakar-auto.com/senegal/** .

    Elle offre une interface simple, rapide et interactive pour :
    - Collecter les données
    - Les analyser
    -  Les visualiser
    """)
    st.divider()
    st.header("Fonctionnalités principales")

    st.markdown("""
    - **Web Scraping automatisé** multi-pages  
    - **Paramétrage flexible** (type de données & nombre de pages)  
    - **Suivi en temps réel** avec progression et logs  
    - **Affichage dynamique** des résultats  
    - **Interface propre et intuitive**
    """)
    st.header("Comment utiliser l’application ?")

    st.markdown("""
    Accédez au menu **Scraping**  
    Choisissez le type de contenu à extraire  
    Sélectionnez le nombre de pages  
    Lancez le scraping  
    Consultez et Visualiser les résultats
    """)
    st.info(" Les données collectées sont utilisées uniquement à des fins d’analyse.")
    st.markdown("---")
    st.caption("© 2026 • Web Scraping Dashboard • Développé avec Streamlit")








def Scraping():
     # Mardown
    st.sidebar.markdown("---")
    st.sidebar.markdown("Options")

    
    # nombre 

    nombre = st.sidebar.number_input(
        "Entrer le nombre de pages à Sraper",
        min_value=1,
        max_value=50,
        step=1
    )
    choix = st.sidebar.selectbox(
        "Choisir le type a Sraper",
        ["Vehicules", "Motos & Scooters", "Location_Vehicules"]
    )


    st.title("Web Scraping Automobile")
    st.subheader("Extraction dynamique des données")
    st.markdown("---")
    st.markdown("**SITE DAKAR AUTO**")

    if st.sidebar.button("Lancer le Scraping"):
        st.sidebar.success(f"Option sélectionnée : {choix} et le nombre de page à scraper seras de {nombre}")

        if  choix == "Vehicules":
            df_vehicule = vehicule(nombre)
            col1, col2, col3 = st.columns(3)
            col1.metric("Pages", nombre)
            col2.metric("Résultats", len(df_vehicule))
            col3.metric("Type", choix)
            st.dataframe(df_vehicule)
            st.session_state["df_vehicule"] = df_vehicule
      


        elif choix == "Motos & Scooters":
            df_moto = motos(nombre)
            col1, col2, col3 = st.columns(3)
            col1.metric("Pages", nombre)
            col2.metric("Résultats", len(df_moto))
            col3.metric("Type", choix)
            st.session_state["df_moto"] = df_moto
            st.dataframe(df_moto)
            
            
        else:
            df_loc_vechicule = loc_vehicule(nombre)
            col1, col2, col3 = st.columns(3)
            col1.metric("Pages", nombre)
            col2.metric("Résultats", len(df_loc_vechicule))
            col3.metric("Type", choix)
            st.session_state["df_loc_vehicule"] = df_loc_vechicule
            st.dataframe(df_loc_vechicule)
    st.info(" Les données collectées sont utilisées uniquement à des fins d’analyse.")
    st.markdown("---")
    st.caption("© 2026 • Web Scraping Dashboard • Développé avec Streamlit")


            
def Web_Scraper():
    st.sidebar.markdown("---")
    st.sidebar.markdown("Options")
    choix = st.sidebar.selectbox("Choisir le type a Sraper",
        ["Vehicules", "Motos & Scooters", "Location_Vehicules"])
    st.title("Web Scraping Automobile")
    st.subheader("Données obtenues avec l'extention Web Scraper")
    st.markdown("---")
    st.markdown("**SITE DAKAR AUTO**")
    if st.sidebar.button("Voir les donnees"):
        st.sidebar.success(f"Option sélectionnée : {choix}")
        if  choix == "Vehicules":
            df_vehicule_web_scraper = pd.read_csv("Donnees/Voiture_Dakar_Auto.csv")
            df_vehicule_web_scraper =  df_vehicule_web_scraper.drop(columns=["web_scraper_order","web_scraper_start_url"])
            col1, col2, col3 = st.columns(3)
            col1.metric("Pages", 50)
            col2.metric("Résultats", len(df_vehicule_web_scraper))
            col3.metric("Type", choix)
            st.dataframe(df_vehicule_web_scraper)

        elif choix == "Motos & Scooters":
            df_moto_scraper = pd.read_csv("Donnees/Moto_dakar_auto.csv")
            df_moto_scraper =  df_moto_scraper.drop(columns=["web_scraper_order","web_scraper_start_url"])
            col1, col2, col3 = st.columns(3)
            col1.metric("Pages", 16)
            col2.metric("Résultats", len(df_moto_scraper))
            col3.metric("Type", choix)
            st.dataframe(df_moto_scraper)

        else:
            df_vehicule_loc_scraper = pd.read_csv("Donnees/Voiture_location_dakar_Auto.csv")
            df_vehicule_loc_scraper =  df_vehicule_loc_scraper.drop(columns=["web_scraper_order","web_scraper_start_url"])
            col1, col2, col3 = st.columns(3)
            col1.metric("Pages", 50)
            col2.metric("Résultats", len( df_vehicule_loc_scraper))
            col3.metric("Type", choix)
            st.dataframe( df_vehicule_loc_scraper)
    st.info("Les données collectées sont utilisées uniquement à des fins d’analyse.")
    st.markdown("---")
    st.caption("© 2026 • Web Scraping Dashboard • Développé avec Streamlit")



def visualiser():
    st.sidebar.markdown("---")
    st.sidebar.markdown("Options")
    choix = st.sidebar.selectbox("Choisir le type a Visualiser",
        ["Vehicules", "Motos & Scooters", "Location_Vehicules"])
    st.title("Web Scraping Automobile")
    st.subheader("Données obtenues Visualiser sont obtenues via votre dernier web Sraping lancer (Le faire si c'est pas encore fait) ")
    st.markdown("---")
    st.markdown("**SITE DAKAR AUTO**")
    if st.sidebar.button("Vusialiser"):
        st.sidebar.success(f"Option sélectionnée : {choix}")

     # VÉRIFICATION DU DATASET
        verification = {
            "Vehicules": "df_vehicule",
            "Motos & Scooters": "df_moto",
            "Location_Vehicules": "df_loc_vehicule"
        }

        key = verification[choix]

        if key not in st.session_state:
            st.warning("Aucun dataset trouvé")
            st.info("Veuillez d'abord lancer le Scraping.")
            st.stop()

        df = st.session_state[key]

        st.success("Données chargées avec succès")
        st.dataframe(df)
        st.subheader("Distribution des prix")

        fig, ax = plt.subplots()
        ax.hist(df["prix"], bins=20)
        ax.set_title("Répartition des prix des véhicules")
        ax.set_xlabel("Prix (FCFA)")
        ax.set_ylabel("Nombre d'annonces")

        st.pyplot(fig)

        st.subheader("Prix moyen par marque")

        prix_moyen = df.groupby("marque")["prix"].mean()

        fig, ax = plt.subplots()
        prix_moyen.plot(kind="bar", ax=ax)
        ax.set_title("Prix moyen par type de véhicule")
        ax.set_xlabel("Type")
        ax.set_ylabel("Prix moyen (FCFA)")
        ax.tick_params(axis='x', rotation=45)

        st.pyplot(fig)
        
        st.subheader("Prix selon l’année")

        fig, ax = plt.subplots()
        ax.scatter(df["annee"], df["prix"])
        ax.set_title("Relation Année - Prix")
        ax.set_xlabel("Année")
        ax.set_ylabel("Prix (FCFA)")

        st.pyplot(fig)

        st.subheader(" Top 10 marques")

        top_marques = df["marque"].value_counts().head(10)

        fig, ax = plt.subplots()
        top_marques.plot(kind="barh", ax=ax)
        ax.set_title("Top 10 des marques")
        ax.set_xlabel("Nombre d'annonces")
        ax.invert_yaxis()

        st.pyplot(fig)


        col1, col2 = st.columns(2)
        col1.metric("Annonces", len(df))
        col2.metric("Année médiane", int(df["annee"].median()))
        st.info("Les données collectées sont utilisées uniquement à des fins d’analyse.")
        st.markdown("---")
        st.caption("© 2026 • Web Scraping Dashboard • Développé avec Streamlit")





def avis():
    st.markdown("Merci de prendre  2-3 minutes pour repondre a notre questionnaire de satisfaction")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(" Aller sur Kobo"):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=https://ee.kobotoolbox.org/x/T1rdPaRc">',
                unsafe_allow_html=True
            )

    with col2:
        if st.button("Aller sur Google forms"):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=https://forms.gle/7HjydWJv6UTgfeRV7">',
                unsafe_allow_html=True
            )
    st.info(" Les données collectées sont utilisées uniquement à des fins d’analyse.")
    st.markdown("---")
    st.caption("© 2026 • Web Scraping Dashboard • Développé avec Streamlit")



if page == "Scraping":
     Scraping()





elif page == "Donnée de Web Sraper":
    Web_Scraper()

elif page == "Vusialiser les données":
    visualiser()

elif page == "Accueil":
   accueil()



elif page == "AVIS":
    avis()