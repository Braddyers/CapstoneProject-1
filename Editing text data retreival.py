# 1. LOAD DATA FUNCTIONS:
'''

Personal_data.txt format:
[[index: int, username: str, login_password: str, first_name: str, surname: str, age: str, date_registered: str, email_address: str], 
[index: int, username: str, login_password: str, first_name: str, surname: str, age: str, date_registered: str, email_address: str]]
'''

# A - Load personal data metho
personal_data_list = []
with open("personal_data.txt", "r") as file:
    for line in file:
        p = line.strip().split(", ")
        personal_key_values = {
            "index": int(p[0]),
            "username": str(p[1]),
            "login_password": str(p[2]),
            "first_name": str(p[3]),
            "surname": str(p[4]),
            "age": int(p[5]),
            "date_registered": str(p[6]),
            "email_address": str(p[7])
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
        t = line.strip().split(", ")
        task_key_values = {
            "index": int(t[0]),
            "username": str(t[1]),
            "task_title": str(t[2]),
            "task_description": str(t[3]),
            "date_time_assigned": str(t[4]),
            "task_due_date": str(t[5]),
            "completed_yes_no": str(t[6]),
        }
        task_data_list.append(task_key_values)
print(f"1.B \n{task_data_list}\n")

'''
# review_task_data.txt format:
# [[index: int, username: str, task_due_date: str, task_sub_time: str],
# [index: int, username: str, task_due_date: str, task_sub_time: str]]

'''

# C - Load review task data
review_task_list = []
with open("review_task_data.txt", "r") as file:
    for line in file:
        r = line.strip().split(", ")
        review_key_values = {
            "index": int(r[0]),
            "username": str(r[1]),
            "task_due_date": str(r[2]),
            "task_sub_time": str(r[3]),
        }
        review_task_list.append(review_key_values)
print(f"1.C \n{review_task_list}\n")

# 2 - PRINT TICKET FUNCTIONS:
# A - Print task ticket (TT) FOR USER

task_data_list = []
with open("task_data.txt", "r") as file:
    for line in file:
        t = line.strip().split(", ")
        task_key_values = {
            "index": int(t[0]),
            "username": t[1],
            "task_title": t[2],
            "task_description": t[3],
            "date_time_assigned": t[4],
            "task_due_date": t[5],
            "completed_yes_no": t[6],
        }
        task_data_list.append(task_key_values)

print(f"2.A \nYou have {len(task_data_list)} tasks due, all listed below:")
for task_ticket in task_data_list:
    print("\n__________________________________" +
        f"TT{task_ticket["index"]}"
        "_________________________________\n\n" +
        f"Task:                      {task_ticket["task_title"]}\n" + 
        f"Date assigned:             {task_ticket["date_time_assigned"]}\n" + 
        f"Task due date:             {task_ticket["task_due_date"]}\n" + 
        f"Task description:        \n{task_ticket["task_description"]}\n" +
        "____________________________________" +
        "____________________________________"
        )
'''

task_data_list = []
with open("task_data.txt", "r") as file:
    for line in file:
        t = line.strip().split(", ")
        task_key_values = {
            "index": int(t[0]),
            "username": t[1],
            "task_title": t[2],
            "task_description": t[3],
            "date_time_assigned": t[4],
            "task_due_date": t[5],
            "completed_yes_no": t[6],
        }
        task_data_list.append(task_key_values)

print(f"2.A \nYou have {len(task_data_list)} tasks due, all listed below:")
for task_ticket in task_data_list:
    print("\n__________________________________" +
        f"TT{task_ticket["index"]}"
        "_________________________________\n\n" +
        f"Task:                      {task_ticket["task_title"]}\n" + 
        f"Date assigned:             {task_ticket["date_time_assigned"]}\n" + 
        f"Task due date:             {task_ticket["task_due_date"]}\n" + 
        f"Task description:        \n{task_ticket["task_description"]}\n" +
        "____________________________________" +
        "____________________________________"
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