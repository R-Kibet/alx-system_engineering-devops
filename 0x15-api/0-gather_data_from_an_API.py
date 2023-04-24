#!/usr/bin/python3
""" get to do list usng REST API """

import requests
from sys import argv


if __name__ == '__main__':
    """ find endpoints , user, todo list """
    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get('{}users/{}'.format(url, userId)).json()
    todo = requests.get('{}todos?userId={}'.format(url, userId)).json()
    completed = []

    """ loop to get done tasks """
    for i in todo:
        if i.get("completed"):
            completed.append(i.get("title"))
    print("Employee {} is done with task({}/{}):"
          .format(user.get('name'), len(completed), len(todo)))
    for i in completed:
        print('     {}'.format(i))
