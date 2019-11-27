import discord
from discord.ext import commands

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def hello(self, ctx):
		await ctx.send('Hello {0.display_name}.'.format(ctx.author))
	
	@commands.command()
	async def bye(self, ctx):
		await ctx.send('Goodbye {0.display_name}.'.format(ctx.author))

def setup(bot):
	bot.add_cog(Greetings(bot))
