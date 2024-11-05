import util
import sys

X = 0
Y = 1

def main():
    vent_data = util.read_stripped_lines('input/day5.txt', '\n')
    vent_data = list(map(lambda line : line.replace('->', '').split(), vent_data))
    vent_data = list(map(lambda line : Line(line), vent_data))
    # print_data(vent_data)
    working_vent_data = []
    for vent in vent_data:
        if (vent.start[X] == vent.end[X]):
            vent.direction = 'col'
            working_vent_data.append(vent)
            vent.print_data()
        elif(vent.start[Y] == vent.end[Y]):
            vent.direction = 'row'
            working_vent_data.append(vent)
            vent.print_data()

    vent_map = map_data(working_vent_data)
    print_map(vent_map)
    count_overlap(vent_map)

def count_overlap(vent_map):
    count = 0
    for row in vent_map:
        for value in row:
            if value > 1:
                count += 1
    print(f'Count: {count}')

def map_data(vent_data):
    # create base map
    max_x = 0
    max_y = 0
    for vent in vent_data:
        max_x = max(max_x, max(vent.start[X], vent.end[X]))
        max_y = max(max_y, max(vent.start[Y], vent.end[Y]))
    print(f'Max: x = {max_x}, y = {max_y}')
    vent_map = [[0] * (max_x+1)] * (max_y+1)
    vent_map = [[0] * (max_x+1) for _ in range(max_y+1)]

    # fill in data
    for vent in vent_data:
        if vent.direction == 'col':
            row_index = min(vent.start[Y], vent.end[Y])
            col_index = vent.start[X]
            while row_index <= max(vent.start[Y], vent.end[Y]):
                vent_map[row_index][col_index] += 1
                row_index += 1
        elif vent.direction == 'row':
            col_index = min(vent.start[X], vent.end[X])
            row_index = vent.start[Y]
            while col_index <= max(vent.start[X], vent.end[X]):
                vent_map[row_index][col_index] += 1
                col_index += 1
        else:
            print('An error has occured')
            sys.exit(1)
    return vent_map


def print_map(vent_map):
    for row in vent_map:
        for value in row:
            print(value, end=' ')
        print()

def print_data(vent_data):
    for vent_index, vent in enumerate(vent_data):
        print(f'Vent {vent_index}')
        vent.print_data()

class Line():
    def __init__(self, line):
        self.start = {}
        self.end = {}
        self.direction = None
        self.define_points(line)

    def define_points(self, line):
        self.start = list(map(int, line[0].split(',')))
        self.end = list(map(int, line[1].split(',')))
    
    def print_data(self):
        print(f'Direction: {self.direction}')
        print(f'Start: ', end='')
        print(f'\tx: {self.start[X]}')
        print(f'\ty: {self.start[Y]}')
        print(f'End: ', end='')
        print(f'\tx: {self.end[X]}')
        print(f'\ty: {self.end[Y]}\n')


main()