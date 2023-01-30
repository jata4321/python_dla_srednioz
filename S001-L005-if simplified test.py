import os
from urllib import request

pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

data_dir = os.getcwd()

for page in pages:
    path = f'{data_dir}\\{page["name"]}.html'
    try:
        request.urlretrieve(page['url'], filename=path)
    except:
        print('This page is non existent.')

print('End of file.')
