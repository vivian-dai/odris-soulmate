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
TARGET_CHANNEL_NAME = ["info-stalking"]
RGB_COLOURS = {"YouTube": (255, 0, 0)}
#--------------------SOME BOT SET UP STUFF---------------
description = "odri's soulmate"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "-", description = description, intents = intents)

@client.event
async def on_ready():
    """code to fire up when bot is online

    changes the Discord status
    starts scraping info
    prints "bot is alive" to show the bot has successfully entered the world of onlineness
    """
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="and silently judging everyone"))
    scrape_info.start()
    print("bot is alive")

def generate_embed(stalk_source, post_title, stalk_link, image, author_name, author_pfp):
    """generates an embed

    Args:
        stalk_source (str): source the info came from (eg. YouTube, Twitter, Facebook, etc.)
        post_title (str): title of the post (or whatever is being stalked lol)
        stalk_link (str): URL for the original source
        image (str): URL for the image used in the post (or whatever is being stalked lol x2)
        author_name (str): name of creator of stalked content
        author_pfp (str): URL for profile picture of the author of stalked content

    Returns:
        discord.Embed: a hopefully nicely generated embed to send
    """
    embed = discord.Embed(
        title = post_title,
        description = f"{stalk_source}: [{stalk_link}]({stalk_link})",
        colour = discord.Color.from_rgb(RGB_COLOURS[stalk_source][0], RGB_COLOURS[stalk_source][1], RGB_COLOURS[stalk_source][2])
    )
    embed.add_image(url = image)
    embed.set_author(name = author_name, icon_url = author_pfp)
    return embed

@tasks.loop(seconds=10)
async def scrape_info():
    """scrapes info every 10 seconds

    looks into each guild the bot is in, then checks each channel of the guild 
    and if the channel name is a channel in the list TARGET_CHANNEL_NAME then 
    send a message to the channel
    """
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name in TARGET_CHANNEL_NAME:
                async with channel.typing():
                    # TODO: make this send useful stuff like embeds of some stuff to stalk rather than a meaningless message
                    await channel.send("yes")

client.run(os.environ.get('DISCORD_BOT_TOKEN'))