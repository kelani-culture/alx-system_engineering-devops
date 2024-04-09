#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list,
containing the titles of all hot articles for a given subreddit
"""
import requests



url = requests.get('https://httpbin.org/user-agent')
user_agent = url.json()['user-agent']
def recurse(subreddit, hot_list=[], after=None):
    """
    A functon that recursively queriese the reddit api
    return a list
    """
    # headers = {"User-Agent": user_agent}
    params = {'after': after}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                            params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    for val in data['data']['children']:
        hot_list.append(val['data']['title'])
        
    
    if data['data']['after']:
        recurse(subreddit, hot_list, after=data['data']['after']) 
    return hot_list
