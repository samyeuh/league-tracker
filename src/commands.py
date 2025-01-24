from discord.ext import commands
import discord
from database.database import Database
from tracker import Tracker


class LeagueCommands(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        self.tracker = Tracker()
        self.database = Database()
    
    """
    COMMANDES POUR ADMINISTRATEURS
    """

    @commands.command()
    async def setup(self, ctx, channel: discord.TextChannel):
        """Initialise le bot pour le serveur"""
        self.tracker.setup(channel)
        await ctx.send(f'Initialising bot in {channel.name}')

    """
    COMMANDES POUR UTILISATEURS
    """

    @commands.command()
    async def ping(ctx):
        """ pong!!!! """
        await ctx.send('Pong!')

    @commands.command()
    async def help(ctx):
        """Affiche la liste des commandes disponibles"""
        # TODO: Implement this

    @commands.command()
    async def link(ctx, region: str, account: str):
        """Lié ton compte discord à ton compte League of legends"""
        # TODO: Implement this
        await ctx.send(f'Linking {ctx.author.id} to {account} on {region}', ephemeral=True)

    @commands.command()
    async def unlink(ctx):
        """Délié ton compte discord de ton compte League of legends"""
        # TODO: Implement this
        await ctx.send(f'Unlinking {ctx.author.name}')

    @commands.command()
    async def profil(ctx):
        """Affiche un resumé de ton profil league of legends"""
        # TODO: Implement this
        await ctx.send(f'Profil de {ctx.author.name}')

    @commands.command()
    async def lastrankeds(ctx):
        """Affiche les dernières parties classées"""
        # TODO: Implement this
        await ctx.send(f'Last ranked games of {ctx.author.name}')

    @commands.command()
    async def lastgames(ctx):
        """Affiche les dernières parties"""
        # TODO: Implement this
        await ctx.send(f'Last games of {ctx.author.name}')

    @commands.command()
    async def lastnormals(ctx):
        """Affiche les dernières parties normales"""
        # TODO: Implement this
        await ctx.send(f'Last normal games of {ctx.author.name}')

async def setup(bot):
    await bot.add_cog(LeagueCommands(bot))
