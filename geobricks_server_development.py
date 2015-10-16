import click
import os
import glob
import subprocess

BASE_FOLDER_PREFIX = 'geobricks_'

@click.command()
@click.option('--cmd', help='Switch between link and unlink georbciks libraries')
@click.option('--python_lib_path', help='Python Lib Path. This should be ideally a virtualenv python')
def cli_create_dev_enviroment(cmd, python_lib_path):

    python_lib_path = os.path.join(python_lib_path, 'site-packages')

    if cmd == 'symlink':
        create_symlinks(python_lib_path)

    elif cmd == 'unlink':
        remove_symlinks(python_lib_path)


def create_symlinks(python_lib_path):

    geobricks_folders = get_geobricks_folders()

    for geobricks_folder in geobricks_folders:
        try:

            print geobricks_folder
            symlink_geobricks_folder(geobricks_folder, python_lib_path)

        except Exception, e:
            print "WARNING: " + str(geobricks_folder)
            print e


def remove_symlinks(python_lib_path):

    geobricks_folders = get_geobricks_folders()

    for geobricks_folder in geobricks_folders:
        try:

            folder_name = os.path.basename(geobricks_folder)
            folder = os.path.join(python_lib_path, folder_name)
            print folder
            unlink_geobricks_folder(folder)

        except Exception, e:
            print "WARNING: " + str(geobricks_folder)
            print e


def symlink_geobricks_folder(geobricks_folder, python_lib_path):
    subprocess.call(["ln", "-s", geobricks_folder, python_lib_path])

def unlink_geobricks_folder(geobricks_python_folder):
    subprocess.call(["unlink", geobricks_python_folder])

# Get all Geobricks folders
def get_geobricks_folders():

    basepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server', '*')

    folders = []
    folders_to_check = glob.glob(basepath)

    for folder in folders_to_check:
        if os.path.isdir(folder):
            if BASE_FOLDER_PREFIX in folder:
                folders.append(os.path.join(folder, os.path.basename(folder)))

    return folders


if __name__ == '__main__':
    cli_create_dev_enviroment()
