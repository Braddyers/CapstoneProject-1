
class IssueTicket:
    def __init__(self, task_number: str, tasked_user: str, task_title: str, task_description: str, date_time_assigned: str, due_date: str, completed_yes_no: str):
        self.task_number = task_number
        self.tasked_user = tasked_user
        self.task_title = task_title
        self.task_description = task_description
        self.due_date = due_date
        self.date_time_assigned = date_time_assigned
        self.completed_yes_no = completed_yes_no

class TaskTicket(IssueTicket):
    def __init__(self, task_number, tasked_user, task_title, task_description, date_time_assigned, due_date, completed_yes_no):
        super().__init__(task_number, tasked_user, task_title, task_description, date_time_assigned, due_date, completed_yes_no)
        return print(
            "Task Ticket:" +
            "\n________________________________________________________" +
            "________________________________________________________\n\n" +
            f"Ticket number:             {task_number}\n" +
            f"Assigned to:               {tasked_user}\n" +
            f"Task:                      {task_title}\n" + 
            f"Date assigned:             {date_time_assigned}\n" + 
            f"Task due date:             {due_date}\n" + 
            f"Task description:        \n{task_description}\n" + 
            "________________________________________________________" +
            "________________________________________________________\n"
            )
        


class ReviewTicket(IssueTicket):
    def __init__(self, ticket_number, tasked_user, task_title, title_description, date_time_assigned, due_date, completed_yes_no):
        super().__init__(ticket_number, tasked_user, task_title, title_description, date_time_assigned, due_date, completed_yes_no)
        
        return print(
        "________________________________________________________" +
        "________________________________________________________\n\n" +
        f"Task title:                {task_title}\n"
        f"Assigned to:               {tasked_user}\n" +
        f"Ticket due date:           {due_date}\n" +
        f"Time task completed:     \n{time_recieved}\n"
        "________________________________________________________" +
        "________________________________________________________\n"
        )