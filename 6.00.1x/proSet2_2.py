balance =3329
annualInterestRate = 0.2

# 12*miniPay+annualInterest=balance
# balance = balance - miniPay
# balance = balance + balance * (annualInterestRate/12)

# Code from me:
# month = 1
# monInRate = annualInterestRate/12
# miniPay = 10
# newbalance = balance
# while newbalance>0:
# 	miniPay = miniPay + 10
# 	while month<12 and newbalance>0:
# 		newbalance -=miniPay
# 		newbalance +=(newbalance*monInRate)
# 		month +=1

# print ("Lowest Payment:"+miniPay)

# Code from stackoverflow
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1

    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
        month += 1
    newbalance = round(newbalance,2)
print ("Lowest Payment:"+str(monthlyPayment))


# def findminiPay(balance,monInRate):
# 	miniPay = 10
# 	while (balance >= 0):
# 		#if balance<0:
# 		#	break
#                        	miniPay = miniPay + 10
# 		while month<12 and balance>0 :
#                                         balance = balance - miniPay
#                                         balance = balance + (balance*monInRate)
#                                         month += 1
		
# 	return miniPay

# miniPayNum = findminiPay(balance,monInRate)
# print ("Lowest Payment:"+str(miniPayNum))
