def CreateFunc(kind='+'):
    source = '''
def func(*args):
    result = 0
    for arg in args:
        result {}= arg
    return result
'''.format(kind)
    exec(source, globals())
    return func


f_sub = CreateFunc('+')
print(f_sub(1, 2, 1))
