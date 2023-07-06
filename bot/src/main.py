#!/usr/bin/env python
import discord
from discord.ext import commands
from config import TOKEN
import os


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = filename[:-3]
            cog_path = f'cogs.{cog_name}'
            try:
                await bot.load_extension(cog_path)
                print(f'Loaded {cog_path} successfully')          
            except commands.ExtensionError as e:
                print(f'Failed to load {cog_path}: {str(e)}')

@bot.event
async def on_ready():
    print(f'Accessed the ICE as {bot.user.name} ({bot.user.id})')
    print('----------')

    # load cogs
    await load_cogs()

    
bot.run(TOKEN)
