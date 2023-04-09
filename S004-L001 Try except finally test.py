from urllib import request
import os
import shutil


url_download = 'http://www.mobilo24.eu/spis/'
directory = 'c:/temp/'
temporary_file = 'download.tmp'
file = 'spis.html'

temp_file_path = os.path.join(directory, temporary_file)
html_file_path = os.path.join(directory, file)


def save_url_to_file(url, temp_file_path):
    with request.urlopen(url) as response:
        body = response.read()
    with open(temp_file_path, "wb") as f:
        f.write(body)


try:
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)

    save_url_to_file(url_download, temp_file_path)

    shutil.copy(temp_file_path, html_file_path)

    x = 1/0

except ConnectionError:
    print('There was an error!')
except FileNotFoundError:
    print('File not found!')
except Exception as e:
    print('General error occured!', str(e).capitalize())
else:
    print('There was no errors pulling data!')
finally:
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
        print(f'File "{temporary_file}" was deleted.')

print('Thank you for using our software.')
