# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

TOKEN = 'NDQyNzkwNTMxODE5NjM0Njg4.DdEQig.5tiD4083_DVfP_cfzXzeR6k-TKI'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('who let the dogs out'):
        msg = 'Who'.format(message)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)