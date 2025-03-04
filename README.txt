README

Installation guide:
Basic user manual:
Common usages:

This is a list of formatting for various files and outputs:

personal_data.txt format:
[[index: int, username: str, login_password: str, first_name: str, surname: str, age: str, date_registered: str, email_address: str], 
[index: int, username: str, login_password: str, first_name: str, surname: str, age: str, date_registered: str, email_address: str]]

task_data.txt format:
[[username: str, due_date_u: str, time_recieved: str], 
[username: str, due_date:_u str, time_recieved: str]]

task_data.txt format:
[[tasked_user: str, task_title: str, task_descrip: str, date_time_assigned: str, due_date: str, completed_yes_no: str],
[tasked_user: str, task_title: str, task_descrip: str, date_time_assigned: str, due_date: str, completed_yes_no: str]]

Output tickets:

Task ticket format:
"________________________________________________________" +
"________________________________________________________\n\n" +
f"Ticket number:             {index}\n" +
f"Assigned to:               {tasked_user}\n" +
f"Task:                      {task_title}\n" + 
f"Date assigned:             {date_assigned}\n" + 
f"Task due date:             {due_date}\n" + 
f"Task description:        \n{task_description}\n" +  
"________________________________________________________" +
"________________________________________________________\n"


Review ticket format:
"________________________________________________________" +
"________________________________________________________\n\n" +
f"Ticket number:             {index}\n"
f"Assigned to:               {tasked_user}\n" +
f"Ticket due date:           {due_date}\n" +
f"Time task completed:     \n{time_recieved}\n"
"________________________________________________________" +
"________________________________________________________\n"