from collections.abc import Sequence
from abc import abstractmethod

class Command():
    def __init__(self, name, aliases):
        self.name = name
        self.aliases = aliases if isinstance(aliases, Sequence) else [aliases]

    def is_call(self, command):
        if command == self.name or command in self.aliases:
            return True
        return False


    @abstractmethod
    def call(self, client, cmd, channel, message):
        """
        Implement the command reaction on call
        """
