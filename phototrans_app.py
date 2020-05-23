# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:26:49 2020

@author: Pratham
"""
"""
Script to develop a python Flask application to make the application more 
user-friendly and versatile.
For instance, images can be uploaded via the web application and extracted 
text can be displayed to user. 

Required libraries are:
    1) flask.Flask - to create the flask application
    2) flask.render_template - to render the HTML file
    3) phototrans.photo_translate - to perform OCR and translation
"""

from flask import Flask, render_template, request
from phototrans import photo_translate

UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app =  Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg = 'No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg = 'No file selected')

        if file and allowed_file(file.filename):
            # call the OCR function on it
            extracted_text = photo_translate(file)
            # extract the text and display it
            return render_template('upload.html', msg = 'Successfully processed', extracted_text = extracted_text, img_src = UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()