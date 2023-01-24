from app import db
from datetime import datetime
from app.models.client import Client

class Project(db.Model):
    project_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(250), nullable=False)
    client_id = db.Column(db.BigInteger, db.ForeignKey(Client.client_id))
    project_start = db.Column(db.Date, nullable=False)
    project_end = db.Column(db.Date, nullable=False)
    project_status = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Project {}>'.format(
            self.project_name,
            self.project_start,
            self.project_end,
            self.project_status,
            self.client_id
        )