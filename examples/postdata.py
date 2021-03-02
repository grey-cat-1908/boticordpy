from boticordpy import BoticordClient
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
boticord = BoticordClient(bot, token="your-boticord-token")

@bot.event
async def on_connect():
    stats = {"servers": 729, "shards": 1, "users": 160895}
    await boticord.postStats(stats)


bot.run("your-bot-token")