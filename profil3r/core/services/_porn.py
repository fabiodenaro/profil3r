from profil3r.modules.porn.pornhub import Pornhub

# Pornhub
def pornhub(self):
    self.result["pornhub"] = Pornhub(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("pornhub")