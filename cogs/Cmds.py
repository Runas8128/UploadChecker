from Common import *

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
        embed = discord.Embed(title="밀린 양 임베드", description="귀찮아서 상위5개 하위5개만 보여드림")
        
        for i in range(0, 4+1):
            embed.add_field(name=f"#{i+1}", value=self.Left[i], inline=True)
        embed.add_field(name='↑ 곧 올라올거 / 최근 추가된거 ↓', value='​', inline=False)
        for i in range(1, 5+1):
            embed.add_field(name=f"#{i+1}", value=self.Left[-i], inline=True)
        
        await ctx.send(embed=embed)

    @commands.command(name='추가')
    @commands.has_permissions(administrator=True)
    async def CMD_Add(self, ctx: commands.Context, *user):
        try:
            user: discord.User = await self.UserConverter.convert(ctx, ' '.join(user))
            self.Left.append(user.mention)
            await self.LogChannel.send(f"New Record Request - from {user.mention}, now left: {len(self.Left)}")
        except (commands.errors.BadArgument, commands.errors.CommandError):
            self.Left.append('Unknown: 관리자가 추가한 값입니다')
            await self.LogChannel.send(f"New Record Request - from Unknown, now left: {len(self.Left)}")
        await ctx.message.add_reaction('👌')
    
    @commands.command(name='삭제', aliases=['제거'])
    @commands.has_permissions(administrator=True)
    async def CMD_Delete(self, ctx: commands.Context):
        mention = self.Left.pop()
        await self.LogChannel.send(f"Deleted Record Request - from {mention}, now left: {len(self.Left)}")
        await ctx.message.add_reaction('👌')

def setup(bot: commands.Bot):
    bot.add_cog(CmdCog(bot))