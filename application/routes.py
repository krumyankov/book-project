from application import app, db
from application.models import Books
from application.forms import BooksList
from datetime import date, timedelta
from flask import render_template, request

Auto_date = date.today()
Default_target_date = date.today() + timedelta(days=60)
Default_book_status = 'Proposed'

@app.route('/', methods = ['GET','POST'])
@app.route('/add', methods = ['GET','POST'])
def add():
    message = ''
    form = BooksList()
    if request.method == 'POST':
        bookname = form.name.data
        author = form.author.data
        addeddate = Auto_date
        bookstatus = Default_book_status
        targetdate = Default_target_date
        suggestedby = form.suggested_by.data
        if form.validate_on_submit():
            newbook = Books(name=bookname, author=author, date_added=addeddate,status=bookstatus, date_target=targetdate,suggested_by=suggestedby)
            db.session.add(newbook)
            db.session.commit()
            message = 'The book has been added to the reading list'
        else:
            message = 'Please complete all the required fields'
    return render_template('input.html',form = form, message = message,Auto_date=Auto_date,Default_target_date=Default_target_date,Default_book_status=Default_book_status)


@app.route('/read')
def read():
    books = Books.query.all()
    bookstring = ''
    for book in books:
        formatted_date1 = str(book.date_added.day) + '/' + str(book.date_added.month) + '/' + str(book.date_added.year)
        formatted_date2 = str(book.date_target.day) + '/' + str(book.date_target.month) + '/' + str(book.date_target.year)
        bookstring += '<br>' + str(book.id) + '*' + book.name + '*' + book.author + '*Status=' + str(book.status) + '*Date added: ' + formatted_date1 + '*To be read by date: ' + formatted_date2
    return bookstring


@app.route('/update/id=<int:id>/newstatus=<status>')
def update(id,status):
    book = Books.query.get(id)
    book.status = status
    db.session.commit()
    return 'Book status updated'


@app.route('/delete/deletebook=<bookname>')
def delete(bookname):
    remove_book = Books.query.filter_by(name=bookname).first()
    db.session.delete(remove_book)
    db.session.commit()
    return 'Book has been removed from list'