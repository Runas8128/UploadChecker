from Common import *
from Manager import manager

class CmdCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        self.UserConverter = commands.UserConverter()
        self.HelpEmbed: discord.Embed = None        
        self.LogChannel: discord.TextChannel = None

    @commands.command(name='딜레이', aliases=['지연시간'])
    async def CMD_latency(self, ctx: commands.Context):
        t1 = time()
        msg = await ctx.send('asdf')
        t2 = time()
        await msg.edit(content=f'현재 딜레이: {round((t2 - t1) * 1000, 2)}ms')

    @commands.command(name='코드보기')
    async def CMD_ViewCode(self, ctx: commands.Context):
        await ctx.send('https://replit.com/@Runas8128/UploadChecker')
    
    @commands.command(name='밀린양')
    async def CMD_LeftRequest(self, ctx: commands.Context):
        await ctx.send(embed=manager.get(self.bot))

    @commands.command(name='추가')
    @commands.has_permissions(administrator=True)
    async def CMD_Add(self, ctx: commands.Context):
        try:
            msg: discord.Message = ctx.message
            for user in msg.mentions:
                manager.add(user.mention)
                await self.LogChannel.send(f"New Record Request - from {user.mention}, now left: {len(self.Left)}")
            await ctx.message.add_reaction('👌')
        except (commands.errors.BadArgument, commands.errors.CommandError):
            await ctx.send("사용법: !추가 (멘션)")
    
    @commands.command(name='삭제', aliases=['제거'])
    @commands.has_permissions(administrator=True)
    async def CMD_Delete(self, ctx: commands.Context, index: int=-1):
        await self.LogChannel.send(
            f"Deleted Record Request - from {self.bot.get_user(manager.pop(index)).display_name}, now left: {len(manager.Left)}"
        )
        await ctx.message.add_reaction('👌')

def setup(bot: commands.Bot):
    bot.add_cog(CmdCog(bot))