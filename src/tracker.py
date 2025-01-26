from discord import TextChannel
from functools import wraps
import api.riot
from database.database import Database
import utils.checker as checker

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
        
    def link(self, user, region: str, name: str, tag: str, serverDiscordId):
        if not checker.checkSetup(self.server, serverDiscordId):
            return Exception("Setup not done")
        try:
            result = api.riot.get_riot_account(region, name, tag)
            account = name + "#" + tag
            accountId = result.get('puuid') # TODO: fix
            if accountId is None:
                print("Error while getting account")
                return Exception("Error while getting account")
            self.player.add_player(user.id, region, account, accountId, serverDiscordId)
        except Exception as e:
            return e
        
    @requires_setup
    def unlink(self):
        pass
    
    @requires_setup
    def profil(self, user):
        pass
