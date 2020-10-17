import json
import re

from discord.errors import NotFound


class Say:
    def __init__(self, client, logging):
        self.client = client
        self.logging = logging
        with open('config/allowed_say.json') as json_file:
            self.allowed_users = {k: v for v, k in enumerate(json.load(json_file))}

    async def do_response(self, message, args):
        if message.author.id not in self.allowed_users:
            self.logging.info("{} is not allowed to say".format(message.author.id))
            return

        if len(args) < 4:
            return

        channel_id = re.findall("\d+", args[2])[0]
        try:
            channel = await self.client.fetch_channel(int(channel_id))
        except NotFound:
            self.logging.error("User not found: {}".format(channel_id))
            return

        await channel.send(message.content[findnth(message.content, ' ', 2):])


def findnth(haystack, needle, n):
    parts = haystack.split(needle, n+1)
    if len(parts) <= n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)