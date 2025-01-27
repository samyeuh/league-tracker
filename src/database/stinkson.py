class StinksOn:
    def __init__(self, database):
        self.cursor = database.getCursor()
        self.conn = database.getConn()
        self.server = database.getServer()
        
    def add_stinkson(self, server_id, player_id):
        """
        Link a player to a server.

        :param server_id:
        """
        self.cursor.execute(f"INSERT INTO stinkson (serverId, playerId) VALUES (?, ?)", (server_id, player_id))
        self.conn.commit()

    def get_players(self, server_id):
        """
        Get all players linked to a server.

        :param server_id: The id of the server.
        """
        self.cursor.execute(f"SELECT * FROM stinkson WHERE (serverId) = (?)", (server_id, ))
        return self.cursor.fetchall()

    def get_servers(self, player_id):
        """
        Get all servers linked to a player.

        :param player_id: The id of the player.
        """
        self.cursor.execute(f"SELECT * FROM stinkson WHERE (playerId) = (?)", (player_id, ))
        return self.cursor.fetchall()

    def remove_stinkson(self, server_id, player_id):
        """
        Remove a player from a server.

        :param server_id: The id of the server.
        :param player_id: The id of the player.
        """

        self.cursor.execute(f"DELETE FROM stinkson WHERE serverId = ? AND playerId = ?", (server_id, player_id))
        self.conn.commit()

        if len(self.get_players(server_id)) == 0:
            self.server.remove_server_byid(server_id)
