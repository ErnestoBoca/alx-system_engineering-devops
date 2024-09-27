#!/usr/bin/python3
"""This script uses a REST API, and for a given employee ID,
returns information about his/her TODO list progress."""
import json
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


def to_csv():
    """exports data in the CSV format"""
    user_id = sys.argv[1]

    tasks_params = {'userId': user_id}
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params=tasks_params).json()

    user_params = {'id': user_id}
    user = requests.get("https://jsonplaceholder.typicode.com/users",
                        params=user_params).json()[0]

    file_name = "{}.csv".format(user_id)
    with open(file_name, 'w', encoding='utf-8') as csv_file:
        for task in tasks:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                            user_id, user.get('username'),
                            task.get('completed'), task.get('title')))


def to_JSON():
    """Exports data in the JSON format"""
    tasks_params = {'userId': user_id}
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params=tasks_params).json()

    user_params = {'id': user_id}
    user = requests.get("https://jsonplaceholder.typicode.com/users",
                        params=user_params).json()[0]
    user_dict = {user_id: []}
    for task in tasks:
        user_dict.get(user_id).append(
                      {"task": task.get("title"),
                       "completed": task.get("completed"),
                       "username": user.get("username")})
    file_name = "{}.json".format(user_id)
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(user_dict, json_file)


def all_to_JSON():
    """Exports data of all users in the JSON format"""
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    users_dict = {}
    for user in users:
        users_dict[user.get("id")] = []
        for task in tasks:
            if task.get("userId") == user.get("id"):
                users_dict.get(user.get("id")).append(
                              {"username": user.get("username"),
                               "task": task.get("title"),
                               "completed": task.get("completed")})
    file_name = "todo_all_employees.json"
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(users_dict, json_file)


def number_of_done(tasks):
    """Return the number of done tasks"""
    done = 0
    for task in tasks:
        if task.get('completed'):
            done += 1
    return done


if __name__ == "__main__":
    all_to_JSON()
