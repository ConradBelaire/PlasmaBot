import discord
from discord.ext import commands
from TwitterAPI import TwitterAPI, TwitterPager
import random

class twitter():

	# api = TwitterAPI("JxnEf70mF6iyRi669yQ2EIgwW", "rBOdLgHYU5xIEG3qvsOrKzTSHq3rEuVOl6hLDESq9AZVuyIBHP", "34954969-LBRBGz3Dim9ke9QtkHjffTsDBPKJgfBXAdXBwZvdE", "rmkoKemZc4WG7jobEEFYdNnpSa6fJ49GMWHUdgKzFFkRp")
	
	
	
	def __init__(self, bot):
		self.bot = bot
		

	@commands.command(name="dril",
					description="Posts a random dril tweet. Can make multiple posts, and adjust how far back to look (further means longer wait time)",
					brief="Random @dril tweet, give it a few seconds")
	async def dril(self, num=1, distance=500):
		# await self.bot.say("Give me a moment!")
		api = TwitterAPI("JxnEf70mF6iyRi669yQ2EIgwW", "rBOdLgHYU5xIEG3qvsOrKzTSHq3rEuVOl6hLDESq9AZVuyIBHP", auth_type='oAuth2')
	
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
				await self.bot.say(item['message'])
				break
		
		for i in range(0, num):
			msg = random.choice(tweets)
			await self.bot.say(msg)
	


def setup(bot):
    bot.add_cog(twitter(bot))
