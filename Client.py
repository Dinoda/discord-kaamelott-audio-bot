import discord
from errors.NotInChannelAuthor import NotInChannelAuthorException

class Client(discord.Client):
    def addCommand(self, command):
        if not hasattr(self, "commands"):
            self.commands = []
        self.commands.append(command)
        self.commandNb = len(self.commands)

    def getSoundboard(self):
        return self.board

    def setSoundboard(self, soundboard):
        self.board = soundboard

    def setIds(self, client_id, owner_id):
        self.client_id = client_id
        self.owner_id = owner_id

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Ignore your own messages
        if message.author.id == self.client_id:
            return
        cmd = None
        channel = None

        if isinstance(message.channel, discord.channel.DMChannel):
            cmd = message.content
            channel = self.get_voice_channel(message.author)
        elif message.content[0] == "!":
            cmd = message.content[1:]
            channel = message.author.voice.channel if message.author.voice else None

        if cmd:
            print(f'Command from {message.author}: {cmd}')
            cmd = cmd.split(' ')
            c = self.get_command(cmd[0])

            if c == None:
                raise UnknownCommandException(cmd)
            try:
                await c.call(self, cmd, channel, message)
            except NotInChannelAuthorException:
                await message.author.send("You must be in a channel to call this command")

    '''
    
    '''
    def get_command(self, cmd):
        for i in range(self.commandNb):
            if self.commands[i].is_call(cmd):
                return self.commands[i]

        return None

    def get_voice_channel(self, user):
        for c in self.get_all_channels():
            if isinstance(c, discord.channel.VoiceChannel):
                for m in c.members:
                    if m.id == user.id:
                        return c
        return None

    def is_owner(self, user):
        return user.id == self.owner

    def is_self(self, user):
        return user.id == self.client

    async def voice_channel_connect(self, channel):
        await channel.connect()

    async def voice_channel_play(self, channel, audio):
        for vc in self.voice_clients:
            if vc.channel == channel:
                vc.play(audio)

    async def voice_channel_disconnect(self, channel):
        for vc in self.voice_clients:
            if vc.channel == channel:
                await vc.disconnect()

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
