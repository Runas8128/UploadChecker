import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=['!'], intents=discord.Intents.all())

cogs = ['Cmds', 'Events', 'Admin', 'Help']

@bot.command()
@commands.is_owner()
async def reload(ctx: commands.Context, me: discord.User=None):
    if me == bot.user:
        for cog in cogs:
            bot.unload_extension(f'cogs.{cog}')
            bot.load_extension(f'cogs.{cog}')
        await ctx.send('reloaded')

for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

from Common import TOKEN
bot.run(TOKEN)