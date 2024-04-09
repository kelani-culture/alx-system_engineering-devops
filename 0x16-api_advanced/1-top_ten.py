#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests
import json

def top_ten(subreddit) -> None:
    """
    return top 10 host posts
    """
    url = requests.get('https://httpbin.org/user-agent')
    user_agent = url.json()['user-agent']
    headers = {'User-Agent': user_agent}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                            headers=headers, allow_redirects=False)
    data = response.json()
    print(json.dumps(data, indent=4))
    if 'data' in data and 'children' in data['data']:
        val = data['data']['children'][:10]
        for val in val:
            print(val['data']['title'])
    return None

top_ten('programming')
