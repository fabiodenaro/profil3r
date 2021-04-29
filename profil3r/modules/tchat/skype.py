import requests
import time

class Skype:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['skype']['rate_limit'] / 1000
        # https://www.skypli.com/profile/{}
        self.format = config['plateform']['skype']['format']
        self.permutations_list = permutations_list
        # tchat
        self.type = config['plateform']['skype']['type']

    # Generate all potential skype usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        skype_usernames = {
            "type": self.type,
            "accounts" : []
        }

        skypli_URL = "https://www.skypli.com/profile/{}"

        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                skypli_formatted_URL = skypli_URL.format(username)
                r = requests.get(skypli_formatted_URL)
            except requests.ConnectionError:
                print("failed to connect to skype")
            
            # If the account exists
            if r.status_code == 200:
                skype_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return skype_usernames