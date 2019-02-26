class Task:
	"""docstring for Task"""
	def __init__(self, description, due_date):
		self.description = description
		self.due_date = due_date

	def __str__(self):
		return ("{} task is due on: {}".format(self.description, self.due_date))
	
	
Task1 = print(Task("Do the dishes","Monday"))


Task2 = print(Task("Eat a burger","Tuesday 11th 6:00am"))


Task3 = print(Task("Finish Work","Friday 25th 11:00pm"))



#Exercise2
class TodoList:
	"""docstring for TodoList"""
tasks_to_do = []
def __init__(self, add_task):
	self.add_task = add_task



@classmethod
def add_task(cls,description, due_date):
	tasks = Task(description, due_date)
	cls.tasks_to_do.append(tasks)


	
Task4 = TodoList.add_task("clean up house", "Sunday")
Task5 = TodoList.add_task("Code", "Friday 9:00pm")
Task6 = TodoList.add_task("Swim", "Wedensday 8:00am")
		
print(TodoList.tasks_to_do)		
print(tasks_to_do)