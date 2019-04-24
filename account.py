class Account():
	"""docstring for ClassName"""
	def __init__(self, first_name,second_name,balance):
		self.first_name = first_name
		self.second_name = second_name
		self.balance = balance

	def Welcome(self):
		return "Hello {} {},your balance is {}".format(self.first_name,self.second_name,self.balance)
	def deposit(self,new_balance):
		self.balance=self.balance + new_balance
		return "Hello {} {}, you have deposited {}".format(self.first_name,self.second_name,new_balance)
	def withdraw(self,amount):
		if amount<self.balance:
			self.balance=self.balance-amount
			return "Hello {} {},you have successfully withdrawn {}.".format(self.first_name,self.second_name,amount)
		else:
			return "Hello {} {},you have insufficient funds to withdraw {}.".format(self.first_name,self.second_name,amount)
	def show_balance(self):
		show_balance=self.balance
		return "Hello {} {},your current mpesa balance is {}".format(self.first_name,self.second_name,self.balance)		
	    