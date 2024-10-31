import util

commands = util.read_stripped_lines('input/day2.txt')

xpos = 0
ypos = 0
aim = 0
for command in commands:
    command = command.split()
    direction = command[0]
    distance = int(command[1])

    if direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance
    else:
        xpos += distance
        ypos += aim * distance

print(f'x: {xpos}')
print(f'y: {ypos}')
print(f'product: {xpos*ypos}')