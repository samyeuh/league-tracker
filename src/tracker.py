from discord import TextChannel
from functools import wraps
from database.database import Database

def requires_setup(method):
    """ Décorateur pour vérifier si `setup` a été appelé """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.setupped:
            return self.sendError("Setup not done")
        return method(self, *args, **kwargs)
    return wrapper


class Tracker:
    def __init__(self):
        # TODO: ajouter serv en base de données
        db = Database()
        self.player = db.getPlayer()
        self.stinkson = db.getStinksOn()
        self.server = db.getServer()
        self.setupped = False
    
    def setup(self, channel: TextChannel, serverDiscordId):
        self.setupped = True
        self.channel = channel
        self.server.add_server(serverDiscordId)
        pass

    def sendError(self, message: str):
        return message
    
    @requires_setup
    def link(self, user, region: str, account: str, serverDiscordId):
        # TODO: ajouter la vérification de l'existence de l'utilisateur
        self.player.add_player(user.id, region, account)
        self.st

    @requires_setup
    def unlink(self):
        pass
    
    @requires_setup
    def profil(self, user):
        pass
