#This program aims to determine either return on investment or monthly repayment on a bond, 
#depending on the users selection

#import math library, used to carry out more complex mathematical functions
import math

#promt user to enter desired information
print("investment: to calculate the amount of interest you'll earn on your investment ")
print("bond: to calculate the amount  you'll have to pay on a home loan ")


calc_type = input("enter either 'bond' or 'investment' from the menu above to proceed: ")

#creates a condition to test for valid spellings of bond or investment
if (calc_type == "Bond") or (calc_type == "BOND") or (calc_type == "bond"):

#prompt user for information needed to perform repayment calculation
    present_val = int(input("please enter your present value of your home: "))
    interest_rate = int(input("please enter the interest rate: "))
    r = float(interest_rate/100)
    no_months = int(input("please enter the number of months over which you wish to repay the bond: "))

    monthly_repayment = (r* present_val)/(1-(1 + r)**(-no_months))
    print("Your monthly repayment will be: " + str(monthly_repayment))

elif (calc_type == "investment") or (calc_type == "INVESTMENT") or (calc_type == "Investment"):
    deposit = int(input("please enter your deposit amount: "))
    interest_rate = int(input("please enter the interest rate: "))
    r = float(interest_rate /100)
    duration = int(input("please enter the investment duration in years: ")) 
    interest_type = input("please select between 'simple' or 'compound' interest: ")
# nested if statement to determine the type of interest required from user    
    if interest_type == "simple":
        return_amount = deposit * (1 + r*duration)
        print(f"in {str(duration)} years, your investment will be worth {str(return_amount)}")

    elif interest_type == "compound":
        return_amount = deposit * math.pow(1+r, duration)
        print(f"in {str(duration)} years, your investment will be worth {str(return_amount)}")

    else: 
        print("please enter a valid interest rate calculation type")    


else:
    print("please enter a valid input")