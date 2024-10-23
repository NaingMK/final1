import os

class AuctionManagementSystem:
    def __init__(self, user_file="users.txt", auction_file="auction_data.txt"):
        self.user_file = user_file
        self.auction_file = auction_file
        self.users = self.load_users()
        self.auctions = self.load_auctions()

    def load_users(self):
        users = []
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as file:
                for line in file:
                    username, _ = line.strip().split(',')
                    users.append(username)
        return users

    def save_users(self):
        with open(self.user_file, 'w') as file:
            for user in self.users:
                file.write(f"{user}\n")

    def load_auctions(self):
        auctions = []
        if os.path.exists(self.auction_file):
            with open(self.auction_file, 'r') as file:
                for line in file:
                    auction_data = line.strip().split(',')
                    auction = {
                        'item': auction_data[0],
                        'description': auction_data[1],
                        'starting_bid': float(auction_data[2]),
                        'current_bid': float(auction_data[3]),
                        'bidder': auction_data[4] if len(auction_data) > 4 else None
                    }
                    auctions.append(auction)
        return auctions

    def save_auctions(self):
        with open(self.auction_file, 'w') as file:
            for auction in self.auctions:
                file.write(f"{auction['item']},{auction['description']},{auction['starting_bid']},{auction['current_bid']},{auction['bidder']}\n")

    def register_user(self, username):
        if username in self.users:
            print("Username already exists. Please choose another one.")
        else:
            self.users.append(username)
            self.save_users()
            print(f"User {username} registered successfully.")

    def create_auction(self, item, description, starting_bid):
        for auction in self.auctions:
            if auction['item'] == item:
                print(f"Item {item} already exists in the auction.")
                return
        new_auction = {
            'item': item,
            'description': description,
            'starting_bid': float(starting_bid),
            'current_bid': float(starting_bid),
            'bidder': None
        }
        self.auctions.append(new_auction)
        print(f"Auction for item {item} created successfully.")
        self.save_auctions()

    def place_bid(self, username, item, bid_amount):
        for auction in self.auctions:
            if auction['item'] == item:
                if bid_amount > auction['current_bid']:
                    auction['current_bid'] = bid_amount
                    auction['bidder'] = username
                    print(f"Bid placed successfully on item {item} by {username} with a bid of ${bid_amount}.")
                    self.save_auctions()
                else:
                    print(f"Your bid of ${bid_amount} is not higher than the current bid of ${auction['current_bid']}.")
                return
        print(f"Item {item} not found in the auction.")

    def display_auction_status(self, item):
        for auction in self.auctions:
            if auction['item'] == item:
                print("\nAuction Status:")
                print("-----------------")
                print(f"Item: {auction['item']}")
                print(f"Description: {auction['description']}")
                print(f"Starting Bid: ${auction['starting_bid']}")
                print(f"Current Bid: ${auction['current_bid']}")
                print(f"Current Bidder: {auction['bidder']}")
                print("-----------------")
                return
        print(f"Item {item} not found in the auction.")

# User Interface
if __name__ == "__main__":
    auction_system = AuctionManagementSystem()

    while True:
        print("\nAuction Management System")
        print("1. Register User")
        print("2. Create Auction")
        print("3. Place Bid")
        print("4. Auction Status")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            username = input("Enter your username: ")
            auction_system.register_user(username)
        elif choice == '2':
            item = input("Enter item to auction: ")
            description = input("Enter item description: ")
            starting_bid = float(input("Enter starting bid amount: "))
            auction_system.create_auction(item, description, starting_bid)
        elif choice == '3':
            username = input("Enter your username: ")
            item = input("Enter item to bid on: ")
            bid_amount = float(input("Enter bid amount: "))
            auction_system.place_bid(username, item, bid_amount)
        elif choice == '4':
            item = input("Enter item to check status: ")
            auction_system.display_auction_status(item)
        elif choice == '5':
            print("Exiting Auction Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")