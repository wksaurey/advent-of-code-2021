import util

def main():
    crab_pos = util.read_stripped_lines('input/day7.txt')[0].split(',')
    crab_pos = list(map(int, crab_pos))
    print(crab_pos)

    fuel_use = []
    for position in range(min(crab_pos), max(crab_pos)):
        fuel = calculate_fuel(crab_pos, position)
        fuel_use.append(fuel)
        print(f'Pos  : {position}')
        print(f'Fuel : {fuel}')
    print(f'Min: {min(fuel_use)}')



def calculate_fuel(crab_pos, position):
    fuel = 0
    for crab in crab_pos:
        distance = abs(position - crab)
        for value in range(distance+1):
            fuel += value
    return fuel

main()