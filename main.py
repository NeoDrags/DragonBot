from dotenv import load_dotenv
import discord
from discord.ext.commands import Bot
from discord.utils import get
import os
import asyncio
import random
import json

load_dotenv()

client = Bot(command_prefix ="$")
client.remove_command('help')

owner = os.getenv("OWNER")

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print("Connected to Discord as: " + client.user.name)

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Soaring High in Servers!"))
        await asyncio.sleep(6)
        await client.change_presence(activity=discord.Game(name= f"In {len(client.guilds)} servers"))
        await asyncio.sleep(6)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"Trying to be the Best Bot"))
        await asyncio.sleep(6)
        await client.change_presence(activity=discord.Game(name = "Being trained by My Master NeoDrags"))
        await asyncio.sleep(6)

@client.command()
async def ping(ctx):
    '''
    Gets the latency of the bot
    '''
    await ctx.send(':table_tennis: smashed at you with a ping of {} ms'.format(round(client.latency * 1000, 1)))

f = open('badword.json')
arr = json.load(f)

@client.command()
async def help(message):
    e = discord.Embed(
        color = discord.Colour.dark_purple()
    )
    e.set_author(name= "Help")
    e.add_field(name = "Commands that you can execute", value = """Here are the commands that you can type they are :
                        1) Type *$verify* to verify yourself But this only works if you have a Members role (no spelling mistakes)
                        2) Type *$help* to execute this command which will display the commands that you can execute
                        3) Type *$ping* to get the ping of the bot
                        4) Type *$toss* to perform a coin toss
                        5) Type *$add* to add two numbers
                        6) Type *$subtract* to subtract two numbers
                        7) Type *$multiply* to multiply two numbers
                        8) Type *$divide* to divide two numbers""" , inline = False)
    await message.channel.send(embed=e)

@client.command()
async def toss(message):
    e = discord.Embed(
        color = discord.Colour.dark_gold()
    )
    response = "Coin tossed"
    await message.channel.send(response)
    result = random.randint(0, 1)
    if(result == 0):
        e.set_author(name= "Heads")
        e.set_image(url = "https://lh3.googleusercontent.com/proxy/ND5Nq8ccVGoQy3Slk8i4NcVYG_pNbsZ4ZDvSyGlBDNPloXHo4yEGGETCX2kN0d8N2bWqbivZNpjdYBkaM0SPuE7Ln2evx2D7sG98LBO1n2IHtCVFlG7xmbym_9tDTYqKgX32zet7jurLO7Ei1XLXGtdhA0JFKuhdfBTNi-a-IA")
    else:
        e.set_author(name= "Tails")
        e.set_image(url = "https://www.pngjoy.com/pngm/146/2933990_quarter-tails-on-a-coin-transparent-png.png")
    await message.channel.send(embed = e)


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
    if(str(ctx.author.id) == str(owner)):
        await ctx.message.delete()
        await ctx.send(f"{text}")

@client.command()
async def add(ctx, num1:int, num2:int):
    await ctx.send(f"Sum is: {num1 + num2}")

@client.command()
async def subtract(ctx, num1:int, num2:int):
    await ctx.send(f"Difference is: {num1 - num2}")

@client.command()
async def multiply(ctx, num1:int, num2:int):
    await ctx.send(f"Product is: {num1 * num2}")

@client.command()
async def divide(ctx, num1:int, num2:int):
    await ctx.send(f"Result is: {num1 / num2}")

print("Running the bot...")
try:
    client.run(os.getenv("TOKEN"))
except Exception as e:
    print("An error occured: " + str(e))