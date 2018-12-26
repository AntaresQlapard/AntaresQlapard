import discord
from discord.ext.commands import bot
from discord.ext import commands
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "?")
@client.event
async def on_ready():p
    print("Thankyou For Using Video Bot")
    await client.change_presence(game=discord.Game(name="prefix ?"))
	
	
