#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers in a subreddit
    """
    headers = {
        'User-Agent':
            'User-Agent: linux:com.example.myapp:v1.0.0 (by /u/Illustrious-Can4699)'
    }
    sub_reddit = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                              headers=headers, allow_redirects=False)
    if sub_reddit.status_code != 200:
        print(f'Error {sub_reddit.status_code}')
        return 0
    sub_reddit = sub_reddit.json()
    return sub_reddit['data']['subscribers']


print(number_of_subscribers('programming'))