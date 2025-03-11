#=====importing libraries=====#
from datetime import datetime
#=====funtions section=====#

# LOAD DATA FUNCTIONS:
# Read and convert personal_data.txt into a nested list WHICH METHOD BELOW IS MORE USEFUL?
def load_personal_data(file_path):
    personal_data_list = []
    with open("personal_data.txt", "r") as file:
        for line in file:
            keys = line.strip().split(", ")
            personal_key_values = {
                "index": int(keys[0]),
                "username": str(keys[1]),
                "login_password": str(keys[2]),
                "first_name": str(keys[3]),
                "surname": str(keys[4]),
                "age": int(keys[5]),
                "date_registered": str(keys[6]),
                "email_address": str(keys[7])
            }
            personal_data_list.append(personal_key_values)
    return personal_data_list

def load_personal_data(file_path):
    personal_data_list = []
    with open(file_path, "r") as file:
        for line in file:
            raw_personal_data = line.strip().split(", ")  # Split each line into a list
            personal_data_list.append(raw_personal_data)  # Append the list to personal_data_list
    return personal_data_list

def load_personal_data(file_path):
    personal_data_list = []
    with open(file_path, "r") as file:
        for index, line in enumerate(file, start = 1):
            raw_personal_data = line.strip().split(", ")
            personal_data_list.append(raw_personal_data)
            
            print(personal_data_list)
            print(raw_personal_data)
            print(index)
    return personal_data_list

# Read and convert user_data.txt into a nested list THIS IS WRONG: review ticket list?
def load_task_data(file_path):
    task_data_list = []
    with open(file_path, "r") as file:
        for line in file:
            raw_task_data = line.strip().split(", ")  # Split each line into a list
            task_data_list.append(raw_task_data)  # Append the list to personal_data_list
    return task_data_list

# Read and convert review task_data.txt into a nested list:


def load_review_task_list(file_path):
    review_task_list = []
    with open(file_path, "r") as file:
        for line in file:
            raw_review_task_data = line.strip().split(", ")  # Split each line into a list
            review_task_list.append(raw_review_task_data)  # Append the list to personal_data_list
    return review_task_list

# PRINT TASK TICKET FUNCTION       
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