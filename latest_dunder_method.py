
class Ticket:
    def __init__(self, tasked_user: str, task_title: str, title_description: str, date_time_assigned: str, due_date: str, completed_yes_no: str):
            self.tasked_user = tasked_user
            self.task_title = task_title
            self.title_description = title_description
            self.due_date = due_date
            self.date_time_assigned = date_time_assigned
            self.completed_yes_no = completed_yes_no

class TaskTicket(Ticket):
    def __init__(self, tasked_user, task_title, title_descrip, date_time_assigned, due_date, completed_yes_no):
         super().__init__(tasked_user, task_title, title_descrip, date_time_assigned, due_date, completed_yes_no)

class ReviewTicket(Ticket):
     def __init__(self, tasked_user, task_title, title_descrip, date_time_assigned, due_date, completed_yes_no):
         super().__init__(tasked_user, task_title, title_descrip, date_time_assigned, due_date, completed_yes_no)
