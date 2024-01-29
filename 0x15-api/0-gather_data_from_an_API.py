#!/usr/bin/python3
"""Fetch data from a url using request module"""
import requests
import sys



def employee_data(emp_id):
    base_url = "https://jsonplaceholder.typicode.com"
    emp_info = requests.get(f'{base_url}/users/{emp_id}')
    emp_info = emp_info.json()
    name = emp_info.get('name')
 
    # task completed
    task_info = requests.get(f'{base_url}/todos?userId={emp_id}')
    task_info = task_info.json() 
    total_task = len([task.get('completed') for task in task_info])
    task_completed = sum(task.get('completed') for task in task_info)

    print(f"Employee {name} is done with tasks({task_completed}/{total_task}):")
    for task in task_info:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    employee_data(emp_id)
