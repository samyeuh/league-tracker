import requests

nametag_url = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
puuid_url = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"

def get_riot_account(region, name, tag):
    response = requests.get(nametag_url.format(region=region, name=name, tag=tag))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error while getting account")

def get_riot_account_by_puuid(region, puuid):
    response = requests.get(puuid_url.format(region=region, puuid=puuid))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error while getting account")
