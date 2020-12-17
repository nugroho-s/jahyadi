from datetime import datetime

from model.User import User
from util.Util import try_send


class EconomyBase:
    def __init__(self, session):
        self.session = session

    async def do_response(self, message, args):
        count = self.session.query(User).filter(User.user_id == message.author.id).count()
        if count == 0:
            self.session.add(User(message.author.id, 0, None))
            self.session.commit()

    async def is_cooldown(self, lut, seconds, channel):
        if lut is not None:
            if (datetime.now() - lut).total_seconds() < seconds:
                await try_send(channel, "kecepetan bodoh delaynya {} detik".format(seconds))
                return True
        return False
