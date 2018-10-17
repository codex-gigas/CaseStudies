'''
Case Study: An Investment Report
It has been said that compound interest is the eighth wonder of the world. Our next
case study, which computes an investment report, shows why.

Request
Write a program that computes an investment report

program: Investment.py
Author: Fairoz Ahmed Shaik 

pseudocode :

Input the starting balance, number of years, and interest rate
Set the total interest to 0.0
Print the table's heading
For each year
	compute the interest
	compute the ending balance
	print the year, starting balance, interest, and ending balance
	update the starting balance
	update the total interest
print the ending balance and the total interest

'''

#Solution 
#Ask for inputs from user

invest=float(input("Enter the investement ammount: "))
years= int(input("Enter the no of years: "))
rate= int(input("Enter the rate %: "))
#converting rate into decimal
rate=rate/100
total_interest=0.0
#Displaying the Headers 
print("%4s%18s%10s%16s" % ("Year", "Starting balance","Interest", "Ending balance"))
for year in range(1,years+1):
	interest=invest*rate

	endBalance=invest+interest

	print("%4d%18.2f%10.2f%16.2f"%(year, invest, interest, endBalance))
	invest=endBalance

	total_interest+=interest

print("\nEnding Balance is $%0.2f"%endBalance)
print("Total Interest is $%0.2f"%total_interest)

'''
Output:

Enter the investment amount: 10000
Enter the number of years: 5
Enter the rate as a %: 5
Year 	Starting balance 	Interest 	Ending balance
 1 				10000.00 	  500.00 		  10500.00
 2 				10500.00 	  525.00 		  11025.00
 3				 1025.00 	  551.25 		  11576.25
 4 				11576.25 	  578.81 		  12155.06
 5 				12155.06 	  607.75 		  12762.82

Ending balance: $12762.82
Total interest earned: $2762.82
'''