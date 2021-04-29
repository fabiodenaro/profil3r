import requests
import time

class Pinterest:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['pinterest']['rate_limit'] / 1000
        # https://pinterest.fr/{username}
        self.format = config['plateform']['pinterest']['format']
        # pinterest usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # social
        self.type = config['plateform']['pinterest']['type']

    # Generate all potential pinterest usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        pinterest_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to pinterest")
            
            # If the account exists
            if r.status_code == 200:
                pinterest_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return pinterest_usernames