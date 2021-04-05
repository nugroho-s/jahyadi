import json
import urllib

import discord

from command.Command import Command
from util.Util import try_send


class Quran(Command):
    def __init__(self, logging):
        self.logging = logging
        pass

    async def do_response(self, message, args):
        if len(args) < 3:
            return
        url = "resources/quran/{}.json".format(args[2])
        with open(url) as quran_response:
            data = json.load(quran_response)
            surah = data[next(iter(data))]
            if len(args) == 3:
                response = discord.Embed(title=surah['name_latin'])
                response.add_field(name='arabic', value=surah['name'], inline=False)
                response.add_field(name='jumlah ayat', value=surah['number_of_ayah'], inline=False)
                response.add_field(name='arti', value=surah['translations']['id']['name'], inline=False)
            if len(args) == 4:
                response = discord.Embed(title="{}:{}".format(surah['name_latin'], args[3]))
                response.add_field(name='arabic', value=surah['text'][args[3]][:1024], inline=False)
                translations_text = surah['translations']['id']['text'][args[3]]
                if len(translations_text) > 1024:
                    translations_text = translations_text[:1021] + '...'
                response.add_field(name='arti', value=translations_text, inline=False)
                self.logging.info(surah['translations']['id']['text'][args[3]])
            await try_send(message.channel, embed=response)
