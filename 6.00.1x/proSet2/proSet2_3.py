# Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
# Produce the same return value as you did in Problem 2.

# Init
balance = 320000
annualInterestRate = 0.2

monthlyInRate = annualInterestRate/12
newbalance = balance
loPay = balance/12
hiPay = (balance*(1+monthlyInRate)**12)/12
# print hiPay
# print loPay
epsilon = 0.01
# guessed = False
# while not guessed:
# x= monthlyPayment*12 - balance
# while abs(x)>epsilon:
while round(loPay,2)!=round(hiPay,2):
	monthlyPayment = (loPay +hiPay)/2.0
	newbalance = balance
	# hlcompare = hiPay - loPay
	for x in range(1,13):
		newbalance -= monthlyPayment
		interest = monthlyInRate * newbalance
		newbalance += interest
        
    # if abs(hlcompare)<0.1:
    # 	monthlyPayment = monthlyPayment + 0.01

	if newbalance>0:
		loPay = monthlyPayment
	elif newbalance<0:
		hiPay = monthlyPayment

    # else:
    # 	break

print 'Lowest Payment:',round(monthlyPayment,2)