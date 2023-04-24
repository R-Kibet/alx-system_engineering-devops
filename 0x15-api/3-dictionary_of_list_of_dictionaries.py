#!/usr/bin/python3
""" get to do list usng REST API """

import requests
import json


if __name__ == '__main__':
    """ find endpoints , user, todo list """
    url = requests.get("https://jsonplaceholder.typicode.com/users")
    users = url.json()
    url = requests.get("https://jsonplaceholder.typicode.com/todos")
    task = url.json()

    """ change to dictionary """
    dic = {
        str(data.get('id')): [
            {
                'username': data.get('username'),
                'task': item .get('titles'), 'completed':
                    item.get('completed')
            }
            for item in task
            if item.get('userId') == data.get('id')
        ]
        for data in users
    }
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dic, json_file)
