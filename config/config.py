import os
basedir = os.path.abspath(os.path.dirname(__file__))

class test():

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "data-test.db?check_same_thread=False")


class dev():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "data-dev.db?check_same_thread=False")

config = {
    'test':test,
    'dev':dev
}