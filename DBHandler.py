import sqlite3
from os import path, mkdir

# Projects table: guild_id | project name | collaborators_ids | project_url | guild_id | likes/dislikes id##
DATABASE_DIR = path.join(path.dirname(__file__), 'database')


class Database(object):

    def __init__(self, db='collab.db'):
        self.path = path.join(DATABASE_DIR, db)

        if not path.exists(DATABASE_DIR):
            mkdir(DATABASE_DIR)

    def __enter__(self):
        """
        with statement magic method constructor
        :return: Database instance
        """
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        with statement magic method destructor
        """
        self.cursor.close()
        self.conn.close()

    def check_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS projects (guild_id INTEGER, project_name TEXT,
                                    collaborators INTEGER, project_url TEXT)""")


with Database() as f:
    f.check_table()