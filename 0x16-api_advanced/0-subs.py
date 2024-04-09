#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests

def number_of_subscribers(subreddit : str) -> int:
    """
    returns the number of subscribers in a subreddit
    """
    
    url = requests.get('https://httpbin.org/user-agent')
    user_agent = url.json()['user-agent']
    headers = {'User-Agent': user_agent}
    sub_reddit = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)
    sub_reddit = sub_reddit.json()
    if 'data' in sub_reddit and 'subscribers' in sub_reddit['data']:
        return sub_reddit['data']['subscribers']
    return 0
