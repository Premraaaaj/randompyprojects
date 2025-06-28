# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bidders={}
people=False

while not people:
    name=input("Enter your name:")
    price=int(input("Enter your price:"))
    bidders[name]=price
    x=input("Are there anymore bidders? y for yes,n for no:")
    if x=="y":
        print("\n"*20)
    else:
        people=True
highest_bidder=max(bidders,key=bidders.get)
highest_bid=max(bidders.values())
print(bidders)
print(f"the winner is {highest_bidder} with the amount {highest_bid}")



