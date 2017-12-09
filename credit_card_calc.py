#!/usr/bin/env python3
'''Credit Card Calculation Program

A simple program that allows the user to determine the length of time needed
to pay off a credit card balance, as well as total interest paid.

The problem:
    Generate a table showing the decreasing balance and accumlating interest 
    paid on the credit card for a given credit card balance, interest rate 
    and monthly payment.  
'''
#### PROBLEM ANALYSIS
# Factors that determine how quickly a loan is paid off :-
    # Amount of the loan
    # Interest Rate charged
    # Monthly payments made (minimum payment 2%-3%  of the outstanding balance each month)
    # Time to pay off the card by making minimum payments only

##### PROGRAM DESIGN
## Meeting Program requirements
    # Output Display Format - Tabular
    # Relevant Information - User Input 
    # Time to pay off the loan - Compute & display
    # Total interest paid - Compute & display
    # Give user the choice to assume  the monthly payments to be the required-min or a larger specified amount

## Data Description
# All data that needs to be represented in the program are numerical values for:
    # Loan amount
    # Interest Rate
    # Monthly payments made
# No need to create a data structure as the table of payments can be generated as it is displayed

## Algorithmic Approach
# Calculation of the required minimum payment
    # Minimun payment - 2% of the outstanding balance each month
    # Lower limit of minimum payment - $20

#########################  THE PROGRAM  #######################################

def display_welcome():
    '''Program Greeting'''
    print('\n.... Entering function display welcome')
    print(format(' Credit Card Calculation Program ', '|^80'))
    
def display_payments(balance, int_rate, monthly_payment):
    '''Calculate and display the paydown of the balance as well
    as the interest paid over each month of the payoff period.  
    '''
    print('\n.... Entering function display_payments')
    print(format(' Applicaple Payments ', '|^80'))
    print('Parameter balance = ', balance)
    print('Parameter int_rate =', int_rate)
    print('Paramter monthly_payment = ', monthly_payment)

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
    print(format(' Minimun payment Selected ', '|^80'))
    monthly_payment = 20
else:
    print(format(' User-entered monthly payments selected ', '|^80'))
    monthly_payment = int(input('Enter monthly payment: '))

# Display monthly payoff
display_payments(balance, monthly_int_rate, monthly_payment)

