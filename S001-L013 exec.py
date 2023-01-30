from time import time, ctime

start_time = time()

source = '''
for i in range(8000):
    zet = i ** i
'''

result = exec(source)

end_time = time()

timer = end_time - start_time

print(zet)
print(timer, ctime(start_time), ctime(end_time))
