import SampleShare
from SampleShare import app
from flask import Flask, request, render_template, redirect,url_for
from werkzeug import secure_filename
from os import path
import os
import sys

UPLOAD_FOLDER = '../'
UPLOAD_FOLDER = path.abspath(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = set(['wav'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return "Hello World"

@app.route('/uploaded_file')
def uploaded_file():
    return "Hello World"

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html')