from discord import Embed, Color, Client, errors
from DBHandler import Database


class GitEmbed(object):
    """
    Git Embed class
    """
    def __init__(self, project_name: str, guild_id: int):
        """
        GitEmbed instance constructor
        :param project_name: Project name
        :param guild_id: Guild id
        """

        super().__init__()

        # Embed fields
        self.message = None
        self.embed = None
        self.color = Color(int("0x482574", 16))  # Purple hex color
        self.thumbnail = None

        # Project fields
        self.owner = None
        self.collaborators = []
        self.url = None
        self.name = project_name
        self.guild = guild_id

    def generate_embed(self):
        """
        Generates an embed object
        :return: Embed object
        """
        if not self.owner:
            return "Can't find project {0} in this guild".format(self.name)

        embed = Embed(title="Repository link", url=self.url, thumbnail=self.thumbnail, color=self.color)
        embed.set_author(name=self.name)
        embed.add_field(name="Owner:", value="{0}".format(self.owner), inline=True)
        embed.set_footer(text="Collaborators: {0}".format(" ".join(self.collaborators)))

        return embed

    async def fetch_data(self, client):
        """
        Fetches data from database
        """
        data = None

        with Database() as db:
            query = "SELECT * FROM projects WHERE project_name='{0}' AND guild_id='{1}'".format(self.name, self.guild)
            res = db.conn.execute(query)
            data = res.fetchone()

        if data is None:
            raise FetchException("Can't find such project")

        self.guild, self.name, owner, collaborators, self.url = data

        try:
            user_info = await Client.get_user_info(client, user_id=owner)
            print(user_info.avatar_url)
            self.thumbnail = user_info.avatar
            self.owner = user_info.name

        except errors.NotFound:
            self.thumbnail = "https://i.imgur.com/0loMzLZ.png"
            self.owner = "Unknown"

        for collaborator in collaborators.split(','):
            try:
                user_info = await Client.get_user_info(client, user_id=collaborator)
                self.collaborators.append(user_info)
            except errors.NotFound:
                self.collaborators.append("Unknown")


class FetchException(Exception):
    def __init__(self, *args):
        super().__init__(args)


