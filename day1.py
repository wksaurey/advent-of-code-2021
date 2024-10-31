import util
import matplotlib.pyplot as plt

depth_data = util.read_stripped_lines('input/day1.txt')
depth_data = list(map(int, depth_data))

depth_increase_count = 0
depth_not_increase_count = 0
for index, value in enumerate(depth_data):
    if index == 0:
        continue
    if value > depth_data[index-1]:
        depth_increase_count += 1

print(depth_increase_count)

# y_values = list(map(lambda x : -int(x) , depth_data))
# x_values = list(range(1, 2001))
# plt.plot(x_values, y_values)

# plt.savefig("day1_graph.png")


# 1712 too low