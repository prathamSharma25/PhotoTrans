# PhotoTrans
A Flask web application to extract text from uploaded images and translate it. 

This web application is designed as a tool to extract text from images and translate it into the English languge.
It is designed as a Flask application and makes use of the following libraries:
  1) PyTesseract - a python wrapper for Google's Tesseract-OCR Engine. It is an Optical Character Recognition tool for python. It is used        to extract text from uploaded images.
  2) Googletrans - a free and unlimited python library that implements Google Translate API. This is used to translate the extracted text 
     to English.
  3) OpenCV-Python - wrapper package for OpenCV python bindings. It is used to perform pre-processing functions such as grayscaling and          thresholding on uploaded images for better OCR performance.
  4) Pillow - Python Imaging Library. It provides support for opening, manipulating and saving many different image file formats.

The web application utilises essential python functions defined for the processing operations.
Python scripts and their functionality are described bellow:
  1) preprocessing.py - performs image pre-processing functions to improve accuracy of OCR
  2) ocr_engine.py - performs OCR on the uploaded image and returns the extracted text
  3) translate.py - translates the text extracted by ocr_engine.py into English
  4) phototrans.py - integrates functions from each of the above three python scripts to perform the complete operation
  5) phototrans_app.py - Flask web application to provide user-interface to upload images and get result
  
The web application is designed using simple HTML and HTML forms.

It is recommended to implement the project in a python virtual environemt and install all required libraries and dependencies in the virtual environment. Find instructions to create virtual environment, install libraries and execute the project in the 'instructions.txt' file (Windows only).
