
from datetime import datetime

class TicketData:
    def __init__(self, ticket_number: str,task_number: str,tasked_user: str,task_title: str,task_description: str,date_time_assigned: str,task_due_date: str,completed_yes_no: str):
        self.ticket_number = ticket_number
        self.task_number = task_number
        self.tasked_user = tasked_user
        self.task_title = task_title
        self.task_description = task_description
        self.task_due_date = task_due_date
        self.date_time_assigned = date_time_assigned
        self.completed_yes_no = completed_yes_no

class TaskTicket(TicketData):
    def __init__(self,ticket_number,task_number,tasked_user,task_title,task_description,date_time_assigned,task_due_date,completed_yes_no):
        super().__init__(ticket_number,task_number,tasked_user,task_title,task_description,date_time_assigned,task_due_date,completed_yes_no)
        return print(
            "\n________________________________________________________" +
            "________________________________________________________\n\n" +
            f"Task title:                {task_title}\n" + 
            f"Date assigned:             {date_time_assigned}\n" + 
            f"Due date:                  {task_due_date}\n" + 
            f"Task description:        \n{task_description}\n" + 
            "________________________________________________________" +
            f"{ticket_number}" +
            "________________________________________________________\n"
            )
        

class ReviewTicket(TicketData):
    def __init__(self, ticket_number, task_number, tasked_user, task_title, title_description, date_time_assigned, task_due_date, completed_yes_no):
        super().__init__(ticket_number, task_number, task_title, title_description, date_time_assigned, task_due_date, completed_yes_no)
        date_time_submitted = datetime.now()
        admin_message = ""
        if date_time_submitted > task_due_date:
            admin_message = f"{tasked_user}'s task is late"
            

        return print(
            "________________________________________________________" +
            "________________________________________________________\n\n" +
            f"Task title:                {task_title}\n"
            f"Assigned to:               {tasked_user}\n" +
            f"Due date:                  {task_due_date}\n" +
            f"Date and time submitted: \n{date_time_submitted}\n"
            f"                {admin_message}" +
            "________________________________________________________" +
            f"{ticket_number}" +
            "________________________________________________________\n"
            )