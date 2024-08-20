from Command import Command
from errors.NotInChannelAuthor import NotInChannelAuthorException

class JoinCommand(Command):
    async def call(self, client, cmd, channel, message):
        if not channel:
            raise NotInChannelAuthorException()
        await client.voice_channel_connect(channel)
