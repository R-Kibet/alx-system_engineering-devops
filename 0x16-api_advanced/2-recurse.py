#!/usr/bin/python3
""" using recurse function """

import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=''):
    """ function to call recurse """
    headers = {'User-Agent': 'me'}
    subreddit = argv[1]
    url = 'http://reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        parent = res.json().get('data').get('children')
        key = res.json().get('data').get('after')

        for i in parent:
            hot_list.append(i.get('data').get('title'))
        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
