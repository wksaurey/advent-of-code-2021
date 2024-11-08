import util

debug = True

def main():
    filepath = 'input/day9.txt'
    heightmap = list(map(lambda line : list(map(int, line)), util.read_stripped_lines(filepath)))
    
    low_points = find_low_points(heightmap)

    result_sum = sum(low_points)
    print(f'Risk Level: {result_sum + len(low_points)}')

    basins = find_basins(low_points, heightmap)
    basin_sizes = list(map(len, basins))
    largest = [0] * 3
    for index in range(len(largest)):
        largest[index] = (max(basin_sizes))
        basin_sizes.remove(max(basin_sizes))
    print(product(largest))

def product(values):
    product = values[0]
    for index in range(1, len(values)):
        product *= values[index]
    return product


def find_basins(low_points, heightmap):
    basins = []
    for low_point in low_points:
        to_check = Queue()
        to_check.add(low_point)
        checked = []

        while to_check.head:
            check_point = to_check.pop()
            if not check_point:
                # return results
                return
            
            # check surroundings
            index = check_point.col_index
            row_index = check_point.row_index
            if index != 0:
                left_point = Point(heightmap[row_index][index-1], row_index, index-1)
                if left_point.value != 9:
                    if not left_point in checked:
                        to_check.add(left_point)
            if index != len(heightmap[row_index])-1:
                right_point = Point(heightmap[row_index][index+1], row_index, index+1)
                if right_point.value != 9:
                    if not right_point in checked:
                        to_check.add(right_point)
            if row_index != 0:
                top_point = Point(heightmap[row_index-1][index], row_index-1, index)
                if top_point.value != 9:
                    if not top_point in checked:
                        to_check.add(top_point)
            if row_index != len(heightmap)-1:
                bottom_point = Point(heightmap[row_index+1][index], row_index+1, index)
                if bottom_point.value != 9:
                    if not bottom_point in checked:
                        to_check.add(bottom_point)

            if not check_point in checked:
                checked.append(check_point)
        for checked_point in checked:
            print(checked_point)
        print()
        basins.append(checked)
    for index, basin in enumerate(basins):
        print(f'Basin {index}: {len(basin)}')
    return basins


def find_low_points(heightmap):
    low_points = []
    for row_index, row in enumerate(heightmap):
        for index, value in enumerate(row):
            if index != 0:
                left_value = row[index-1]
                if value >= left_value:
                    continue
            if index != len(row)-1:
                right_value = row[index+1]
                if value >= right_value:
                    continue
            if row_index != 0:
                top_value = heightmap[row_index-1][index]
                if value >= top_value:
                    continue
            if row_index != len(heightmap)-1:
                bottom_value = heightmap[row_index+1][index]
                if value >= bottom_value:
                    continue

            low_point = Point(value, row_index, index, True)
            low_points.append(low_point)
    return low_points

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, point):
        new_node = Node(point)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head == None:
            print('Queue is empty')
            return None
        result = self.head
        if self.head == self.tail:
            self.tail = result.next
        self.head = result.next
        return result.point

        

class Node():
    def __init__(self, point):
        self.point = point
        self.next = None
        self.before = None


class Point():
    def __init__(self, value, row_index, col_index, is_low_point=False):
        self.value = value
        self.row_index = row_index
        self.col_index = col_index
    
    def __eq__(self, other):
        return (self.row_index == other.row_index and self.col_index == other.col_index)

    def __add__(self, other):
        return self.value + other.value
    
    def __radd__(self, other):
        if isinstance(other, int):
            return self.value + other
        return self.__add__(other)

    def __str__(self):
        return f'{str(self.value)}: [{self.col_index}, {self.row_index}]'

    def __gt__(self, other):
        return self.value > other.value
    

main()