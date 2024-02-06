#!/usr/bin/python3
"""Exports data from a employee in JSON format.
The file name will be: 'USER_ID.json'.
"""
import json
import requests

API_url = f"https://jsonplaceholder.typicode.com/users/"
all_users_API = requests.get(API_url)
all_users_data = all_users_API.text
all_users_data = json.loads(all_users_data)
todo_API = requests.get(f"https://jsonplaceholder.typicode.com/todos/")
todo_list = todo_API.text
todo_list = json.loads(todo_list)

user_dictionary = {}

for user in all_users_data:
    user_id = user['id']
    user_name = user['username']
    user_todo_list = [todo for todo in todo_list if todo['userId'] == user_id]
    new_todo_list = []

    for dict in user_todo_list:
        new_dict = {}
        new_dict['username'] = user_name
        new_dict['task'] = dict['title']
        new_dict['completed'] = dict['completed']
        new_todo_list.append(new_dict)

    user_dictionary[f"{user_id}"] = new_todo_list

json_dictionary = json.dumps(user_dictionary)

with open("todo_all_employees.json", "w") as f:
    f.write(json_dictionary)
