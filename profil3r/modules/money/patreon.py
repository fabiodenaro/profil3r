import requests
import time

class Patreon:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['patreon']['rate_limit'] / 1000
        # https://patreon.com/{username}
        self.format = config['plateform']['patreon']['format']
        # patreon usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # money
        self.type = config['plateform']['patreon']['type']

    # Generate all potential patreon usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        patreon_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to patreon")
            
            # If the account exists
            if r.status_code == 200:
                patreon_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return patreon_usernames