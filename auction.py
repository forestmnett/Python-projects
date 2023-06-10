#rough auction program MVP for sure. Only sorts by 1st number. Doesnt clear when bid is submitted.
import operator
logo = '''
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
print("Welcome to the silent auction!")
bidder_list = []
def clear_screen():
    print("\033c", end="")
def find_high_bid(bidder_list):
    high_bid = 0
    for bidder in bidder_list:
        bid_amount = bidder_list[bidder]
        if bid_amount > high_bid:
            bid_amount = high_bid
    print(high_bid)
def add_bidder(name, bid):
    new_bidder = {}
    name = input("what is your name?")
    bid = input("What is your bid?")
    new_bidder["name"] = name
    new_bidder["bid"] = bid
    bidder_list.append(new_bidder)
    i = input("Are there other bidders?")
    if i == "no":
        done_bidding = True
    else:
        add_bidder("name", "bid")
done_bidding = False
if done_bidding == False:
    add_bidder("name","bid")
    clear_screen()
 
sorted_bidder_list = sorted(bidder_list, key=operator.itemgetter('bid'),reverse=True)
print(f"Congrats {sorted_bidder_list[0]} you've won!")
print(bidder_list)
