from dotenv import load_dotenv
import discord
from discord.ext.commands import Bot
from discord.utils import get
import os
import json

load_dotenv()

client = Bot(command_prefix ="$")

@client.event
async def on_ready():
    game = discord.Game("Ready to roar!")
    await client.change_presence(status=discord.Status.dnd, activity=game)
    print("Connected to Discord as: " + client.user.name)

@client.command()
async def ping(ctx):
    '''
    Gets the latency of the bot
    '''
    await ctx.send(f":table_tennis: smashed at you wih a ping of {client.latency} ms")

f = open('badword.json')
arr = json.load(f)

@client.event
async def onSwear(ctx):
    for i in arr['BadWords']:
        if i in ctx.message.content:
            await ctx.message.delete()
            await ctx.send(f"**{ctx.message.author} has been warned he has sworn**")

@client.command()
async def verify(message):
    '''
    Verifies you NOTE: This only works if you have a role name called Members with no aliteration in spelling or name
    '''
    member = message.author
    role = discord.utils.get(message.guild.roles, name = "Members")
    await member.add_roles(role)
    await message.channel.send(f"{member.name} has been verified")

@client.command()
async def say(ctx, * , text):
    '''
    Echos what you say
    '''
    await ctx.message.delete()
    await ctx.send(f"{text}")

print("Running the bot...")
try:
    client.run(os.getenv("TOKEN"))
except Exception as e:
    print("An error occured: " + str(e))