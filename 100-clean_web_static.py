#!/usr/bin/python3
""" Function that deploys """
from fabric.api import env, local, sudo


env.hosts = ["3.84.237.196", "3.80.19.23"]


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    sudo('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
