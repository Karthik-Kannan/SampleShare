from flask import Flask
from flask import render_template

app = Flask(__name__)
import SampleShare.views

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://oceanshare_admin:dqWHbHaf3YuHP@oceanshare-samples.c9val8nncp23.us-west-2.rds.amazonaws.com/samples'
db = SQLAlchemy(app)


class Sample(db.Model):
    __tablename__ = 'sample'
    date_time = db.Column(db.DateTime)
    username = db.Column(db.String(80))
    id_val = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.VARCHAR(500))
    uploader = db.Column(db.String(80))
    file_size = db.Column(db.Float)
    def __init__(self, username = 'a', date_time = '12/04/2011 12:00:00 AM', id_val = 1, url = 'blah', uploader = 'blahagain', file_size = 30):
        self.date_time = date_time
        self.username = username
        self.id_val = id_val
        self.url = url
        self.uploader = uploader
        self.file_size = file_size

