import discord
import asyncio
from discord.ext import commands
import logging

# Configurer le logger de Discord.py
logging.basicConfig(level=logging.INFO)  # Change `INFO` en `DEBUG` pour plus de détails
logger = logging.getLogger("discord")


intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='lt.')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        await bot.tree.sync()
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")
    
    
async def load_extension():
    await bot.load_extension("commands")

async def main():
    await load_extension()
    await bot.start('')
    
if __name__ == "__main__":
    asyncio.run(main())
    
