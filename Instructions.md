# Introduction

## Topics covered

Command line input and output. Using variables, operators, basic math functions and control flow structures.

## Goal achieved

By the end of the exercise you will have created a command line tool to consult items in stock and simulate placing orders.

## Data

The source data are two lists, each one containing the names of all items in a warehouse. The current system has two different warehouses (1 and 2) and two different lists are provided.

The [sample directory](sample) in this repository has some sample data you can use to test your code with. The directory contains these files:

- **data.py**: this module contains the data. To make it easier to work, the data is placed in a different file and is loaded from the main script.
- **query.py**: this module will contain your script. The first lines show a little help message and load the data into the module. You will have the lists available with the names `warehouse1` and `warehouse2`.

You can copy these two files into your project repository.

You will have to use these lists the way you have seen during the lecture with the `range` function.

```python
for item in warehouse1:
    # instructions
```

## Description

Go to your repository and create a directory named `cli` (standing for Command Line Interface). Copy the files  `data.py` and `query.py` from the [sample](sample) directory to your repository directory.

Edit the file `query.py` and write a script that produces the following workflow:

1. The user is asked to provide a name.
1. The user is greeted by its name.
1. A menu is printed out showing 3 options: `1. List items by warehouse`, `2. Search an item and place an order` and `3. Quit`.
1. The user is asked to pick a choice using the numeric values associated.
    1. If the user picked `1`, the script should print each of the items in each of the warehouses (first all items from a warehouse and then all items from the other). Then it should stop execution.
    1. If the user picked `2`, the script should:
        1. Ask the user to input an item name and search the warehouses.
        1. The script will print:
            1. The total amount of items in any warehouse that match that name.
            2. The location of those items: the name of the warehouse (ex: `Warehouse 1`), if it can only be found in one, `Both warehouses` if it is in both and `Not in stock` if it is in none.
            3. If it can be found in more than one warehouse, it will also print a line saying which warehouse has the highest amount of those items (and how many does it have).
        1. Ask the user if they want to place an order for this item.
            1. If the answer is no, it will do nothing else.
            1. If the answer is yes, it should ask the user how many do they want.
                1. If the desired amount is equal or lower than the total available, it will proceed and show a message saying the order has been placed. *The message should show the item name and amount ordered*.
                1. If the desired amount is higher than the total available, it should show an error message and should ask the user if they want to order the maximum available, instead.
                    1. If they answer yes, it will proceed and show a message saying the order has been placed. *The message should show the item name and amount ordered*.
                    1. If they answer no, it will do nothing else.
    1. If the user picked `3`, the script should do nothing else.
    1. If the user types anything different than `1`, `2` or `3` it should show an error message indicating the operation entered is not valid.
1. Display a final message thanking the user for the visit, using their name typed at the beginning.

> **IMPORTANT**
>
> Do not forget to push all the changes to the remote repository once you are done. Commit the changes with a meaningful description.

> **Not enough?**
>
> *If you want to do more you can pick some of these add-ons*.
> - Use a while loop to let the user order multiple items during the same session.

## Sample outputs
You can use these samples to get a better idea of what the script should do. The text does not need to be exactly as it appears here. This is your project and you can adapt it as you wish, but the general flow should be as described.

**Listing all items**
```
What is your user name? Mathilda

Hello, Mathilda!
What would you like to do?
1. List items by warehouse
2. Search an item and place an order
3. Quit
Type the number of the operation: 1

Items in warehouse 1:
- Brand new laptop
- Exceptional monitor
- Cheap tablet
...
- Second hand mouse
Items in warehouse 2:
- High quality tablet
- Second hand headphones
...
- Almost new router
- High quality monitor

Thank you for your visit, Mathilda!
```
**Search & found in 1 location, no order**

```
What is your user name? Martin

Hello, Martin!
What would you like to do?
1. List items by warehouse
2. Search an item and place an order
3. Quit
Type the number of the operation: 2

What is the name of the item? Cheap tablet
Amount available: 2
Location: Warehouse 1

Would you like to order this item?(y/n) n

Thank you for your visit, Martin!
```
**Search & found in 2 locations. Order more than available and accepting maximum.**

```
What is your user name? Mathilda

Hello, Mathilda!
What would you like to do?
1. List items by warehouse
2. Search an item and place an order
3. Quit
Type the number of the operation: 2

What is the name of the item? Almost new router
Amount available: 3
Location: Both warehouses
Maximum availability: 2 in Warehouse 2

Would you like to order this item?(y/n) y
How many would you like? 4
**************************************************
There are not this many available. The maximum amount that can be ordered is 3
**************************************************
Would you like to order the maximum available?(y/n) y
3 Almost new router have been ordered.

Thank you for your visit, Mathilda!
```
**Order more than available and not accepting maximum.**

```
What is your user name? Ruth

Hello, Ruth!
What would you like to do?
1. List items by warehouse
2. Search an item and place an order
3. Quit
Type the number of the operation: 2

What is the name of the item? Second hand headphones
Amount available: 8
Location: Both warehouses
Maximum availability: 4 in Warehouse 1

Would you like to order this item?(y/n) y
How many would you like? 10
**************************************************
There are not this many available. The maximum amount that can be ordered is 8
**************************************************
Would you like to order the maximum available?(y/n) n

Thank you for your visit, Ruth!
```
**Item not found.**
```
What is your user name? Leia

Hello, Leia!
What would you like to do?
1. List items by warehouse
2. Search an item and place an order
3. Quit
Type the number of the operation: 2

What is the name of the item? Bigger headphones
Amount available: 0
Location: Not in stock

Thank you for your visit, Leia!
```
**Unsupported operation.**
```
What is your user name? Sherlock

Hello, Sherlock!
What would you like to do?
1. List items by warehouse
2. Search an item and place an order
3. Quit
Type the number of the operation: Search

**************************************************
Search is not a valid operation.
**************************************************

Thank you for your visit, Sherlock!
```
**Quit.**
```
What is your user name? John Doe

Hello, John Doe!
What would you like to do?
1. List items by warehouse
2. Search an item and place an order
3. Quit
Type the number of the operation: 3


Thank you for your visit, John Doe!
```
