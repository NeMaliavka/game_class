from character import Character
from config import GOLD, RESET, FOOD

class Hero(Character):
    def __init__(self):
        super().__init__()
       
        self.exp = 0
        self.bonus_damage += 5

    def fight(self,t):        
        if self.hp <= 5 and self.bags:
            # вместо хода будем лечиться
            g = self.show_my_bags(self,FOOD.keys())
            if g:
                i, b, s = next(g | ('','',''))
                i-=1
                s = s.split(', ')# s list из str
                # автоматическая подборка лучшей еды из имеющейся | ищем во всех сумках
                set_item = set()
                for item in s:
                    pass
                #sort_s = sorted(s, lambda:)           

        else:
            super().fight(t)

    def __str__(self):
        # Подсвечиваем имя золотым
        name_tag = f"{GOLD}{self.name.upper()}{RESET}"
        return f"""
{'-'*30}
[ {name_tag} ] Lvl: {self.lvl} | {self.prof}
HP: {self.get_hp_bar()}
ATK: {self.damage} | DEF: {self.defence}
{'-'*30}
XP: {self.exp} |"""