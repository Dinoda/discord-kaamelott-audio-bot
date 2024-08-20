from dotenv import load_dotenv
from Soundboard import Soundboard
from Client import Client

import os
import discord

from commands.Join import JoinCommand
from commands.Random import RandomCommand
from commands.Leave import LeaveCommand

# Load the environment variables
load_dotenv()

self_id = int(os.getenv("self_id"))
owner_id = int(os.getenv("owner_id"))
token = os.getenv("token")
soundspath = os.getenv("sounds")

# Load the soundboards
soundboard = Soundboard(soundspath)

# Initialise a basic client
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

# Set client data
client.setSoundboard(soundboard)
client.setIds(self_id, owner_id)

# Set client commands
client.addCommand(JoinCommand("join", "j"))
client.addCommand(RandomCommand("random", "r"))
client.addCommand(LeaveCommand("leave", "l"))

# Run client
client.run(token)

