from Command import Command
from errors.NotInChannelAuthor import NotInChannelAuthorException
import discord

class RandomCommand(Command):
    async def call(self, client, cmd, channel, message):
        if not channel:
            raise NotInChannelAuthorException()

        sb = client.get_soundboard()
        await client.voice_channel_play(channel, sb.random())
