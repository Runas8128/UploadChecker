from Common import *

class EventCog(commands.Cog):
    LogChannel: discord.TextChannel
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
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
            activity=discord.Game("!λμλ§")
        )

        self.LogChannel = self.bot.get_channel(881882849316323370)

        print('ready')
    
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author.bot:
            return

        if msg.channel.id == 853948758177087498 and self.isRequest(msg):
            if msg.reference == None:
                manager.add(msg.author.id)
                await self.LogChannel.send(f"New Record Request - from {msg.author.mention}, now left: {len(self.Left)}")
                await msg.add_reaction('π')
            else:
                await self.LogChannel.send(f"Record Edit Request - from {msg.author.mention}, now left: {len(self.Left)}")
                await msg.add_reaction('π')
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandNotFound):
            return
        
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('κ΄λ¦¬μ κΆν λͺλ Ήμ΄μλλ€!')
        
        elif isinstance(error, commands.NotOwner):
            await ctx.send('κ°λ°μ μ μ© λͺλ Ήμ΄μλλ€! ~~μμλ~~')

        else:
            await self.bot.get_channel(863719856061939723).send(error)
            await ctx.send('μ μ μ€λ₯κ° λ¬μ΄μ! κ°λ°μνν μ€λ₯ λ΄μ©μ λ³΄λ΄λ¨μΌλ, μ μ κΈ°λ€λ €μ£ΌμΈμ!\n~~μμμ μ°Ύκ² μ§ λ­~~')

    @tasks.loop(hours=1)
    async def Loop_Check(self):
        if now().hour == 12:
            uid = manager.pop(0)
            user = self.bot.get_user(uid)
            if user:
                await self.LogChannel.send(f"Deleted Record Request - from {user.display_name}, now left: {len(manager.Left)}")
            elif uid:
                await self.LogChannel.send(f"Deleted Record Request - from user id {uid}, now left: {len(manager.Left)}")
    
def setup(bot: commands.Bot):
    bot.add_cog(EventCog(bot))