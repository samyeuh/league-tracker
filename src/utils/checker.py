
def checkLink(region, gamename, tag):
    return region.upper() in ["EUW", "NA", "KR", "JP", "BR", "LAN", "LAS", "OCE", "TR", "RU"]
    
    
def checkSetup(server, serverDiscordId):
    if server.get_server(serverDiscordId) is None:
        return False