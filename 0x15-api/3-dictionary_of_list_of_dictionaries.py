#!/usr/bin/python3
"""Get all users information from the api requests"""
import json
import requests


def employee_data():
    base_url = "https://jsonplaceholder.typicode.com"
    emp_info = requests.get(f'{base_url}/users')
    emp_info = emp_info.json()
    all_data = {}

    for emp in emp_info:
        emp_id = emp.get('id')
        task_info = requests.get(f'{base_url}/todos?userId={emp_id}')
        task_info = task_info.json()
        user_data = []
        for task in task_info:
            user_data.append({
                            "title": task.get('title'),
                            "completed": task.get('completed'),
                            "username": emp.get('name')
                            })
        all_data[emp_id] = user_data
    with open('todo_all_employees.json', 'w') as json_f:
        json.dump(all_data, json_f)


if __name__ == '__main__':
    employee_data()
