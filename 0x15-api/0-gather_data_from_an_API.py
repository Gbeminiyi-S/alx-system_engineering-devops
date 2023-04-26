#!/usr/bin/python3
"""Return an employee's TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get(f"{url}users/{sys.argv[1]}").json().get("name")
    tasks = requests.get(f"{url}users/{sys.argv[1]}/todos").json()
    c_tasks = [task for task in tasks if task.get("completed") is True]
    titles = [task.get("title") for task in tasks
              if task.get("completed") is True]

    print(f"Employee {name} is done with tasks({len(c_tasks)}/{len(tasks)}):")
    for title in titles:
        print(f"\t{title}")
