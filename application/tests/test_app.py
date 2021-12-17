from flask_testing import TestCase
from application import app, db
from application.models import Books
from flask import url_for
from datetime import date, timedelta

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost:3306/books',
            SECRET_KEY='test_secret_key',
            DEBUG=True,
            WTF_CSFR_ENABLED = False)
        return app

    def setUp(self):
        db.create_all()
        Auto_date = date.today
        Default_target_date = date.today() + timedelta(days=60)
        sample = Books(book_name = 'Test book', suthor = 'Test author', date_added = Auto_date, book_status = 'Proposed', date_target = Default_target_date, suggested_by='Tester')
        db.session.add(sample)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
