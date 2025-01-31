import discord
from tracker import Tracker
from database.database import Database
from discord import app_commands, Interaction, TextChannel, ui, TextStyle, SelectOption
from discord.ext import commands
from utils.checker import checkLink
from utils.exceptions import LTException

class LinkModal(ui.Modal, title="link your account"):
    def __init__(self, tracker: Tracker):
        super().__init__()
        self.tracker = tracker
        self.region = ui.TextInput(
            label="Region",
            style=TextStyle.short,
            placeholder="example: euw, na, kr etc..",
            required=True,
            max_length=10,
        )
        self.add_item(self.region)
        self.name = ui.TextInput(label="Gamename", style=TextStyle.short, placeholder="in league#tracker, league is the gamename", required=True, max_length=16)
        self.add_item(self.name)
        self.tag = ui.TextInput(label="Tag", style=TextStyle.short, placeholder="in league#tracker, tracker is the tag", required=True, max_length=16)
        self.add_item(self.tag)

    async def on_submit(self, interaction: Interaction):
        self.region = self.region.value.upper()
        okEmbed = discord.Embed(title="Account linked", description=f"your account **{self.name}#{self.tag}** has been linked to region **{self.region}**", color=discord.Color.green())
        
        try:
            checkLink(self.region, self.name, self.tag)
            self.tracker.link(interaction.user, self.region, self.name, self.tag, interaction.guild.id)
            await interaction.response.send_message(embed=okEmbed)
        except LTException as e:
            await interaction.response.send_message(embed=e.getMessage(), ephemeral=True)
            return
        
        
    
class LeagueCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tracker = Tracker()
        self.database = Database()
    
    """
    COMMANDES POUR ADMINISTRATEURS
    """
    async def is_admin(interaction: discord.Interaction) -> bool:
        """Vérifie si l'utilisateur a les permissions administrateur."""
        if not interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="Permission Error", description="You must be an administrator to use this command.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return False
        return True

    @app_commands.command(name="setup", description="Sets a special channel for the server")
    @app_commands.check(is_admin)
    async def setup(self, interaction: discord.Interaction, channel: TextChannel):
        """Initialise le bot pour le serveur"""
        try:
            self.tracker.setup(channel, interaction.guild_id)
        except Exception as e:
            await interaction.response.send_message(f'Error during setup: {e}', ephemeral=True)
        else:
            await interaction.response.send_message(f'Initialising bot in {channel.name}')

    """
    COMMANDES POUR UTILISATEURS
    """

    @app_commands.command(name="ping", description="Pong!")
    async def ping(self, interaction: Interaction):
        """ pong!!!! """
        await interaction.response.send_message('Pong!', ephemeral=True)

    # @commands.command()
    # async def help(self, ctx):
    #     """Affiche la liste des commandes disponibles"""
    #     # TODO: Implement this

    @app_commands.command(name="link", description="Link your discord account to your League of legends account")
    async def link(self, interaction: Interaction):
        """Lié ton compte discord à ton compte League of legends"""
        # TODO: Implement this
        await interaction.response.send_modal(LinkModal(self.tracker))

    @app_commands.command(name="unlink", description="Unlink your discord account to your League of legends account")
    async def unlink(self, interaction: Interaction):
        """Délié ton compte discord de ton compte League of legends"""
        try:
            self.tracker.unlink(interaction.user, interaction.guild_id)
        except LTException as e:
            await interaction.response.send_message(embed=e.getMessage(), ephemeral=True)
        
        embed = discord.Embed(title="Account unlinked", description=f'Account linked to {interaction.guild.name} has been unlinked', color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="profil", description="Display a summary of your league of legends profile")
    async def profil(self, interaction: Interaction):
        """Affiche un resumé de ton profil league of legends"""
        # TODO: Implement this
        await interaction.response.send_message(f'Profil of {interaction.member.name}')

    @app_commands.command(name="last", description="Display the last five games played")
    @app_commands.choices(
        gametype=[
            app_commands.Choice(name="normal", value="type=normal&"),
            app_commands.Choice(name="all ranked", value="type=ranked&"),
            app_commands.Choice(name="ranked soloq" , value="queue=420&"),
            app_commands.Choice(name="ranked flex"  , value="queue=440&"),
            app_commands.Choice(name="arams", value="queue=450&"),
            app_commands.Choice(name="urf"  , value="queue=900&"),
            app_commands.Choice(name="all", value=""),
        ]
    )
    async def last(self, interaction: Interaction, count: int, gametype: app_commands.Choice[str]):
        """Affiche les dernières parties"""
        try:
            await interaction.response.defer()
            embedList = self.tracker.getLastMatchs(interaction.user, gametype, interaction.guild_id, count)
        except LTException as e:
            await interaction.followup.send(embed=e.getMessage(), ephemeral=True)
        if embedList is not None:
            await interaction.followup.send(embeds=embedList)
        else:
            noMatchEmbed = discord.Embed(title="No match found", description=f"No match found for type: **{gametype.name}**", color=discord.Color.red())
            await interaction.followup.send(embed=noMatchEmbed, ephemeral=True)



async def setup(bot):
    await bot.add_cog(LeagueCommands(bot))