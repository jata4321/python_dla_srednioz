import os


class IniFfile:

    def __init__(self, path):
        self.path = path
        self.parameters = {}
        self.read_from_disk()

    def read_from_disk(self):
        try:
            with open(self.path) as file:
                for line in file:
                    parts = line.replace('\n', '').split('=')
                    self.parameters[parts[0]] = parts[1]
        except IOError:
            print('File not found')

    def read_parameters(self, key):
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None

    def write_parameters(self, key, value):
        self.parameters[key] = value

    def save_on_disk(self):
        with open(self.path, 'w') as file:
            for key, value in self.parameters.items():
                line = f'{key}={value}'
                file.writelines(line)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


my_file = r'C:\Users\jakub\Documents\Kursy Udemy\Python dla sredniozaawansowanych\my.txt'
ini1 = IniFfile(my_file)
ini1.write_parameters('klucz', 1)
ini1.save_on_disk()

with IniFfile(my_file) as ini:
    print(ini.parameters['klucz'])
