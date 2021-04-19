from profil3r.core.colors import Colors
import threading

def run(self):
    self.print_logo()

    # No argument
    if not len(self.items):
        print('''Profil3r is an OSINT tool that allows you to find potential profiles of a person on social networks, as well as their email addresses. This program also alerts you to the presence of a data leak for the found emails.

    Usage : ./main.py <arguments>
    for exemple : ./main.py john doe
                ./main.py john doe 67''')

    else:
        self.menu()
        self.get_permutations()

        modules = self.get_report_modules()

        print("\n" + "Profil3r will search : \n " + Colors.BOLD + "[+] " + Colors.ENDC +  "{} \n".format(str('\n ' + Colors.BOLD + "[+] " + Colors.ENDC).join(modules)))

        for module in modules:
            thread = threading.Thread(target=self.modules[module]["method"])
            thread.start()
            thread.join()
        self.generate_report()