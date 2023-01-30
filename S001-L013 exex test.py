import os

path_1 = r'C:\Users\jakub\Documents\Kursy Udemy\Python dla sredniozaawansowanych\sin_squared.txt'
path_2 = r'C:\Users\jakub\Documents\Kursy Udemy\Python dla sredniozaawansowanych\square_root.txt'

print(os.path.basename(path_1))


file = open(path_1, 'r')
source = file.read()
file.close()

exec(source)

with open(path_2, 'r') as f:
    file = f.read()
    print(os.path.basename(path_2))
    exec(file)
