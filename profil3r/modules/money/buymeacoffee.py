import requests
import time

class BuyMeACoffee:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['buymeacoffee']['rate_limit'] / 1000
        # https://buymeacoffee.com/{username}
        self.format = config['plateform']['buymeacoffee']['format']
        # buymeacoffee usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # money
        self.type = config['plateform']['buymeacoffee']['type']

    # Generate all potential buymeacoffee usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        buymeacoffee_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to buymeacoffee")
            
            # If the account exists
            if r.status_code == 200:
                buymeacoffee_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return buymeacoffee_usernames