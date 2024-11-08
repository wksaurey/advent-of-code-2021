import util

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

        low_points.append(value)

print(f'Low Points: {low_points}')
print(f'Risk Level: {sum(low_points) + len(low_points)}')