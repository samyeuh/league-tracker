import os
import requests
from utils.exceptions import LTException

summonerId_url = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={api_key}"

lol_regions = {
    "NA": "na1",
    "BR": "br1",
    "LAN": "la1",
    "LAS": "la2",
    "EUW": "euw1",
    "EUNE": "eun1",
    "OCE": "oc1",
    "KR": "kr",
    "RU": "ru",
    "TR": "tr1",
    "JP": "jp1",
    "PH": "ph2",
    "SG": "sg2",
    "TH": "th2",
    "TW": "tw2",
    "VN": "vn2"
}

def get_lol_region(region):
    if region in lol_regions:
        return lol_regions[region]
    else:
        raise LTException("Invalid region", "Please, enter a valid region")

def get_summoner_id(region, puuid):
    lolRegion = get_lol_region(region)
    response = requests.get(summonerId_url.format(region=lolRegion, puuid=puuid, api_key=os.getenv('API_KEY')))
    if response.status_code == 200:
        return response.json().get('id')
    else:
        raise LTException("LOL API Error", f"Error while getting account: {response.status_code} - {response.text}")