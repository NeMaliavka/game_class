from config import BAGS, info_items  

class Inventory:
    #BAGS ={}

    def __init__(self, view): #view — это ТИП нашей сумки-> str
        self.view = view
        self.hp = BAGS[view]['hp'] + BAGS[view]['material']['hp']
        self.size = BAGS[view]['size'] #20
        self._current_size = 0 #занятые слоты
        self.name = 'Супер-пупер сумка'
        self.owner = None
        self.items = []

    def load_for_list(self):
        info_bags = [getattr(self, i) for i in ['view', 'hp', 'size', 'name', 'owner', 'items', '_current_size']]
        return info_bags
    
    def show_param(self):
        # получить инфу о параметрах gettatr('size')
        return self._current_size
    
    def set_current_size(self, value:int, add:bool = True): # add not class bool
        if isinstance(value, int) and (0 < value <= (self.size - self._current_size)) and isinstance(add, bool):
            if add:
                self._current_size += value
                return True
            else:
                self._current_size -= value
                return True            
            
        else:
            print('НЕЛЬЗЯ: value должно числом и должно быть свободное место')
            return False 

    def add_item(self, item):
        data_item = info_items(item)[1] # {} или None
        print(data_item)
        # if item in 
        if not data_item: # если что-то вернулось, то эта проверка не пройдёт
            print(':(')
            return False
        if self._current_size < self.size:
            res = self.set_current_size(data_item.get('size_own'))
            print(res, self._current_size)
            if res:
                self.items.append(item)
                print(f'Предмет {item} успешно добавлен')
            else:
                pass
        else:
            print('Сумка и так уже забита предметами')

    def remove_item(self, item):
        if isinstance(item, str):
            if item in self.items:
                self.items.remove(item)
                self.set_current_size(add=False, value=1)
                print('Всё получилось')
            else:
                print('Такого предмета НЕТ в ТВОЕЙ сумке, или вообще в игре!')
        else:
            print(f'А что это такое {item}? Я не знаю такого предмета')

    def get_item(self, item):
        if isinstance(item, str):
            if item in self.items:
                # get_i = self.items.pop(self.items.index(item))
                index = self.items.index(item)
                new_value_for_save_item = self.items[index]
                # del self.items[index]
                self.remove_item(item)
                print('полезная инфа')
                return new_value_for_save_item
            else:
                return False
        else:
            print(f'А что это такое {item}? Я не знаю такого предмета')
            return False
        
    def show_items(self):
        print(f"Сейчас в твоей сумке: {', '.join(self.items) if len(self.items)>0  else 'пусто' }") # self.items = ['меч', 'лошадь', 'топор'] -> меч, лошадь, топор

    # def __del__(self):
    #     print(f"\n{self.name} покидает этот мир... Его приключения окончены.")
    #     # как удалить объект полностью 


if '__main__' == __name__:
    print(__name__)
    i = Inventory('Паучья сумка')
    i.add_item('яблочко')
    # d = i
    # print(i)
    # del i 
    # # print(d)
    # o = object()
    # print(o)

    