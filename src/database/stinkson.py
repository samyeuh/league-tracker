class StinksOn:
    def __init__(self, database):
        self.cursor = database.getCursor()
        self.conn = database.getConn()
        
    def add_stinkson(self, server_id, player_id):
        """
        Link a player to a server.

        :param server_id:
        """
        self.cursor.execute(f"INSERT INTO stinkson (server_id, player_id) VALUES (?, ?)", (server_id, player_id))
        self.conn.commit()

    def get_players(self, server_id):
        """
        Get all players linked to a server.

        :param server_id: The id of the server.
        """
        self.cursor.execute(f"SELECT * FROM stinkson WHERE server_id = ?", (server_id))
        self.conn.commit()
        return self.cursor.fetchall()

    def get_servers(self, player_id):
        """
        Get all servers linked to a player.

        :param player_id: The id of the player.
        """
        self.cursor.execute(f"SELECT * FROM stinkson WHERE player_id = ?", (player_id))
        self.conn.commit()
        return self.cursor.fetchall()

    def remove_stinkson(self, server_id, player_id):
        """
        Remove a player from a server.

        :param server_id: The id of the server.
        :param player_id: The id of the player.
        """

        self.cursor.execute(f"DELETE FROM stinkson WHERE server_id = ? AND player_id = ?", (server_id, player_id))
        self.conn.commit()