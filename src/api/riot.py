import requests

api_key = ""
nametag_url = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}{api_key}"
puuid_url = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"

def get_riot_account(region, name, tag):
    if region == "EUW":
        region = "europe"
    response = requests.get(nametag_url.format(region=region, name=name, tag=tag, api_key=api_key))
    if response.status_code == 200:
        data = response.json()
        if not data.get('puuid'):
            raise ValueError("Invalid Riot account data: missing PUUID")
        return data
    else:
        raise Exception(f"Error while getting account: {response.status_code} - {response.text}")

def get_riot_account_by_puuid(region, puuid):
    response = requests.get(puuid_url.format(region=region, puuid=puuid))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error while getting account")
