from setuptools import setup

setup(

    name='flask-todolist',
    version='0.1',
    packages=['app'],
    url='http://localhost:7000',
    license='',
    author='ybelhadr',
    author_email='',
    description='flask to do list',
    install_requires=[
        "flask",
        "flask-bootstrap",
        "flask-cas",
        "gunicorn",
    ],
    include_package_data=True,
)
