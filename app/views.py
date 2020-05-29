from flask import flash,jsonify, request, render_template, redirect, url_for

from . import app, db
from . import models
from .forms import PostForm, TaskForm
from .tables import Task


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    result = models.get_tasks()
    data = result
    columns = ['id', 'content', 'category']

    table_d = data

    return render_template('index.html', columns=columns,
                           table_data=table_d)



@app.route('/task', methods=['GET','POST'])
def createtask():
    form = TaskForm()
    if form.validate_on_submit():
        post=Task(content=form.content.data,category=form.category.data)
        print(post)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))

    return render_template('index.html', title='Add a task', form=form,task='task')


@app.route("/api/v1.0/task",methods=['GET'])
def get_tasks():
    result = models.get_tasks()
    return jsonify({'tasks': result}), 201


@app.route("/api/v1.0/task",methods=['POST'])
def create_task():

    models.createtask(request.json)
    return jsonify({'item': 'task cree'}), 201

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404