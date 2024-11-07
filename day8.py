import util
import sys

file_path = 'input/day8_test.txt'
value_signal_lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def main():
    decode_input = list(map(lambda input : [input[0].split(), input[1].split()], map(lambda input : input.split('|'), util.read_stripped_lines(file_path))))
    result_total = 0
    for input in decode_input:
        number_lengths = [[] for _ in range(8)]
        solutions = [''] * 10
        signal_patterns = input[0]
        output_values = input[1]
        # signal_patterns = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
        
        for pattern in signal_patterns:
            number_lengths[len(pattern)].append(pattern)
            if len(pattern) == 2:
                solutions[1] = pattern
            elif len(pattern) == 3:
                solutions[7] = pattern
            elif len(pattern) == 4:
                solutions[4] = pattern
            elif len(pattern) == 7:
                solutions[8] = pattern

        # solve len 5 nums
        for index_0, pattern_0 in enumerate(number_lengths[5]):
            for index_1, pattern_1 in enumerate(number_lengths[5]):
                if index_0 == index_1:
                    continue
                not_included = difference(pattern_0, pattern_1)
                if len(not_included) == 2:
                    values = [0, 1, 2]
                    for value in values:
                        if value != index_0 or value != index_1:
                            solutions[3] = number_lengths[5][value]
                            if len(difference(number_lengths[5][index_0], solutions[4])) == 3:
                                solutions[2] = number_lengths[5][index_0]
                                solutions[5] = number_lengths[5][index_1]
                            else:
                                solutions[2] = number_lengths[5][index_1]
                                solutions[5] = number_lengths[5][index_0]


        for pattern in number_lengths[6]:
            if len(difference(solutions[1], pattern)) == 1:
                solutions[6] = pattern
            elif len(difference(solutions[3], pattern)) == 1:
                solutions[0] = pattern
        number_lengths[6].remove(solutions[0])
        number_lengths[6].remove(solutions[6])
        

        solutions[9] = number_lengths[6][0]

        # print('Solution:')
        # for index, solution in enumerate(solutions):
        #     print(f'{index}: {solution}')

        result = ''
        for value in output_values:
            for index, solution in enumerate(solutions):
                if difference(value, solution) == '' and difference(solution, value) == '':
                    result += str(index)
                    break
        print(result)
        result_total += int(result)
    print(f'Result Total: {result_total}')

def difference(pattern_0, pattern_1):
    not_included = ''
    for char_0 in pattern_0:
        if char_0 not in pattern_1:
            not_included += char_0
    return not_included

main()