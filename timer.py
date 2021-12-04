import discord
from discord import client
from discord.ext import commands
from discord_slash import SlashCommand
from discord.ext import commands, tasks
import discord_slash.cog_ext as cog_ext
from discord_slash.utils.manage_commands import create_option

class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.say_hi.start()

    @tasks.loop(seconds=60)
    async def say_hi(self):
        channel = self.bot.get_channel(916487777091219456)
        await channel.send("Hello World!")