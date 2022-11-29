class BankAccount:
	"""A regular bank account"""
	def __init__(self, initial_balance=0):
		self._balance = initial_balance

	def deposit(self, amount):
		if amount > 0:
			self._balance += amount
			print(f"Deposited ${amount}")

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self._balance -= amount
			print(f"Withdrew ${amount}")

	def __repr__(self):
		# instance_name = SavingsBankAccount, HighInterestSavingsBankAccount
		# __mro__ -> tupple(class names in full inheritance chain from subslasses to object)
		instance_name = "".join([t.__name__ for t in type(self).__mro__[:-1]])
		return f"A {instance_name} with ${self.balance} in it"

	@property
	def balance(self):
		return self._balance


class Savings(BankAccount):
	"""Like a bank account but interest-earning"""
	interest = 0.0035

	def pay_interest(self):
		interest_earned = round(self.balance * self.interest, 2)
		self.deposit(interest_earned)


class HighInterest(Savings):
	"""
	Like a savings account but with much higher interest rate in exchange for a higher withdrawal fee
	"""
	interest = 0.007

	def __init__(self, initial_balance=0, withdrawal_fee=5):
		super().__init__(initial_balance)
		self.withdraw_fee = withdrawal_fee

	def withdraw(self, amount):
		if 0 < amount + self.withdraw_fee <= self.balance:
			self._balance -= self.withdraw_fee
			super().withdraw(amount)


class LockedIn(HighInterest):
	"""
	Like a high interest savings account but having much higher interest in
	exchange for the lack of ability to withdraw early
	"""
	interest = 0.009

	def withdraw(self, amount):
		return f"Can't make early withdrawal from a Locked-in Savings Account"


b = BankAccount(100)
print(b)

s = Savings(230)
print(s)

l = LockedIn(1000)
print(l)

s.deposit(200)
s.pay_interest()
s.withdraw(20)

hi = HighInterest(200)
hi.deposit(20)
hi.pay_interest()
print(hi)
hi.withdraw(1.54)

print(hi)
