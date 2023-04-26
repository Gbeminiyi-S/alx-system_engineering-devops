#!/usr/bin/python3
"""a Python script that, using `REST API`, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get(f"{url}users/{sys.argv[1]}").json()["name"]
    tasks = requests.get(f"{url}users/{sys.argv[1]}/todos").json()
    c_tasks = [task for task in tasks if task["completed"] is True]
    titles = [task["title"] for task in tasks if task["completed"] is True]

    print(f"Employee {name} is done with tasks({len(c_tasks)}/{len(tasks)}):")
    for title in titles:
        print(f"\t{title}")
