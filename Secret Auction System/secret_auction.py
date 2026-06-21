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
print("Welcome to the secret auction program.")
bids = {}
other_bid = True
def calculate_highest(bid_dict):
    greatest_bid = 0
    winner = ""
    for person in bid_dict:
        price = bid_dict[person]
        
        if greatest_bid < price:
            greatest_bid = price
            winner = person
    print(f"The winner is {winner} with a bid of ${greatest_bid}")

while other_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    other_person = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_person == "no":
        other_bid = False
        calculate_highest(bids)
