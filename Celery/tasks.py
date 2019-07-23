from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
#app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')


@app.task
def add(x, y):
    return x + y
