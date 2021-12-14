from application import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(100))
    author = db.Column(db.String(50))
    date_added = db.Column(db.DateTime)
    book_status = db.Column(db.String(10))
    date_target = db.Column(db.DateTime)
    suggested_by = db.Column(db.String(50))