
# Create Class Todolist
class Todolist:

	# Initiate class Todolist with "date" and list("tasks") class attributes
    def __init__(self, date, tasks = []):
    	self.date = date
    	self.tasks = tasks
        
    # Method to add task to the list where "task" attribute is the new task   
    def add_task(self, task):
        self.tasks.append(task)

    # Method to mark task as complete where "x" is the index of completed task
    def mark_as_complete(self, x):
    	self.tasks[x] = self.tasks[x] + u" \u2713" # mark sign

    # Method to delete task "x" is the index of task to be deleted
    def delete_task(self, x):
    	del(self.tasks[x])

    # Method to make a line by line list of tasks
    def li(self, x):
    	for i in x:
    		print(f"{i}\n") 

    # Method to show tasks 
    def show_tasks(self):
       print(f"Your Tasks For {self.date} are:\n") # heading
       self.li(self.tasks) # line by line list


#Test ----------------------------------------------------

# instance of the class Todolist
todo = Todolist("20/05/2024", [])
# add a task
todo.add_task("Wake up")
# add a task
todo.add_task("Brush teeth")
# add a task
todo.add_task("Perform ablution")
# add a task
todo.add_task('Pray')
# add a task
todo.add_task("Take a bath")
# mark third task as complete
todo.mark_as_complete(2)
todo.mark_as_complete(3)
# show all tasks
todo.show_tasks()
# delete second task
todo.delete_task(1)
# show all task
todo.show_tasks()