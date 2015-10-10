import sys
from os import path
sys.path.append(path.abspath('SampleShare'))
from SampleShare import app

if __name__ == '__main__':
    app.run(debug=True)

