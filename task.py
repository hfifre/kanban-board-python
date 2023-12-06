import locale
import datetime

locale.setlocale(locale.LC_TIME, 'fr-FR')

class Task:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.contributors = []
        self.sub_tasks = []
        self.event_history = []
        self.add_event(datetime.datetime.now().strftime("%A, %d-%m-%Y %H:%M:%S"))
    
    def add_contributor(self,contributor):
        self.contributors.append(contributor)

    def add_sub_task(self,sub_task):
        self.sub_tasks.append(sub_task)

    def add_event(self, event):
        self.event_history.append(event)