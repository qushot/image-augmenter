import sys
import os
from PIL import Image
import tensorflow as tf

# exts.
EXTS = ['png', 'jpg']


def get_images():
    src_path = os.getcwd() + '/src'

    # get all images.
    src_files = os.listdir(src_path)
    image_paths = [image_path(i) for i in src_files if permitted_image(i)]
    images = [Image.open(i) for i in image_paths]

    return images


def image_path(filename):
    return 'src/' + filename


def permitted_image(filename):
    ext = filename.split('.')[-1]
    return ext in EXTS


if __name__ == '__main__':
    print(get_images())