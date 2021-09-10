from typing import List
from Common import *

class Manager:
    def __init__(self):
        self.Left: List[int] = toGen(db['Left'])
    
    def add(self, author: discord.User):
        self.Left.append(author.id)
        db['Left'] = self.Left
    
    def pop(self, index:int):
        var = self.Left.pop(index)
        db['Left'] = self.Left
        return var
    
    def get(self, bot: commands.Bot):
        embed = discord.Embed(title="밀린 양 임베드", description="귀찮아서 상위5개 하위5개만 보여드림")
        
        for i in range(0, 4+1):
            embed.add_field(name=f"#{i+1}", value=bot.get_user(self.Left[i]).display_name, inline=True)
        embed.add_field(name='↑ 곧 올라올거 / 최근 추가된거 ↓', value='​', inline=False)
        for i in range(1, 5+1):
            embed.add_field(name=f"#{i+1}", value=bot.get_user(self.Left[-i]).display_name, inline=True)
        
        return embed
    
manager = Manager()