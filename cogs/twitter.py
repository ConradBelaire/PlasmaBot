import discord
from discord.ext import commands
from TwitterAPI import TwitterAPI, TwitterPager
import random
from secrets import k1, k2

class Twitter(commands.Cog):

	
	def __init__(self, bot):
		self.bot = bot
		

	@commands.command(name="dril",
					description="Posts a random dril tweet. Can make multiple posts, and adjust how far back to look (further means longer wait time)",
					brief="Random @dril tweet, give it a few seconds")
	async def dril(self, ctx, num=1, distance=500):
		# await self.bot.say("Give me a moment!")
		api = TwitterAPI(k1, k2, auth_type='oAuth2')
	
		SCREEN_NAME = 'dril'
		pager = TwitterPager(api,'statuses/user_timeline', {'screen_name':SCREEN_NAME, 'count':200})
		count = 0
		tweets = []
		for item in pager.get_iterator(wait=0.1):
			if 'text' in item:
				count = count + 1
				# await self.bot.say(str(count) + ". " + item['text'])
				tweets.append(item['text'])
				if (count > distance):
					break
			elif 'message' in item:
				await ctx.send(item['message'])
				break
		
		for i in range(0, num):
			if not tweets:
				break
			msg = random.choice(tweets)
			await ctx.send(msg)
			tweets.remove(msg)
	


def setup(bot):
    bot.add_cog(Twitter(bot))
