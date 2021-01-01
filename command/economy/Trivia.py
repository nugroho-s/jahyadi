import math
from datetime import datetime

from command.economy.EconomyBase import EconomyBase
from command.fun.Quote import Quote
from model.User import User
from util.Util import try_send
import random


class Trivia(EconomyBase):
    def __init__(self, client, logging, session):
        super().__init__(session)
        self.logging = logging
        self.client = client
        pass

    async def do_response(self, message, args):
        await super().do_response(message, args)
        user = self.session.query(User).filter(User.user_id == message.author.id).one()

        if await super().is_cooldown(user.last_trivia, 5, message.channel):
            return

        # coin = math.ceil(max(random.gauss(25, 20), 0))
        # user.jahyadi_coin = user.jahyadi_coin + coin
        user.last_trivia = datetime.now()
        self.session.commit()
        quote = Quote.get_random_quote()
        quote_array = quote.split()
        random_idx = random.randrange(0, len(quote_array))
        quote_array[random_idx] = '`' + ('_ ' * len(quote_array[random_idx])) + '`'
        print(' '.join(quote_array))
        await try_send(message.channel, ' '.join(quote_array))
