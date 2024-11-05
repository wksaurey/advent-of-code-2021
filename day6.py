import util
import time
TOTAL_DAYS=256

fish_scan_data = util.read_stripped_lines('input/day6.txt')[0].split(',')
fish_data = list(map(int, fish_scan_data))
print(f'Initial state: {",".join(map(str, fish_data))}')

buffer = [0] * 7
new_fish = [0] * 2
for fish in fish_data:
    buffer[fish] += 1
pointer_index = 0
print(buffer)
print(new_fish)

start = time.time()
for day_index in range(TOTAL_DAYS):
    # print(f'Day {day_index}')
    temp = new_fish[0]    
    new_fish[0] = new_fish[1]
    new_fish[1] = buffer[pointer_index]
    buffer[pointer_index] += temp
    pointer_index += 1
    if pointer_index == 7:
        pointer_index = 0

    print(f'Day: {day_index}')
    print(f'Population {sum(buffer) + sum(new_fish)}')
end = time.time()
print(f'Run in {end-start} seconds')