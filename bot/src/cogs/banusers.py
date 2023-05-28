#!/usr/bin/env python
from discord.ext import commands
from config import USER_ID


banned_names = [
    'kiyo',
    'taka',
    'ayano',
    'koji',
    'ayanokoji',
    'ayanokouji',
    'sainlow',
    'pon',
    'aya'
]

class BanUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banusers(self, ctx):
        if ctx.author.id == USER_ID:
            print('executing')
            print(ctx.guild.me.guild_permissions.ban_members)
            banned_users = []
            for member in ctx.guild.members:
                if any(name in member.name.lower() for name in banned_names):
                    await member.ban(reason='ayanokoji wannabe issue')
                    banned_users.append(member.name)
            if banned_users:
                await ctx.send('all ayanokoji wannabes have been banned')
            else:
                await ctx.send('Server is Clear!')
        else:
            await ctx.send(f"{ctx.author.mention}, you're not worthy of using me.")
        pass

async def setup(bot):
    await bot.add_cog(BanUsers(bot))