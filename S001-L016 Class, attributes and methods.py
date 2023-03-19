import pickle
import csv
import os
import glob

kind_of_cake = 'cake'


class Cake:
    def __init__(self, name, kind, taste, additives, filling, text, gluten_free=False):
        self._Cake__gluten_free = None
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additive = additives
        self.filling = filling
        self.__text = text
        self.__gluten_free = gluten_free

    def show_info(self):
        return print(f'{str.upper(self.name)}, {self.taste}, {self.filling}, {self.__gluten_free}')

    def set_filling(self, new_filling):
        self.filling = new_filling
        return self.filling

    def get_text(self):
        return self.__text

    def set_text(self, new_text):
        if kind_of_cake == 'cake':
            self.__text = new_text
            print('Status changed')
        else:
            print('Status unchanged')

    @property
    def text(self):
        return print(f'New text on cake is set to "{self.__text}"')

    @text.setter
    def text(self, new_text):
        self.__text = new_text

    change_text = property(get_text, set_text, None)

    def save_to_file(self, path, filename, ext='.bks'):
        file_path = os.path.join(path, filename + ext)
        with open(file_path, 'wb+') as f:
            pickle.dump(self, f)

    def export_to_csv(self, path, filename, ext='.csv'):
        file_path = os.path.join(path, filename+ext)
        with open(file_path, 'w+') as f:
            cursor = csv.writer(f, delimiter=',')
            cursor.writerow([self.name, self.filling, self.taste])
            print('Data export success!')

    @classmethod
    def read_from_file(cls, path, filename, ext='.bks'):
        file_path = os.path.join(path, filename + ext)
        with open(file_path, 'rb+') as f:
            loaded_cake = pickle.load(f)
        return loaded_cake

    @staticmethod
    def list_picked_cakes(path, ext='.bks'):
        file_path = os.path.join(path + '*' + ext)
        cake_list = glob.glob(file_path)
        return cake_list


cake_01 = Cake('Brownie', 'muss', 'sweet', 'milk', 'none', True, 'Hi')
cake_02 = Cake('Cheesecake', 'cake', 'v. sweet', ['cheese', 'resins'], 'none', 'Hi ho!')
cake_03 = Cake('Vanilla cake', 'cake', 'vanilla', 'nuts', '', 'cream')

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

print(cake_02.change_text)
cake_02.change_text = 'Happy birthday!'
print(cake_02.change_text)

# this line was changed due to different operating system switch. Linux versus Windows.
cake_02.save_to_file('./', 'cake_02')
caked = Cake.read_from_file('./', 'cake_02')

print('Pickled cake is:')
caked.show_info()

print('List of files:')
print(*Cake.list_picked_cakes('./'))  # This line was also changed under Linux OS. Should be reverted under Windows.

cake_02.text = "bla bla"
cake_02.text

cake_01.export_to_csv('./', 'cake_text')
print(dir(Cake))
