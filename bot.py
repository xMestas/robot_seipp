import util
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
	print("I'm ready!")

@bot.command(aliases=["fuckyouseipp", "seipp"])
async def fys(ctx):
    await ctx.send('Fuck you Seipp!')

bot.run(util.read_key("./keys/discord_api.key"))
