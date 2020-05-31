from flask import flash, jsonify, request, render_template, redirect, url_for, Blueprint
from flask_paginate import Pagination, get_page_parameter, get_page_args

from . import db
from . import models
from .forms import AddTaskForm, DeleteTaskForm
from .tables import Task

blueprint = Blueprint('app', __name__, url_prefix='/', template_folder='templates',
                     static_folder='static')




@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/index', methods=['GET', 'POST'])
def index():

    addTaskform, deleteTaskform = AddTaskForm(), DeleteTaskForm()
    count_tasks = models.countTasks()
    columns = ['id', 'content', 'category']
    page, per_page = int(request.args.get('page', 1)), 3
    offset = (page - 1) * per_page
    tasks = models.getPaginationTasks(offset,per_page)
    pagination = Pagination(page=page,
                            per_page = per_page,
                            total=count_tasks,
                            search=False,
                            record_name='tasks',
                           css_framework='bootstrap3')

    if deleteTaskform.validate_on_submit():
        models.deleteTask(deleteTaskform.id.data)
        return redirect(url_for('app.index'))

    if addTaskform.validate_on_submit():
        content, category = addTaskform.content.data, addTaskform.category.data
        models.createTask(content, category)
        return redirect(url_for('app.index'))



    return render_template('index.html', columns=columns,
                           data=tasks,
                           pagination=pagination, delete_form=deleteTaskform,add_form=addTaskform,css_framework='bootstrap3',post_form=None)



def delete_task(task):
    _delete_task = models.deleteTask(task)

def create_task(content, category):
    _create_task = models.createTask(content, category)
    flash('Your post is now live!')




@blueprint.route('/create_task', methods=['GET', 'POST'])
def createtask():
    form = AddTaskForm()
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
