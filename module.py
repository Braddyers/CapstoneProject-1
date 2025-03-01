#=====importing libraries=====#
from datetime import datetime
#=====funtions section=====#

# LOAD DATA FUNCTIONS:
# Read and convert task_data.txt into a nested list
def load_task_data(file_path):
    task_ticket_list = []
    with open(file_path, "r") as file:
        for task_number, line in enumerate(file, start = 1):
            task_data = line.strip().split(", ")    
            task_ticket_list.append(task_data)
            
            print(task_ticket_list)
            print(task_data)
            print(task_number)
    return task_ticket_list

# Read and convert user_data.txt into a nested list THIS IS WRONG: review ticket list?
def load_user_data(file_path):
    review_ticket_list = []
    with open(file_path, "r") as file:
        for line in enumerate(file, start = 1):
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

# PRINT TICKET FUNCTION       
def print_task_ticket(file_path) -> str:
    for task_number, tasked_user, task_title, task_description, date_time_assigned, due_date, task_ticket_number in file_path:
        return print(
            "\n________________________________________________________" +
            "________________________________________________________\n\n" +
            f"Ticket number:             {task_number}\n" +
            f"Assigned to:               {tasked_user}\n" +
            f"Task:                      {task_title}\n" + 
            f"Date assigned:             {date_time_assigned}\n" + 
            f"Task due date:             {due_date}\n" + 
            f"Task description:        \n{task_description}\n" +
            "________________________________________________________" +
            f"{task_ticket_number}"
            "________________________________________________________\n"
            )    