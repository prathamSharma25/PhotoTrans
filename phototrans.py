# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:28:37 2020

@author: Pratham
"""

"""
Main script to integrate functions from each of the three python scripts, 
'ocr_engine.py', 'preprocessing.py' and 'translate.py'.

This script makes use of 'ocr_core' function defined in the python script 
'ocr_engine.py' to extract text from image uploaded by user.

This script also utilises various image pre-processing functions defined in the
python script 'preprocessing.py'. Required function(s) are imported.

Text detected from the given image is passed onto the translation functions 
defined in the python script 'translate.py'. Text is translated by default to 
the English language.

Other required libraries are:
    1) PIL.Image - to read image file
    2) langdetect.detect - to detect language of original text extracted
"""

try:
    from PIL import Image
except ImportError:
    import PIL.Image
from ocr_engine import ocr_core
from preprocessing import preprocess
from translate import translator
from langdetect import detect

def photo_translate(image_file):
    # image_file = preprocess(image_file)
    text = ocr_core(Image.open(image_file))
    trans_text = translator(text)
    return ''.join(('  ', text, ' (' + detect(text) + ') ', ' --> ', trans_text, ' (en)'))
