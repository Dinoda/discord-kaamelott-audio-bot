import os
import discord

class Sound():
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.fullpath = os.path.join(self.path, self.filename)
        
        if not os.path.isfile(self.fullpath):
            raise Exception(f'File "{self.fullpath}" not found')

    def get_playable_audio(self):
        return discord.FFmpegPCMAudio(self.fullpath)
