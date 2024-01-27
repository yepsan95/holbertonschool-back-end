#!/usr/bin/python3
"""
Exports data from a employee in JSON format.
The file name will be: 'USER_ID.json'.
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
    employee_name = employee_data['name']

    user_todo_list = [todo for todo in todo_list if todo['userId'] == user_id]
    json_dictionary = {}
    json_todo_list = []
    for dict in user_todo_list:
        new_dict = {}
        new_dict['task'] = dict['title']
        new_dict['completed'] = dict['completed']
        new_dict['username'] = employee_name
        json_todo_list.append(new_dict)

    json_dictionary[f"{user_id}"] = json_todo_list
    json_object = json.dumps(json_dictionary)

    with open(f"{user_id}.json", "w") as f:
        f.write(json_object)
