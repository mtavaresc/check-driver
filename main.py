from glob import glob
from os import path, remove, getcwd
from platform import system
from time import sleep
from zipfile import ZipFile

from requests import get


def download_file(url):
    local_filename = url.split('/')[-1]
    r = get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return local_filename


def unzip(filezip):
    with ZipFile(filezip, 'r') as zip_ref:
        zip_ref.extractall(getcwd())

    remove(path.join(getcwd(), filezip))


def check_driver():
    systems = {'Darwin': 'mac64', 'Linux': 'linux64', 'Windows': 'win32'}
    os = systems[system()]
    base_url = 'https://chromedriver.storage.googleapis.com'

    if not glob('chromedriver*'):
        lr = get('{url}/LATEST_RELEASE'.format(url=base_url))
        last_version = lr.text
        download_file('{url}/{lv}/chromedriver_{os}.zip'.format(url=base_url, lv=last_version, os=os))
        sleep(5)
        unzip('chromedriver_{}.zip'.format(os))


if __name__ == '__main__':
    check_driver()
