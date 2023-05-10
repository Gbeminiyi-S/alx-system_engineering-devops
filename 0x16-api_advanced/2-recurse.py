#!/usr/bin/python3
"""Function to query a list of all hot posts for a given Reddit subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0)\
               Gecko/20100101 Firefox/89.0"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        for entry in results.get("children"):
            hot_list.append(entry.get("data").get("title"))

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
