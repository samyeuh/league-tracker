import sqlite3


class Database:
   def __init__(self):
         self.conn = sqlite3.connect('tracker.db')
         self.cursor = self.conn.cursor()
         self.cursor.execute(''' DROP TABLE IF EXISTS Server; ''')
         self.cursor.execute('''CREATE TABLE  Server(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  discordId VARCHAR(500) NOT NULL,
                  channelId VARCHAR(500) NOT NULL,
                  UNIQUE(discordId)
               );
            ''')
         self.conn.commit()
         # TODO: ajouter region et puuid
         self.cursor.execute('''DROP TABLE IF EXISTS Player;''')
         self.cursor.execute('''CREATE TABLE  Player(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  discordId VARCHAR(500) NOT NULL,
                  region VARCHAR(50) NOT NULL,
                  summonerName VARCHAR(500) NOT NULL,
                  summonerId VARCHAR(500) NOT NULL,
                  UNIQUE(discordId),
                  UNIQUE(summonerId)
               );
            ''')
         self.conn.commit()
         self.cursor.execute('''DROP TABLE IF EXISTS StinksOn;''')
         self.cursor.execute('''CREATE TABLE StinksOn(
                  serverId INT,
                  playerId INT,
                  PRIMARY KEY(serverId, playerId),
                  FOREIGN KEY(serverId) REFERENCES Server(id),
                  FOREIGN KEY(playerId) REFERENCES Player(id)
               );
         ''')
         self.conn.commit()
         from database.server import Server
         from database.stinkson import StinksOn
         from database.player import Player
         self.server = Server(self)
         self.stinkson = StinksOn(self)
         self.player = Player(self)

   def getConn(self):
      return self.conn
   
   def getCursor(self):
      return self.cursor
   
   def getServer(self):
      return self.server
   
   def getStinksOn(self):
      return self.stinkson
    
   def getPlayer(self):
        return self.player