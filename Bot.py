from discord.ext import commands
import discord
from DBHandler import Database
from Utils.GitEmbed import GitEmbed

description = """
Collabot - Collaboration management suited for discord
"""


class Collabot(commands.Bot):

    def __init__(self, prefix):
        """
        Create Collabot instance
        """

        # super commands.Bot constructor
        super().__init__(command_prefix=prefix, description=description)
        self.prefix = prefix
        # Make sure the database has a projects table
        with Database() as db:
            db.check_table()

    async def on_message(self, message: discord.Message):
        channel = message.channel

        if message.author.bot:
            return

        if message.content.startswith(self.prefix):
            await self.send_message(channel, "TODO: handle command")
