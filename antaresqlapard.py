import discord
from discord.ext.commands import bot
from discord.ext import commands
import async
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "?")
@client.event
async def on_ready():
    print("Thankyou For Using Disocrd Bot")
    await client.change_presence(game=discord.Game(name="Discord Bot"))

@client.event
async def on_messsage(message):
    if message.content.startswith("?hi"):
        msg = 'Hello (0.author.mention) How are you?'.format(message)
        await client.send_message(message.channel)
	
client.run(rafsanrahman)

	
	
