import discord

'''
    Defines the commands and if they are limited to the owner.
'''
commands = {
    "join": True,
    "leave": True,
    "random": False,
        }

class Client(discord.Client):
    def setSoundboard(self, soundboard):
        self.board = soundboard

    def setIds(self, client_id, owner_id):
        self.client = client_id
        self.owner = owner_id

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if isinstance(message.channel, discord.channel.DMChannel):
            await self.command(message, message.content)
        elif message.content[0] == '/':
            await self.command(message, message.content[1:])

    async def command(self, message, command):
        if not self.is_self(message.author):
            if command in commands.keys():
                if not commands[command] or self.is_owner(message.author):
                    func = getattr(self, command)
                    await func(message, command)
        

    def is_owner(self, user):
        return user.id == self.owner

    def is_self(self, user):
        return user.id == self.client

    async def join(self, message, command):
        c = await self.find_member_in_channel(message.author.id)
        if c != None:
            await c.connect()

    async def leave(self, message, command):
        for vc in self.voice_clients:
            await vc.disconnect()

    async def random(self, message, command):
        audio = discord.FFmpegPCMAudio(self.board.random())
        self.voice_clients[0].play(audio)

    '''
        Returns the channel where is the given member, or None
    '''
    async def find_member_in_channel(self, id):
        for g in self.guilds:
            for c in g.channels:
                if isinstance(c, discord.VoiceChannel):
                    for m in c.members:
                        if m.id == id:
                            return c
        return None
