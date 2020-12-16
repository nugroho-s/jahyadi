import logging
from datetime import datetime
from os import environ

import discord
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from command.Balance import Balance
from command.Beg import Beg
from command.Empati import Empati
from command.Intonasi import Intonasi
from command.Kontribusi import Kontribusi
from command.Penis import Penis
from command.Quote import Quote
from command.Say import Say
from model.User import User
from util.Util import try_send

logging.basicConfig(format='[%(levelname)s] [%(name)s] %(message)s', level=logging.INFO)
prefix = "sudah"

engine = create_engine(environ.get('DATABASE_URL'), echo=True)
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
                    "bal": Balance(client, logging, session)
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

    if args[1] in commandhandlers:
        await commandhandlers[args[1]].do_response(message, args)


client.run(environ.get('BOT_TOKEN'))
