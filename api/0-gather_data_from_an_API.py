#!/usr/bin/python3
"""For a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import json
import sys

if sys.argv[1] is not None:
    user_id = sys.argv[1]

API_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
employee_API = requests.get(API_url)
employee_data = employee_API.text
employee_data = json.loads(employee_data)
todo_API = requests.get(f"https://jsonplaceholder.typicode.com/todos/")
todo_list = todo_API.text
todo_list = json.loads(todo_list)

employee_name = employee_data['name']

tasks_completed = 0
total_tasks = 0
completed_tasks = []

for todo in todo_list:
    if todo['userId'] == eval(user_id):
        for k in todo:
            if k == "completed":
                total_tasks += 1
                if todo['completed'] is True:
                    completed_tasks.append(todo['title'])
                    tasks_completed += 1

print(f"Employee {employee_name} is done \
        with tasks({tasks_completed}/{total_tasks}):")

for task in completed_tasks:
    print(f"\t {task}")
