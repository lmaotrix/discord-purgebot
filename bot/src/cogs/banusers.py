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
    'aya',
    'OtakuGamer',
    'KawaiiWarrior', 
    'ShinigamiNinja', 
    'AnimeAddict', 
    'MechaPilot',                      
    'DragonSlayer', 
    'SamuraiGamer', 
    'MoeMaiden', 
    'BlackRoseAssassin', 
    'SuperSaiyanGamer',                      
    'CyberpunkNinja', 
    'ValkyrieGoddess', 
    'MagicalGirl', 
    'GalacticWarrior', 
    'NekoGamer#8901',
    'ShadowAssassin', 
    'SwordArtGamer', 
    'GundamPilot', 
    'KpopAnimeFan', 
    'DragonBallZFan',
    'SailorMoonLover', 
    'ChibiGamer', 
    'ShonenHero', 
    'PokemonMaster', 
    'MangaFan',
    'KawaiiOtaku', 
    'NarutoFan', 
    'OnePieceLover', 
    'BleachFan', 
    'FairyTailWizard',
    'InuyashaFan', 
    'TokyoGhoulFan', 
    'AttackOnTitanFan', 
    'MyHeroAcademiaFan', 
    'DemonSlayerFan', 
    'FullmetalAlchemistFan',
    'CowboyBebopFan',
    'TrigunFan',
    'HunterxHunterFan', 
    'JoJosBizarreAdventureFan', 
    'PsychoPassFan', 
    'VioletEvergardenFan', 
    'DeathParadeFan',                      
    'ClannadFan', 
    'SteinsGateFan', 
    'ReZeroFan', 
    'KonosubaFan'
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
                if any(name in (member.global_name or "") for name in banned_names):
                    await member.ban(reason='ayanokoji wannabe issue')
                    banned_users.append(member.display_name)
            if banned_users:
                await ctx.send('All ayanokoji wannabes have been banned')
            else:
                await ctx.send('Server is clear!')
        else:
            await ctx.send(f"{ctx.author.mention}, you're not worthy of using me.")

async def setup(bot):
    await bot.add_cog(BanUsers(bot))