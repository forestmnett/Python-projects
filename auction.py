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
print("Welcome to the silent auction!")
bidder_list = {}

def add_bidder(name, bid):
    name = input("what is your name?")
    bid = input("What is your bid?")
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = bid
    print(new_bidder)
#    bidder_list.append(new_bidder)
add_bidder("name","bid")
print(bidder_list)

