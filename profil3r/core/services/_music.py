from profil3r.modules.music.soundcloud import Soundcloud

# Soundcloud
def soundcloud(self):
    self.result["soundcloud"] = Soundcloud(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("soundcloud")