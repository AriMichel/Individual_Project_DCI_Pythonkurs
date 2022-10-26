"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""


from data import warehouse1, warehouse2
products= warehouse1 + warehouse2

# YOUR CODE STARTS HERE

# Get the user name
name = str(input("What's your name? "))

# Greet the user
print ("Hello ", name, "Welcome to our Warehouse")


# Show the menu and ask to pick a choice
print (" these are your options, choose one: ")
print ("1: List of the items by warehouse.")
print ("2: Search an item and place an order.")
print ("3: Quit")
activity = int (input("1, 2 or 3? "))

option1= 1
option2= 2
option3= 3


# If they pick 1

if activity == 1:
    print ("This are the items in our warehouse in Berlin: ", warehouse1)
    print("")
    print("")
    print("")
    print ("This are the items in our warehouse in Munich: ", warehouse2)
#
# Else, if they pick 2
elif activity == 2:
    item = str (input ("What do you want to order: "))

    if item in products:
        

        if item in warehouse1 and item in warehouse2:
            indices = [i for i, x in enumerate(warehouse1) if x == item]
            indices2 = [i for i, x in enumerate(warehouse2) if x == item]
            print ("There are", len(indices), "pieces in Berlin")
            print ("There are", len(indices2), "pieces in Munich")
            
        

        elif item in warehouse1:
            indices = [i for i, x in enumerate(warehouse1) if x == item]
            
            print ("There are", len(indices), "pieces")
            print(item, "is available in Berlin")


        elif item in warehouse2:
            indices = [i for i, x in enumerate(warehouse2) if x == item]
            print ("There are", len(indices), "pieces")
            print (item, "is available in Munich")
        
    else: 
        print (item, "? Really? We don't sell those, sorry mate!")

    order = str (input("Do you want to order? Yes or Not?"))
    if order == "Yes":
        print("What do you want to order?")

    elif order == "No":
        print ("Got it!")

    else:
        print("Not a valid option. Bye")





        
    

#
# Else, if they pick 3
#

elif activity == 3:
    print ("3")
# Else

else:
    print("operation not valid")


print(" Thanks for your visit", name)
# Thank the user for the visit
