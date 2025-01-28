import os
import requests
from api.lol import get_summoner_id
from utils.exceptions import LTException

nametag_url = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={api_key}"
puuid_url = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={api_key}"

def getRiotRegion(region):
    if region in ["EUW", "EUNE", "TR", "RU", "ME"]:
        return "europe"
    elif region in ["NA","BR", "LAN", "LAS"]:
        return "americas"
    elif region in ["KR", "JP"]:
        return "asia"
    elif region in ["OCE", "SG", "PH", "TH", "TW", "VN"]:
        return "sea"
    else:
        raise LTException("Invalid region", "Please, enter a valid region")

def get_riot_account(region, name, tag):
    riotregion = getRiotRegion(region)
    response = requests.get(nametag_url.format(region=riotregion, name=name, tag=tag, api_key=os.getenv('API_KEY')))
    if response.status_code == 200:
        data = response.json()
        print(data.get('puuid'))
        if not data.get('puuid'):
            raise ValueError("Invalid Riot account data: missing PUUID")
        return get_summoner_id(region, data.get('puuid')), data.get('puuid')
    else:
        raise LTException("Riot API Error", f"Error while getting account: {response.status_code} - {response.text}")

def get_riot_account_by_puuid(region, puuid):
    response = requests.get(puuid_url.format(region=region, puuid=puuid, api_key=os.getenv('API_KEY')))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error while getting account")
