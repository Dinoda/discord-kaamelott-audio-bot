import os
import random
from Sound import Sound

class Soundboard():
    def __init__(self, path):
        self.path = path
        self.board = [Sound(self.path, f) for f in os.listdir(self.path)]
        self.size = len(self.board)

    def random(self):
        f = self.board[random.randrange(self.size)]
        return f.get_playable_audio()
