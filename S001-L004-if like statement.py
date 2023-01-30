import os

mypath = r'.\data\mydata.txt'

if os.path.isfile(mypath):
    print('File %s already exist' % mypath)
else:
    print('File %s not yet exist' % mypath)

os.path.exists(mypath) or open(mypath, 'x', encoding='utf-8').close()
