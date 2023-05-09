#!/usr/bin/python3
""" using recurse function """

import requests


def recurse(subreddit, hot_list=[], after=''):
    """ function to call recurse """
    headers = {'User-Agent': 'me'}
    url = 'http://reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        top = res.json()
        key = top['data']['after']
        parent = top['data']['children']

        for obj in parent:
            hot_list.append(obj['data']['title'])

        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
