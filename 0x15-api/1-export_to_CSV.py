#!/usr/bin/python3
"""Fetch data from a url using request module"""
import requests
import sys
import csv

def employee_data(emp_id):
    base_url = "https://jsonplaceholder.typicode.com"
    emp_info = requests.get(f'{base_url}/users/{emp_id}')
    emp_info = emp_info.json()
    name = emp_info.get('name')
 
    # task completed
    task_info = requests.get(f'{base_url}/todos?userId={emp_id}')
    task_info = task_info.json() 
    
    user_data = []
    
    for task in task_info:
        user_data.append({"USER_ID": task['userId'],
                          "USERNAME": name,
                          "TASK_COMPLETED_STATUS": task['completed'],
                          "TASK_TITLE": task['title']
                          }) 
    file = str(emp_id) + '.csv'
    with open(file, 'w') as user_info:
        fieldnames = user_data[0].keys()
        write_data = csv.DictWriter(user_info, fieldnames=fieldnames)
        write_data.writeheader()
        for data in user_data:
            write_data.writerow(data)

if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    employee_data(emp_id)
