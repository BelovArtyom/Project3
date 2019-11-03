""" Project 3. String manipulation
Developers:
Belov A. (100%)

"""

# This program helps the user create secure passwords

# Asking user for maximum length of a password he wants
usermaxchar = None
while usermaxchar is None:
    usermaxchar = input("What is the maximum length of a password you can remember?")
    if usermaxchar.isdigit() is False:
        print("ERROR: Incorrect input.")
    elif int(usermaxchar) > 20:
        print("It is highly inadvisable to overestimate one's memory.")
        usermaxchar = None
    elif int(usermaxchar) < 5:
        print("It is highly inadvisable to underestimate one's memory.")
        usermaxchar = None
        while answer is None:
            answer = input("Continue? Y/N")
            if answer == "Y":
                print("Continuing...")
            elif answer == "N":
                print("A wise choice. Going back.")
                usermaxchar = None
            else:
                print("\nERROR: Incorrect input.")
                answer = None
    else: continue
usermaxchar = int(usermaxchar)

# Asking the user to input some string in for further manipulation
userstring = None
while userstring is None:
    userstring = input("Input a string of characters, please.")
    if len(userstring) < 3:
        print("ERROR: Length is too short, try again, please.")
        userstring = None
    elif len(userstring) > usermaxchar:
        print("Input length is over ", usermaxchar - 4, ", this password will be hard to remember, continue?", sep="")
        answer = input("If yes, write \"yes\", please.")
        if answer == "yes":
            continue
        else:
            print("Cutting input to fit", usermaxchar, "characters...")
            userstring = userstring[0:int(usermaxchar - 1)]

# Strengthening user generated password with user's date of birth
# As safety labs have proven, it's more important to have a long
# unbruteforceable password than a laconic random one
print("Now we get to the magic of all secure passwords.")
userdateofbirth = None
while userdateofbirth is None:
    userdateofbirth = input("What is the year you were born?")
    if userdateofbirth.isdigit() is False:
        print("ERROR: Incorrect input.")
        userdateofbirth = None
    elif int(userdateofbirth) > 3019:
        print("Does humanity still exist after over 1000 years of writing this code?")
        print("I don't really trust you. You've most likely made a typo.")
        userdateofbirth = None
    elif int(userdateofbirth) < 1900:
        answer = None
        while answer is None:
            answer = input("Are you an alien?")
            if answer.lower() == "no" or answer.lower() == "n":
                print("Then that makes you a very old person.")
            else: print("In whatever alien language that was, alright. I believe you. Go on.")
    else:
        print("Excellent.")

# Now we will reinforce user's password with his year of birth
print("Now we will reinforce your password", userstring, "with your year of birth")
userstring = userstring + userdateofbirth

# Outputting a new password
print("Your newly created password is", userstring)
