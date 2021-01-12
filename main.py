from dotenv import load_dotenv
import discord
from discord.ext.commands import Bot
from discord.utils import get
import os

load_dotenv()

client = Bot(command_prefix ="$")

@client.event
async def on_ready():
    game = discord.Game("Ready to roar!")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Connected to Discord as: " + client.user.name)

@client.command()
async def ping(ctx):
    await ctx.send(f":table_tennis: smashed at you wih a ping of {client.latency}")

@client.command()
async def verify(message):
    member = message.author
    role = discord.utils.get(message.guild.roles, name = "Members")
    await member.add_roles(role)
    await message.channel.send(f"{member.name} has been verified")

@client.command()
async def say(message, * , text):
    await message.channel.send(f"{text}")

print("Running the bot...")
try:
    client.run(os.getenv("TOKEN"))
except Exception as e:
    print("An error occured: " + str(e))