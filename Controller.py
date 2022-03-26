from collections import defaultdict
import sys
from colors import color

class Controller:
    def __init__(self, filters):
        self.filters = filters

    def run(self):
        self.results = defaultdict(bool)
        for f_filter in self.filters:
            if f_filter.match():
                self.results[str(f_filter)] = True

        if any(i > 0 for i in self.results.values()):
            print('Rules matched')
            for key, value in self.results.items():
                if value:
                    print(f"{color.bcolors.FAIL}Rule {key} has {value}{color.bcolors.ENDC}")
                else:
                    print(f"{color.bcolors.OKCYAN}Rule {key} has {value}{color.bcolors.ENDC}")
            sys.exit(-1)
        else:
            print('No rules matched')

class EC2():
    def __repr__(self):
        return f"Rule EC2"
    def __init__(self):
        pass
    def match(self):
        return True
f = [EC2()]
c = Controller(f)
c.run()
