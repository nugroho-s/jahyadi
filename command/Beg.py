import json
from datetime import datetime

from model.User import User
from util.Util import try_send
import random

class Beg:
    def __init__(self, logging, session):
        self.logging = logging
        self.session = session
        pass

    async def do_response(self, message, args):
        count = self.session.query(User).filter(User.user_id == message.author.id).count()
        if count == 0:
            self.session.add(User(message.author.id, 0, datetime.now()))
            self.session.commit()
        user = self.session.query(User).filter(User.user_id == message.author.id).one()
        if count > 0:
            self.logging.info("delay {}".format((datetime.now() - user.updated_time).total_seconds()))
            if (datetime.now() - user.updated_time).total_seconds() < 60:
                await try_send(message.channel, "kecepetan bodoh delaynya semenit")
                return
        coin = 0
        if random.random() > .1:
            coin = random.randrange(0,51)
            user.jahyadi_coin = user.jahyadi_coin + coin
            user.updated_time = datetime.now()
            self.session.commit()
        await try_send(message.channel, 'you got {} coins'.format(coin))