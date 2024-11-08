import util

def main():
    filepath = 'input/day9.txt'
    heightmap = list(map(lambda line : list(map(int, line)), util.read_stripped_lines(filepath)))
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


    result_sum = sum(low_points)
    print(f'Risk Level: {result_sum + len(low_points)}')

class Point():
    def __init__(self, value, row_index, col_index, is_low_point=False):
        self.value = value
        self.row_index = row_index
        self.col_index = col_index
    
    def __eq__(self, other):
        return self.row_index == other.row_index and self.col_index == other.col_index

    def __add__(self, other):
        return self.value + other.value
    
    def __radd__(self, other):
        if isinstance(other, int):
            return self.value + other
        return self.__add__(other)

    def __str__(self):
        return str(self.value)
    

main()