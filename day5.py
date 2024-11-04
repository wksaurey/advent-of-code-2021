import util

def main():
    vent_data = util.read_stripped_lines('input/day5_test.txt', '\n')
    vent_data = list(map(lambda line : line.replace('->', '').split(), vent_data))
    vent_data = list(map(lambda line : Line(line), vent_data))
    for vent_index, vent in enumerate(vent_data):
        print(f'Vent {vent_index}')
        print(f'\tStart:')
        print(f'\t\tx: {vent.start["x"]}')
        print(f'\t\ty: {vent.start["y"]}')
        print(f'\tEnd:')
        print(f'\t\tx: {vent.end["x"]}')
        print(f'\t\ty: {vent.end["y"]}')


class Line():
    def __init__(self, line):
        self.start = {}
        self.end = {}
        self.define_points(line)

    def define_points(self, line):
        self.start = {
            'x': line[0].split(',')[0],
            'y': line[0].split(',')[1]
        }
        self.end = {
            'x': line[1].split(',')[0],
            'y': line[1].split(',')[1]
        }

main()