import os
import random

class Soundboard():
    def __init__(self, path):
        self.path = path
        self.board = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        self.size = len(self.board)

    def random(self):
        f = self.board[random.randrange(self.size)]
        return os.path.join(self.path, f)
