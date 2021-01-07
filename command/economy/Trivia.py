import asyncio
import random
import re
from datetime import datetime

from command.economy.EconomyBase import EconomyBase
from command.fun.Quote import Quote
from model.User import User
from util.Util import try_send


class Trivia(EconomyBase):
    def __init__(self, client, logging, session):
        super().__init__(session)
        self.logging = logging
        self.client = client
        pass

    async def do_response(self, message, args):
        await super().do_response(message, args)
        user = self.session.query(User).filter(User.user_id == message.author.id).one()

        if await super().is_cooldown(user.last_trivia, 60, message.channel):
            return

        user.last_trivia = datetime.now()
        self.session.commit()
        quote = Quote.get_random_quote()
        quote_array = quote.split()
        random_idx = 0
        answer = re.sub(r'[^\w]', '', quote_array[random_idx])
        quote_array[random_idx] = re.sub(r'[\w]', '_ ', quote_array[random_idx])
        quote_array[random_idx] = '`' + quote_array[random_idx] + '`'
        await try_send(message.channel, ' '.join(quote_array))

        def check(m):
            return m.content.lower() == answer.lower() and m.channel == message.channel and m.author == message.author
        try:
            await self.client.wait_for('message', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await try_send(message.channel, "Seems like kau terlalu bodoh untuk menjawab")
        else:
            user.jahyadi_coin += 100
            self.session.commit()
            await try_send(message.channel, "Kau dapat 100 jahyadi coin")
