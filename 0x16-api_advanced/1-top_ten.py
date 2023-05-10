#!/usr/bin/python3
"""Queries the Reddit API and prints data from it"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0)\
               Gecko/20100101 Firefox/89.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for entry in data.get("children"):
            print(entry.get("data").get("title"))
    else:
        print("None")
        return
