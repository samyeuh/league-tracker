
class Server:
    def __init__(self, database):
        self.cursor = database.getCursor()
        self.conn = database.getConn()
    
    def add_server(self, discord_id, channel_id):
        """
        Add a server to the database.

        :param discord_id: The discord id of server.
        :param discord_id: The discord id of channel.
        """
        try:
            self.cursor.execute(f"INSERT INTO Server (discordId, channelId) VALUES (?, ?)", (discord_id, channel_id))
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_server(self, discord_id):
        """
        Get a server from the database.

        :param discord_id: The discord id of server.
        """
        self.cursor.execute(f"SELECT * FROM Server WHERE (discordId) = (?)", (discord_id,))
        return self.cursor.fetchone()

    def remove_server(self, discord_id):
        """
        Remove a server from the database.

        :param discord_id: The discord id of server.
        """
        discord_id = [discord_id]
        self.cursor.execute(f"DELETE FROM Server WHERE (discordId) = (?)", (discord_id))
        self.conn.commit()
    
    def remove_server_byid(self, id):
        """
        Remove a server from the database.

        :param id: The id of the server.
        """
        self.cursor.execute(f"DELETE FROM Server WHERE (id) = (?)", (id,))
        self.conn.commit()
        