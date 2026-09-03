Destination=input("where do want to go? ")
Budget=int(input("how much money do you want to speend?")) #consider it in dollar.
stay=(input("do you want hotel?")) #accommodation type
Time=int(input("how many days do you stay? "))
Flight=input("Do you want a Direct flight or not?") #what kind of flight do you want?

if (Destination =="italy" or Destination== "ITALY" or Destination == "Italy") and (Time >= 7) and (Budget >= 1000):
    print("trip approved")
    if (Flight == "yes" or Flight == "i do" or Flight == "yes i do") and (stay == "yes" or stay == "i do" or stay == "yes I do"):
        print("premium package")

elif (Destination == "italy" or Destination == "ITALY" or Destination == "Italy") and Budget < 1000: 
    print("Budget is not enough")

elif Time < 7:
    print("trip is too short")

elif Destination != "italy" and Destination != "ITALY" and Destination != "Italy": 
    print("destination unavailable")
