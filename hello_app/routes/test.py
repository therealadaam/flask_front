from dataclasses import dataclass
from hello_app.routes.forms import StudentForm
from flask import render_template, Blueprint, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from hello_app.db_init import Student, db
from wtforms import Form

bp_student = Blueprint('bp_student', __name__, template_folder='templates')

@bp_student.route('/',defaults={'page': 'f_index'},methods=['GET','POST'])
@bp_student.route('/<page>')
def show(page):
    try:
        form = StudentForm()
        if form.validate_on_submit():
            student = Student(firstname=form.firstname.data,
                            lastname=form.lastname.data,
                            email=form.email.data,
                            age=form.age.data,
                            bio=form.bio.data,
                            active=form.active.data)
            db.session.add(student)
            db.session.commit()

            return redirect(url_for('.list_all_students'))
        return render_template(f'forms/{page}.html', form=form)
    except TemplateNotFound:
        abort(404)

@bp_student.route('/all')
def list_all_students():
    students = Student.query.all()
    if students:
        return render_template('forms/index.html', students=students)
    else:
        # init DB by adding fake data
        # TODO figure out if this is dangerous and refactor it properly.
        import hello_app.helpers.add_db_data
        students = Student.query.all()
        return render_template('forms/index.html', students=students)

@bp_student.route('/<int:student_id>')
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('forms/student.html', student=student)

@bp_student.route('/<int:student_id>/edit/', methods=['GET','POST'])
def set_student(student_id):
    if request.method == 'GET':
        student = Student.query.get_or_404(student_id)
        form = StudentForm(obj=student)

    elif request.method == 'POST':
        current_student = Student.query.get_or_404(student_id)
        current_student.firstname=request.form["firstname"]
        current_student.lastname=request.form["lastname"]
        current_student.email=request.form["email"]
        current_student.age=request.form["age"]
        current_student.bio=request.form["bio"]

        if request.form["active"] == 'on':
            current_student.active=True
        else:
            current_student.active=False

        form = Form(formdata=request.form)
        if form.validate():
            db.session.commit()
            return redirect(url_for(endpoint='.get_student',student_id=student_id))

    return render_template('forms/edit.html', student=form)

# @app.route('/student/<int:student_id>/edit/', methods=('GET', 'POST'))
# def s_edit(student_id):
#     student = Student.query.get_or_404(student_id)

#     if request.method == 'POST':
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         age = int(request.form['age'])
#         bio = request.form['bio']

#         student.firstname = firstname
#         student.lastname = lastname
#         student.email = email
#         student.age = age
#         student.bio = bio

#         db.session.add(student)
#         db.session.commit()

#         return redirect(url_for('s_index'))

#     return render_template('student/edit.html', student=student)

# @app.post('/student/<int:student_id>/delete/')
# def delete(student_id):
#     student = Student.query.get_or_404(student_id)
#     db.session.delete(student)
#     db.session.commit()
#     return redirect(url_for('s_index'))