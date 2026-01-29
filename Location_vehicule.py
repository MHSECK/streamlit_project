import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get
import streamlit as st
import time

def loc_vehicule(n):
    df = pd.DataFrame()

    progress_bar = st.progress(0)
    status_text = st.empty()

    for index in range(1, n + 1):
        url = f"https://dakar-auto.com/senegal/location-de-voitures-19?&page={index}"
        res = get(url)
        soup = bs(res.content, 'html.parser')

        containers = soup.find_all(
            "div", class_="listings-cards__list-item mb-md-3 mb-3"
        )

        data = []

        for container in containers:
            try:
                gen_inf = container.find('h2',class_="listing-card__header__title mb-md-2 mb-0").a.text.strip().split()
                marque = gen_inf[0]
                annee = int(gen_inf[-1])
                modele = " ".join(gen_inf[1:-1])

                prix = float(container.find('h3',class_="listing-card__header__price font-weight-bold text-uppercase mb-0"
                    ).text.strip().replace('\u202f', '').replace(' F CFA', '')
                )

                quartier = container.find("span", class_="town-suburb d-inline-block").text.replace(',', '')

                region = container.find("span", class_="province font-weight-bold d-inline-block").text

                proprietaire = container.find("p", "time-author m-0").text.replace("Par ", "")

                data.append({
                    "marque": marque,
                    "annee": annee,
                    "modele": modele,
                    "prix": prix,
                    "quartier": quartier,
                    "region": region,
                    "Proprietaire": proprietaire
                })

            except:
                pass

        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

        #  PROGRESSION
        percent = int((index / n) * 100)
        progress_bar.progress(percent)
        status_text.markdown(
            f" Location de véhicules : **Page {index}/{n}** — **{percent}%**"
        )

    status_text.success("Scraping location terminé avec succès !")
    time.sleep(1)
    progress_bar.empty()
    status_text.empty()

    return df
