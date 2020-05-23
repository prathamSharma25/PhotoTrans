# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:01:05 2020

@author: Pratham
"""

"""
This python script contains functions to perform pre-processing on the 
uploaded image. Attributes of the image such as brightness and constrast are 
adjusted in order to enhance the accuracy of the OCR process.

Three operations, namely grayscaling, thresholding and noise removal are performed.
"""

import cv2

# get grayscale image
def get_grayscale(image_file):
    return cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
# noise removal
def remove_noise(image_file):
    return cv2.medianBlur(image_file,5)
# thresholding
def thresholding(image_file):
    return cv2.threshold(image_file, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# image pre-processing
def preprocess(image_file):
    image_file = get_grayscale(image_file)
    image_file = remove_noise(image_file)
    image_file = thresholding(image_file)
    return image_file
    