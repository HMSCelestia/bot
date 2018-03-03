import discord
#from discord.ext.commands import Bot
#from discord.ext import commands
import asyncio
client = discord.Client()
bot_prefix="?"


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.send_message('general', 'Tutorial here, ready to roll.')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('soy'):
        await client.send_message(message.channel, 'SOYBOY')




#341930220154126336

client.run("NDE5MzMwMzk0NDU0NzUzMjg0.DXuj1w.m7kPD3vvRaIqHkNP3PDGt1TkXCI")