import discord
from discord.ext import commands

class Mathstuff():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def square(self, number : int):
		squared_value = int(number) * int(number)
		await self.bot.say(str(number) + "^2 = " + str(squared_value))
		


def setup(bot):
    bot.add_cog(Mathstuff(bot))
