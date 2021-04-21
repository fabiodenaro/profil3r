from profil3r.modules.email import email
import json

class Core(object):

    from ._menu import menu
    from ._permutations import get_permutations
    from ._results import print_results
    from ._run import run
    from ._report import generate_report
    from ._modules import modules_update, get_report_modules
    from ._logo import print_logo
    
    from .services._social import facebook, twitter, instagram, tiktok, pinterest
    from .services._forum import zeroxzerozerosec, jeuxvideo, hackernews
    from .services._programming import github, pastebin, replit
    from .services._tchat import skype
    from .services._music import soundcloud, spotify
    from .services._entertainment import dailymotion
    from .services._email import email
    from .services._porn import pornhub, redtube

    def __init__(self, config_path, items):
        self.version = "1.2.4"

        with open(config_path, 'r') as f:
            self.CONFIG = json.load(f)

        self.separators = []
        self.result = {}
        # Items passed from the command line
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
            "pinterest":         {"method" : self.pinterest},
            # Music
            "soundcloud":        {"method" : self.soundcloud},
            "spotify":           {"method" : self.spotify},
            # Programming 
            "github":            {"method" : self.github},
            "pastebin":          {"method" : self.pastebin},
            "replit":            {"method" : self.replit},
            # Forums:
            "0x00sec":           {"method" : self.zeroxzerozerosec},
            "jeuxvideo.com":     {"method" : self.jeuxvideo},
            "hackernews":        {"method" : self.hackernews},
            # Tchat
            "skype":             {"method" : self.skype},
            # Entertainment
            "dailymotion":       {"method" : self.dailymotion},
            # Porn 
            "pornhub":           {"method" : self.pornhub},
            "redtube":           {"method" : self.redtube}
        }