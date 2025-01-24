import discord
from tracker import Tracker
from discord.ext import commands
from database.database import Database
import asyncio

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(intents=intents, command_prefix='#')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
async def load_extension():
    await bot.load_extension("commands")

if __name__ == "__main__":
    asyncio.run(load_extension())
    bot.run('caca')
