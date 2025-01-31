from discord import TextChannel, TextInput
from functools import wraps
import api.riot as riot
import api.lol as lol
from database.database import Database
import utils.checker as checker
from utils.exceptions import LTException
import utils.embedder as embedder

def requires_setup(method):
    """ Décorateur pour vérifier si `setup` a été appelé """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        serverDiscordId = kwargs.get('serverDiscordId')
        if not checker.checkSetup(self.server, serverDiscordId):
            return Exception("Setup not done")
        return method(self, *args, **kwargs)
    return wrapper

class Tracker:
    def __init__(self):
        db = Database()
        self.player = db.getPlayer()
        self.stinkson = db.getStinksOn()
        self.server = db.getServer()
    
    def setup(self, channel: TextChannel, serverDiscordId):
        self.server.add_server(serverDiscordId, channel.id)
        
    def sendError(self, message: str):
        return message
        
    def link(self, user, region: str, name: TextInput, tag: TextInput, serverDiscordId):
        if not checker.checkSetup(self.server, serverDiscordId):
            raise LTException("Setup not done", "Please do the setup before trying to link an account")
        summonerId, accountId = riot.get_riot_account(region, name, tag)
        summonerName = name.value + "#" + tag.value
        self.player.add_player(user.id, region, summonerName, accountId, summonerId, serverDiscordId)
        
    def unlink(self, user, serverDiscordId):
        if not checker.checkSetup(self.server, serverDiscordId):
            raise LTException("Setup not done", "Please do the setup before trying to unlink an account")
        self.player.remove_player(serverDiscordId, user.id)
    
    def profil(self, user):
        pass
    
    def getLastMatchs(self, user, gametype, serverDiscordId,count=5):
        if not checker.checkSetup(self.server, serverDiscordId):
            raise LTException("Setup not done", "Please do the setup before trying to get your last matchs")
        player = self.player.get_player(user.id)
        if player is None:
            raise LTException("Player not found", "Please link your account before trying to get your last matchs")
        matchsId = lol.get_last_matchs(player[4], player[2], gametype, count)
        embedderList = []
        for matchId in matchsId:
            match = lol.get_match_info(matchId)
            embed = embedder.matchEmbed(match)
            embedderList.append(embed)
        return embedderList if embedderList else None
