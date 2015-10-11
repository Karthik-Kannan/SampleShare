import SampleShare
from SampleShare import app, db, Sample
from flask import Flask, request, render_template, redirect,url_for
from werkzeug import secure_filename
from os import path
import os
import sys
import uuid
import datetime

UPLOAD_FOLDER = 'samples'
UPLOAD_FOLDER = path.abspath(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = set(['wav'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            savepath =os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(savepath)
            id = uuid.uuid
            timestamp = datetime.datetime.now()
            name ="Philip Chow"
            url = savepath
            uploader = "192.168.1.1"
            size = os.stat(savepath).st_size
            tags = "Snare, Drums, Downtempo"
            a= Sample(name, timestamp, id, url, uploader,size,tags)
            db.session.add(a)
            db.session.commit()
            db.session.close()
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('index.html')


@app.route('/uploaded_file')
def uploaded_file():
    return "Hello World"

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            savepath =os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(savepath)
            id = uuid.uuid
            timestamp = datetime.datetime.now()
            name ="Philip Chow"
            url = savepath
            uploader = "192.168.1.1"
            size = os.stat(savepath).st_size
            tags = "Snare, Drums, Downtempo"
            a= Sample(name, timestamp, id, url, uploader,size,tags)
            db.session.add(a)
            db.session.commit()
            db.session.close()
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return render_template('upload.html')