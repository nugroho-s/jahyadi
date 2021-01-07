import discord
import re
import random

from command.Command import Command
from util.Util import try_send


class Intonasi(Command):
    def __init__(self, client, logging):
        self.client = client
        self.logging = logging

    async def do_response(self, message, args):
        i = random.randint(0, 100)
        user = message.author
        if len(args) > 2:
            user_id = args[2]
            user_id = re.findall("\d+", user_id)[0]
            try:
                user = await self.client.fetch_user(int(user_id))
            except discord.errors.NotFound:
                self.logging.error("User not found: {}".format(user_id))
                return

        await try_send(message.channel, embed=discord.Embed(title="Intonation rate machine",
                                                      description="{}'s intonation {}%".format(user.name, i),
                                                      color=0x00ff00))
        if i >= 80:
            await try_send(message.channel, '{} sudah datang dengan intonasi tinggi'.format(user.name))