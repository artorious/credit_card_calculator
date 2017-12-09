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


#########################  OVERALL PROGRAM STEPS  #######################################

# Program Greeting

# Get Card Balance, Annual Interest Rate, and Monthly payment - User Input

# Calculate and Display Payoff of Loan and Total Interest Paid
