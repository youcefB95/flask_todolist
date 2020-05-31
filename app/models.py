from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from app.tables import Task
from app import db

# engine = create_engine('mysql+pymysql://root:root@127.0.0.1/bd_notes', pool_pre_ping=True)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# connection = engine.raw_connection()
# cursor = connection.cursor()

global tasks
tasks = []


def getPaginationTasks(offset,per_page):
    tasks = Task.query.limit(per_page)
    tasks = tasks[offset: offset + per_page]
    return tasks


def getTasks():
    del tasks[:]
    rows = db.session.query(Task).all()
    for task in rows:
        item = {
            "id": task.id,
            "content": task.content,
            "category": task.category
        }
        tasks.append(item)

    return tasks

def countTasks():
    count = db.session.query(Task.id).count()
    return count


def createTask(content, category):
    task_to_create = Task(content=content, category=category)
    db.session.add(task_to_create)
    db.session.commit()


def deleteTask(id):
    task_to_delete = db.session.query(Task).filter(Task.id == id).first()
    db.session.delete(task_to_delete)
    db.session.commit()
