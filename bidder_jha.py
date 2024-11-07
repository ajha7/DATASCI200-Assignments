# import matplotlib.pyplot as plt
import random
class Bidder:
    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.__epsilon = 0.1
        self.means = {}
        self.current_best_user = None
        self.current_best_avg = 0
        self.curr_user_id = None
        self.balance = 0
        self.balance_history = []
        
    def bid(self, user_id):
        # epsilon-greedy strategy
        self.curr_user_id = user_id
        if user_id not in self.means:
            self.means[user_id] = []
            return 0.5
            
        avg = (sum(self.means[user_id])) // len(self.means[user_id]) if self.means[user_id] != [] else 0.5
        # explore
        if random.random() <= self.__epsilon:
            return avg
            
        # exploit
        else:    
            if user_id == self.current_best_user:
                return avg * 1.0
            else:
                return 0

    def notify(self, auction_winner, price, clicked):
        if auction_winner:
            self.balance -= price
            if clicked:
                self.balance += 1
            self.means[self.curr_user_id].append(clicked)
            
            avg = sum(self.means[self.curr_user_id]) // len(self.means[self.curr_user_id])
            if (not self.current_best_user) or (avg > self.current_best_avg):
                self.current_best_user = self.curr_user_id
                self.current_best_avg = avg

            self.balance_history.append(self.balance)

    # def plot_history(self):
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(range(len(self.balance_history)), self.balance_history, label="Bidder Balance", color='b')
    #     plt.title("Bidder's Balance History")
    #     plt.xlabel("Auction Round")
    #     plt.ylabel("Balance ($)")
    #     plt.grid(True)
    #     plt.legend()
    #     plt.show()
        
    def __str__(self):
        return str(id(self))
        
    def __repr__(self):
        return str((id(self)))