import logging
from os import environ

import discord
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from command.economy.Balance import Balance
from command.economy.Beg import Beg
from command.fun.Empati import Empati
from command.fun.Intonasi import Intonasi
from command.fun.Penis import Penis
from command.fun.Quote import Quote
from command.economy.Rich import Rich
from command.Say import Say
from util.Util import try_send

logging.basicConfig(format='[%(levelname)s] [%(name)s] %(message)s', level=logging.INFO)
prefix = "sudah"

engine = create_engine(environ.get('DATABASE_URL'))
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

client = discord.Client()

commandhandlers = {
                    "penis": Penis(client, logging),
                    "quote": Quote(logging),
                    "say": Say(client, logging),
                    "empati": Empati(client, logging),
                    "intonasi": Intonasi(client, logging),
                    "beg": Beg(logging, session),
                    "bal": Balance(client, logging, session),
                    "rich": Rich(client, logging, session)
                  }


@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '750726551762370680>' in message.content:
        await try_send(message.channel, 'Kalau mau aku baikan, dont ever tag me!!')

    comparator_prefix = message.content[:len(prefix)].lower()
    if comparator_prefix != prefix:
        return

    args = message.content.lower().split(' ')

    if args[1] == "help":
        help_str = ""
        for key in commandhandlers.keys():
            help_str = help_str + key + ', '
        await try_send(message.channel, help_str[0:-2])

    if args[1] in commandhandlers:
        await commandhandlers[args[1]].do_response(message, args)


client.run(environ.get('BOT_TOKEN'))
