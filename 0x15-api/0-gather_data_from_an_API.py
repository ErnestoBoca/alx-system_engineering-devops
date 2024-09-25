#!/usr/bin/python3
"""This script uses a REST API, and for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


def get_todo_list():
    """Prints the todo list for a given eployee"""
    user_id = sys.argv[1]

    tasks_params = {'userId': user_id}
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params=tasks_params).json()

    user_params = {'id': user_id}
    user = requests.get("https://jsonplaceholder.typicode.com/users",
                        params=user_params).json()

    print("Employee {} is done with tasks({}/{}):".format(
          user[0].get('name'), number_of_done(tasks), len(tasks)))
    for task in tasks:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))


def number_of_done(tasks):
    """Return the number of done tasks"""
    done = 0
    for task in tasks:
        if task.get('completed'):
            done += 1
    return done


if __name__ == "__main__":
    get_todo_list()
