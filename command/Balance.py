from datetime import datetime

from model.User import User
from util.Util import try_send
import random

class Balance:
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
        await try_send(message.channel, 'jahyadi coinmu {}'.format(user.jahyadi_coin))