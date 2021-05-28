#!/usr/bin/env python3
from PIL import Image
import os


def format_images(path, size, ext):
    for image in filter(lambda x: x.endswith(".tiff"), os.listdir(path)):
        with Image.open(os.path.join(path,image)) as im:
            im = im.resize(size).convert('RGB')
            im.save(os.path.join(path, image.replace(".tiff", "." + ext)), ext)


if __name__ == '__main__':
    format_images(path="supplier-data/images",
                  size=(600, 400),
                  ext="jpeg")
