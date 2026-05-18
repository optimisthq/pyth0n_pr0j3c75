#print("Hello World!")

#Let's build a robot named Barista for pur coffee shop !!

print("HELLO, Welcome to 0ptimist's coffee shop")

name = input("What is your name? \n")

if name == "Ben" or name == "Patricia" or name == "Loki" or name == "Sagar":
    ans = input("Ok " + name + ", Are you evil? \n")
    if ans == "Yes":
        deeds = int(input("How many good deeds have you done today? \n"))
        if deeds >=4 and ans == "Yes" :
            print("Well, you have been good today, " + name)
#alternatively just use the conditions nested if : if deeds >=4 : as it is already specified for "Yes"
        else:
            print("You are not welcome here Evil " + name +", Get Out!!!!")
            exit()
    else:
        print("Oh, you are one of those good " + name +"s, Come on in!")
else:
    print("Hello " + name + ", Thank you for coming in! \n\n")

menu = "Black Coffee, Latte, Espresso, Cappucino, Frappucino"

print(name + ", what would you like to have today? Here is our menu : \n" + menu)

order = input()

if order == "Frappucino":
    cost = 13
elif order == "Black Coffee":
    cost = 9
elif order == "Cappucino":
    cost = 12
elif order == "Espresso":
    cost = 11
elif order == "Latte":
    custom_lat = input("Do you want whipped cream?")
    if custom_lat == "yes" or custom_lat == "Yes":
        cost = 9
    else:
        cost = 8
else:
    print("Sorry, We dont have that here.")
    exit()

count = int(input("How many " + order + " would u like? \n"))

total = cost*count

print("The total cost is : ", total, "$")

print("Sounds good " + name + ", We'll have the " + order + " for you in a moment")


