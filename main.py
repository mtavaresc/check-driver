import requests
import zipfile
import os


def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return local_filename


def unzip(filezip):
    folder = os.getcwd()
    with zipfile.ZipFile(filezip, "r") as zip_ref:
        zip_ref.extractall(folder)

    os.remove(r"{}\{}".format(folder, filezip))


def chromedriver():
    if not os.path.exists("chromedriver.exe"):
        lr = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
        last_version = lr.text
        download_file("https://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip".format(last_version))
        unzip("chromedriver_win32.zip")
