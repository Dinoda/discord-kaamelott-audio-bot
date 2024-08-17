from dotenv import load_dotenv
from Soundboard import Soundboard
from Client import Client
import os
import discord

load_dotenv()

self_id = int(os.getenv("self_id"))
owner_id = int(os.getenv("owner_id"))
token = os.getenv("token")
soundspath = os.getenv("sounds")

soundboard = Soundboard(soundspath)

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

client.setSoundboard(soundboard)
client.setIds(self_id, owner_id)
client.run(token)

