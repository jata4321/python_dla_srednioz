import os


def file_read(path):
    with open(path, 'r') as f:
        file_content = f.read()
        words = file_content.split(' ')
        number_words = len(words)
    return number_words


my_path = r'.\data\newfile.txt'

if os.path.exists(my_path):
    my_output = file_read(path=my_path)
    print(my_output)
else:
    print(f'File {my_path} is not existing.')

# another approach to the problem above - less readable but short
os.path.exists(my_path) and print(file_read(my_path))
