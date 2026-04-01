from character import Character
from config import PURPLE, RESET, LOCATION, RACES
import random

class Enemy(Character):
    def __init__(self, info_location='Тёмный лес'):
        super().__init__()
        self.race = random.choice(LOCATION[info_location][2])
        self.base_hp = RACES[self.race]['hp']
        self.base_damage = RACES[self.race]['damage']
        self.base_defence = RACES[self.race]['defence']

    #@property
    def level(self):
        rnd = random.randint(1, 100)
        if rnd <= 10:
            self.lvl = random.randint(LOCATION['Тёмный лес'][-1][-2], LOCATION['Тёмный лес'][-1][-1])
        else:
            self.lvl = random.randint(LOCATION['Тёмный лес'][-1][0], LOCATION['Тёмный лес'][-1][1])


    def fight(self,t):
        if self.name == 'Паук':
            t.base_hp -= self.damage # - defence_for_spider
            # механика начисления урона от яда
            print(f'{self.name} Нанёс урон {t.name} В размере {self.damage}, у него осталось {t.hp}')
        else:
           super().fight(t)

    def __str__(self):
        # Подсвечиваем имя противно сиреневым
        name_tag = f"{PURPLE}{self.name.upper()}{RESET}"
        visual = " /\\(o0o)/\\ " if self.name == 'Паук' else " [Монстр] "
        
        return f"""
👾 ВРАГ ЗАМЕЧЕН! 👾 {visual}
{'-'*30}
[ {name_tag} ] Lvl: {self.lvl}
HP: {self.get_hp_bar()}
ATK: {self.damage} | DEF: {self.defence}
{'-'*30}"""


if __name__ == '__main__':
    e = Enemy()
    e.rnd_lvl()