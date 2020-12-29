import json
import logging
import random
import time
import urllib.request

from util.Util import try_send

logging.basicConfig(format='[%(levelname)s] [%(name)s] %(message)s', level=logging.INFO)


class Quote:
    refresh_time = 3600
    quotes_cache = {}

    def __init__(self, logging):
        self.logging = logging
        with open('quotes.json') as json_file:
            Quote.quotes_cache['quotes'] = json.load(json_file)
            Quote.quotes_cache['lut'] = time.time()

    @staticmethod
    def refresh_quotes():
        logging.info("refreshing quotes")
        with urllib.request.urlopen("https://raw.githubusercontent.com/nugroho-s/jahyadi/master/quotes.json") as url:
            Quote.quotes_cache['quotes'] = json.loads(url.read().decode())
            Quote.quotes_cache['lut'] = time.time()
            logging.info(Quote.quotes_cache)

    @staticmethod
    def get_random_quote():
        if time.time() - Quote.quotes_cache['lut'] > Quote.refresh_time:
            Quote.refresh_quotes()
        return random.choice(Quote.quotes_cache['quotes'])

    async def do_response(self, message, args):
        await try_send(message.channel, Quote.get_random_quote())
