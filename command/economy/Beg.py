import math
from datetime import datetime

from command.economy.EconomyBase import EconomyBase
from model.User import User
from util.Util import try_send
import random


class Beg(EconomyBase):
    def __init__(self, logging, session):
        super().__init__(session)
        self.logging = logging
        pass

    async def do_response(self, message, args):
        await super().do_response(message, args)
        user = self.session.query(User).filter(User.user_id == message.author.id).one()

        if await super().is_cooldown(user.updated_time, 60, message.channel):
            return

        coin = math.ceil(max(random.gauss(25, 20), 0))
        user.jahyadi_coin = user.jahyadi_coin + coin
        user.updated_time = datetime.now()
        self.session.commit()
        await try_send(message.channel, 'kau dapat {} jahyadi coins'.format(coin))
