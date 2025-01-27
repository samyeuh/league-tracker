from discord import TextChannel, TextInput
from functools import wraps
import api.riot
from database.database import Database
import utils.checker as checker
from utils.exceptions import LTException

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
        result = api.riot.get_riot_account(region, name, tag)
        account = name.value + "#" + tag.value
        accountId = result.get('puuid')
        if accountId is None:
            raise LTException("API Error", "Error while getting account")
        self.player.add_player(user.id, region, account, accountId, serverDiscordId)
        
    def unlink(self, user, serverDiscordId):
        if not checker.checkSetup(self.server, serverDiscordId):
            raise LTException("Setup not done", "Please do the setup before trying to unlink an account")
        self.player.remove_player(serverDiscordId, user.id)
    
    def profil(self, user):
        pass
