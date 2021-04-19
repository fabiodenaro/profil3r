from profil3r.colors import Colors
import threading

def run(self):
    self.menu()

    modules = self.get_report_modules()

    print("\n" + "Profil3r will search : \n " + Colors.BOLD + "[+] " + Colors.ENDC +  "{} \n".format(str('\n ' + Colors.BOLD + "[+] " + Colors.ENDC).join(modules)))

    for module in modules:
        thread = threading.Thread(target=self.modules[module]["method"])
        thread.start()
        thread.join()
    self.generate_report()