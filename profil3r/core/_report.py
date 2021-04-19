from profil3r.colors import Colors
import json
import os

# Generate a report in JSON format containing the collected data
# Report will be in "./reports/"
# You can modify th path in the config.json file
def generate_report(self):
    # Create ./reports directory if not exists
    if not os.path.exists('reports'):
        os.makedirs('reports')

    file_name = self.CONFIG["report_path"].format("_".join(self.items[:-1]))
    try:
        with open(file_name, 'w') as fp:
            json.dump(self.result, fp, indent=2)
    except Exception as e:
        print(e)

    print("\n" + Colors.BOLD + "[+] " + Colors.ENDC + "Report was generated in {}".format(file_name))