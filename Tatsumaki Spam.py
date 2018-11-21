import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "#") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "keke or fish dragon?":
        await client.send_message(message.channel, "undefined") #responds with Cookie emoji when someone says "cookie"

@client.event
async def on_message(message):
    if 'poll' in message.content:
        #emoji = get(client.get_all_emojis(), name='<U0001f36a>')
        await client.add_reaction(message,  u"\U0001F36A")
        
client.run("NDkyOTMxNDkwNjIwMTEyODk3.DtZ9YA.BB8K8MesZ730YOSfu8cBvmzum74")

