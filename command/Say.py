import json
import re

from discord.errors import NotFound
from discord.errors import Forbidden

from model.AllowedSay import AllowedSay
from util.Util import try_send


class Say:
    def __init__(self, client, logging, session):
        self.client = client
        self.logging = logging
        self.session = session

    async def do_response(self, message, args):
        if not Say.is_allowed_users(self.session, message.author.id):
            return

        if len(args) < 4:
            return

        channel_id = re.findall("\d+", args[2])[0]
        try:
            channel = await self.client.fetch_channel(int(channel_id))
        except NotFound:
            self.logging.error("Channel not found: {}".format(channel_id))
            return
        except Forbidden:
            return

        content = message.content[findnth(message.content, ' ', 2)+1:]
        self.logging.info('{} is saying to {}: {}'.format(
            message.author,
            channel.id,
            content
        ))
        await try_send(channel, content)

    @staticmethod
    def is_allowed_users(session, user_id):
        result_count = session.query(AllowedSay).filter(AllowedSay.user_id == user_id).count()
        return result_count == 1



def findnth(haystack, needle, n):
    parts = haystack.split(needle, n+1)
    if len(parts) <= n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)