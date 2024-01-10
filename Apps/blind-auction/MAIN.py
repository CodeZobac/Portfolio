from replit import clear
bids = {}

def highest_bider():
    while True:
        name = input('What is your name? ')
        bid = int(input('What is your bid? '))
        bids[name] = bid
        other_biders = input('Are there other biders? Type "yes" or "no": ').lower()
        if other_biders == 'yes':
            clear()
        else:
            highest_bid = 0
            highest_bidder_name = ''
            for name, bid in bids.items():
                if bid > highest_bid:
                    highest_bid = bid
                    highest_bidder_name = name
            print(f'The highest bidder is {highest_bidder_name} with a bid of {highest_bid}.')
            break
highest_bider()