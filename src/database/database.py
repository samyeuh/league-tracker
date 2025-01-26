import sqlite3


class Database:
   def __init__(self):
         conn = sqlite3.connect('tracker.db')
         self.cursor = conn.cursor()
         self.cursor.execute('''
               CREATE TABLE IF NOT EXISTS Server(
                  id INT,
                  discordId BIGINT NOT NULL,
                  PRIMARY KEY(id),
                  UNIQUE(discordId)
               );
            ''')
         # TODO: ajouter region et puuid
         self.cursor.execute('''CREATE TABLE IF NOT EXISTS Player(
                  id INT,
                  discordId BIGINT NOT NULL,
                  region VARCHAR(50) NOT NULL,
                  summonerName VARCHAR(500) NOT NULL,
                  PRIMARY KEY(id),
                  UNIQUE(discordId),
                  UNIQUE(summonerName)
               );
            ''')
         self.cursor.execute('''CREATE TABLE IF NOT EXISTS StrinksOn(
                  serverId INT,
                  playerId INT,
                  PRIMARY KEY(serverId, playerId),
                  FOREIGN KEY(serverId) REFERENCES Serveur(id),
                  FOREIGN KEY(playerId) REFERENCES Joueur(id)
               );
         ''')
         from database.server import Server
         from database.stinkson import StinksOn
         from database.player import Player
         self.server = Server(self)
         self.stinkson = StinksOn(self)
         self.player = Player(self)


   def getCursor(self):
      return self.cursor
   
   def getServer(self):
      return self.server
   
   def getStinksOn(self):
      return self.stinkson
    
   def getPlayer(self):
        return self.player