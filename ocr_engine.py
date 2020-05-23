# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:51:50 2020

@author: Pratham
"""

"""
This script performs Optical Character Recognition (OCR) for uploaded image 
file and returns the text detected in the image for further processing.
"""

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'

def ocr_core(image_file):
    """
    This function handles the OCR processing of uploaded image file.
    """
    custom_config = r'--psm 6 -l afr+amh+ara+asm+aze+aze_cyrl+bel+ben+bod+bos+bre+bul+cat+ceb+ces+chi_sim+chi_tra+chr+cym+dan+deu+dzo+ell+eng+enm+epo+est+eus+fas+fin+fra+frk+frm+gle+glg+grc+guj+hat+heb+hin+hrv+hun+iku+ind+isl+ita+ita_old+jav+jpn+kan+kat+kat_old+kaz+khm+kir+kmr+kor+kor_vert+kur+lao+lat+lav+lit+ltz+mal+mar+mkd+mlt+mon+mri+msa+mya+nep+nld+nor+oci+ori+pan+pol+por+pus+que+ron+rus+san+sin+slk+slv+snd+spa+spa_old+sqi+srp+srp_latn+sun+swa+swe+syr+tam+tat+tel+tgk+tgl+tha+tir+ton+tur+uig+ukr+urd+uzb+uzb_cyrl+vie+yid+yor'
    return pytesseract.image_to_string(image_file, config = custom_config)
