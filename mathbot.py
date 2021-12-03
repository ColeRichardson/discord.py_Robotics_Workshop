import discord
from discord import client
from discord.ext import commands
from discord_slash import SlashCommand
from discord.ext import commands, tasks
import discord_slash.cog_ext as cog_ext
from discord_slash.utils.manage_commands import create_option

class Mathbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="math",
                       description="do some math in discord",
    options=[
        create_option(
            name="left_operand",
            description="a number we are going to use",
            option_type=int,
            required=True
        ),
        create_option(
            name="operation",
            description="the operation to perform, choose one of: +, -, *, div",
            option_type=str,
            required=True
        ),
         create_option(
             name="right_operand",
             description="a number we are going to use",
             option_type=int,
             required=True
         )
        ],
    guild_ids=[916113016712466462]
     )
    async def do_math(self, ctx, left_operand, right_operand, operation):
        await ctx.defer()
        if operation == "+":
            res = left_operand + right_operand
        elif operation == "-":
            res = left_operand - right_operand
        elif operation == "*":
            res = left_operand * right_operand
        elif operation == "/":
            res = left_operand / right_operand
        await ctx.send(str(res))

