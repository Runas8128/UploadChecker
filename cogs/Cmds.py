from Common import *

class CmdCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='딜레이', aliases=['지연시간'])
    async def CMD_latency(self, ctx: commands.Context):
        t1 = time()
        msg = await ctx.send('asdf')
        t2 = time()
        await msg.edit(content=f'현재 딜레이: {round((t2 - t1) * 1000, 2)}ms')

    @commands.command(name='코드보기')
    async def CMD_ViewCode(self, ctx: commands.Context):
        await ctx.send('https://github.com/Runas8128/UploadChecker')
    
    @commands.command(name='밀린양')
    async def CMD_LeftRequest(self, ctx: commands.Context):
        await ctx.send(embed=manager.get(self.bot))

def setup(bot: commands.Bot):
    bot.add_cog(CmdCog(bot))