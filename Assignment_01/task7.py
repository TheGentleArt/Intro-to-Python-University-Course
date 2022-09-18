#
# Problems statement for problem # 7 on homework:
#
#For this problem, you will have to write a Python program that calculates 
# how long it will take one to save for the down payment of a car. This program
# should ask for the following inputs:
# (a) Annual salary
# (b) Savings rate
# (c) Car price
# We will assume that the down payment on the car is 40 % of the total cost of
# the car. We will also assume that you save your money smartly and earn a 6% 
# on it annually; divide by 12 to find out a monthly rate of earning, which is
# what you should work with, i.e., report after how many months you have more 
# than 40% required for the down payment. Assume that you start off with $0 in
# your savings account.
# The program should return the number of months it will take to save enough 
# for the down payment with the text given below. Submit the python script 
# named task7.py to Canvas.
# Test Case :
# $ python3 prob7 . py
# Enter annual salary: 120000
# Enter your savings rate as a decimal: 0.1
# Enter car price: 100000
# Number of months required to save for down payment: 37.
#

#Assumptions:
# savings is put in at the end of the month, and thus that monthly savings does
# not get counted for interest calculations
down_payment_pct = 0.4
savings_int_rate_annual = 0.0006
savings_int_rate_monthly = savings_int_rate_annual/12 # Assume not compounded
initial_savings = 0
# Ask user to input info
annual_salary = float(input('Enter your annual salary: '))
savings_rate = float(input('Enter your savings rate from your salary (as a decimal): '))
price_car = float(input('Enter the price of the vehicle: '))

down_payment_req = price_car * down_payment_pct
savings_monthly_deposit = annual_salary * savings_rate

months = 0
savings = initial_savings
while savings < down_payment_req:
    months+=1 # add 1 to the value of months
    interest_earned_this_month = savings*savings_int_rate_monthly
    savings = savings + interest_earned_this_month + savings_monthly_deposit
print("In ",months," months you will have saved ",savings," dollars. This is enough.")

    
