# 1. LOAD DATA FUNCTIONS:
'''

Personal_data.txt format:
[[index: int, username: str, login_password: str, first_name: str, surname: str, age: str, date_registered: str, email_address: str], 
[index: int, username: str, login_password: str, first_name: str, surname: str, age: str, date_registered: str, email_address: str]]

'''
# A - Load personal data method
personal_data_list = []
with open("personal_data.txt", "r") as file:
    for line in file:
        stripped_personal_data = line.strip().split(", ")
        personal_key_values = {
            "index": int(stripped_personal_data[0]),
            "username": stripped_personal_data[1],
            "login_password": stripped_personal_data[2],
            "first_name": stripped_personal_data[3],
            "surname": stripped_personal_data[4],
            "age": stripped_personal_data[5],
            "date_registered": stripped_personal_data[6],
            "email_address": stripped_personal_data[7]
        }
        personal_data_list.append(personal_key_values)
print(f"1.A \n{personal_data_list}\n")


'''
# task_data.txt format:
# [[index: int, username: str, task_title: str, task_description: str, date_time_assigned: str, task_due_date: str, completed_yes_no: str],
# [index: int, username: str, task_title: str, task_description: str, date_time_assigned: str, task_due_date: str, completed_yes_no: str]]

'''

# B - Load task data method
task_data_list = []
with open("task_data.txt", "r") as file:
    for line in file:
        stripped_task_data = line.strip().split(", ")
        task_data_key_values = {
            "index": int(stripped_task_data[0]),
            "username": stripped_task_data[1],
            "task_title": stripped_task_data[2],
            "task_description": stripped_task_data[3],
            "date_time_assigned": stripped_task_data[4],
            "task_due_date": stripped_task_data[5],
            "completed_yes_no": stripped_task_data[6],
        }
        task_data_list.append(task_data_key_values)
print(f"1.B \n{task_data_list}\n")

'''
# review_task_data.txt format:
# [[index: int, username: str, task_due_date: str, task_sub_time: str],
# [index: int, username: str, task_due_date: str, task_sub_time: str]]

'''

# C - Load review task data
review_task_list = []
with open("task_data.txt", "r") as file:
    for line in file:
        stripped_review_data = line.strip().split(", ")
        review_data_key_values = {
            "index": int(stripped_review_data[0]),
            "username": stripped_review_data[1],
            "task_due_date": stripped_review_data[2],
            "task_sub_time": stripped_review_data[3],
        }
        review_task_list.append(review_data_key_values)
print(f"1.C \n{review_task_list}\n")

# 2 - PRINT TICKET FUNCTIONS:
# C - Print task ticket (TT) FOR USER

task_data_list = []
with open("task_data.txt", "r") as file:
    for index, line in enumerate(file, start = 1):
        raw_task_data = line.strip().split(", ")
        task_data_list.append(raw_task_data)
        #print(f"1.B \n{task_data_list}\n")
'''
print(
    "\n_______________________________________________________" +
    "f"TT{task_ticket_number}"
    "_________________________________________________________\n\n" +
    f"Task:                      {task_title}\n" + 
    f"Date assigned:             {date_time_assigned}\n" + 
    f"Task due date:             {task_due_date}\n" + 
    f"Task description:        \n{task_description}\n" +
    "________________________________________________________" +
    "________________________________________________________\n"
    )
'''
# B - Print task ticket (TT) FOR ADMIN
'''
print(
    "\n_______________________________________________________" +
    "f"TT{index}"
    "_________________________________________________________\n\n" +
    f"Username:                  {username}\n" +
    f"Task:                      {task_title}\n" + 
    f"Date assigned:             {date_time_assigned}\n" + 
    f"Task due date:             {task_due_date}\n" +
    "________________________________________________________" +
    "________________________________________________________\n"
    )
'''


# C - Print review ticket (RT) FOR ADMIN
'''
print(
    "\n_______________________________________________________" +
    "f"RT{index}"
    "_________________________________________________________\n\n" +
    f"Username:                  {username}\n" + 
    f"Date assigned:             {date_time_assigned}\n" + 
    f"Task due date:             {task_due_date}\n" +
    f"                           {warning_message}\n" +
    f"Task:                      {task_title}\n" +
    f"Task description:        \n{task_description}\n" + 
    "________________________________________________________" +
    "________________________________________________________\n"
    )
'''