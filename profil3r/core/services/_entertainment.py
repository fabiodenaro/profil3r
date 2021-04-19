from profil3r.modules.entertainment.dailymotion import Dailymotion

# Dailymotion
def dailymotion(self):
    self.result["dailymotion"] = Dailymotion(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("dailymotion")