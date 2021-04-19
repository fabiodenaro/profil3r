from profil3r.modules.forum.zeroxzerozerosec import ZeroxZeroZeroSec
from profil3r.modules.forum.jeuxvideo import JeuxVideo

# 0x00sec
def zeroxzerozerosec(self):
    self.result["0x00sec"] = ZeroxZeroZeroSec(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("0x00sec")

# jeuxvideo.com
def jeuxvideo(self):
    self.result["jeuxvideo.com"] = JeuxVideo(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("jeuxvideo.com")