import pymysql.cursors


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root')

conn.cursor().execute('CREATE DATABASE IF NOT EXISTS books')

conn.cursor().execute('CREATE TABLE IF NOT EXISTS books.books (id INTEGER NOT NULL AUTO_INCREMENT, book_name VARCHAR(100) NOT NULL, author VARCHAR(50) NOT NULL, date_added DATE NOT NULL, book_status VARCHAR(10) NOT NULL DEFAULT \'Proposed\', date_target DATE NOT NULL, suggested_by VARCHAR(50) NOT NULL, PRIMARY KEY (id), UNIQUE (book_name))')