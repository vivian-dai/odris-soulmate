import discord
from discord.ext import commands, tasks
from discord.utils import find
import os
'''
File name: main.py
Author: Vivian Dai
Description: main file to run to start Discord bot and do all the fun fun background tasks
License: MIT
Version: 1.0.0
Date created: 2021-05-22
Date last modified: 2021-05-22
Python Version: 3.6.0
Email: viviandai@protonmail.com
'''
#-------------------------CONSTANTS----------------------
TARGET_CHANNEL_NAME = "info-stalking"
#--------------------SOME BOT SET UP STUFF---------------
description = "odri's soulmate"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "-", description = description, intents = intents)

@client.event
async def on_ready():
    """[summary]
    """
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="and silently judging everyone"))
    scrape_info.start()
    print("bot is alive")

@tasks.loop(seconds=10)
async def scrape_info():
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name == TARGET_CHANNEL_NAME:
                async with channel.typing():
                    # TODO: make this send useful stuff like embeds of some stuff to stalk rather than a meaningless message
                    await channel.send("yes")

client.run(os.environ.get('TOKEN'))