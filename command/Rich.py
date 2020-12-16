from datetime import datetime

import discord

from model.User import User
from util.Util import try_send


class Rich:
    def __init__(self, client, logging, session):
        self.client = client
        self.logging = logging
        self.session = session
        pass

    async def do_response(self, message, args):
        results = self.session.query(User).order_by(User.jahyadi_coin.desc()).limit(10)
        richest10 = "Para penghasil kapital ekonomi:\n"
        i = 1
        for row in results:
            try:
                userDiscord = await self.client.fetch_user(row.user_id)
                richest10 = richest10 + ("{}. {} - {}\n".format(i, userDiscord, row.jahyadi_coin))
                i = i+1
            except discord.errors.NotFound:
                pass

        await try_send(message.channel, richest10)