import random

import discord

from command.economy.EconomyBase import EconomyBase
from model.User import User
from util.Util import try_send

MIN_COIN = 100


class Bet(EconomyBase):
    def __init__(self, client, logging, session):
        super().__init__(session)
        self.client = client
        self.logging = logging

    async def do_response(self, message, args):
        await super().do_response(message, args)
        user = self.session.query(User).filter(User.user_id == message.author.id).one()

        if len(args) < 3:
            await try_send(message.channel, "Bet berapa?")
            return

        bet_amount = int(args[2])
        dice_player = random.randrange(1, 7)
        dice_dealer = random.randrange(1, 7)
        if dice_player > dice_dealer:
            user.jahyadi_coin = user.jahyadi_coin + bet_amount
            title = "kau menghasilkan kapital ekonomi"
        else:
            user.jahyadi_coin = user.jahyadi_coin - bet_amount
            title = "mampus kalah judi"
        self.session.commit()
        response = discord.Embed(title=title)
        response.add_field(name="{}'s Dice".format(message.author.name), value="{}".format(dice_player), inline=True)
        response.add_field(name="Dealer's Dice", value="{}".format(dice_dealer), inline=True)
        await try_send(message.channel, embed=response)
