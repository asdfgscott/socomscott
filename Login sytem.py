#create a log in system
#have a list of users in a dictionary 
#have a register

users = {"user1":"password1", "user2":"password2", "users3":"password3"}

def login():
    # Just like logging in in real life, it asks for both to then say something so you don't know what is wrong
    user = input("Username: ")
    password = input("Password: ")

    # Checks to see if the user is even in the system
    if(user in users):
        # If username in the system, and the password matches, you're logged in.
        if(users[user] == password):
            print("You're logged in")

    # If the user is not in the system, the else statement runs
    else:
        print("Invalid Credentials.")
        # Asks the user if they would like to register
        quest = input("Would you like to register? y/n ")
        # If yes
        if(quest == "y"):
            newuser = input("New Username: ")
            newpassworld = input("New Password: ")
            # Checks to see if the new username is already if the system
            # If there is, the while loop will keep running
            while(newuser in users):
                print("Username already taken.")
                newuser = input("New Username: ")
                newpassworld = input("New Password: ")
            # Appending the new key and value to the dictionary
            users[newuser] = newpassworld
            # Just to check the new key and value are appended
            print(users)
            login()
        #If no, run the function again from the begining
        else:
            login()


login()




