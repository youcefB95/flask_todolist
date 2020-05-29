from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from app import db, app
from app.tables import Task

# engine = create_engine('mysql+pymysql://root:root@127.0.0.1/bd_notes', pool_pre_ping=True)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
connection = engine.raw_connection()
cursor = connection.cursor()

global tasks
tasks= []

def get_tasks():
    del tasks[:]
    sql = "SELECT * FROM tasks"
    item = {}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        for row in results:
            item = {
                "id": row[0],
                "content": row[1],
                "category": row[2]
            }
            tasks.append(item)
    except Exception as e:
        print(e)
    return tasks


def createtask(task):
    sql = "INSERT INTO tasks(content,category) VALUES ('%s', '%d')" % (
        task['content'], task['category'])
    results = {}
    try:
        cursor.execute(sql)
        connection.commit()



    except Exception as e:

        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            connection.rollback()
            print("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            connection.close()
