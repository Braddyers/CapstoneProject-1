#=====importing libraries=====#
from datetime import datetime
#=====funtions section=====#

# LOAD DATA FUNCTIONS:
# Read and convert task_data.txt into a nested list
def load_task_data(file_path):
    task_ticket_list = []
    with open(file_path, "r") as file:
        for index, line in enumerate(file, start = 1):
            task_data = line.strip().split(", ")               #task_data or line?
            task_ticket_list.append(task_data)
            
            print(task_ticket_list)
            print(task_data)
            print(index)
    return task_ticket_list

# Read and convert user_data.txt into a nested list:
def load_user_data(file_path):
    review_ticket_list = []
    with open(file_path, "r") as file:
        for index, line in enumerate(file, start = 1):
            review_data = line.strip().split(", ")
            review_ticket_list.append(review_data)
            
            print(review_ticket_list)
            print(review_data)
            print(index)
    return review_ticket_list

# Read and convert personal_data.txt into a nested list:
def load_personal_data(file_path):
    personal_data_list = []
    with open(file_path, "r") as file:
        for index, line in enumerate(file, start = 1):
            personal_data = line.strip().split(", ")
            personal_data_list.append(personal_data)
            
            print(personal_data_list)
            print(personal_data)
            print(index)
    return personal_data_list
        
    
    
'''
def print_task_tickets(file_path):
    for index, task in enumerate(task, start=1):
        task_data = line.strip().split(", ")               #task_data or line?
        )
        print("________________________________________________________" +
              "________________________________________________________\n")
        print(f"Ticket number:             {index}")
        print(f"Assigned to:               {tasked_user}")
        print(f"Task:                      {task_title}")
        print(f"Date assigned:             {date_assigned}")
        print(f"Task due date:             {due_date}")
        print(f"Task description:        \n{task_description}\n")
        print("________________________________________________________" +
              "________________________________________________________\n")
'''