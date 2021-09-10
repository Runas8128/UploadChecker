import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=['!'], intents=discord.Intents.all())

@bot.command()
@commands.is_owner()
async def reload(ctx: commands.Context, me: discord.User=None):
    if me == bot.user:
        bot.unload_extension('MainCog')
        bot.load_extension('MainCog')
        await ctx.send('reloaded')

bot.load_extension('MainCog')
bot.run('ODc5NzEwMDQ5NTkxNzc1Mjcy.YSTr1A.JLGow16XEirHjVvCLVtoFZIMTy0')