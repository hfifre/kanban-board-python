from task import *

class Board:

    def __init__(self):
        self.columns = {State.TODO : [], State.IN_PROGRESS : [], State.TESTING : [], State.DONE : []}

    def add_task(self, title, description):
        self.columns[State.TODO].append(Task(title, description))
            
    def search_for_task_with_title(self, title):
        for task_list in self.columns.values():
            for task in task_list:
                if task.title == title:
                    return task
                
    def move_task(self, task, state_destination):
        self.columns[task.state].remove(task)
        self.columns[state_destination].append(task)
        task.state = state_destination

    def display_tasks(self):
        for state in self.columns.values():
            for task in state:
                print(f"state of {task.title} : {task.state.name}")
        print()

# board = Board()
# board.add_task("create UI", "tmtc")
# board.add_task("create Task", "tmtc")
# board.add_task("integration", "tmtc")
# board.add_task("Finalize process", "tmtc")

# board.display_tasks()

# board.move_task(board.search_for_task_with_title("create UI"), State.IN_PROGRESS)
# board.move_task(board.search_for_task_with_title("create Task"), State.IN_PROGRESS)
# board.move_task(board.search_for_task_with_title("integration"), State.TESTING)
# board.display_tasks()
# board.move_task(board.search_for_task_with_title("create UI"), State.TESTING)
# board.display_tasks()
# board.move_task(board.search_for_task_with_title("create UI"), State.DONE)
# board.move_task(board.search_for_task_with_title("integration"), State.IN_PROGRESS)
# board.move_task(board.search_for_task_with_title("Finalize process"), State.TESTING)
# board.display_tasks()