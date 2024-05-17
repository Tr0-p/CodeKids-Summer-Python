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
    snooze = input("Would you like to snooze (Yes/No)? ").upper() # yes/Yes/yES/YES/yEs ----> YES when we use .upper()
    if snooze == "YES": # nested conditional (if statement)
        snooze_time = int(input("How long would you like to snooze for?" ))
        print(f"You will snooze for {snooze_time} seconds")
        time.sleep(snooze_time) # pause the code for sleep_time seconds
        print("WAKE UPPPPPP!")
    else: # if they didn't type yes, then tell them to wake
        print("WAKE UPPPPPP!")

else:
    print("I didn't understand that - but please wake up for school!")





  

