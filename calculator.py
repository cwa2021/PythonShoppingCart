# Connor Applegate
# Small program to relearn dictionaries
# Program will take user input and produce a dictionary that will contain the item to buy and it's price then calculate total price

# Print users their selection options
print("press 1 to keep inputting items, 2 to calculate total cost and any other integer value to stop program")
userSelection = 1
item_dict = {}

# While loop that will continue until user selection is anything but 1 or 2
while userSelection == 1 or userSelection == 2:
    itemName = ""
    itemPrice = 0

    userSelection = int(input("what is your selection? "))
    # Will add user item and its price to dictionary
    if userSelection == 1:
        itemName = str(input("what is the name of your item: "))
        itemPrice = float(input("what is the price of your item: $"))
        item_dict[itemName] = itemPrice
    # Prints total value of all items in dictionary
    if userSelection == 2: 
        total_value = 0
        for value in item_dict.values():
            total_value += value
        print("The total value of the object(s) inputted is ${:.2f}".format(total_value))
