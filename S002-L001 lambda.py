def f(x):
    return len(x)


print(f('a 19-letters string'))

text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

print(list(map(f, text_list)))
print(list(map(lambda s: len(s), text_list)))


f = list(map(lambda x: len(x), text_list))
print(f)
print(list(map(lambda x: len(x), text_list)))
