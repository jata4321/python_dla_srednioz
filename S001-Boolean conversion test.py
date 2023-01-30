mylist = ['load data', 'export data', 'analyze & predict']
myNlist = []

for i, item in enumerate(mylist):
    myNlist.append(int(i))
    print(i, ' - ', item)

answer = 0

while answer in mylist or myNlist:
    answer = input('Input choice or press Enter to exit: ')
    print('You have selected: ', answer)
    print(type(answer))
    if answer == '':
        break
