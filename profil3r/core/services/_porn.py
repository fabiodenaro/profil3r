from profil3r.modules.porn.pornhub import Pornhub
from profil3r.modules.porn.redtube import Redtube

# Pornhub
def pornhub(self):
    self.result["pornhub"] = Pornhub(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("pornhub")

# Redtube
def redtube(self):
    self.result["redtube"] = Redtube(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("redtube")