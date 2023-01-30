list = [1, 2, 3]
print('Variable list', list, id(list))
list.append(4)

list2 = list
print('Variable list', list, id(list))
print('Variable list2', list2, id(list2))

list2.append(5)
print('Variable list', list, id(list))
print('Variable list2', list2, id(list2))

list3 = list.copy()
list3.append(6)
print('Variable list', list, id(list))
print('Variable list3', list3, id(list3))
