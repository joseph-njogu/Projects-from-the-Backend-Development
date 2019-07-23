from fabric.api import *


def runserver():
    local('python3 manage.py runserver')
