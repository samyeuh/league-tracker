import discord

class LTException(Exception):
   
    def __init__(self, title, message):
        self.embed = discord.Embed(title=title, description=message, color=discord.Color.red())
    
    def getMessage(self):
        return self.embed
    
    pass
