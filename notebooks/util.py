# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt


def display_image(img, cmap=None, right=None, top=None):

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img, cmap=cmap)
    plt.subplots_adjust(right=right, top=top)
