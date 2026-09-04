import json # Helps us save the data we scrape in a JSON file
import pandas as pd # Helps us save the data we scrape in a CSV file
from bs4 import BeautifulSoup # Helps us parse the HTML we scrape
from datetime import datetime # Helps us get the current date and time

def extract_cards(har_path):

    with open(har_path, "r") as file:
        har_data = json.load(file)

    entries = har_data["log"]["entries"]

    cards = []

    for entry in entries:
        website_url = entry["request"]["url"]

        if website_url.startswith("https://dokkaninfo.com/cards/"):
            content = entry["response"]["content"]
            
    content = card_entry["response"]["content"]
    
    html = content["text"]
    
    soup = BeautifulSoup(html, "html.parser")

    card_info = soup.find("card-info")
    
    data_json = card_info["v-bind:datajson"]
    
    card_data = json.loads(data_json)
    
    card = card_data["card"]
    
    return card

cards = []

df = pd.DataFrame(cards)

fresh_df = df[["id", "name", "rarity", "element", "cost", "atk_max", "def_max", "hp_max", "open_at"]]

fresh_df["open_at"] = pd.to_datetime(
    fresh_df["open_at"],
    unit="s"
)

fresh_df = fresh_df.rename(columns={"open_at": "release_date"})

fresh_df["release_year"] = fresh_df["release_date"].dt.year