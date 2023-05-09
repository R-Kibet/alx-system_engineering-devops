#!/usr/bin/python3
""" queries number of subs """

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ function for no. of subs """
    headers = {'User-Agent': 'me'}
    subreddit = argv[1]
    url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        subs = res.json().get('data').get('subscribers')
        return subs
    else:
        return 0
