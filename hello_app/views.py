from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, url_for
from . import app
from . import db, Student

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ] # later make this a db-independant module like sqlalchemy

@app.route('/msg')
@app.route('/msg/index')
def index():
    return render_template('msg/index.html', messages=messages)

@app.route('/msg/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('msg/create.html')

@app.route('/student')
def s_index():
    students = Student.query.all()
    if students:
        return render_template('student/s_index.html', students=students)
    else:
        # init DB by adding fake data
        # db.create_all()

        student_john = Student(firstname='john', lastname='doe',
                            email='jd@example.com', age=23,active=True,
                            bio='Biology student')

        sammy = Student(firstname='Sammy',
                    lastname='Shark',
                    email='sammyshark@example.com',active=True,
                    age=20,
                    bio='Marine biology student')

        carl = Student(firstname='Carl',
                    lastname='White',
                    email='carlwhite@example.com', active=True,
                    age=22,
                    bio='Marine geology student')

        db.session.add(sammy)
        db.session.add(carl)
        db.session.add(student_john)
        db.session.commit()
        students = Student.query.all()
        return render_template('student/s_index.html', students=students)

@app.route('/student/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student/student.html', student=student)

@app.route('/student/create/', methods=('GET', 'POST'))
def s_create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        student = Student(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('s_index'))

    return render_template('student/s_create.html')

@app.route('/student/<int:student_id>/edit/', methods=('GET', 'POST'))
def s_edit(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age
        student.bio = bio

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('s_index'))

    return render_template('student/edit.html', student=student)

@app.post('/student/<int:student_id>/delete/')
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('s_index'))