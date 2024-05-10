import time # import functionality related to time

print("Good morning Orlando!")
print("Are you ready for school?")



is_awake = input("Are you awake? (Yes/No)").upper() # makes our input uppercase


if is_awake == "YES":
    print("Awesome - we'll start making breakfast then!")

    breakfast_choice = input("What would you like for breakfast? (cereal/toast/eggs)").upper()

    if breakfast_choice == "CEREAL":
        print("Great - I'll start making your cereal!")
    elif breakfast_choice == "TOAST":
        print("I'll put the toaster on!")
    elif breakfast_choice == "EGGS":
        print("I'll get the frying pan")
    else:
        print("Sorry, that's not one of the options!")
    

elif is_awake == "NO":
    print("WAKE UPPPPPP!")

else:
    print("I didn't understand that - but please wake up for school!")





  

