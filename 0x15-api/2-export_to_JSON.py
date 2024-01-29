#!/usr/bin/python3
"""Fetch data from a url using request module"""
import requests
import sys
import json

emp_id = int(sys.argv[1])

def employee_data(emp_id):
    base_url = "https://jsonplaceholder.typicode.com"
    emp_info = requests.get(f'{base_url}/users/{emp_id}')
    emp_info = emp_info.json()
    name = emp_info['name']
 
    # task completed
    task_info = requests.get(f'{base_url}/todos?userId={emp_id}')
    task_info = task_info.json() 
    
    user_data = []
    for task in task_info:
        user_data.append({
                          "TASK_COMPLETED_STATUS": task['completed'],
                          "TASK_TITLE": task['title']
                          }) 
    
    user_data_dict = {str(emp_id): user_data}
    file = str(emp_id) + '.json'
    
    with open(file, 'w') as json_f:
        json.dump(user_data_dict, json_f)    


if __name__ == "__main__":
    employee_data(emp_id)