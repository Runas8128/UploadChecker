from Common import *

class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot 
        self.LogChannel: discord.TextChannel = None
    
    # Duplicated ready listener for initing Logging channel
    @commands.Cog.listener()
    async def on_ready(self):
        self.LogChannel = self.bot.get_channel(881882849316323370)
    
    @commands.command(name='추가')
    @commands.has_permissions(administrator=True)
    async def CMD_Add(self, ctx: commands.Context):
        if not self.LogChannel:
            pass
        try:
            msg: discord.Message = ctx.message
            for user in msg.mentions:
                manager.add(user.id)
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
    
    @commands.command(name='일괄추가')
    @commands.has_permissions(administrator=True)
    async def CMD_AddCollectively(self, ctx: commands.Context, *ids: int):
        for id in ids:
            manager.add(id)
        await ctx.message.add_reaction('👌')