# from flask import Flask, redirect, render_template, url_for, request
# app = Flask(__name__)

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/anaysis'

# db=SQLAlchemy(app)

# class Student(db.Model):
#   __tablename__='pythonApp'
#   id=db.Column(db.Integer,primary_key=True)
#   fname=db.Column(db.String(40))
#   lname=db.Column(db.String(40))
#   pet=db.Column(db.String(40))

#   def __init__(self,fname,lname,pet):
#     self.fname=fname
#     self.lname=lname
#     self.pet=pet


# userId = 'hello'
# password = "hello12354"

# @app.route('/success/<name>')
# def success(name):
#    return render_template('welcome.html', name = name)

# @app.route('/')
# def hi():
#     return render_template('login.html')

# @app.route('/',methods = ['POST'])
# def login():
#    if request.method == 'POST':
#       user = request.form['daddy']
#       return redirect(url_for('success', name = user))
#    else:
#       return render_template('login.html')

# if __name__ == '__main__':
#    app.run(debug = True)