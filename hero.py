from character import Character
from config import GOLD, RESET

class Hero(Character):
    def __init__(self):
        super().__init__()
       
        self.exp = 0
        self.bonus_damage += 5

    def fight(self,t):        
        if self.hp <= 5 and self.bags:
            # вместо хода будем лечиться
            pass
            

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