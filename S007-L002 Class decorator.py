import random


class MemoryClass:
    list_of_selected_items = []

    def __init__(self, funct):
        print('>>init MemoryClass')
        self.funct = funct

    def __call__(self, lists):
        print('>>call of MemoryClass')
        items_available = list(set(lists) - set(MemoryClass.list_of_selected_items))
        print('Cars available: ', items_available)
        item = self.funct(items_available)
        MemoryClass.list_of_selected_items.append(item)
        print('Cars on promotion:', MemoryClass.list_of_selected_items)
        return item


cars = ['Opel', 'Toyota', 'Fiat', 'VW', 'Ford']


@MemoryClass
def select_promotion(list_of_cars):
    return random.choice(list_of_cars)


@MemoryClass
def select_display(list_of_cars):
    return random.choice(list_of_cars)


print(select_promotion(cars))
print(select_display(cars))
