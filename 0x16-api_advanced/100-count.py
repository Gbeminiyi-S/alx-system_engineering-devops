#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot articles,
   and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after="", dictionary=None):
    if dictionary is None:
        dictionary = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    data = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if data.status_code == 200:
        results = data.json().get("data")
        after = results.get("after")

        for entry in results.get("children"):
            split = entry.get("data").get("title").lower().split()

            for word in split:
                if word in word_list:
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1

        if after:
            count_words(subreddit, word_list, after, dictionary)
        else:
            # sort the dictionary by value
            if len(dictionary) == 0:
                print("")
                return
            sorted_dict = dict(sorted(dictionary.items(),
                               key=lambda x: (-x[1], x[0])))
            for key, value in dictionary.items():
                print("{}: {}".format(key, value))
    else:
        print("")
