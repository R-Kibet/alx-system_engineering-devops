#!/usr/bin/python3
""" get to do list usng REST API """

import csv
import requests
from sys import argv


if __name__ == '__main__':
    """ find endpoints , user, todo list """
    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get('{}users/{}'.format(url, userId)).json()
    todo = requests.get('{}todos?userId={}'.format(url, userId)).json()

    """ export to csv """
    with open('{}.csv'.format(userId), 'w') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in todo:
            write.writerow([int(userId), user.get(
                'username'), i.get('completed'), i.get('title')])
