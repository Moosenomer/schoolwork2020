#-------------------------------------------------------------------
# Program: Assignment 1 - Cash Register Program
# Author: Erik Floyd
# Date: Feb 6, 2020
# Description: The program calculates the HST tax,
#            total amount of a purchase, the total change
#            and denomination of the change to be given
# Input: User input of the cost of an item and the cash Tendered.
#-------------------------------------------------------------------

#Importing sys
import sys

#Starting message
print("CASH REGISTER PROGRAM ERIK FLOYD")

#Declaring all the variables to keep them organized
pAmount = 0
HST = 0
totalCost = 0
uAmount = 0
totalChange = 0

#Asking user for the cost of the product they wish to buy, this value will be saved in the pAmount variable and rounded to 2 decimal places
pAmount = float(input("\nPlease enter Price of the product > "))
pAmount = round(pAmount, 2)

#Calculating the HST for based on what the user said the cost was, this will be saved in the HST Variable and rounded to 2 decimal places
HST = pAmount * 0.13
HST = round(HST, 2)

#Total cost is calculated by adding the HST and the amount entered by user then its rounded to 2 decimal places and stored in the totalCost variable
totalCost = pAmount + HST
totalCost = round(totalCost, 2)

#Printing the Cost, the HST and the total cost for the user.
print("\nItem Cost:  $ ", pAmount)
print("HST:        $ ", HST)
print("---------------------------------------------------")
print("Total Cost: $ ", totalCost)

#Asking user to enter the amount that they
uAmount = float(input("\nEnter the Cash you hand over > "))

#Check if the user has given enough money so they can pay for the item. If they dont it tells the user and exits the program 
if  (uAmount < totalCost):
    print("\nYou don’t have enough to pay for what you are buying")
    print("GOODBYE")
    sys.exit()

#Calculates the total amount of change that needs to be given to given back. Stores in the totalChange variable and rounds to 2 decimal places
totalChange = uAmount - totalCost
totalChange = round(totalChange, 2)

#Prints the total amount of change that needs to be returned
print("\nTotal Change:  $", totalChange)
print("---------------------------------------------------")



#The same while command for every different type of change
#The exit condition for each loop is if the total change can’t be subtracted by the different change amounts
#If totalChange can be subtracted by the change amount than it adds to the counter and prints how many bills/coins should be given back 
counter = 0

while (totalChange - 50 > 0):
    totalChange -= 50
    counter += 1
    
print("$50  : ", counter)

counter = 0

while (totalChange - 20 > 0):
    totalChange -= 20
    counter += 1
    
print("$20  : ", counter)

counter = 0

while (totalChange - 10 > 0):
    totalChange -= 10
    counter += 1
    
print("$10  : ", counter)

counter = 0

while (totalChange - 5 > 0):
    totalChange -= 5
    counter += 1
    
print("$5   : ", counter)

counter = 0

while (totalChange - 2 > 0):
    totalChange -= 2
    counter += 1
    
print("$2   : ", counter)

counter = 0

while (totalChange - 1 > 0):
    totalChange -= 1
    counter += 1
    
print("$1   : ", counter)

counter = 0

while (totalChange - 0.25 > 0):
    totalChange -= 0.25
    counter += 1
    
print("25", chr(162), ": ", counter)

counter = 0

while (totalChange - 0.10 > 0):
    totalChange -= 0.10
    counter += 1
    
print("10", chr(162), ": ", counter)

counter = 0

while (totalChange - 0.05 > 0):
    totalChange -= 0.05
    counter += 1
    
print("5 ", chr(162), ": ", counter)

counter = 0

while (totalChange - 0.01 > 0):
    totalChange -= 0.01
    counter += 1
    
print("1 ", chr(162), ": ", counter)
