from init import *

import sys

from commands.Join import JoinCommand
from commands.Random import RandomCommand
from commands.Leave import LeaveCommand

argc = len(sys.argv)

client = init_client(init_soundboard())

if argc > 1:
    args = sys.argv[1:]
    if args[0] == 'manifesto':
        client.get_soundboard()
    print(args)

client.add_command(JoinCommand("join", "j"))
client.add_command(RandomCommand("random", "r"))
client.add_command(LeaveCommand("leave", "l"))

run_client(client)

