import discord
from utils.exceptions import LTException
"""
900 - Urf
450 - ARAM
440 - Flex
420 - SoloQ
400 - Normal
"""
def getQueueType(queueType):
    queueTypes = {
        "900": "URF",
        "450": "ARAM",
        "440": "Flex",
        "420": "SoloQ",
        "400": "Normal"
    }
    if queueTypes.get(str(queueType)) is None:
        raise LTException("Queue ID Error", "Queue ID not found")
    
    return queueTypes.get(str(queueType))

def matchEmbed(match):
    matchInfo = match['info']
    embed = discord.Embed(
        title=getQueueType(matchInfo['queueId']),
        description=f"Game duration: {matchInfo['gameDuration']}",
    )
    
    return embed
    