import SampleShare
from SampleShare import app
from flask import Flask, request, render_template
from werkzeug import secure_filename
import sys

sys.path.append('/Users/hennajethani/Hack_CU/SampleShare')
UPLOAD_FOLDER = '/Users/hennajethani/Hack_CU/'

ALLOWED_EXTENSIONS = set(['wav'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploaded_file')
def uploaded_file():
    return "Hello World"

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html')