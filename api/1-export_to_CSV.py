#!/usr/bin/python3
"""Exports data from a employee in CSV format.
The file name will be: 'USER_ID.csv'.
"""
import requests
import json
import sys
import csv

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

employee_name = employee_data['name']
completed_tasks = []
user_todo_list = [todo for todo in todo_list if todo['userId'] == user_id]

with open(f'{user_id}.csv', 'w') as f:

    writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    for todo in user_todo_list:
        row = [str(user_id), employee_name,
               str(todo['completed']),
               todo['title']]
        writer.writerow(row)
