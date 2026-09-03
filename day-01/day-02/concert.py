age = int(input("Enter your age: "))
money = int(input("How much money do you have? "))
ticket = input("Do you have a ticket? ")
vip = input("Do you have a VIP ticket? ")

if age < 16:
    print("You are too young")

if money < 20:
    print("Not enough money")

if ticket == "no":
    print("You need a ticket")

if age >= 16 and ticket == "yes" and money >= 20 and vip == "yes":
    print("Welcome to VIP")
elif age >= 16 and ticket == "yes" and money >= 20:
    print("Welcome to the concert")
