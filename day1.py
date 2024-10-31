import util
import matplotlib.pyplot as plt

depth_data = util.read_stripped_lines('input/day1.txt')
depth_data = list(map(int, depth_data))

depth_increase_count = 0
for index in range(4, len(depth_data)+1):
    previous_window = sum(depth_data[index-4:index-1])
    next_window = sum(depth_data[index-3:index])
    if next_window > previous_window:
        depth_increase_count += 1

print(depth_increase_count)

# y_values = list(map(lambda x : -int(x) , depth_data))
# x_values = list(range(1, 2001))
# plt.plot(x_values, y_values)

# plt.savefig("day1_graph.png")


# 1712 too low day1.1
# 1733 too low day1.2