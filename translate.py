# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:23:12 2020

@author: Pratham
"""

"""
This python script utilises the googletrans module to translate text in any 
given language the English, by default.

Text extracted by the python script 'ocr_engine.py' is translated and returned.
"""

from googletrans import Translator

def translator(text):
    trans = Translator()
    return trans.translate(text).text