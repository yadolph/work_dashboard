

class Dashboard:
	
	def __init__(self, name):
		self.current_tasks = [] # Здесь должна быть загрузка файла
		self.current_employees = [] # Здесь должна быть загрузка файла
		self.name = name

	def create_new_task(self, description, responsible_employee, due_date):
		new_task = Task(description, responsible_employee, due_date, self)
		self.current_tasks.append(new_task)

	def list_all_tasks(self):
		if self.current_tasks:
			for task in self.current_tasks:
				print(f'Задача: {task.description} \nОтветственный: {task.responsible_employee.name} \nСрок: {task.due_date}')
		else:
			print('Список задач пуст')

	def create_new_employee(self, first_name, last_name):
		new_employee = Employee(first_name, last_name)
		self.current_employees.append(new_employee)

	def list_all_employees(self):
		if self.current_employees:
			for employee in self.current_employees:
				print(f'{employee.first_name} {employee.last_name}')
		else:
			print('Список работников пуст')

class Employee:

	def __init__(self, first_name, last_name):
		self.current_tasks = []
		self.first_name = first_name
		self.last_name = last_name
		self.name = f'{first_name} {last_name}'

class Task:
	
	def __init__(self, description, responsible_employee, due_date, dashboard):
		self.description = description
		self.due_date = due_date
		self.dashboard = dashboard
		for employee in self.dashboard.current_employees:
			if employee.last_name in responsible_employee:
				self.responsible_employee = employee
				#Добавить обработку случая, когда такого работника нет
	

def employee_adder(dashboard):
	print('Добавим нового работника?')
	first_name = input('Введите имя работника: ')
	last_name = input('Введите фамилию работника: ')
	check = 0
	for employee in dashboard.current_employees:
		if last_name in employee.last_name:
			print('Такой работник уже зарегистрирован!')
			check = 1
	if check == 0:
		dashboard.create_new_employee(first_name, last_name)

def task_adder(dashboard):
	print('Добавляем новое задание!')
	description = input('Введите суть задания: ')
	responsible_employee = input('Введите фамилию ответственного: ')
	due_date = input('Введите срок исполнения задания: ')
	dashboard.create_new_task(description, responsible_employee, due_date)

def main_menu(dashboard):
	print('\nДобро пожаловать в доску задач! \nВведите команду: \nea - добавить нового работника \nta - добавить новое задание')
	print('le - вывести список работников \nlt - вывести список всех задач')
	choice = input('Ваш выбор: ')
	if choice == 'ea':
		employee_adder(dashboard)
	elif choice == 'ta':
		task_adder(dashboard)
	elif choice == 'le':
		dashboard.list_all_employees()
	elif choice == 'lt':
		dashboard.list_all_tasks()




main_dashboard = Dashboard('main')

while True:
	main_menu(main_dashboard)







