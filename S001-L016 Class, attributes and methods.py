class Cake:
    def __init__(self, name, kind, taste, additives, filling, gluten_free=False):
        self._Cake__gluten_free = None
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additive = additives
        self.filling = filling
        self.__gluten_free = gluten_free

    def show_info(self):
        return print(f'{str.upper(self.name)}, {self.taste}, {self.filling}, {self.__gluten_free}')

    def set_filling(self, new_filling):
        self.filling = new_filling
        return self.filling


cake_01 = Cake('Brownie', 'muss', 'sweet', 'milk', 'none', True)
cake_02 = Cake('Cheesecake', 'cake', 'v. sweet', ['cheese', 'resins'], 'none')
cake_03 = Cake('Vanilla cake', 'cake', 'vanilla', 'nuts', 'cream')

list_of_cakes = [cake_01, cake_02, cake_03]

print('Today in our offer:')
for cake in list_of_cakes:
    print(
        f'{cake.name} - ({cake.kind}) main taste: {cake.taste}, additives: {cake.additive}, '
        f'filled with {cake.filling}. Gluten free? {cake._Cake__gluten_free}.')

cake_01.show_info()
cake_01.set_filling('white-chocolate')
cake_01.show_info()

print(dir(cake_03))
setattr(cake_01, '_Cake__gluten_free', False)
cake_01.show_info()

cake_01._Cake__gluten_free = True
cake_01.show_info()