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
    
    @commands.command(name='μΆκ°')
    @commands.has_permissions(administrator=True)
    async def CMD_Add(self, ctx: commands.Context):
        if not self.LogChannel:
            pass
        try:
            msg: discord.Message = ctx.message
            for user in msg.mentions:
                manager.add(user.id)
                await self.LogChannel.send(f"New Record Request - from {user.mention}, now left: {len(manager.Left)}")
            await ctx.message.add_reaction('π')
        except (commands.errors.BadArgument, commands.errors.CommandError):
            await ctx.send("μ¬μ©λ²: !μΆκ° (λ©μ)")
    
    @commands.command(name='μ­μ ', aliases=['μ κ±°'])
    @commands.has_permissions(administrator=True)
    async def CMD_Delete(self, ctx: commands.Context, index: int=-1):
        uid = manager.pop(index)
        user = self.bot.get_user(uid)
        if user:
            await self.LogChannel.send(f"Deleted Record Request - from {user.display_name}, now left: {len(manager.Left)}")
        elif uid:
            await self.LogChannel.send(f"Deleted Record Request - from user id {uid}, now left: {len(manager.Left)}")
        await ctx.message.add_reaction('π')
    
    @commands.command(name='μΌκ΄μΆκ°')
    @commands.has_permissions(administrator=True)
    async def CMD_AddCollectively(self, ctx: commands.Context, *ids: int):
        for id in ids:
            manager.add(id)
        await ctx.message.add_reaction('π')
    
    @commands.command(name='μμμΆκ°')
    @commands.has_permissions(administrator=True)
    async def CMD_AddCollectivelyFront(self, ctx: commands.Context, *ids: int):
        for id in ids:
            manager.addFront(id)
        await ctx.message.add_reaction('π')
    
    @commands.command(name='μ΄κΈ°ν')
    @commands.has_permissions(administrator=True)
    async def CMD_Clear(self, ctx: commands.Context):
        manager.clear()
        await ctx.message.add_reaction('π')
    
    @commands.command(name='λ²κ·Έ')
    async def CMD_ReportBug(self, ctx: commands.Context, *content: str):
        await self.BugChannel.send(' '.join(content))
        await ctx.send("μ λ³΄ν΄λλ Έμ΄μ! μΈμ  κ° κ³ μΉκ² μ£ (?)")

def setup(bot: commands.Bot):
    bot.add_cog(AdminCog(bot))