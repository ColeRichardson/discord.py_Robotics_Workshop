#discord libraries
import discord
from discord import client
from discord.ext import commands
from discord_slash import SlashCommand
from discord.ext import commands, tasks
from discord_slash import SlashCommand

# python imports
import os
from dotenv import load_dotenv

#internal imports
from mathbot import Mathbot
from timer import Timer

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot("/")
slash = SlashCommand(client,sync_commands=True, sync_on_cog_reload=True)

@client.event
async def on_ready():
    print("discord bot is ready to go!")
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="UTM Robotics Discord Bot Tutorial",
    )
    await client.change_presence(activity=activity)

client.add_cog(Mathbot(client))
client.add_cog(Timer(client))
client.run(TOKEN)
