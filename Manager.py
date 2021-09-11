from typing import List

import discord
from discord.ext import commands

from replit import db
from replit.database.database import ObservedDict, ObservedList

def toGen(tmp):
    if isinstance(tmp, ObservedList):
        tmp = list(tmp)
        return [toGen(_Elem) for _Elem in tmp]
    elif isinstance(tmp, ObservedDict):
        tmp = dict(tmp)
        return {key: toGen(tmp[key]) for key in tmp}
    else:
        return tmp

class Manager:
    def __init__(self):
        self.Left: List[int] = toGen(db['Left']) if db else []
    
    def add(self, id: int):
        self.Left.append(id)
        db['Left'] = self.Left
    
    def addFront(self, id: int):
        self.Left.insert(0, id)
        db['Left'] = self.Left
    
    def pop(self, index:int):
        try:
            var = self.Left.pop(index)
            db['Left'] = self.Left
            return var
        except IndexError:
            return None
    
    def get(self, bot: commands.Bot):
        embed = discord.Embed(title="밀린 양 임베드", description=f"총 {len(self.Left)}개 남아있어요")
        
        for i in range(0, 4+1):
            user = bot.get_user(self.Left[i])
            embed.add_field(name=f"#{i+1}", value=user.display_name if user else self.Left[i], inline=True)
        embed.add_field(name='↑ 곧 올라올거 / 최근 추가된거 ↓', value='​', inline=False)
        for i in range(1, 5+1):
            user = bot.get_user(self.Left[-i])
            embed.add_field(name=f"#{i}", value=user.display_name if user else self.Left[i], inline=True)
        
        return embed
    
    def clear(self):
        self.List = []
        db['Left'] = self.Left
    
manager = Manager()