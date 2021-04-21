from profil3r.modules.money.buymeacoffee import BuyMeACoffee

# BuyMeACoffee
def buymeacoffee(self):
    self.result["buymeacoffee"] = BuyMeACoffee(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("buymeacoffee")