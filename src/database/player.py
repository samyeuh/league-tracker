class Player:
    def __init__(self, database):
        self.stinkson = database.getStinksOn()
        self.server = database.getServer()
        self.cursor = database.getCursor()
        self.conn = database.getConn()

    def add_player(self, discord_id, region, summoner_name, summoner_id, serverDiscordId):
        """
        Add a player on the database.

        :param discord_id: The discord id of the player.
        :param region: The region of the player.
        :param summoner_name: The summoner name of the player.
        :param summoner_id: The summoner id of the player.
        :param serverDiscordId: The guild id of the player.
        """

        self.cursor.execute(f"INSERT INTO players (discordId, region, summonerName, summonerId) VALUES (?, ?, ?, ?)", (discord_id, region, summoner_name, summoner_id))
        self.conn.commit()
        player = self.get_player(discord_id)
        if player is None:
            return Exception("Player not found")
        
        playerServer = self.server.get_server(serverDiscordId)
        if playerServer is None:
            self.server.add_server(serverDiscordId)
            playerServer = self.server.get_server(serverDiscordId)
        
        self.stinkson.add_stinkson(playerServer[0], player[0])

    def get_player(self, discord_id):
        """
        Get a player from the database.

        :param discord_id: The discord id of the player.
        """

        self.cursor.execute(f"SELECT * FROM players WHERE discord_id = ?", (discord_id))
        self.conn.commit()
        return self.cursor.fetchone()

    def remove_player(self, server_id, player_id):
        """
        Remove a player from the database.

        :param server_id: The discord id of the server.
        :param discord_id: The discord id of the player.
        """

        if self.get_player(player_id) is None:
            return Exception("Player not found")
        
        self.stinkson.remove_stinkson(server_id, player_id)

        if len(self.stinkson.get_servers(player_id)) == 0:
            self.cursor.execute(f"DELETE FROM players WHERE discord_id = ?", (player_id))
            self.conn.commit()
            return True
        else:
            return False


"""
def remove_player_fromName(summoner_name):
    
    Remove a player from the database.

    :param summoner_name: The summoner name of the player.
    

    cursor.execute(f"DELETE FROM players WHERE summoner_name = {summoner_name}")

def remove_player_fromRegion(region):
    
    Remove a player from the database.

    :param region: The region of the player.


    cursor.execute(f"DELETE FROM players WHERE region = {region}")
"""