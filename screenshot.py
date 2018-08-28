#!/bin/env python3

import cv2
import numpy
from PIL import Image
from mss import mss

cropQ = {'top': 166, 'left': 15, 'width': 580, 'height': 200}
cropAone = {'top': 380, 'left': 110, 'width': 375, 'height': 65}
cropAtwo = {'top': 480, 'left': 110, 'width': 375, 'height': 65}
cropAthree = {'top': 580, 'left': 110, 'width': 375, 'height': 65}

sct = mss()

def acquire_image():
    imageQ = sct.grab(cropQ)
    imageAone = sct.grab(cropAone)
    imageAtwo = sct.grab(cropAtwo)
    imageAthree = sct.grab(cropAthree)
    imageQ = numpy.array(imageQ)
    imageAone = numpy.array(imageAone)
    imageAtwo = numpy.array(imageAtwo)
    imageAthree = numpy.array(imageAthree)
    cv2.imwrite('/Users/coltinkifer/desktop/cashShowQ.png', imageQ)
    cv2.imwrite('/Users/coltinkifer/desktop/cashShowAone.png', imageAone)
    cv2.imwrite('/Users/coltinkifer/desktop/cashShowAtwo.png', imageAtwo)
    cv2.imwrite('/Users/coltinkifer/desktop/cashShowAthree.png', imageAthree)
    