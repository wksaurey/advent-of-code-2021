import util

diag_report = util.read_stripped_lines('input/day3.txt')

gamma_rate = '' # common values
epsilon_rate = '' # least common values

for bit_index in range(len(diag_report[0])):
    bitCounts = [0, 0]

    for num in diag_report:
        bitCounts[int(num[bit_index])] += 1

    if bitCounts[0] > bitCounts[1]:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(f'gamma: {gamma_rate}')
print(f'epsilon: {epsilon_rate}')

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(f'gamma: {gamma_rate}')
print(f'epsilon: {epsilon_rate}')
print(f'power_consumption: {gamma_rate*epsilon_rate}')