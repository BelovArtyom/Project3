""" Project 3. String manipulation
Developers:
Belov A. (100%)

"""

# This program helps the user create extra secure passwords.

# Asking user for maximum length of a password he wants
usermaxchar = None
answer = None

while usermaxchar is None:
    usermaxchar = input("What is the maximum length of a password you can remember?")
    if usermaxchar.isdigit() is False:
        print("ERROR: Incorrect input.")
    elif int(usermaxchar) > 20:
        # Making sure the user understands their intentions.
        print("Are you sure you want a password longer than 20 characters?")
        while answer is None:
            answer = input("Continue? Y/N")
            if answer == "Y":
                print("Continuing...")
            elif answer == "N":
                print("A wise choice. Going back.")
                usermaxchar = None
            else:
                print("ERROR: Incorrect input.")
                answer = None

    elif int(usermaxchar) < 5:
        print("Are you sure you want a password shorter than 5 characters?")
        while answer is None:
            answer = input("Continue? Y/N")
            if answer == "Y":
                print("Continuing...")
            elif answer == "N":
                print("A wise choice. Going back.")
                usermaxchar = None
            else:
                print("ERROR: Incorrect input.")
                answer = None
    else: continue

# Making usermaxchar an integer for math manipulations later
usermaxchar = int(usermaxchar)
# Resetting answer to be None
answer = None

# Asking the user to input some string in for further manipulation
userstring = None
while userstring is None:
    userstring = input("Input a string of characters, please.")
    if len(userstring) < 3:
        print("ERROR: Length is too short, try again, please.")
        userstring = None

    elif len(userstring) > usermaxchar:
        print("Input length is over ", usermaxchar, ", this password will be hard to remember, continue?")
        answer = input("If yes, write \"yes\", please.")
        if answer == "yes":
            continue
        else:
            print("Shortening input to fit", usermaxchar, "characters...")
            userstring = userstring[0:int(usermaxchar - 1)]

# Strengthening user generated password with user's date of birth
# As safety labs have concluded, it's more important to have a long
# unbruteforceable password than a laconic random one

print("Now we get to the magic of all secure passwords.")
userdateofbirth = None
while userdateofbirth is None:
    userdateofbirth = input("What is the year you were born?")
    if userdateofbirth.isdigit() is False or int(userdateofbirth) > 9999 or int(userdateofbirth) < 1848:
        print("ERROR: Please, input years from 1848 to 9999.")
        userdateofbirth = None
    else:
        print("Excellent.")

# Now we will reinforce user's password with his reversed year of birth
userdateofbirth = userdateofbirth[::-1]

print("Now we will reinforce your password", userstring)
print("with your reversed year of birth", userdateofbirth)
userstring = userstring + userdateofbirth

# Outputting a new password
print("Your newly created password is", userstring)
print("Thank you for using our password creator!")
