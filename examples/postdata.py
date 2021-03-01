import boticordpy
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
boticord = boticordpy.BoticordClient(bot, token="your-boticord-token")

@bot.event
async def on_connect():
    stats = {"servers": 15000, "shards": 5, "users": 500000}
    await boticord.postStats(stats)


bot.run("your-bot-token")