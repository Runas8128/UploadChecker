from Common import *

class AdminCog(commands.Cog):
    LogChannel: discord.TextChannel
    BugChannel: discord.TextChannel

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Duplicated ready listener for initing Logging channel
    @commands.Cog.listener()
    async def on_ready(self):
        self.LogChannel = self.bot.get_channel(881882849316323370)
        self.BugChannel = self.bot.get_channel(884356850248724490)
    
    @commands.command(name='추가')
    @commands.has_permissions(administrator=True)
    async def CMD_Add(self, ctx: commands.Context):
        if not self.LogChannel:
            pass
        try:
            msg: discord.Message = ctx.message
            for user in msg.mentions:
                manager.add(user.id)
                await self.LogChannel.send(f"New Record Request - from {user.mention}, now left: {len(manager.Left)}")
            await ctx.message.add_reaction('👌')
        except (commands.errors.BadArgument, commands.errors.CommandError):
            await ctx.send("사용법: !추가 (멘션)")
    
    @commands.command(name='삭제', aliases=['제거'])
    @commands.has_permissions(administrator=True)
    async def CMD_Delete(self, ctx: commands.Context, index: int=-1):
        uid = manager.pop(index)
        user = self.bot.get_user(uid)
        if user:
            await self.LogChannel.send(f"Deleted Record Request - from {user.display_name}, now left: {len(manager.Left)}")
        elif uid:
            await self.LogChannel.send(f"Deleted Record Request - from user id {uid}, now left: {len(manager.Left)}")
    
    @commands.command(name='일괄추가')
    @commands.has_permissions(administrator=True)
    async def CMD_AddCollectively(self, ctx: commands.Context, *ids: int):
        for id in ids:
            manager.add(id)
        await ctx.message.add_reaction('👌')
    
    @commands.command(name='앞에추가')
    @commands.has_permissions(administrator=True)
    async def CMD_AddCollectivelyFront(self, ctx: commands.Context, *ids: int):
        for id in ids:
            manager.addFront(id)
        await ctx.message.add_reaction('👌')
    
    @commands.command(name='초기화')
    @commands.has_permissions(administrator=True)
    async def CMD_Clear(self, ctx: commands.Context):
        manager.clear()
        await ctx.message.add_reaction('👌')
    
    @commands.command(name='버그')
    async def CMD_ReportBug(self, ctx: commands.Context, *content: str):
        await self.BugChannel.send(' '.join(content))
        await ctx.send("제보해드렸어요! 언젠간 고치겠죠(?)")

def setup(bot: commands.Bot):
    bot.add_cog(AdminCog(bot))