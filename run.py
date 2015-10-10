from flask import Flask
from flask import render_template

app = Flask(__name__)
UPLOAD_FOLDER = '/test/'

@app.route('/hello')
def hello_world():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()