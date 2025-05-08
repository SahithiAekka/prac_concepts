# Dictonaries 
# allow us to group together and tag related pices of information
# two parts to it - key and value  {Key : Value} seperate  each key value pair using a comma 
# data structure that allows us to associate a key to a value and pair the two pieces of data together.

# This is how you create a dictionary in Python:

# # An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

# This is how you retrieve items from a dictionary:


# #Will print "green"
# This is how to create an empty dictionary:

# my_empty_dictionary = {}
# This is how you can add new items to an existing dictionary:

# colours["peach"] = "pink"
# This is also how you can edit an existing value in a dictionary:

colours["apple"] = "green"
print(colours["apple"])



# loop through a dictionary 
# Remember that looping through a Dictionary will only give you the keys and not the values.
for value in colours:
    print(value)
    

# NESTING 

travel_log={
    "France":["Paris","Dijon","Lille"],
    "India":["Hyd","chn","hydgs"]
}

print(travel_log["France"][2])

nested_list=["a","b",["c","d"]]


# print(nested_list[2][1])

# Max function 
fruits = {"apple":2, "banana":4, "strawberry":25}
print(max(fruits, key=fruits.get))


print("######################   Auction ##############################")

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
