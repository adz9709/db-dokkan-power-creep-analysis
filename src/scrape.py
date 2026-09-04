import json # Helps us save the data we scrape in a JSON file
import pandas as pd # Helps us save the data we scrape in a CSV file
from bs4 import BeautifulSoup # Helps us parse the HTML we scrape
from datetime import datetime # Helps us get the current date and time


def extract_card(har_path, target_url):

    with open(har_path, "r") as file:
        har_data = json.load(file)

    entries = har_data["log"]["entries"]
    
    for entry in entries:
        entry_url = entry["request"]["url"]

        if entry_url == target_url:
            card_entry = entry

    content = card_entry["response"]["content"]

    html = content["text"]

    soup = BeautifulSoup(html, "html.parser")

    card_info = soup.find("card-info")

    data_json = card_info["v-bind:datajson"]

    card_data = json.loads(data_json)

    card = card_data["card"]

    return card

goku = extract_card("data/dokkaninfo.com.har", "https://dokkaninfo.com/cards/1034031")
frieza = extract_card("data/dokkaninfo.com2.har", "https://dokkaninfo.com/cards/1033971")

cards = [goku, frieza]

df = pd.DataFrame(cards)

fresh_df = df[["id", "name", "rarity", "element", "cost", "atk_max", "def_max", "hp_max"]]