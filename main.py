import discord
from discord.ext import commands
import random
from secrets import TOKEN

BOT_PREFIX = ("``")

DESCRIPTION = '''A bot with just a bunch of random stuff.

PlasmaLink's baby.'''

# this specifies what extensions to load when the bot starts up
startup_extensions = ["greetings", "twitter"]

bot = commands.Bot(command_prefix=BOT_PREFIX, description=DESCRIPTION)

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(ctx):
    possible_responses = [
        'yee haw',
        'yee naw',
        'uuuuuuuuuuuuuhhhhhhhhhhhhhhhhhhhhhh',
        'BIG naw',
        'yeet',
		'Sir this is a wendys'
    ]
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)

		

'''
@bot.command()
async def ISS(name="ISS",
				description:"Prints information to the console"):
	# Set up the parameters we want to pass to the API.
	# This is the latitude and longitude of New York City.
	parameters = {"lat": 40.71, "lon": -74}

	# Make a get request with the parameters.
	response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

	# Get the response data as a python object.  Verify that it's a dictionary.
	data = response.json()
	print(type(data))
	print(data)
'''

'''	
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
	
'''


@bot.event
async def on_ready():
	# await bot.change_presence(game=Game(name="``help"))
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	
	for extension in startup_extensions:
		try:
			bot.load_extension('cogs.' + extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))
	
	
# bot.loop.create_task(list_servers())
bot.run(TOKEN)