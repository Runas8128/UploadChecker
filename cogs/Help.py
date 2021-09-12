from Common import *

class HelpCog(commands.Cog):
    HelpEmbed: discord.Embed

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        self.HelpEmbed = discord.Embed(
            title='도움말',
            description='대충 도움말이에요'
        )
        self.HelpEmbed.add_field(
            name='!밀린양',
            value='`!밀린양`으로 볼 수 있습니다. 지금까지 밀린 양을 보여줍니다.\n~~님이 몇번째인지는 모름~~', inline=False
        )
        self.HelpEmbed.add_field(
            name='!추가 (멘션, 여러개 가능), !삭제 (위치)',
            value='대기 리스트에 적당히 추가하거나 제거해요. 관리자 전용이에요', inline=False
        )
        self.HelpEmbed.add_field(
            name='!일괄추가/!앞에추가 (UID, 여러개 가능)',
            value='일괄 추가는 아이디로 맨 뒤에 추가하려고 만들었고, 앞에추가는 리스트 맨 앞에 추가해줘요. 관리자 전용이에요.', inline=False
        )
        self.HelpEmbed.add_field(
            name='!도움말', 
            value='이걸 보여줘요', inline=False
        )
        self.HelpEmbed.add_field(
            name='!딜레이, !지연시간',
            value='지금 메시지 보내는데 걸리는 시간을 보여줍니다.', inline=False
        )
        self.HelpEmbed.add_field(
            name='!코드보기',
            value='지금 이 코드를 보여줍니다. ~~이걸 쓸 사람이 있을까?~~', inline=False
        )

    @commands.command(name="도움말")
    async def Help(self, ctx: commands.Context):
        await ctx.send(embed=self.HelpEmbed)

def setup(bot: commands.Bot):
    bot.add_cog(HelpCog(bot))