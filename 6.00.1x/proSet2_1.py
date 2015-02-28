# Write a program to calculate the credit card balance after 
# one year if a person only pays the minimum monthly payment required by the credit card company each month.
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monInRate = annualInterestRate/12
def miniPayRate(inbalance,monthPayRate):
	return inbalance*monthPayRate

def miniInPay(inbalance,monInRate):
	return inbalance*monInRate

def inputCreditPay(inbalance,monthPayRate,monInRate):
	total = 0
	for x in range(1,13):
		miniPay = miniPayRate(inbalance,monthPayRate)
		inbalance = inbalance - miniPay
		miniIn = miniInPay(inbalance,monInRate)
		inbalance = inbalance + miniIn
		total = total + miniPay
		print ("Month:"+str(x)+"\n")
		print ("Minimum monthly payment:%.2f\n"%miniPay)
		print ("Remaining balance:%.2f\n"%inbalance)
	print ("Total paid:%.2f\n"%total)
	print ("Remaining balance:%.2f\n"%inbalance)

inputCreditPay(balance,monthlyPaymentRate,monInRate)