#!/usr/bin/python3


# project variables

NAME_OF_DOMAIN = 'GoodFriendsBook.com'


# backend variables

FOLDERNAME_OF_BACKEND = os.path.dirname(os.environ['SCRIPT_FILENAME']).replace(f'/html/{NAME_OF_DOMAIN}', '')


# frontend variables

UPLOAD_FOLDER = f'{os.path.dirname(os.environ['SCRIPT_FILENAME'])}/upload'
AJAX_FOLDER = f'{os.path.dirname(os.environ['SCRIPT_FILENAME'])}/ajax'
AJAX_WWW = os.environ['REQUEST_URI'].replace('/ajax/','')




# database variables


def include(str_val):
    with open(str_val) as f: exec(f.read())
    