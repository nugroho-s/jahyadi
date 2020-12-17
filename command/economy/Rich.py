from datetime import datetime

import discord

from command.economy.EconomyBase import EconomyBase
from model.User import User
from util.Util import try_send


class Rich(EconomyBase):
    def __init__(self, client, logging, session):
        super().__init__(session)
        self.client = client
        self.logging = logging

    async def do_response(self, message, args):
        results = self.session.query(User).order_by(User.jahyadi_coin.desc()).limit(10)
        richest10 = "Para penghasil kapital ekonomi:\n"
        i = 1
        for row in results:
            try:
                user_discord = await self.client.fetch_user(row.user_id)
                richest10 = richest10 + ("{}. {} - {}\n".format(i, user_discord, row.jahyadi_coin))
                i = i+1
            except discord.errors.NotFound:
                pass

        await try_send(message.channel, richest10)