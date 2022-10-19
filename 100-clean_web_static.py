#!/usr/bin/python3
""" A fabric script that generates a .tgz
    archive and uploads to web servers
"""
from fabric.api import local, put, sudo, env, cd
import time
import os

env.hosts = ["3.238.25.45", "44.192.21.5"]


def do_pack():
    """ Archive the web_static folder using the
        tar command
    """
    try:
        local("mkdir -p versions")

        local("tar -cvzf versions/web_static_{}.tgz web_static".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".
                format(time.strftime("%Y%m%d%H%M%S")))
    except Exception as e:
        return None


def do_deploy(archive_path):
    """ Uploads archive to web servers

    Args:
        archive_path (str): Path of archive

    Returns:
        True if successful, False if unsuccessful
    """

    if not os.path.exists(archive_path):
        return False
    else:
        path_name = "/data/web_static/releases/" + archive_path[9:-4]
        file_path = "/tmp/" + archive_path[9:]
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(path_name))
        sudo("tar -xzf {} -C {}".format(file_path, path_name))
        sudo("rm {}".format(file_path))
        sudo("mv {}/web_static/* {}".format(path_name, path_name))
        sudo("rm -rf {}/web_static".format(path_name))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(path_name))
        print("New Version Deployed")
        return True


def deploy():
    """ Combine both do_pack and do_deploy functions """
    path = do_pack()
    if not os.path.exists(path):
        return False
    state = do_deploy(path)
    return state


def do_clean(number=0):
    """ Deletes out of date archives

    Args:
        number (int): Number of archives to keep
    """
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    path = "/data/web_static/releases"
    local("cd versions; ls -t | tail +{} | xargs rm -rf".format(number))
    with cd(path):
        sudo("ls -t | tail +{} | xargs rm -rf".format(number))
