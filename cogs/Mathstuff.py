import discord
import random
from discord.ext import commands

class Mathstuff():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="square",
					description="Returns the square of a number.",
					brief="Square a number.")
	async def square(self, number : int):
		squared_value = int(number) * int(number)
		await self.bot.say(str(number) + "^2 = " + str(squared_value))
		
	
	@commands.command(name="roll",
				description="Roll a dice with specified sides",
				brief="Roll a die!",
				aliases=['r', 'dice'])
	async def roll(self, number):
		try:
			d = int(number)
			r = random.randrange(1, d+1)
			await self.bot.say("Rolling a d" + number + "... It returned a " + str(r) + "!")
		except ValueError:
			await self.bot.say("That's not a valid number!")
		


def setup(bot):
    bot.add_cog(Mathstuff(bot))
