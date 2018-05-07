import random
import requests
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("``", "@PlasmaBot#0176")
TOKEN = "NDQyNzkwNTMxODE5NjM0Njg4.DdEQig.5tiD4083_DVfP_cfzXzeR6k-TKI"  # Get at discordapp.com/developers/applications/me
DESCRIPTION = '''A bot with just a bunch of random stuff.

PlasmaLink's baby.'''

# this specifies what extensions to load when the bot starts up
startup_extensions = ["Mathstuff", "twitter"]

bot = Bot(command_prefix=BOT_PREFIX, description=DESCRIPTION)

@bot.command(name='8ball',
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
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

	
	
@bot.command(name="roll",
				description="Roll a dice with specified sides",
				brief="Roll a die!",
				aliases=['r', 'dice'])
async def roll(number):
	try:
		d = int(number)
		r = random.randrange(1, d+1)
		await bot.say("Rolling a d" + number + "... It returned a " + str(r) + "!")
	except ValueError:
		await bot.say("That's not a valid number!")

@bot.command()
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
	
@bot.command(name="astros",
				description="Displays how many people are currently in space.",
				brief="How many are in space?")
async def astros():
	response = requests.get("http://api.open-notify.org/astros.json")
	data = response.json()
	await bot.say("There are currently " + str(data["number"]) + " people in space right now!")
	

async def list_servers():
	await bot.wait_until_ready()
	while not bot.is_closed:
		print("Current servers:")
		for server in bot.servers:
			print(server.name)
		await asyncio.sleep(600)
	
@bot.event
async def on_ready():
	await bot.change_presence(game=Game(name="big mood"))
	print("Logged in as " + bot.user.name)
	
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))
	
	
bot.loop.create_task(list_servers())
bot.run(TOKEN)