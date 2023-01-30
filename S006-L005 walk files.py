import os

my_path = r'C:\Users\jakub\Documents'

my_search_string = 'Nugat'
my_extension = '.txt'


# for dir_name, subdir, filenames in os.walk(path):
#     for filename in filenames:
#         if filename.endswith(extension):
#             fullname = os.path.join(dir_name, filename)
#             for line in open(fullname):
#                 if search_string in line:
#                     print(dir_name, filename)


def generate_files(path, extension):
    for dir_name, subdir, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(extension):
                fullname = os.path.join(dir_name, filename)
                yield fullname


def grep_files(search_string, files):
    for file in files:
        with open(file, 'r') as text:
            if search_string in text.read():
                print(search_string)
                yield file


file_gen = generate_files(my_path, my_extension)

for file in grep_files(my_search_string, file_gen):
    print(file)
