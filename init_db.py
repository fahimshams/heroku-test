import os
import psycopg2
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'sql5487255'
app.config['MYSQL_PASSWORD'] = '3rH8Iu6dNx'
app.config['MYSQL_HOST'] = 'sql5.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql5487255'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)
# conn = psycopg2.connect(
#         host="localhost",
#         database="sql5487255",
#         user = 'sql5487255',
#         password='3rH8Iu6dNx')

# # Open a cursor to perform database operations
# cur = conn.cursor()
# # cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
# #                                  'title varchar (150) NOT NULL,'
# #                                  'author varchar (50) NOT NULL,'
# #                                  'pages_num integer NOT NULL,'
# #                                  'review text,'
# #                                  'date_added date DEFAULT CURRENT_TIMESTAMP);'
# #                                  )

# cur.execute('SELECT * FROM books')

# conn.commit()

# cur.close()
# conn.close()

@app.route('/')
def index():
    cur = mysql.connection.cursor()
#     cur.execute('CREATE TABLE example (id INTEGER, name VARCHAR(20))')

#     cur.execute('''INSERT INTO example VALUES (1, 'Anthony')''')
    cur.execute('''UPDATE example VALUES (2, 'Billy')''')
    mysql.connection.commit()

    cur.execute('SELECT * FROM example')
    results = cur.fetchall()
    print(results)
    return str(results[1]['id'])

if __name__ == '__main__':
   app.run(debug = True)