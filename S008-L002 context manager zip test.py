import os
import zipfile
import requests


class FileFromWeb:
    def __init__(self, url, temp_file):
        self.url = url
        self.temp_file = temp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.temp_file, 'wb') as file:
            response_content = file.write(response.content)
            print(response_content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError or exc_type == KeyError:
            print(exc_type)
            return True
        else:
            return False


web_address = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'
temporary_file = 'c:/temp/euroxref.zip'

with FileFromWeb(web_address, temporary_file) as f:
    with zipfile.ZipFile(f.temp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir("c:/temp")
        z.extract(a_file, '.', None)
