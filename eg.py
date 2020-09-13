Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/Users/jasminuser/Desktop/ass4.py =================
>>> class Bankaccount: 
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

