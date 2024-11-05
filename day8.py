import util

file_path = 'input/day8.txt'
value_signal_lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

decode_input = list(map(lambda input : [input[0].split(), input[1].split()], map(lambda input : input.split('|'), util.read_stripped_lines(file_path))))
solution_lengths = [2, 3, 4, 7]
solution = 0
for input in decode_input:
    signal_patterns = input[0]
    output_values = input[1]
    
    for value in output_values:
        if len(value) in solution_lengths:
            solution += 1
            print(value)
    print()
print(f'Solution: {solution}')