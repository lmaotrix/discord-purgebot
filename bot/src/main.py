import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

banned_names = [
  'kiyo', 'taka', 'ayano', 'koji', 'ayanokoji', 'ayanokouji', 'sainlow' 'pon', 'aya']
user_id = 618881902266286092 #replace user_id with your own ID

@bot.command()
async def banusers(ctx):
  
    if ctx.author.id == user_id:
    
        print('executing')
        print(ctx.guild.me.guild_permissions.ban_members)
        for member in ctx.guild.members:
            if any(name in member.name.lower() for name in banned_names):
                await member.ban(reason='ayanokoji wannabe issue')

        await ctx.send('all ayanokoji wannabes have been banned')

    else:
        await ctx.send(f"{ctx.author.mention}, you're not worthy of using me. sucks to suck")



bot.run(TOKEN)