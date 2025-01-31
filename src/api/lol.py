import os
import requests
from utils.exceptions import LTException
import api.riot

summonerId_url = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={api_key}"
get_matchs_url = "https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?{gametype}start=0&count={count}&api_key={api_key}"
match_info_url = "https://{region}.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={api_key}"

"""
Queue ID Info:
900 - Urf
450 - ARAM
440 - Flex
420 - SoloQ
400 - Normal
"""

def get_lol_region(region):
    lol_regions = {"NA": "na1","BR": "br1","LAN": "la1","LAS": "la2","EUW": "euw1","EUNE": "eun1","OCE": "oc1","KR": "kr",
                   "RU": "ru","TR": "tr1","JP": "jp1","PH": "ph2","SG": "sg2","TH": "th2","TW": "tw2","VN": "vn2"}
    if region in lol_regions:
        return lol_regions[region]
    else:
        val = [k for k, v in lol_regions.items() if v == region.lower()][0]
        if val:
            return val
        else:
            raise LTException("Invalid region", "Please, enter a valid region")

def get_summoner_id(region, puuid):
    lolRegion = get_lol_region(region)
    response = requests.get(summonerId_url.format(region=lolRegion, puuid=puuid, api_key=os.getenv('API_KEY')))
    if response.status_code == 200:
        return response.json().get('id')
    else:
        raise LTException("LOL API Error", f"Error while getting account: {response.status_code} - {response.text}")


def get_last_matchs(puuid, playerRegion, gametype, count=5):
    continent = api.riot.getRiotRegion(playerRegion)
    response = requests.get(get_matchs_url.format(region=continent, gametype=gametype.value, puuid=puuid, count=count, api_key=os.getenv('API_KEY')))
    if response.status_code == 200:
        return response.json()
    else:
        raise LTException("LOL API Error", f"Error while getting matchs {response.status_code} - {response.text}")

def get_match_info(matchId):
    server = matchId.split("_")[0]
    region = get_lol_region(server)
    continent = api.riot.getRiotRegion(region)
    response = requests.get(match_info_url.format(region=continent, matchId=matchId, api_key=os.getenv('API_KEY')))
    if response.status_code == 200:
        return response.json()
    else:
        raise LTException("LOL API Error", f"Error while getting match info {response.status_code} - {response.text}")