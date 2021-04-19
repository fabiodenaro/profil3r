from profil3r.modules.social.facebook import Facebook
from profil3r.modules.social.twitter import Twitter
from profil3r.modules.social.tiktok import TikTok
from profil3r.modules.social.instagram import Instagram

# Facebook
def facebook(self):
    self.result["facebook"] = Facebook(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("facebook")

# Twitter
def twitter(self):
    self.result["twitter"] = Twitter(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("twitter")

# TikTok
def tiktok(self):
    self.result["tiktok"] = TikTok(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("tiktok")

# Instagram
def instagram(self):
    self.result["instagram"] = Instagram(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("instagram")