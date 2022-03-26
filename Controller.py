from collections import defaultdict
from sys import exit

class Controller:
    def __init__(self, filters):
        self.filters = filters

    def run(self):
        self.results = defaultdict(int)
        for f_filter in self.filters:
            if f_filter.match():
                d[str(f_filter)] = 1

        if any(i > 0 for i in self.results.values()):
            print('Rules matched')
            for key, value in self.results:
                print(f"Rule {key} has {value}")
            sys.exit(-1)
        else:
            print('No rules matched')

