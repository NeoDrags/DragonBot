from dotenv import load_dotenv
import discord
from discord.ext.commands import Bot
from discord.utils import get
import os
import asyncio
import random
import json

load_dotenv()

client = Bot(command_prefix ="$", case_insensitive = True)
client.remove_command('help')

owner = os.getenv("OWNER")

with open("servers.json") as f:
    serversAndMembers = json.load(f)

print(serversAndMembers)

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

@client.command()
async def help(message, arg=None):
    if(arg == "mod"):
        e = discord.Embed(
            color = discord.Color.random(),
            title = "Mod Commands"
        )
        e.set_thumbnail(url="https://images-ext-2.discordapp.net/external/ToRp80b4LrArOZXM4tA6UMMpgfS1PZMQer5TehaRAi4/%3Fid%3DOIP.NJm0nFz7IBTZk2YQ2wJE9QHaHD%26pid%3DApi%26P%3D0%26w%3D164%26h%3D157/https/tse2.mm.bing.net/th")
        e.add_field(name="**Moderation**", value="""
        `$verify` for verification""")
        await message.channel.send(embed=e)
    else:
        e = discord.Embed(
            color = discord.Color.random(),
            title = "Welcome to my cave. I was once a Dragon..."
        )
        e.set_thumbnail(url= "https://image.freepik.com/free-vector/blue-robot-dragon-sticker_85893-72.jpg")
        e.add_field(name = "**Here is what you can do**", value = """
                            *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   * 
                            **:tools:  Moderation**
                                `$help mod`
                           
                            **:fireworks:  fun**
                                `$help fun`

                            **:heavy_plus_sign: maths**
                                `$help

                            """ , inline = False)
        e.set_author(name=f"Requested by {message.author.name}", icon_url=message.author.avatar_url)
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
async def setVerifyRole(message, arg):
    if(str(message.guild.name) in serversAndMembers):
        if(str(arg) in serversAndMembers.values()):
            message.channel.send("Error this is already present in the server")
        else:
            serversAndMembers[str(message.guild.name)] = str(arg)
    else:
            serversAndMembers[str(message.guild.name)] = str(arg)

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