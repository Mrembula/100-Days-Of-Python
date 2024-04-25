from replit import clear
import gavel
# HINT: You can call clear to clear the output in the console.abs
print(gavel.logo)
bidding_candidates = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidding_candidates[name] = bid

    others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if others == "yes":
        print("okay")
        clear()
    else:
        break

highest_bid = 0
bidder_name = ''
for name in bidding_candidates:
    price = bidding_candidates[name]
    if price > highest_bid:
        highest_bid = price
        bidder_name = name

print(f"The winner is {bidder_name} with a bid of ${highest_bid}")
