class employee(object):
	"""docstring for employee"""
	empcount = 0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		employee.empcount += 1

	def displaycount(self):
		print("Total employee:" + str(employee.empcount))

	def printemployee(self):
		print("name:" + str(self.name) + "salary:" + str(self.salary))

emp1 = employee("Marry", 1000)
emp2 = employee("David", 2000)

emp1.name = "Peter"
#change emp1.name into Peter
emp1.printemployee()
emp2.printemployee()
print(employee.empcount)


		
		
		