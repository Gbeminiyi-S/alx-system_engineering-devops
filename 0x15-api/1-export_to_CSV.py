#!/usr/bin/python3
"""Exports to-do list data for an employee to CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    tasks = requests.get("{}users/{}/todos".format(url, sys.argv[1])).json()
    data_rows = [[sys.argv[1], user.get("username"), task.get("completed"),
                 task.get("title")] for task in tasks]

    # open a new CSV file in write mode
    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(data) for data in data_rows]