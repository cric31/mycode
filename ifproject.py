#!/usr/env/python3

# Logistics package delivery cost based on location and total amount

total = int(input("Enter the amount for the item: "))
city = input("Enter the state name in South Carolina: ")
if city == "Greenville":
    if total <= 150:
        print("Delivery cost in Greenville is $60")
    elif total > 150 and total <= 250:
        print("Delivery cost in Greenville is $40")
    else:
        print("Delivery cost in Greenville is $10")

elif city == "Fort Mill":
    if total <= 150:
        print("Delivery cost in Fort Mill is $35")
    elif total > 150 and total <= 250:
        print("Delivery cost for Fort Mill is $25")
    else:
        print("Delivery cost in Fort Mill is $15")

elif city == "Rock Hill":
    if total <= 150:
        print("Delivery cost in Rock Hill is $20")
    elif total >150 and total <= 250:
        print("Delivery cost in Rock Hill is 10")
    else:
        print("Shipping cost is FREE")

else:
    print("Invalid City name")
