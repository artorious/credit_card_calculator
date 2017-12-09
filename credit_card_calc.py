#!/usr/bin/env python3
'''Credit Card Calculation Program

A simple program that allows the user to determine the length of time needed
to pay off a credit card balance, as well as total interest paid.

The problem:
    Generate a table showing the decreasing balance and accumlating interest 
    paid on the credit card for a given credit card balance, interest rate 
    and monthly payment.  
'''

# TODO: Formatting the Displayed Output
    # Add input error checking. 
    # Modifiy to allow the user to continue to enter various monthly payments for recalculating a given balance pay-off. 
    # Add Output formatting to make the displayed information more readable. 
    # Correct the display of a negative balance at the end of the payoff schedule.

def display_welcome():
    '''Program Greeting'''
    print(format(' Credit Card Calculation Program ', '|^80'))
    print()
    print('This program will determine the time to pay off a credit')
    print('card and the interest paid based on the current balance,')
    print('the interest rate, and the monthly payments made.')
    print()

def display_payments(balance, int_rate, monthly_payment):
    '''Calculate and display the paydown of the balance as well
    as the interest paid over each month of the payoff period.  
    '''
    # Init
    num_months = 0 
    total_int_paid = 0

    # Display Loan Info
    print(format(' PayOff Schedule ', '|^80'))
    print()
    print('Credit Card Balance: ${0:,.2f}'.format(balance))
    print('Annual Interest Rate: {0}%'.format(str(1200 * int_rate)))
    print('Monthly Payment: ${0:,.2f} '.format(monthly_payment))
    print()
    
    # display year-by-year account status
    while balance > 0: # Iterate
        monthly_int = balance * int_rate
        total_int_paid += monthly_int # Track  & update total interest paid
        balance += monthly_int - monthly_payment

        year = (num_months // 12) + 1
        print('{0} {1:,.2f} {2:,.2f}'.format(year, balance, total_int_paid))
        
        num_months += 1   # Tarck & update number of months(lines) displayed

# ---- Main

# display welcome screen
display_welcome()

# Get Card Balance, Annual Interest Rate (APR) 
balance = int(input('\nEnter the balance on your credit card: '))
apr = int(input('Enter the Annual interest rate (APR) on the card: '))
monthly_int_rate = apr/1200  # Convert apr to monthly-int-rate and into decimal form

# Determine Monthly payment - Give user the choice to assume the monthly 
# payments to be the required-min or a larger specified amount
response = input('Use the minimum monthly payment? (y/n): ')

if response in ('y', 'Y'):
    if balance < 1000:
        monthly_payment = 20
    else:
        monthly_payment = balance * .02
else:
    monthly_payment = int(input('Enter monthly payment: '))

# Display monthly payoff
display_payments(balance, monthly_int_rate, monthly_payment)

