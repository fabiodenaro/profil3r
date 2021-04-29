import requests
import time

class Spotify:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['spotify']['rate_limit'] / 1000
        # https://open.spotify.com/user/{}
        self.format = config['plateform']['spotify']['format']
        # spotify usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # spotify
        self.type = config['plateform']['spotify']['type']

    # Generate all potential spotify usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        spotify_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to spotify")
            
            # If the account exists
            if r.status_code == 200:
                spotify_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return spotify_usernames