# Sailing Facts bot, a simple discord bot to display sailing facts on a discord server
# Copyright (C) 2022  Antoine Meloche

import os
import discord
import random

facts= ["Sailing is the act of using wind to propel a vessel through the water.","Sailing has been used since ancient times and was integral to the development of civilization.","The first boats are thought to have been used for fishing and transportation of goods.","The first sailing boats were probably built in the Nile Valley in Egypt.","The first sailing boats were made from reeds or papyrus and were propelled by oars.","The first sails were probably made from animal skins.","The first recorded use of sails was by the Phoenicians around 3,000 BCE.","The first sailing boats were used for trade and transportation.","The first sailing boats were used in warfare by the Greeks and Romans.","The first sailing boats were used in exploration by the Polynesians.","The first sailing boats were used in recreation by the Chinese.","The first recorded America's Cup race was in 1851.","The America's Cup is the oldest international sporting trophy.","The first keelboat regatta was held in America in 1876.","The first yacht club in America was founded in 1828.","The first yacht club in the world was founded in England in 1815.","The first transatlantic yacht race was held in 1866.","The first sailing school in America was founded in 1874.","The first intercollegiate sailing competition was held in 1897.","The first women's intercollegiate sailing competition was held in 1973.","The first international women's sailing event was held in England in 1949.","The first African American women's sailing event was held in 1984.","The first Latino American sailing event was held in 1997.","The first Asian American sailing event was held in 1998.","The first disabled sailing event was held in England in 1971.","The first Special Olympics sailing event was held in 1987.","The first Youth Sailing World Championship was held in 1971.","The first Women's Match Racing World Championship was held in 1999.","The first Open Match Racing World Championship was held in 2004.","The first Paralympic Sailing Competition was held in 2000.","The first America's Cup World Series was held in 2011.","The first America's Cup World Championship was held in 2013.","The first America's Cup Challenger Selection Series was held in 2017.","The America's Cup has been held 32 times.","The America's Cup has been won by 25 different yacht clubs.","The America's Cup has been won by 10 different nations.","The America's Cup was first held in the United Kingdom in 1851.","The America's Cup was first held in the United States in 1857.","The America's Cup was first held in Australia in 1983.","The America's Cup was first held in New Zealand in 2000.","The America's Cup was first held in Spain in 2007.","The America's Cup was first held in Italy in 2017.","The America's Cup is currently held by the Royal New Zealand Yacht Squadron.","The America's Cup is currently defended by Emirates Team New Zealand.","The America's Cup is currently contested by America's Cup World Series events.","The next America's Cup is scheduled to be held in 2021.","The America's Cup is sailed in 75-foot (23-meter) catamarans."]

class SailingFacts(discord.Client):

    async def on_ready(self):
        print(f'Bot has logged in as {client.user}')
        await client.change_presence(activity=discord.Activity(name=r'use %fact to get a sailing fact', type=0))

    async def on_message(self,message):
        if message.author == client.user:
            return
        
        if message.content.startswith(r'%help'):
            await message.channel.send('```%fact: display a random sailing fact\n%fact #: display a specific sailing fact```')

        if message.content.startswith(r'%fact '):
            try:
                pos = int(message.content.split(r'%fact ')[1])-1
            except Exception:
                await message.channel.send('```%fact #: display a specific sailing fact```')
                return

            try:
                fact = facts[pos]
                await message.channel.send(fact)
            except IndexError:
                await message.channel.send('```The maximum fact number is currently '+str(len(facts))+'```')
                return
        elif message.content.startswith(r'%fact'):
            num = random.randrange(0,len(facts))
            await message.channel.send(facts[num])

is_heroku = os.environ.get('IS_HEROKU', None)

if is_heroku:
    token = os.environ.get('BOT_TOKEN')
else:
    try:
        with open('token.txt', 'r') as f:
            token = f.read()
    except Exception:
        print('No token found, either the `token.txt` file is missing or the file is empty.')
        exit(1)

client = SailingFacts()
client.run(token)