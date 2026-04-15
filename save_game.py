import json

def save_json(hero, list_enemy = None):
    table_load = {
        'info_hero':{'name': hero.name,
                     'base_hp': hero.base_hp,
                     'max_hp': hero.max_hp,
                     'slots': hero.slots,
                     'base_damage': hero.base_damage,
                     'base_defence': hero.base_defence,
                     'inventory_size': hero.inventory_size,
                     'bags': [i.load_for_list() for i in hero.bags]
                    #  'parts': [slot['type'] for slot in hero.slots],
                    #  'equip': [slot['content'] for slot in hero.slots],
                    #  'parts_important': [slot['important'] for slot in hero.slots]
                     }
    }

    if list_enemy:
        # list_enemy — список объектов
        table_load['battle'] = True
        table_load['info_enemy'] = []
        for e in list_enemy:
            table_load['info_enemy'].append({
                'base_hp': e.base_hp
            })
    
    with open('save.json', 'w', encoding='utf-8') as file_json:
        json.dump(table_load, file_json, ensure_ascii=False, indent=4)
        # s = json.dumps(table_load, ensure_ascii=False)
        # print(s)



def load_json(file_name='save.json'):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data 
