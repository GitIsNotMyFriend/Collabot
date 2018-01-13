from Bot import Collabot
import sys

client = Collabot('^')


@client.event
async def on_ready():
    print("Running {client.user} (ID: {client.user.id})")

TOKEN_PATH = 'token'

if len(sys.argv) > 1:
    TOKEN_PATH = sys.argv[1]

with open(TOKEN_PATH) as t:
    client.run(t.read().strip('\n'))
