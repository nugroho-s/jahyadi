import discord

from command.Command import Command
from util.Util import try_send

import numpy as np


class Stat(Command):
    def __init__(self):
        pass

    async def do_response(self, message, args):
        avg_ltcy = sum(Command.execution_durations) / len(Command.execution_durations)
        p95_ltcy = np.percentile(Command.execution_durations, 95)
        response = discord.Embed(title="Jahyadi is UP")
        response.add_field(name='Average Latency', value="{} ms".format(round(avg_ltcy, 2)), inline=True)
        response.add_field(name='P95 Latency', value="{} ms".format(round(p95_ltcy, 2)), inline=True)
        response.color = 0x00ff00
        await try_send(message.channel, embed=response)