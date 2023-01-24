from app import db
from datetime import datetime

class Client(db.Model):
    client_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(250), nullable=False)
    client_address = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Client {}>'.format(self.client_name)