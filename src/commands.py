import discord
from tracker import Tracker
from database.database import Database
from discord import app_commands, Interaction, TextChannel
from discord.ext import commands



class LeagueCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tracker = Tracker()
        self.database = Database()
    
    """
    COMMANDES POUR ADMINISTRATEURS
    """
    
    async def is_admin(interaction: Interaction):
        """Check if user has admin permissions"""
        return interaction.author.guild_permissions.administrator
    
    @app_commands.command(name="setup", description="Initialise un channel spécial pour le serveur")
    @app_commands.check(is_admin)
    async def setup(self, interaction: discord.Interaction, channel: TextChannel):
        """Initialise le bot pour le serveur"""
        self.tracker.setup(channel)
        await interaction.response.send_message(f'Initialising bot in {channel.name}')

    """
    COMMANDES POUR UTILISATEURS
    """

    @app_commands.command(name="ping", description="Pong!")
    async def ping(self, interaction: Interaction):
        """ pong!!!! """
        await interaction.response.send_message('Pong!')

    # @commands.command()
    # async def help(self, ctx):
    #     """Affiche la liste des commandes disponibles"""
    #     # TODO: Implement this

    @app_commands.command(name="link", description="Lié ton compte discord à ton compte League of legends")
    async def link(self, interaction: Interaction, region: str, account: str):
        """Lié ton compte discord à ton compte League of legends"""
        # TODO: Implement this
        await interaction.response.send_message(f'Linking {interaction.author.id} to {account} on {region}', ephemeral=True)

    @app_commands.command(name="unlink", description="Délié ton compte discord de ton compte League of legends")
    async def unlink(self, interaction: Interaction):
        """Délié ton compte discord de ton compte League of legends"""
        # TODO: Implement this
        await interaction.response.send_message(f'Unlinking {interaction.author.name}', ephemeral=True)

    @app_commands.command(name="profil", description="Affiche un resumé de ton profil league of legends")
    async def profil(self, interaction: Interaction):
        """Affiche un resumé de ton profil league of legends"""
        # TODO: Implement this
        await interaction.response.send_message(f'Profil de {interaction.author.name}')

    @app_commands.command(name="last", description="Affiche les cinq dernières parties")
    @app_commands.choices(
        type=[
            app_commands.Choice(name="rankeds", value="rankeds"),
            app_commands.Choice(name="drafts", value="drafts"),
            app_commands.Choice(name="arams", value="arams"),
            app_commands.Choice(name="all", value="all"),
        ]
    )
    async def last(self, interaction: Interaction, type: app_commands.Choice[str]):
        """Affiche les dernières parties classées"""
        # TODO: Implement this
        await interaction.response.send_message(f'Last {type.name} games')



async def setup(bot):
    await bot.add_cog(LeagueCommands(bot))