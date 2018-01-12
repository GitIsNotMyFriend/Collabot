from discord.ext import commands
import discord

description = """
Collabot - Collaboration management suited for discord
"""


class Collabot(commands.Bot):

    def __init__(self, prefix):
        """
        Create Collabot instance
        """

        super().__init__(command_prefix=prefix, description=description)





