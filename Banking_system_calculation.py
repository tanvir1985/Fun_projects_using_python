## Simple account balance maintain using OOP concept
class User(): # parent class : User
	def __init__(self,name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def show_details(self):
		print("Personal details")
		print("Name",self.name)
		print("Age",self.age)
		print("Gender",self.gender)

##child class inherit all properties of parent class
class Bank(User): 
	def __init__(self,name,age,gender):
		super().__init__(name,age,gender)
		self.balance = 0
	
	def deposits(self,amount):
		self.amount = amount
		self.balance = self.balance+self.amount
		print("Account balance has been updated($):",self.balance)

	def withdraw(self,amount):
		self.amount = amount
		if self.amount>self.balance:
			print("Insufficient fund")
			print("Available balance", self.balance)
		else:
			self.balance = self.balance-self.amount
			print("Account balance has been updated", self.balance)

	def view_balance(self):
		self.show_details()
		print("Account balance has been updated", self.balance)








Johan = Bank('Johan',21,'Male')
Johan.deposits(200)
Johan.withdraw(50)
Johan.view_balance()





