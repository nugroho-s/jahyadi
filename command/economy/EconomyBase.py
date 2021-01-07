import math
from datetime import datetime

from command.Command import Command
from model.User import User
from util.Util import try_send


class EconomyBase(Command):
    def __init__(self, session):
        self.session = session

    async def do_response(self, message, args):
        count = self.session.query(User).filter(User.user_id == message.author.id).count()
        if count == 0:
            self.session.add(User(message.author.id, 0, None))
            self.session.commit()

    async def is_cooldown(self, lut, seconds, channel):
        if lut is not None:
            elapsed = (datetime.now() - lut).total_seconds()
            if elapsed < seconds:
                await try_send(channel, "kecepetan bodoh tunggu {} detik lagi".format(math.ceil(seconds - elapsed)))
                return True
        return False
