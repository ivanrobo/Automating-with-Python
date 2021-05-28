#!/usr/bin/env python3
import requests
import os


def upload_images(path, url):
    for image in filter(lambda x: x.endswith(".jpeg"), os.listdir(path)):
        with open(os.path.join(path, image), 'rb') as opened:
            response = requests.post(url, files={'file': opened})
            response.raise_for_status()


if __name__ == '__main__':
    path = "supplier-data/images"
    url = ""
    upload_images(path, url)