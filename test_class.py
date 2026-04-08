from hero import Hero
from enemy import Enemy
from config import LOCATION
import time
from json import JSONDecodeError
from save_game import save_json, load_json

try:
    data = load_json('save.json')
    #print(data)
    hero = Hero()
    hero.load_characters(data['info_hero'])
    # hero.name = data["info_hero"]['name']
    #print(hero.name)
    
    # hero.game_char(data["info_hero"]['race'])
except (FileNotFoundError, JSONDecodeError):
    print('Сохранений не найдено')
    name = input('Как зовут тебя, путник? ').strip().title()
    if len(name) >0:
        hero = Hero()
        hero.name=name
    else:
        hero = Hero()
    hero.game_char()

#молвить = print

# print(hero.slots)
hero.add_bag('Паучья сумка')
for i in hero.bags:
    i.add_item('Костяной шип')

#hero.bags[2].add_item('Молодильное яблочко')
print(hero.show_my_bags('Молодильное яблочко', 'Молодильное яблочко', 'Костяной шип' ))
save_json(hero)

enemy = Enemy()
enemy.name = 'Паук'
print('Информация о враге')
print(enemy)
#help(Character)
loc = list(LOCATION.keys())
start= True
count = 0

while start:
    count += 1

    if hero.hp > 0 and enemy.hp>0:
        if count %2 == 0:
            print(f"Враг: {enemy.get_hp_bar()}")
            hero.fight(enemy)
            print(f"Враг: {enemy.get_hp_bar()}")
            time.sleep(1)
            print()
        else:
            print(f"Герой: {hero.get_hp_bar()}")
            enemy.fight(hero)
            print(f"Герой: {hero.get_hp_bar()}")
            time.sleep(1)
            print()
    else:
        start = False
else:
    print('Бой окончен!')
   


