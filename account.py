pclass Account():
	"""docstring for ClassName"""
	def __init__(self, first_name,second_name):
		self.first_name = first_name
		self.second_name = second_name
		self.balance = 0
		self.deposits = []
		self.withdrawals = []
		self.loan = 0

	def Welcome(self):
		return "Hello {} {},welcome to your account,your balance is {}".format(self.first_name,self.second_name,self.balance)
	def deposit(self,new_balance):
		self.balance=self.balance + new_balance
		self.deposits.append(new_balance)
		return "Hello {} {}, you have deposited {}".format(self.first_name,self.second_name,new_balance)
	def withdraw(self,amount):
		if amount<self.balance:
			self.balance=self.balance-amount
			self.withdrawals.append(amount)
			return "Hello {} {},you have successfully withdrawn {}.".format(self.first_name,self.second_name,amount)
		else:
			return "Hello {} {},you have insufficient funds to withdraw {}.".format(self.first_name,self.second_name,amount)
	def show_balance(self):
		show_balance=self.balance
		return "Hello {} {},your current mpesa balance is {}".format(self.first_name,self.second_name,self.balance)	
	def show_deposits(self):
		for new_balance in self.deposits:
			print(new_balance)
	def show_withdrawals(self):
		for amount in self.withdrawals:
			print(amount)
	def give_loan(self,amount): 
		if len(self.deposits)>=5 and amount < (1/3)*(sum(self.deposits)) and self.loan==0:
			self.loan=self.loan+amount
			self.balance = self.balance + amount
			return "Hello {} {}, you have qualified for a loan of K.shs {},your outstanding loan balance is {}.".format(self.first_name,self.second_name,amount,self.balance)
		else:
             return "Hello {} {}, you don't qualify to borrow {},Read the terms and conditions to qualify for this service".format(self.first_name,self.second_name,amount)
    def repay_loan(self,amount):
    	if self.loan==0:
    		return "You do not have an outstanding loan, check our terms and conditions to borrow our loan service"
    	elif amount<self.loan:
    		self.loan= self.loan-amount
    		self.balance = self.balance-amount
    		return "Hello {} {},you have repaid {} from your loan, your outstanding loan balance is {}."format(self.first_name,second_name,amount,self,balance)
    	elif amount==self.loan:
    		self.loan= self.loan- amount
    		self.balance = self.balance-amount
    		return "Hello {} {}, you have fully repaid your loan,your current balance is {}.".format(self.first_name,self.second_name,self.balance)
    	elif amount>self.loan:
    		excess=amount-self.loan
    		self.balance=self.balance-amount
    		self.balance=self.balance+excess
    		self.loan=(self.loan+excess)-amount
    		return "Hello {} {},you have successfully repaid your loan,your excess amount deposited is {}, your outstanding bakance is {}".format(self.first_name,self.second_name,excess,self.balance)

    		

            
		

				

					































































		



				
	    