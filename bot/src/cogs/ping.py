from discord.ext import commands
from config import USER_ID


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #@commands.Cog.listener()
    #async def on_message(self, message):
     #   if message.author == self.bot.user:
      #      return
        
       # if self.bot.user in message.mentions:
        #    if message.author.id == USER_ID:
         #       await message.channel.send('At your service, sir!')
          #  else:
           #     await message.channel.send("What color is your Bugatti? Get rich first")
    
    #@commands.command()
    #async def ping(self, ctx):
     #   if ctx.author.id == USER_ID:
      #      await ctx.send('At your service, sir!')
       # else:
        #    await ctx.send("What color is your Bugatti? Get rich first")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if self.bot.user in message.mentions and message.author.id != self.bot.user.id:
            if message.author.id == USER_ID:
                await message.channel.send('At your service, sir!')
            else:
                await message.channel.send("What color is your Bugatti? Get rich first")



async def setup(bot):
    await bot.add_cog(Ping(bot))