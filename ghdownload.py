import requests
import os

def download_gh():
    base_url = 'https://data.gharchive.org/2015-01-01-{}.json.gz'
    res = requests.get(base_url.format(10))
    f = open('2015-01-01-10.json.gz','wb')
    f.write(res.content)
    os_path = os.path.abspath('2015-01-01-10.json.gz')
    f.close()
    return os_path