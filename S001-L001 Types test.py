a = b = c = 10
print(a, b, c)
print(id(a), id(b), id(c))
a = 20
print(id(a), id(b), id(c))

a = b = c = [1, 2, 3]
print(a, b, c)
print(id(a), id(b), id(c))
a.append(4)
print(a, b, c)
print(id(a), id(b), id(c))

print('-----------------------------')
x = 10
y = 10 + 12345678901234567890 - 12345678901234567890
print(id(x), id(y))

print('-----------------------------')
y = y + 1234567890 - 1234567890
print(id(x), id(y))
