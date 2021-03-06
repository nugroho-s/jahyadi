import math
import random
import re
from datetime import datetime

import discord
import sqlalchemy

from command.economy.EconomyBase import EconomyBase
from model.User import User
from util.Util import try_send

MIN_COIN = 100


class Steal(EconomyBase):
    def __init__(self, client, logging, session):
        super().__init__(session)
        self.client = client
        self.logging = logging

    async def do_response(self, message, args):
        await super().do_response(message, args)
        user = self.session.query(User).filter(User.user_id == message.author.id).one()

        if await super().is_cooldown(user.last_steal, 60, message.channel):
            return

        if len(args) > 2:
            user_id = args[2]
            user_id = re.findall("\d+", user_id)[0]
            try:
                targetDc = await self.client.fetch_user(int(user_id))
            except discord.errors.NotFound:
                self.logging.error("User not found: {}".format(user_id))
                return
        try:
            target = self.session.query(User).filter(User.user_id == user_id).one()
        except sqlalchemy.orm.exc.NoResultFound:
            self.logging.error(user_id)
            await try_send(message.channel, "targetmu miskin jahyadi coin")

        if user.jahyadi_coin < MIN_COIN:
            await try_send(message.channel, "kau miskin jahyadi coin, kau perlu {}".format(MIN_COIN))
            return

        if target.jahyadi_coin < MIN_COIN:
            await try_send(message.channel, "{} miskin jahyadi coin".format(targetDc.name))
            return

        user.jahyadi_coin = user.jahyadi_coin - MIN_COIN
        user.last_steal = datetime.now()

        random_steal = random.random()
        if random_steal <= .35:
            # success
            payout = 0
            if random_steal < .05:
                payout = random.uniform(.5, .6) * target.jahyadi_coin
            elif random_steal <= .1:
                payout = random.uniform(.25, .5) * target.jahyadi_coin
            else:
                payout = random.uniform(.1, .25) * target.jahyadi_coin

            payout = math.floor(payout)
            target.jahyadi_coin = target.jahyadi_coin - payout
            user.jahyadi_coin = user.jahyadi_coin + MIN_COIN + payout
        else:
            # fail
            target.jahyadi_coin = target.jahyadi_coin + MIN_COIN

        self.session.commit()
        await try_send(message.channel, "Pencurian {} jahyadi coinmu sekarang {} dan jahyadi coin {} sekarang {}".format(
            "sukses" if random_steal <= .35 else "gagal",
            user.jahyadi_coin,
            targetDc.name,
            target.jahyadi_coin
        ))
