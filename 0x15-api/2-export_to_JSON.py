#!/usr/bin/python3
""" get to do list usng REST API """

import requests
from sys import argv
import json


if __name__ == '__main__':
    """ find endpoints , user, todo list """
    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get('{}users/{}'.format(url, userId)).json()
    todo = requests.get('{}todos?userId={}'.format(url, userId)).json()

    """ export to json """
    with open('{}.json'.format(userId), 'w',  encoding='utf-8') as f:
        json.dump({userId:
                   [{
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")}
                    for task in todo]},
                  f)
