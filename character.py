import math, random
from inventory import Inventory
from config import *

'''
try
except
else
finally
'''
'''
while count > 10:
    if ...:
        break

else
'''

class Character:
    '''doc.... '''
        
    def __init__(self, race = 'Человек'):
        self.name = 'Гость'
        self.race = race
        self.lvl = 1
        self.base_hp = RACES[self.race]['hp']
        self.max_hp = self.hp # Добавляем максимум для расчета полоски
        
        self.base_damage = RACES[self.race]['damage'] # основное
        self.speed = 1
        self.stamina = 1
        self.base_defence = RACES[self.race]['defence']

        self.bonus_damage = 1 
        self.bonus_defence = 1

        self.bags = [] # начальная идея по сумкам, которых больше 1 | len()
        self.inventory_size = 0 # текущее кол-во сумок / можно не использовать, а работать с len()
        self.max_inv = 5 # кол-во сумок
        self.slots = []
        
        # print(self.slots)

    @property
    def damage(self):
        return round((1 + self.lvl/10) * self.base_damage + self.bonus_damage, 2) # 1 + 1/10 -> (1 + lvl/10) base_damage
    #hero.damage
    @property
    def defence(self):
        return round((1 + self.lvl/20) * self.base_defence + self.bonus_defence, 2) # (1 + 1/20) *

    @property
    def hp(self):
        return round((1 + round(self.lvl/15, 2) + 0.015) * self.base_hp, 2)#0.07
    
    def equip_armor(self, armors): # обмундирование полное
        trash = []
        if isinstance(armors, (float, int)) :
                print('Моя твоя не понимать')
        elif len(armors) != 0:
            if isinstance(armors, str):
                armors = [armors]
            for item in armors:
                data_item = info_items(item)[1]
                if not data_item:
                    print(f'предмета {item} нет в наличии')
                    continue
                slot = data_item.get('slot', None) # arm
                need_slots = data_item.get('slot_type', 1) # кол-во слотов , необходимое для экипировки

                if slot not in PARTS: #slot -> строчка, которую пытаемся проверить в словаре
                    print('Сработала защита от Дурака: Данной части тела нет в проекте')
                    print('ERROR 404') 
                    continue
            
                a_n_t_slot = [s for s in self.slots if s['type'] == slot] # все arm
                if len(a_n_t_slot) < need_slots:
                    print(f'данному герою никак не представляется возможным использовать {item}')
                    continue
                free_a_n_t_slot = [f for f in a_n_t_slot if f['content'] == None] # []
                #print(f'free_a_n_t_slot = {free_a_n_t_slot}')
                for i in a_n_t_slot:
                    if len(free_a_n_t_slot) < need_slots: # 0 < 2
                        if i['content'] != None:
                            past_armor = i['content'] #getattr(self.slots['type'], slot) # arm
                            #self.recalck_char() #снять характеристики
                            i['content'] = None                            
                            # вот ТУТ нужен метод добавления в сумку
                            bag = self.show_my_bags()
                            if bag: # ПОДУМАТЬ БЫ НАД ЭТИМ
                                bag.add_item(past_armor)
                            else:
                                trash.append(past_armor) # если нет inventory ПОДУМАТЬ БЫ НАД ЭТИМ
                            free_a_n_t_slot.append(i)
                    else:
                        if i in free_a_n_t_slot: #if i['content'] is None:
                            i['content'] = item
                            #self.recalck_char()
                            print(f'{item} экипировано')
                            free_a_n_t_slot.pop()
                            #print(f'free_a_n_t_slot = {free_a_n_t_slot}')
                            break
        self.recalck_char()
                        
    def unequip(self, target: str): # target может быть и рукой, и предметом
        print(f">>> Попытка {'оголить' if target in PARTS else 'снять'} {target} <<<") 

        trash = []
        for slot in self.slots:
            if slot.get('type') == target or slot.get('content') == target: #сработает, если target — рука                
                trash.append(slot['content'])
                slot['content'] = None
                self.recalck_char()
                print('Успех')
                break
            
    def recalck_char(self):
        self.bonus_damage = 0
        self.bonus_defence = 0

        for slot in self.slots:
            if item:= slot.get('content'):        
                damage_data_w = WEAPON.get(item, {}).get('damage', 0)
                defence_data_w = WEAPON.get(item, {}).get('defence', 0)
                damage_data_a = ARMOR.get(item, {}).get('damage', 0)
                defence_data_a = ARMOR.get(item, {}).get('defence', 0)
                if not damage_data_w and not defence_data_a:
                    print(f'Что-то пошло не так. item ={item} не найден')
                self.bonus_damage += damage_data_w + damage_data_a
                self.bonus_defence += defence_data_w + defence_data_a
        #print('Что же происходит')

    def add_bag (self, view): # view -> str, 'Паучья сумка'
        if view in BAGS:
            bag_size = BAGS[view]['size_own']
            if len(self.bags) + bag_size <= self.max_inv:
                inv = Inventory(view)
                inv.owner = self.name
                self.bags.append(inv) # self.bags.remove('Паучья сумка')
                print(F'{[i.view for i in self.bags]}')
                self.inventory_size += 1
                
    def show_my_bags(self, *found_items): # := set, *found_items = () + yield
        # frozenset()
        # complex() 

        if len(self.bags)>0:
            if not found_items:
                a = range(1, len(self.bags)+1)
                for i in a:
                    print(f'{i}. {self.bags[i-1].name}. В данной сумке свободного места: {self.bags[i-1].size - self.bags[i-1].show_param()} ')
    
                choice = input('Выберите номер сумки: ').replace(' ', '') #                  1           2   .strip() = '1           2'
                if choice.isdigit() and int(choice) in a:
                    yield self.bags[int(choice)-1], None, None #.items    у меня есть сомнение, что надо скрывать items
            else:
                # отсортировать сумки
                found_bags = {}
                print(found_items, type(found_items))
                found_items = frozenset(found_items)
                #print(found_bags)
                for i in self.bags: # [obj1, obj2] obj1
                    if matches:=[b for b in i.items if b in found_items]:
                        matches = frozenset(matches)
                        if matches in found_bags:
                            found_bags[matches].append(self.bags.index(i))
                        else:
                            found_bags[matches] = [self.bags.index(i)]
                print(f' это найденные сумки: {found_bags}')
                # print()
                if len(found_bags)>0:
                    print('упс')
                    for i in found_bags:
                        for ind in found_bags[i]:
                            yield ind+1, self.bags[ind].name, ', '.join(item for item in i)
                            # print()
                            # print(f"{ind+1}.{self.bags[ind].name} хранит внутри себя искомые предметы: {', '.join(item for item in i)}")
                else:
                    print('хорошо')
                    yield False, False, False
                #                              #                  1             .split() = [' ', ' ','1']
        yield False, False, False                                                        #                  1           2   .replace('Авада Кедавра', '') = '12'
    

    def game_char(self, race=None, prof=None):

    #  RACES = {
    #     'Эльф':    {'hp': 40,  
    #                 'damage': 12, 
    #                 'defence': 2,
    #                 'limbs': {
    #                     'arm': 2,    # для оружия
    #                     'head': 1,   # для шлемов
    #                     'body': 1,   # для нагрудников
    #                     'legs': 1 }   # для поножей/сапог
    #     }}
    # PROFS = {
    #     "Новичок" : {'hp_mod': 0.5, 'dmg_mod': 0.5},
    #     'Лучник': {'hp_mod': 1.1, 'dmg_mod': 1.5},
    #     'Воин':   {'hp_mod': 1.5, 'dmg_mod': 1.1, 'def_mod': 2}
       
        # начислить х-тики, зависящие от race и prof

        self.name_race = race if race in RACES else random.choice(list(RACES.keys()))#RACES.get(race, random.choice(RACES.keys()))
        self.name_prof = prof if prof in PROFS else random.choice(list(PROFS.keys()))#PROFS.get(prof, random.choice(PROFS.keys()))
        char_race = RACES[self.name_race]
        char_prof = PROFS[self.name_prof]

        bonus = 0
        # if self.name_race == 'Эльф' and self.name_prof == 'Лучник':
        #     bonus = 7
        
        match [self.name_race, self.name_prof]:
            case ['Эльф', 'Лучник']:
                bonus = 7
                print('Уху, ты выбрал хорошую комбинацию')
            
            
        self.base_hp = char_race.get('hp', 1) * char_prof.get('hp_mod', 1) + bonus
        self.base_damage = char_race.get('damage', 1) * char_prof.get('dmg_mod', 1) + bonus
        self.base_defence = char_race.get('defence', 1) * char_prof.get('def_mod', 1) + bonus

        self.max_hp = self.hp

        stats = RACES[self.name_race]
        for part_type, count in stats['limbs'].items():
            for _ in range(count):
                self.slots.append({
                    'type': part_type, 
                    'content': None , # Сюда будем класть название предмета или его данные
                    'important': 1 if count==1 else 0,
                    'урон на будущее': 0
                })
        print(self.name_race, self.name_prof)
        
    def fight(self, t):
        actuall_damage = self.damage - t.defence
        if actuall_damage <0:
            actuall_damage = 0
        t.base_hp -= actuall_damage
        t.base_hp = round(t.base_hp, 2)
        
        print(f'{self.name} нанёс урон {t.name} в размере {actuall_damage}. У него осталось {t.hp if t.hp>0 else 0}')
    
    def get_hp_bar(self):
        bar_length = 10
        # Ограничиваем, чтобы не было отрицательных значений
        current_hp = max(0, self.hp)
        filled_units = math.ceil((current_hp / max(self.max_hp, 1)) * bar_length)

        
        color = GREEN if current_hp > (self.max_hp / 2) else RED
        bar = color + '█' * filled_units + END + '-' * (bar_length - filled_units)
        return f"[{bar}] {color}{current_hp}{END}/{self.max_hp}"
    
    def load_characters(self, data:dict):
        for i in ['name', 'lvl', 'exp', 'max_hp','base_damage', 'base_defence', 'base_hp', 'slots']:
            if i in data:
                setattr(self, i, data[i]) # hero.i = data[i]
        if data.get('bags'):#'bags' in data and len(data['bafs'])>0:
            for i in data['bags']:
                # print(f'i = {i}')
                # print(f"data['bags'] = {data['bags']}, {data['bags'][0]}")
                
                inv = Inventory(i[0])
                for j, k in enumerate(['hp', 'size', 'name', 'owner', 'items', '_current_size']):
                    setattr(inv, k, i[j+1])# ПРОДУМАТЬ, КАК ВЫТАЩИТЬ ИНФУ ПО ИНДЕКСАМ
                self.bags.append(inv)
            print(F'{[i.view for i in self.bags]}')
    
    def __str__(self):
        # Теперь __str__ просто вызывает метод выше!
        return f"""
{'-'*30}
[ {self.name.upper()} ] Lvl: {self.lvl} | {self.prof}
HP: {self.get_hp_bar()}
ATK: {self.damage} | DEF: {self.defence}
{'-'*30}"""
