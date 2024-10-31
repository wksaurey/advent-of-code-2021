import util

commands = util.read_stripped_lines('input/day2.txt')

xpos = 0
ypos = 0
for command in commands:
    command = command.split()
    direction = command[0]
    distance = int(command[1])

    if direction == 'up':
        ypos -= distance
    elif direction == 'down':
        ypos += distance
    else:
        xpos += distance

print(f'x: {xpos}')
print(f'y: {ypos}')
print(f'product: {xpos*ypos}')