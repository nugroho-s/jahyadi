import re
from datetime import datetime

import discord

from command.economy.EconomyBase import EconomyBase
from model.User import User
from util.Util import try_send
import random


class Balance(EconomyBase):
    def __init__(self, client, logging, session):
        super().__init__(session)
        self.client = client
        self.logging = logging

    async def do_response(self, message, args):
        await super().do_response(message, args)
        user_id = message.author.id
        if len(args) > 2:
            user_id = args[2]
            user_id = re.findall("\d+", user_id)[0]
            try:
                user = await self.client.fetch_user(int(user_id))
            except discord.errors.NotFound:
                self.logging.error("User not found: {}".format(user_id))
                return
        user = self.session.query(User).filter(User.user_id == user_id).one()
        user_discord = await self.client.fetch_user(user.user_id)
        await try_send(message.channel, 'jahyadi coin {} {}'.format(user_discord.name, user.jahyadi_coin))
