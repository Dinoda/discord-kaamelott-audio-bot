from dotenv import load_dotenv
import os
import discord
import random

load_dotenv()

self_id = int(os.getenv("self_id"))
owner_id = int(os.getenv("owner_id"))
token = os.getenv("token")
soundspath = os.getenv("sounds")

class Soundboard():
    def __init__(self):
        self.board = [f for f in os.listdir(soundspath) if os.path.isfile(os.path.join(soundspath, f))]
        self.size = len(self.board)
    
    def random(self):
        f = self.board[random.randrange(self.size)]
        return os.path.join(soundspath, f)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.chans = self.get_all_channels()
        
#        for g in self.guilds:
#            print("Server: " + g.name)
#            for c in g.channels:
#                print("\tChannel: " + c.name)
#                if isinstance(c, discord.VoiceChannel):
#                    for m in c.members:
#                        print("\t\tMember: " + m.name)


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author.id == self_id:
            print("I'm the author, ignore message")
        elif message.author.id == owner_id:
            print("User is OWNER")
            match message.content:
                case "join":
                    await self.message_join(message)
                case "leave":
                    await self.message_leave(message)
                case "random":
                    await self.message_random(message)
                case _:
                    await self.message_unknown(message)
        else:
            print("User isn't owner")
            match message.content:
                case "random":
                    await self.message_random(message)
                case _:
                    await self.message_unknown(message)

    async def message_join(self, message):
        c = await self.find_member_in_channel(message.author.name)
        if c != None:
            await c.connect()

    async def message_leave(self, message):
        await self.voice_clients[0].disconnect()

    async def message_random(self, message):
        audio = discord.FFmpegPCMAudio(soundboard.random())
        self.voice_clients[0].play(audio)
    
    async def message_unknown(self, message):
        await message.author.send(content="This command is unknown")

    '''
        Returns the channel where is the given member, or None
    '''
    async def find_member_in_channel(self, name):
        for g in self.guilds:
            for c in g.channels:
                if isinstance(c, discord.VoiceChannel):
                    for m in c.members:
                        if m.name == name:
                            return c
        return None

soundboard = Soundboard()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

