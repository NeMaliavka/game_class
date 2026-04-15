from character import Character
from config import GOLD, RESET, FOOD

class Hero(Character):
    def __init__(self):
        super().__init__()
       
        self.exp = 0
        self.bonus_damage += 5

    def fight(self,t):  
        flag = False 
        if self.hp <= 390 and self.bags:
            # вместо хода будем лечиться
            all_food = set()
            best_food = ''
            for i, b, s in self.show_my_bags(*FOOD.keys()):
                if not i:
                    continue
                else:
                    s = set(s.split(', '))
                    all_food.update(s)
                    flag = True
            if flag:
                # решили создать словарь с имеющейся едой и уже его подвернуть сортировке
                # решили создать словарь с имеющейся едой и уже его подвернуть сортировке
                return       

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