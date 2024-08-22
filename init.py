# General imports
from dotenv import load_dotenv
import os

import discord

# Local imports
from Soundboard import Soundboard
from Client import Client

# General initialisation
load_dotenv()

options = {
        "self_id": int(os.getenv("self_id")),
        "owner_id": int(os.getenv("owner_id")),
        "token": os.getenv("token"),
        "soundspath": os.getenv("sounds")
        }

def init_soundboard():
    return Soundboard(options["soundspath"])

def init_client(soundboard):
    intents = discord.Intents.default()
    intents.message_content = True

    client = Client(intents=intents)

    client.set_soundboard(soundboard)

    client.set_ids(options['self_id'], options['owner_id'])

    return client

def run_client(client):
    client.run(options['token'])
