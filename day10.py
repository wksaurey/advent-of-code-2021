import util

# filepath = 'input/day10_test.txt'
filepath = 'input/day10.txt'
nav_code = util.read_stripped_lines(filepath)
for line in nav_code:
    print(line)

open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']
illegal_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

illegal_score = 0

for line in nav_code:
    char_stack = []
    for char in line:
        if char in open_chars:
            char_stack.append(char)
        elif char in close_chars:
            if len(char_stack) == 0:
                # incomplete line
                break
            open_char = char_stack[-1]
            if open_chars.index(open_char) == close_chars.index(char):
                # close current chunk
                char_stack.pop()
            else:
                illegal_score += illegal_scores[char]
                break

print(f'Illegal Score: {illegal_score}')
