import requests
import time

class Hackernews:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['hackernews']['rate_limit'] / 1000
        # https://news.ycombinator.com/user?id={username}
        self.format = config['plateform']['hackernews']['format']
        # hackernews usernames are not case sensitive
        self.permutations_list = permutations_list
        # forum
        self.type = config['plateform']['hackernews']['type']

    # Generate all potential hackernews usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        hackernews_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to hackernews")
            
            # If the account exists
            if r.text.find("No such user.") != 0:
                hackernews_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return hackernews_usernames