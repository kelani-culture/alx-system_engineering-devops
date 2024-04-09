#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests
import json

def top_ten(subreddit: str) -> any:
    """
    return top 10 host posts
    """
    url = requests.get('https://httpbin.org/user-agent')
    user_agent = url.json()['user-agent']
    headers = {'User-Agent': user_agent}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json?limit=9', headers=headers)
    v = json.dumps(response.json(), indent = 3)    
    data = response.json()
    if 'data' in data and 'children' in data['data']:
        res = []
        val = data['data']['children']
        for val in val:
            res.append(val['data']['title'])
        return '\n'.join(res)
    return None
print(top_ten('programming'))