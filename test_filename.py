import requests
import os
import json
import gzip
from ghdownload import download_gh

def test_download_gh():
    downloaded_path = download_gh()
    assert os.path.exists(downloaded_path)

    with gzip.open(downloaded_path, 'rt', encoding='utf-8') as f:
        line = f.readline()
        data_json = json.loads(line)
        assert isinstance(data_json, dict)