
class Server:
    def __init__(self, database):
        self.cursor = database.getCursor()

    def add_server(self, discord_id):
        """
        Add a server to the database.

        :param discord_id: The discord id of server.
        """
        self.cursor.execute(f"INSERT INTO Serveur (discordId) VALUES ({discord_id})")

    def get_server(self, discord_id):
        """
        Get a server from the database.

        :param discord_id: The discord id of server.
        """
        self.cursor.execute(f"SELECT * FROM Serveur WHERE discordId = {discord_id}")
        return self.cursor.fetchone()

    def remove_server(self, discord_id):
        """
        Remove a server from the database.

        :param discord_id: The discord id of server.
        """
        self.cursor.execute(f"DELETE FROM Serveur WHERE discordId = {discord_id}")