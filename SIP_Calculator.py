#created this SIP Calculator.
#Takes Input for necessary parameters and gives the future value of your investment.

def SIPcalculator(): 
    sip = int(input("Enter Montly Investment Value: "))
    n = int(input("Enter Time Period in years: "))
    R = (float(input("Enter Expected rate of Return: "))/100)/12
    n = n*12
    
    future_value = (sip*(((1+R)**n)-1)*(1+R))/R
    invested_amount = (sip*n)
    gain_amount = future_value - invested_amount
    
    print("Your Total Wealth is {} with total investment of {}".format(round(future_value),invested_amount))
    print("Your Total Wealth gain is {}".format(round(gain_amount)))
