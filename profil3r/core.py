import sys
from itertools import chain, combinations, permutations
import json
from profil3r.modules.email import email
from profil3r.modules.social import facebook, twitter, tiktok, instagram
from profil3r.modules.music import soundcloud
from profil3r.modules.forum import zeroxzerozerosec, jeuxvideo
from profil3r.modules.programming import github, pastebin
from profil3r.modules.tchat import skype
from profil3r.modules.entertainment import dailymotion
from profil3r.colors import Colors
import threading
import json
import os

result = {}

class Core:

    def __init__(self, config_path, items):
        with open(config_path, 'r') as f:
            self.CONFIG = json.load(f)
        # Items passed from the command line
        self.items = items
        self.permutations_list = []
        self.modules = {
            # Emails
            "email":             {"method" : self.email },
            # Social
            "facebook":          {"method" : self.facebook},
            "twitter":           {"method" : self.twitter},
            "tiktok":            {"method" : self.tiktok},
            "instagram":         {"method" : self.instagram},
            # Music
            "soundcloud":        {"method" : self.soundcloud},
            # Programming 
            "github":            {"method" : self.github},
            "pastebin":          {"method" : self.pastebin},
            # Forums:
            "0x00sec":           {"method" : self.zeroxzerozerosec},
            "jeuxvideo.com":     {"method" : self.jeuxvideo},
            # Tchat
            "skype":             {"method" : self.skype},
            # Entertainment
            "dailymotion":       {"method" : self.dailymotion}
        }

    # Remove modules that do not exist
    def get_report_modules(self):
        return list( set(self.CONFIG["report_elements"]) & set(list(self.CONFIG["plateform"].keys())) )

    # return all possible permutation for a username
    # exemple : ["john", "doe"] -> ("john", "doe", "johndoe", "doejohn", "john.doe", "doe.john") 
    def get_permutations(self):
        self.items.append('.')
        combinations_list = list(chain(*map(lambda x: combinations(self.items, x), range(1, len(self.items) + 1))))   
        for combination in combinations_list:
            # Remove combinations that start or end by a dot
            for perm in list(permutations(combination)):
                if not perm[0] == "." and not perm[-1] == ".":
                    self.permutations_list.append("".join(perm))
    
    # Emails
    def email(self):
        result["email"] = email.Email(self.CONFIG, self.permutations_list).search()
        # print results
        self.print_results("email")

    # Facebook
    def facebook(self):
        result["facebook"] = facebook.Facebook(self.CONFIG, self.permutations_list).search()
        # print results
        self.print_results("facebook")
    
    # Twitter
    def twitter(self):
        result["twitter"] = twitter.Twitter(self.CONFIG, self.permutations_list).search()
        # print results
        self.print_results("twitter")

    # TikTok
    def tiktok(self):
        result["tiktok"] = tiktok.TikTok(self.CONFIG, self.permutations_list).search()
        # print results
        self.print_results("tiktok")

    # Instagram
    def instagram(self):
        result["instagram"] = instagram.Instagram(self.CONFIG, self.permutations_list).search()
        # print results
        self.print_results("instagram")
    
    # Soundcloud
    def soundcloud(self):
        result["soundcloud"] = soundcloud.Soundcloud(self.CONFIG, self.permutations_list).search()
        # print results
        self.print_results("soundcloud")

    # Github
    def github(self):
        result["github"] = github.Github(self.CONFIG, self.permutations_list).search()
        # print results
        self.print_results("github")

    # 0x00sec
    def zeroxzerozerosec(self):
        result["0x00sec"] = zeroxzerozerosec.ZeroxZeroZeroSec(self.CONFIG, self.permutations_list).search() 
        # print results
        self.print_results("0x00sec")

    # jeuxvideo.com
    def jeuxvideo(self):
        result["jeuxvideo.com"] = jeuxvideo.JeuxVideo(self.CONFIG, self.permutations_list).search() 
        # print results
        self.print_results("jeuxvideo.com")

    # Skype
    def skype(self):
        result["skype"] = skype.Skype(self.CONFIG, self.permutations_list).search() 
        # print results
        self.print_results("skype")
    
    # Dailymotion
    def dailymotion(self):
        result["dailymotion"] = dailymotion.Dailymotion(self.CONFIG, self.permutations_list).search() 
        # print results
        self.print_results("dailymotion")

    # Pastebin
    def pastebin(self):
        result["pastebin"] = pastebin.Pastebin(self.CONFIG, self.permutations_list).search() 
        # print results
        self.print_results("pastebin")

    def print_results(self, element):
        if element in result:
            element_results = result[element]
            
            # Section title

            # No results
            if not element_results["accounts"]:
                print("\n" + Colors.BOLD + "└──" + Colors.ENDC + Colors.OKGREEN + " {} ✔️".format(element.upper()) + Colors.ENDC + Colors.FAIL + " (No results)" + Colors.ENDC)
                return 
            # Results
            else: 
                print("\n" + Colors.BOLD + "└──" + Colors.ENDC + Colors.OKGREEN + " {} ✔️".format(element.upper()) + Colors.ENDC)

            # General case
            if element != "email":
        
                for account in element_results["accounts"]:
                    print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.HEADER + account["value"] + Colors.ENDC)
            
            # Emails case
            else:
                possible_emails_list = [account["value"] for account in element_results["accounts"]]
                
                for account in element_results["accounts"]:
                     # We pad the emails with spaces for better visibility
                    longest_email_length = len(max(possible_emails_list))
                    email = account["value"].ljust(longest_email_length + 5)

                    # Breached account
                    if account["breached"]:
                        print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.HEADER + email + Colors.FAIL + "[BREACHED]" + Colors.ENDC)
                    # Safe account
                    else:
                        print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.HEADER + email + Colors.OKGREEN + "[SAFE]" + Colors.ENDC)

    # Generate a report in JSON format containing the collected data
    # Report will be in "./reports/"
    # You can modify th path in the config.json file
    def generate_report(self):
        # Create ./reports directory if not exists
        if not os.path.exists('reports'):
            os.makedirs('reports')

        file_name = self.CONFIG["report_path"].format("_".join(self.items[:-1]))
        try:
            with open(file_name, 'w') as fp:
                json.dump(result, fp, indent=2)
        except Exception as e:
            print(e)

        print("\n" + Colors.BOLD + "[+] " + Colors.ENDC + "Report was generated in {}".format(file_name))

    def run(self):
        modules = self.get_report_modules()

        print("\n" + "Profil3r will search : \n " + Colors.BOLD + "[+] " + Colors.ENDC +  "{} \nyou can add more services in the config.json file\n".format(str('\n ' + Colors.BOLD + "[+] " + Colors.ENDC).join(modules)))

        for module in modules:
            thread = threading.Thread(target=self.modules[module]["method"])
            thread.start()
            thread.join()
        self.generate_report()