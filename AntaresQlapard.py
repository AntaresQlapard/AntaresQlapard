import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.bot)
	print(bot.user.id)
	print('------')
	
@bot.command()
async def hi():
	await bot.say('Hello There!')
bot.run('NTI3MTIzMDgyMzgxMzYxMTUy.DwUCwQ.YbzGHKH3U9XalfLAvChxih7rkLo')
