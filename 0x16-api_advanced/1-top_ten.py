#!/usr/bin/python3
""" queries top 10 """

import requests
from sys import argv


def top_ten(subreddit):
    """ function for top ten tittles """
    headers = {'User-Agent': 'me'}
    subreddit = argv[1]
    url = 'http://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        post = res.json().get('data').get('children')
        if post:
            for i in post:
                print(i.get('data').get('title'))
        else:
            print("None")
    else:
        print("None")
