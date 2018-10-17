'''
							PROBLEM STATEMENT
							==================
Case Study: Income Tax Calculator
===========
Most of the chapters in this book include a case study that illustrates 
the software development process. This approach may seem overly elaborate 
for small programs, but it scales up well when programs become larger. 
The first case study develops a program that calculates income tax.
Each year, nearly everyone with an income faces the unpleasant task of 
computing his or her income tax return. If only it could be done as easily 
as suggested in this case study! We start with the customer request phase.

Request: The customer requests a program that computes a person’s income tax
========
'''

''' 
This problem is solved By "Fairoz Ahmed Shaik" and Analysed using "WATERFALL MODEL"
						  ====================
	==========Pseudo_Code==========
	1.Input the gross Income and number of dependents
	2.calc the taxable income using following formula::
	3.taxable=gross income - standard deduction - (taxpayer * no of dependents)
	4.compute the income tax using following formula::
	5.income_tax = taxable * 0.20 (Charged aflat tax of 20% so, 0.20)
	6.print the income_tax

'''

def IncomeTax_Compute():
	#standard Deduction
	standard=10000
	#taxpayers Deduction
	taxpayer=3000
	#Asking input from user to calc gross_income
	gross_income=float(input('enter your income: '))
	#the grossIncome should be more than a lakh.appling condition
	if gross_income>=100000:
		#asking no of dependents in their family
		no_of_dependents=int(input('Enter dependents: '))
		#formula to calculate Taxable income
		taxable_income = gross_income - standard - (taxpayer * no_of_dependents)
		#Formula to calculate total income tax to the user
		income_tax = taxable_income * 0.20
		#printing the income tax that they need to pay
		income_tax=round(income_tax,2)
		print("%.2f"%income_tax)
	else:
		#if income is low then this statement will execute
		print('You dont have to pay Income Tax. Your income is low')
IncomeTax_Compute()