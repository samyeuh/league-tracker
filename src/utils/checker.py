from database.server import Server
from utils.exceptions import LTException

def checkLink(region, gamename, tag):
    if region.upper() not in ["EUW", "NA", "KR", "JP", "BR", "LAN", "LAS", "OCE", "TR", "RU"]:
        raise LTException("Region Error", "Region not found")
    
    
def checkSetup(server: Server, serverDiscordId):
    if server.get_server(serverDiscordId) is None:
        return False
    else:
        return True