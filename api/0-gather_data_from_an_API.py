#!/usr/bin/python3
"""For a given employee ID, returns
information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == '__main__':
    try:
        if sys.argv[1] is not None:
            user_id = int(sys.argv[1])
    except IndexError:
        exit(1)
    except ValueError:
        exit(1)

    API_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    employee_API = requests.get(API_url)
    employee_data = employee_API.text
    employee_data = json.loads(employee_data)
    todo_API = requests.get(f"https://jsonplaceholder.typicode.com/todos/")
    todo_list = todo_API.text
    todo_list = json.loads(todo_list)

    try:
        employee_name = employee_data['name']
    except KeyError:
        exit(1)
    completed_tasks = []
    user_todo_list = [todo for todo in todo_list if todo['userId'] == user_id]

    for todo in user_todo_list:
        if todo['completed'] is True:
            completed_tasks.append(todo['title'])

    total_tasks = len(user_todo_list)
    tasks_completed = len(completed_tasks)
    result = f"Employee {employee_name} is done "
    result += f"with tasks({tasks_completed}/{total_tasks}):"
    print(result)

    for task in completed_tasks:
        print(f"\t {task}")
