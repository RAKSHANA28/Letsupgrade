class Bankaccount: 
	def owner(self):
		amount = float(input("Enter amount to be deposited: "))
		self.balance += amount 
		print("\n Amount Deposited:", amount)
	def withdraw(self): 
		amount = float(input("Enter amount to be withdrawn: ")) 
		if self.balance >= amount: 
			self.balance -= amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

