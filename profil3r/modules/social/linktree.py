import requests
import time

class LinkTree:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['linktree']['rate_limit'] / 1000
        # https://linktr.ee/{username}
        self.format = config['plateform']['linktree']['format']
        # linktree usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # social
        self.type = config['plateform']['linktree']['type']

    # Generate all potential linktree usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        linktree_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to linktree")
            
            # If the account exists
            if r.status_code == 200:
                linktree_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return linktree_usernames