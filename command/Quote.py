import json
import random


class Quote:
    def __init__(self):
        with open('quotes.json') as json_file:
            self.quotes = json.load(json_file)

    async def do_response(self, message, args):
        await message.channel.send(random.choice(self.quotes))
