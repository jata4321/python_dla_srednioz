import requests
import os
import functools


def save_url_file(dir, msg, file, url):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


dir_temp = 'c:/temp/'
msg = "Please wait - the file {} will be downloaded"

short_save_url_file = functools.partial(save_url_file, dir_temp, msg)

file = 'spis.html'
url = 'http://mobilo24.eu/spis'

# save_url_file(dir_temp, msg, file, url)
short_save_url_file(file, url)
file = 'logo.png'
url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
# save_url_file(dir_temp, msg, file, url)

short_save_url_file(file, url)
