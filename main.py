import random
import requests
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("``")
TOKEN = "NDQyNzkwNTMxODE5NjM0Njg4.DdEQig.5tiD4083_DVfP_cfzXzeR6k-TKI"  # Get at discordapp.com/developers/applications/me
DESCRIPTION = '''A bot with just a bunch of random stuff.

PlasmaLink's baby.'''

client = Bot(command_prefix=BOT_PREFIX, description=DESCRIPTION)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'like zoinks, heck no scoob',
        'Yeah sure why not',
        'uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',
        'owo',
        'yup yup yup'
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(number):
	squared_value = int(number) * int(number)
	await client.say(str(number) + "^2 = " + str(squared_value))
	
	
@client.command(name="roll",
				description="Roll a dice with specified sides",
				brief="Roll a die!",
				aliases=['r', 'dice'])
async def roll(number):
	try:
		d = int(number)
		r = random.randrange(1, d+1)
		await client.say("Rolling a d" + number + "... It returned a " + str(r) + "!")
	except ValueError:
		await client.say("That's not a valid number!")

@client.command()
async def ISS():
	# Set up the parameters we want to pass to the API.
	# This is the latitude and longitude of New York City.
	parameters = {"lat": 40.71, "lon": -74}

	# Make a get request with the parameters.
	response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

	# Get the response data as a python object.  Verify that it's a dictionary.
	data = response.json()
	print(type(data))
	print(data)
	
@client.command(name="astros",
				description="Displays how many people are currently in space.",
				brief="How many are in space?")
async def astros():
	response = requests.get("http://api.open-notify.org/astros.json")
	data = response.json()
	await client.say("There are currently " + str(data["number"]) + " people in space right now!")
	

async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed:
		print("Current servers:")
		for server in client.servers:
			print(server.name)
		await asyncio.sleep(600)
	
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="big mood"))
    print("Logged in as " + client.user.name)
	
	
client.loop.create_task(list_servers())
client.run(TOKEN)