from datetime import datetime

from model.User import User
from util.Util import try_send


class Rich:
    def __init__(self, client, logging, session):
        self.client = client
        self.logging = logging
        self.session = session
        pass

    async def do_response(self, message, args):
        results = self.session.query(User).filter(User.user_id == message.author.id).order_by(User.jahyadi_coin.desc()).limit(10)
        richest10 = "Para penghasil kapital ekonomi:\n"
        i = 1
        for row in results:
            userDiscord = await self.client.fetch_user(row.user_id)
            richest10 = richest10 + ("{}. {}".format(i, userDiscord))
            i = i+1

        await try_send(message.channel, richest10)