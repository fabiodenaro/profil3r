import requests
import time

class Pornhub:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['pornhub']['rate_limit'] / 1000
        # https://pornhub.com/users/{username}
        self.format = config['plateform']['pornhub']['format']
        # pornhub usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # porn
        self.type = config['plateform']['pornhub']['type']

    # Generate all potential pornhub usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        pornhub_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to pornhub")
            
            # If the account exists
            if r.status_code == 200:
                pornhub_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return pornhub_usernames