import os, random
# Специальный фикс для Windows, чтобы работали цвета

if os.name == 'nt':
    os.system('color')

GOLD = "\033[93m"
PURPLE = "\033[95m"
RESET = "\033[0m"
        
GREEN = "\033[92m"
RED = "\033[91m"
END = "\033[0m"

PARTS = ('arm', 'head', 'body', 'legs', 'tail') # arms и arm

RACES = {
    'Эльф':    {'hp': 40,  
                'damage': 12, 
                'defence': 2,
                'limbs': {
                    'arm': 2,    # для оружия
                    'head': 1,   # для шлемов
                    'body': 1,   # для нагрудников
                    'legs': 1 }   # для поножей/сапог
    },
    'Человек': {'hp': 60,  
                'damage': 8,  
                'defence': 5,
                'limbs': {
                    'arm': 2,    # для оружия
                    'head': 1,   # для шлемов
                    'body': 1,   # для нагрудников
                    'legs': 1 }   # для поножей/сапог
    },
    'Орк':     {'hp': 100, 
                'damage': 15, 
                'defence': 1,
                'limbs': {
                    'arm': 2,    # для оружия
                    'head': 1,   # для шлемов
                    'body': 1,   # для нагрудников
                    'legs': 1 }   # для поножей/сапог
    },
    'Ящеролюд':    {'hp': 70,  
                'damage': 14, 
                'defence': 2,
                'limbs': {
                    'arm': 2,    # для оружия
                    'head': 1,   # для шлемов
                    'body': 1,   # для нагрудников
                    'legs': 1 ,
                    'tail': 1}   # для поножей/сапог
    },
    'Великан':    {'hp': 240,  
                'damage': 17, 
                'defence': 7,
                'limbs': {
                    'arm': 4,    # для оружия
                    'head': 1,   # для шлемов
                    'body': 1,   # для нагрудников
                    'legs': 1 }   # для поножей/сапог
    },

}
PROFS = {
    "Новичок" : {'hp_mod': 0.5, 'dmg_mod': 0.5},
    'Лучник': {'hp_mod': 1.1, 'dmg_mod': 1.5},
    'Воин':   {'hp_mod': 1.5, 'dmg_mod': 1.1}
}

MATERIALS = {'cotton':{'hp':5,
                        'name':'Хлопок'},
            'leather': {'hp': 10, 'name': 'кожа'},
            'spider_silk': {'hp': 8, 'name': 'паучий шелк'},
            'iron': {'hp': 20, 'name': 'железо'},
            'mythril': {'hp': 150, 'name': 'мифрил'},
            'bone': {'hp': 15, 'name': 'кость'},
            'wood': {'hp': 13, 'name': 'древесина'}}

BAGS = {'Паучья сумка':{'hp':10, 
                        'size': 10, 
                        'material': MATERIALS['cotton'], 
                        'size_own': 1},
        'Кожаная сумка': {
                    'hp': 15,
                    'size': 2,
                    'material': MATERIALS['leather'],
                    'size_own': 1},
        'Бездонный карман': { 
                    'hp': 5,
                    'size': 50,
                    'material': MATERIALS['mythril'],
                    'size_own': 1},
        'Треснутый сундук': {
                    'hp': 20,
                    'size': 25,
                    'material': MATERIALS['wood'],
                    'size_own': 5}}

WEAPON = {'Ржавый кинжал': {
            'damage': 3,
            'durability': 5,
            'material': MATERIALS['iron'],
            'size_own': 1,
            'slot': 'arm',
            'slot_type':1}, # обычный или двуручка
        'Костяной шип': {
            'damage': 5,
            'durability': 4,
            'material': MATERIALS['bone'],
            'size_own': 2,
            'slot': 'tail',
            'slot_type':2},
        'Игольчатая рапира': {
            'damage': 7,
            'durability': 8,
            'material': MATERIALS['iron'],
            'size_own': 2,
            'slot': 'arm',
            'slot_type': 1},
        'Митриловый короткий меч': {
            'damage': 10,
            'durability': 20,
            'material': MATERIALS['mythril'],
            'size_own': 3,
            'slot': 'arm',
            'slot_type': 1}}

ARMOR = {# стартовый набор
        'Простая броня': {
            'defence': 1,
            'durability': 2, #долговечность/прочность брони
            'material': MATERIALS['cotton'],
            'size_own': 1,
            'slot': 'body'},
        'Обычный шлем': {
            'defence': 1,
            'durability': 2, 
            'material': MATERIALS['cotton'],
            'size_own': 1,
            'slot': 'head'},
        'Походные сапоги': {
            'defence': 1,
            'durability': 2, 
            'material': MATERIALS['cotton'],
            'size_own': 1,
            'slot': 'legs'},

        # для дальнейшей игры
        'Тканевый халат': {
            'defence': 1,
            'durability': 4,
            'material': MATERIALS['cotton'],
            'size_own': 3,
            'slot': 'body'},
        'Кожаная куртка': {
            'defence': 3,
            'durability': 8,
            'material': MATERIALS['leather'],
            'size_own': 4,
            'slot': 'body'},
        'Железный шлем': {
            'defence': 2,
            'durability': 10,
            'material': MATERIALS['iron'],
            'size_own': 2,
            'slot': 'head'},
        'Мифриловый жилет': {
            'defence': 6,
            'durability': 25,
            'material': MATERIALS['mythril'],
            'size_own': 3,
            'slot': 'body'},

        'Кожаные поножи': {
            'defence': 2,
            'durability': 7,
            'material': MATERIALS['leather'],
            'size_own': 3,
            'slot': 'legs'}}

FOOD = {'Молодильное яблочко':{
            'hp':15, 
            'size_own':1},
        'Торт': {
            'hp':3, 
            'size_own':1},
        'Сушёное мясо': {
            'hp': 5,
            'size_own': 1},
        'Суп из корней': {
            'hp': 8,
            'size_own': 2},
        'Подозрительный гриб': {
            'hp': random.randint(-5, 5),
            'size_own': 1},
        'Эльфийский хлеб': {
            'hp': 20,
            'size_own': 1}}

THING = {} # надо заполнить

Labubu = {'Оружие': {'1':1},
            'Еда': {'2': 2}}
Labubu['Оружие'] = {'3': 3} # Labubu = {'Оружие': {'3': 3}}
Labubu['Оружие'].update({'1': 3}) # Labubu = {'Оружие': {'1': 3}}

def info_items(item):
    all_items = {
        'thing': THING,
        'bags': BAGS,
        'food': FOOD,
        'armor': ARMOR,
        'weapon': WEAPON # этой строки не было 
    }

    for category, data in all_items.items():
        if item in data:
            return (category, data[item]) # THING['iron']
    
    return None, None 

LOCATION = {'Тёмный лес': ('описание...',
                           ['Костяной шип', 'Подозрительный гриб'],
                           ['Эльф', 'Ящеролюд'],
                           (0, 0, 0),
                           (1, 3, 100, 300))}# list(range(1, 4))
#index

