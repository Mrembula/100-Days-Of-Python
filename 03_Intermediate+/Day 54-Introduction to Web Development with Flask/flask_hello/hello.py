from flask import Flask
import time
from functools import wraps

app = Flask(__name__)


def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"<b>{text}</b>"
    return wrapper


def make_emphasis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"<em>{text}</em>"
    return wrapper


def make_underlined(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"<u>{text}</u>"
    return wrapper

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img width="200px" src="https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2">')


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'bye, world'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello, {name} you are {number} years old"


if __name__ == '__main__':
    app.run(debug=True)










'''
def delay_decorator(func):
    def wrapper():
        time.sleep(2)
        func()
    return wrapper()


@delay_decorator # Only this will run after 2 sec
def say_hello():
    print('Hello, World!')


@delay_decorator
def say_bye():
    print('Bye, World!')


@delay_decorator
def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
'''