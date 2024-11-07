import random

class User:
    def __init__(self):
        self.__probability = random.random()

    def show_ad(self):
        chance = random.random()
        if chance <= self.__probability:
            return True
        return False

    def __str__(self):
        return str(id(self))

    def __repr__(self):
        return str((id(self)))

class Auction:
    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in bidders}

    def execute_round(self):
        chosen_user = random.choice(self.users)
        highest_bid = 0
        winning_price = 0
        winning_bidder = []
        for bidder in self.bidders:
            # curr_bid = bidder.bid(chosen_user)
            curr_bid = bidder.bid(chosen_user)
            if curr_bid > highest_bid:
                winning_price = highest_bid
                winning_bidder = [bidder]
                highest_bid = curr_bid
                
            elif curr_bid == highest_bid:
                winning_bidder.append(bidder)
                winning_price = highest_bid
            else:
                winning_price = max(winning_price, curr_bid)
                
        clicked = chosen_user.show_ad()
        
        if len(winning_bidder) > 1:
            winning_bidder = random.choice(winning_bidder)
        else:
            winning_bidder = winning_bidder[0]

        for bidder in self.bidders:
            if bidder == winning_bidder:
                self.balances[bidder] -= winning_price
                if clicked:
                    self.balances[bidder] += 1
                bidder.notify(True, winning_price, clicked)
                if self.balances[bidder] < -1000:
                    self.bidders.remove(bidder)
            else:
                bidder.notify(False, winning_price, None)