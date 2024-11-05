import util
TOTAL_DAYS=80

fish_scan_data = util.read_stripped_lines('input/day6.txt')[0].split(',')
fish_data = list(map(int, fish_scan_data))
# 0 is new fish, 1 has already repopulated
# print(f'Initial state: {",".join(map(str, fish_data))}')

for day_index in range(TOTAL_DAYS):
    new_fish = []
    for fish_index, fish in enumerate(fish_data):
        if fish == 0:
            new_fish.append(8)
            fish_data[fish_index] = 6
        else:
            fish_data[fish_index] -= 1
    fish_data = fish_data + new_fish
    # print(f'After {day_index} days: {",".join(map(str, fish_data))}')
print(f'Fish Count: {len(fish_data)}')