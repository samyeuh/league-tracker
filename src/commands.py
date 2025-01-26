import discord
from tracker import Tracker
from database.database import Database
from discord import app_commands, Interaction, TextChannel, ui, TextStyle, SelectOption
from discord.ext import commands
from utils.checker import checkLink

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
        errorEmbed = discord.Embed(title="Account not linked", description=f"Informations given (**{self.name}#{self.tag}** in region **{self.region}**) are incorrect, please check it and retry.", color=discord.Color.red())
        okEmbed = discord.Embed(title="Account linked", description=f"your account **{self.name}#{self.tag}** has been linked to region **{self.region}**", color=discord.Color.green())

        if not checkLink(self.region, self.name, self.tag):
            errorEmbed.description += " Erreur lors du checklink"
            embed = errorEmbed
            await interaction.response.send_message(embed=embed)
            return
        if not interaction.guild:
            raise ValueError("Guild ID is missing")
        
        try:
            self.tracker.link(interaction.user, self.region, self.name, self.tag, interaction.guild.id)
            embed = okEmbed
        except Exception as e:
            print(e)
            errorEmbed.description += " Erreur lors du link + " + str(e)
            embed = errorEmbed
        
        await interaction.response.send_message(embed=embed)
    
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
        return interaction.user.guild_permissions.administrator

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
        # TODO: Implement this
        await interaction.response.send_message(f'Unlinking {interaction.member.name}', ephemeral=True)

    @app_commands.command(name="profil", description="Display a summary of your league of legends profile")
    async def profil(self, interaction: Interaction):
        """Affiche un resumé de ton profil league of legends"""
        # TODO: Implement this
        await interaction.response.send_message(f'Profil of {interaction.member.name}')

    @app_commands.command(name="last", description="Display the last five games played")
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