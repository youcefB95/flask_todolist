from flask import flash, jsonify, request, render_template, redirect, url_for, Blueprint

from . import db
from . import models
from .forms import TaskForm, DeleteTaskForm
from .tables import Task

blueprint = Blueprint('app', __name__, url_prefix='/')


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/index', methods=['GET', 'POST'])
def index():
    form = DeleteTaskForm()
    count_tasks = models.countTasks()
    result = models.getTasks()
    data = result
    columns = ['id', 'content', 'category']
    table_d = data
    if form.validate_on_submit():
        _delete_task = models.deleteTask(form.id.data)
        return redirect(url_for('app.index'))
    if count_tasks==0:
        return redirect(url_for('app.createtask'))

    return render_template('index.html', columns=columns,
                           table_data=table_d, delete_form=form)


@blueprint.route('/create_task', methods=['GET', 'POST'])
def createtask():
    form = TaskForm()
    if form.validate_on_submit():
        content, category = form.content.data, form.category.data
        _post_task = models.createTask(content, category)
        flash('Your post is now live!')
        return redirect(url_for('app.index'))

    return render_template('index.html', title='Add a task', post_form=form, task='task')


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/index', methods=['GET', 'POST'])
def deleteTask():
    form = DeleteTaskForm()
    if form.validate_on_submit():
        content, category = form.content.data, form.category.data
        _post_task = models.createTask(content, category)
        flash('Your post is now live!')
        return redirect(url_for('app.index'))

    return render_template('index.html', title='Add a task', delete_form=form, task='task')


## Documentation REST API
@blueprint.route("/api/v1.0/task", methods=['GET'])
def get_tasks():
    result = models.getTasks()
    return jsonify({'tasks': result}), 201


@blueprint.route("/api/v1.0/task", methods=['POST'])
def create_task():
    content, category = request.json['content'], request.json['category']
    models.createTask(content, category)
    return jsonify({'item': 'task cree', 'content': content}), 201


@blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404
