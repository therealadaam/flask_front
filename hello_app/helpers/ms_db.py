import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from .. import app

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    tenant_name = db.Column(db.String(100), nullable=False)
    tenant_guid = db.Column(db.String(36), nullable=False)

    displayname = db.Column(db.String(100), nullable=False)
    sku_names = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(80), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<User {self.displayname}>'


class TenantSku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku_name = db.Column(db.String(100), nullable=False)
    sku_guid = db.Column(db.String(36), unique=True, nullable=False)

    tenant_name = db.Column(db.String(100), nullable=False)
    tenant_guid = db.Column(db.String(36), nullable=False)

    consumed = db.Column(db.Integer)
    warning = db.Column(db.Integer)
    enabled = db.Column(db.Integer)
    suspended = db.Column(db.Integer)

    active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<TenantSku {self.sku_name}>'


db.create_all()
