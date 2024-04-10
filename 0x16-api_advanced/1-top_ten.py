#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit) -> None:
    """
    return top 10 host posts
    """
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                            params={'limit': 10}, allow_redirects=False)
    data = response.json()
    if 'data' in data and 'children' in data['data']:
        val = data['data']['children']
        for val in val:
            print(val['data']['title'])
    return None

top_ten('programming')
