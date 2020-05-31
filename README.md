# flask-todolist

A simple flask app to 
create to do list

[Live demo](http://flask-cas-extension-demo.cameronbwhite.com)

## Installation

1. Clone it `git clone https://github.com/Youbel95/flask-todolist`
2. Enter it `cd flask-todolist`
3. Create python virtual environment `virtualenv venv`
4. Activate virtual environment `source venv/bin/activate` or `venv\Scripts\activate.bat`
5. Install it and dependencies `python setup.py install`

## Running

There are a few ways to run the application. The first way is to run it in
flask's web server. The second way is to use gunicorn. Its also all set
up to run on Heroku.

### Flask web server (NOT FOR PRODUCTION)


```sh
python app.py --debug True --config dev
```

### Gunicorn

1. Add `SECRET_KEY` `export SECRET_KEY=[its a secret]`
2. Run it `gunicorn app:app`

### Heroku

Its ready to go. All you have to do is make an account and upload it.
You will need to set up the enviroment like gunicorn.

