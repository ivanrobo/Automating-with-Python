#!/usr/bin/env python3
import requests
import os


def upload_description(path, url):
    p = {}
    for file in filter(lambda x: x.endswith(".txt"), os.listdir(path)):
        with open(os.path.join(path, file), 'r') as f:
            p["name"] = f.readline().strip()
            p["weight"] = int(f.readline().strip("\n lbs"))
            p["description"] = f.readline().strip()
            p["image_name"] = file.replace(".txt", ".jpeg")
            response = requests.post(url, json=p)
            response.raise_for_status()


if __name__ == '__main__':
    path = "supplier-data/descriptions"
    url = ""
    upload_description(path, url)
