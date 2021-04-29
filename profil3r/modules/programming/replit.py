import requests
import time

class Replit:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['replit']['rate_limit'] / 1000
        # https://replit.com/@{username}
        self.format = config['plateform']['replit']['format']
        self.permutations_list = permutations_list
        # programming 
        self.type = config['plateform']['replit']['type']

    # Generate all potential replit usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        replit_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to replit")
            
            # If the account exists
            if r.status_code == 200:
                replit_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return replit_usernames