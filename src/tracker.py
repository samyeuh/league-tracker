from discord import TextChannel
from database.database import Database

class Tracker:
    def __init__(self):
        # TODO: ajouter serv en base de données
        db = Database()
        self.player = db.getPlayer()
    
    def setup(self, channel: TextChannel):
        pass

    def sendError(self, message: str):
        return message
    
    def link(self, user, region: str, account: str):
        # TODO: ajouter la vérification de l'existence de l'utilisateur
        self.player.add_player(user.id, region, account)

    def unlink(self):
        pass
    
    def profil(self, user):
        pass
