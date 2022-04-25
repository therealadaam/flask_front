# from dataclasses import dataclass
# from hello_app.routes.forms import StudentForm
from flask import render_template, Blueprint, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from hello_app.helpers.ms_db import User, db, TenantSku
# from wtforms import Form

bp_ms_lic = Blueprint('ms_lic', __name__, template_folder='ms_lic')


@bp_ms_lic.route('/', methods=['GET', 'POST'])
def show_main():
    try:
        skus = TenantSku.query.all()
        if skus:
            return render_template(f'ms_lic.html', skus=skus)
        else:
            return render_template(f'ms_lic.html')
    except TemplateNotFound:
        abort(404)


@bp_ms_lic.route('/users', methods=['GET'])
def show_users():
    try:
        users = User.query.all()
        if users:
            return render_template(f'list_users.html', users=users)
        else:
            return render_template(f'list_users.html')
    except TemplateNotFound:
        abort(404)


@bp_ms_lic.route('/dbInit')
def init_ms_db():
    try:
        # init DB by adding fake data
        # TODO figure out if this is dangerous and refactor it properly.
        import hello_app.helpers.add_ms_db_data
        skus = TenantSku.query.all()
        # return render_template('forms/index.html', students=students)
        return render_template(f'ms_lic.html', skus=skus)
    except TemplateNotFound:
        abort(404)

# @bp_ms_lic.route('/<int:student_id>')
# def get_student(student_id):
#     student = Student.query.get_or_404(student_id)
#     return render_template('forms/student.html', student=student)

# @bp_ms_lic.route('/<int:student_id>/edit/', methods=['GET','POST'])
# def set_student(student_id):
#     if request.method == 'GET':
#         student = Student.query.get_or_404(student_id)
#         form = StudentForm(obj=student)

#     elif request.method == 'POST':
#         current_student = Student.query.get_or_404(student_id)
#         current_student.firstname=request.form["firstname"]
#         current_student.lastname=request.form["lastname"]
#         current_student.email=request.form["email"]
#         current_student.age=request.form["age"]
#         current_student.bio=request.form["bio"]

#         if request.form["active"] == 'on':
#             current_student.active=True
#         else:
#             current_student.active=False

#         form = Form(formdata=request.form)
#         if form.validate():
#             db.session.commit()
#             return redirect(url_for(endpoint='.get_student',student_id=student_id))

#     return render_template('forms/edit.html', student=form)
