#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0)\
               Gecko/20100101 Firefox/89.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
