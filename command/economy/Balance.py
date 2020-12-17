from datetime import datetime

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
        user = self.session.query(User).filter(User.user_id == message.author.id).one()
        userDiscord = await self.client.fetch_user(user.user_id)
        await try_send(message.channel, 'jahyadi coin {} {}'.format(userDiscord.name, user.jahyadi_coin))