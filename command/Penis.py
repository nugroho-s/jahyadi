import discord
import re
import random


class Penis:
    def __init__(self, client, logging):
        self.client = client
        self.logging = logging

    async def do_response(self, message, args):
        i = random.randint(0, 10)
        penis_size = "8" + ("=" * i) + "D"
        user = message.author
        if len(args) > 2:
            user_id = args[2]
            user_id = re.findall("\d+", user_id)[0]
            try:
                user = await self.client.fetch_user(int(user_id))
            except discord.errors.NotFound:
                self.logging.error("User not found: {}".format(user_id))
                return
        embed_var = discord.Embed(title="Peepee size machine",
                                  description="{}'s penis\n{}".format(user.name, penis_size), color=0x00ff00)
        await message.channel.send(embed=embed_var)
        if i == 0:
            await message.channel.send('Apa kau ga malu, punya penis 8D?')