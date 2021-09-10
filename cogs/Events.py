from typing import List
from Common import *

class EventCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.Left: List[int] = toGen(db['Left'])

    def isRequest(self, message: discord.Message):
        if 'https://drive.google.com/file/d/' in message.content:
            return True

        atts = message.attachments
        if len(atts) == 0:
            return False
        else:
            return ('.zip' in atts[0].filename) or ('.adofai' in atts[0].filename)

    @commands.Cog.listener()
    async def on_ready(self):
        self.Loop_Check.start()
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game("!도움말")
        )
        self.LogChannel = self.bot.get_channel(881882849316323370)

        print('ready')
    
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author.bot:
            return

        if msg.channel.id == 853948758177087498 and self.isRequest(msg):
            if msg.reference == None:
                self.Left.append(msg.author.mention)
                await self.LogChannel.send(f"New Record Request - from {msg.author.mention}, now left: {len(self.Left)}")
                await msg.add_reaction('👌')
            else:
                await self.LogChannel.send(f"Record Edit Request - from {msg.author.mention}, now left: {len(self.Left)}")
                await msg.add_reaction('👍')
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandNotFound):
            return
        
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('관리자 권한 명령어입니다!')
        
        elif isinstance(error, commands.NotOwner):
            await ctx.send('개발자 전용 명령어입니다! ~~있었나~~')

        else:
            await self.bot.get_channel(863719856061939723).send(error)
            await ctx.send('잠시 오류가 났어요! 개발자한테 오류 내용을 보내놨으니, 잠시 기다려주세요!\n~~알아서 찾겠지 뭐~~')

    @tasks.loop(hours=1)
    async def Loop_Check(self):
        db['Left'] = self.Left
        if now().hour == 12:
            mention = self.Left.pop()
            await self.LogChannel.send(f"Deleted Record Request - from {mention}, now left: {len(self.Left)}")