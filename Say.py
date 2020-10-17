import re

from discord.errors import NotFound


class Say:
    def __init__(self, client, logging):
        self.client = client
        self.logging = logging

    async def do_response(self, message, args):
        self.logging.info(message.content)
        channel = message.channel
        if len(args) > 2:
            channel_id = re.findall("\d+", args[2])[0]
            try:
                channel = await self.client.fetch_channel(int(channel_id))
            except NotFound:
                self.logging.error("User not found: {}".format(channel_id))
                return

        await channel.send(message.content)