from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from pandas import DataFrame
import re

site = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete?enteredFrom=one_step_search"
domain="https://www.immobilienscout24.de"
wohnung_data = DataFrame()


def get_links(url):
    try:
        url = urlopen(url)
    except:
        print("Fehler beim Oeffnen der Website")
    try:
        site_extract = BeautifulSoup(url.read(), "lxml")
    except:
        print("Fehler beim Einlesen in BeautifulSoup")
    try:
        link_list_raw = []
        for option in site_extract.find_all("option"):
            link_list_raw.append(option["value"])
    except:
        print("Fehler beim Loop")
    try:
        link_list = [link for link in link_list_raw if "Suche" in link]
    except:
        print("Fehler beim Saeubern")
    else:
        return link_list

    
def get_data(url):
    try:
        url = urlopen(url)
    except HTTPError as e:
        return None
    try:
        site_extract = BeautifulSoup(url.read(), "lxml")
        rawdata_extract = site_extract.find_all("div", {"class":"result-list-entry__data"})
    except AttributeError as e:
        return None
    global wohnung_data
    for i in range(1,len(rawdata_extract)):
        price = []
        size = []
        location = []
        try:
            price.append(rawdata_extract[i].find_all("dd")[0].get_text().strip())
        except:
            price.append(None)
        try:
            size.append(rawdata_extract[i].find_all("dd")[1].get_text().strip())
        except:
            size.append(None)
        try:
            location.append(rawdata_extract[i].find_all("div", {"class":"result-list-entry__address nine-tenths"})[0].get_text().strip())
        except:
            location.append(None)
        wohnung_data = wohnung_data.append(DataFrame({"price":price, "size":size,"location":location}), ignore_index=True)
    


def immo_crawl(start):
    links = get_links(start)
    for link in links:
        get_data(domain+link)
        print("Bearbeiten von "+link)
        
immo_crawl(site)

wohnung_data.to_csv("~/wohnung_data_raw.csv", sep=";", index=False)

def clean_pricesize(data):
    data = data.replace("€", "")
    data = data.replace(".", "")
    data = data.replace("m²", "")
    data = re.sub(re.compile(" \D.*"), "", data)
    data = data.strip()
    return data

def get_firstlayer(data):
    fist_layer = data.split(",")[0]
    return fist_layer.strip()

def get_lastlayer(data):
    last_layer = data.split(",")[-1]
    return last_layer.strip()
    
wohnung_data_clean = wohnung_data.dropna(axis=0)
wohnung_data_clean["price"] = wohnung_data_clean["price"].apply(clean_pricesize)
wohnung_data_clean["size"] = wohnung_data_clean["size"].apply(clean_pricesize)
wohnung_data_clean["location_first"] = wohnung_data_clean["location"].apply(get_firstlayer)
wohnung_data_clean["location_last"] = wohnung_data_clean["location"].apply(get_lastlayer)

wohnung_data_clean.to_csv("~/wohnung_data_clean.csv", sep=";", index=False)