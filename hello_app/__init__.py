import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'cd668a81b31786c38b7187082b8633b0828f7adf97105432'
from hello_app.db_init import db, Student