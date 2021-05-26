# Refund system
# Have 20, 10, 5, 1, and then all the cents
# Have a stock
# Get input from user
# Spit out the input


# Stock of the denominations
stock = [20,20,20,20,20,20,20,20]
# 20s, 10s, 5s, 1s, quaters, dimes, nickles, pennies
denomination = [20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

def math():
    x = dif
    twentcount = 0
    tencount = 0
    fivecount = 0
    onecount = 0
    quartcount = 0
    dimecount = 0
    nickcount = 0
    pencount = 0

    while(x/20 >= 1):
        x = round(x-20,2)
        twentcount += 1
    print(f"We need {twentcount} x $20")

    while(x/10 >= 1):
        x = round(x-10,2)
        tencount += 1
    print(f"We need {tencount} x $10")

    while(x/5 >= 1):
        x = round(x-5,2)
        fivecount += 1
    print(f"We need {fivecount} x $5")

    while(x/1 >= 1):
        x = round(x-1,2)
        onecount += 1
    print(f"We need {onecount} x $1")

    while(x/0.25 >= 1):
        x = round(x-0.25,2)
        quartcount += 1
    print(f"We need {quartcount} x $0.25")

    while(x/0.10 >= 1):
        x = round(x-0.10,2)
        dimecount += 1
    print(f"We need {dimecount} x $0.10")

    while(x/0.05 >= 1):
        x = round(x-0.05,2)
        nickcount += 1
    print(f"We need {nickcount} x $0.05")

    while(x/0.01 >= 1):
        x = round(x-0.01,2)
        pencount += 1
    print(f"We need {pencount} x $0.01")

def mathv2():
    x = dif
    position = 0
    counter = 0
    # Checks if there is enough money in the register
    if(total() > x):
        # While there is still a remainder, keep doing the math
        while(x != 0):
            # Checks if the denomination is big enough 
            if (x >= denomination[position]):
                # Keeps running the math if the current demoniation can go into x evenly
                while(x/denomination[position] >= 1):
                    x -= denomination[position]
                    x = round(x,2)
                    counter += 1
                print(f"{counter} x ${denomination[position]}")
                stock[position] -= counter
                counter = 0
                position += 1
            # If demoniation is too low, move position
            else:
                position += 1
        print(stock)
    # If there isn't enough money in the register
    else:
        print("Not enough in register.")

def total():
    i = 0
    position = 0
    for number in stock:
        i += (stock[position] * denomination[position])
        position += 1
    return i


while(0 not in stock):
    dif = round(float(input("What is your change?")),2)
    mathv2()
    print(f"${total()} in Register")


