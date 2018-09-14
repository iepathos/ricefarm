#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import subprocess


def pywal_image(image_path):
    cmd = ['wal', '-g', '-i', image_path]
    print(' '.join(cmd))
    subprocess.call(cmd)


def rotate_background(backgrounds_dir):
    background_imgs = [os.path.join(backgrounds_dir, img) for img in os.listdir(backgrounds_dir)]
    pywal_image(random.choice(background_imgs))


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Passing directory containing images to use:  ./rotate_backgrounds.py /path/to/backgrounds_directory')
    else:
        backgrounds_dir_path = sys.argv[1]
        if '~' in backgrounds_dir_path:
            backgrounds_dir_path = os.path.expanduser(backgrounds_dir_path)
        rotate_background(backgrounds_dir_path)
