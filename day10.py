import util

filepath = 'input/day10.txt'
# filepath = 'input/day10.txt'
nav_code = util.read_stripped_lines(filepath)

open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']
illegal_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

illegal_score = 0
completion_scores = []

for line in nav_code:
    char_stack = []
    complete_chars = []
    is_legal = True
    for char in line:
        if char in open_chars:
            char_stack.append(char)
        elif char in close_chars:
            open_char = char_stack[-1]
            if open_chars.index(open_char) == close_chars.index(char):
                # close current chunk
                char_stack.pop()
            else:
                is_legal = False
                illegal_score += illegal_scores[char]
                break
    if is_legal:
        completion_score = 0
        for char in char_stack:
            complete_chars[:0] = (close_chars[open_chars.index(char)])
        complete_chars = ''.join(complete_chars)
        print(complete_chars)
        for char in complete_chars:
            completion_score *= 5
            completion_score += close_chars.index(char)+1
        completion_scores.append(completion_score)


print(f'Illegal Score: {illegal_score}')
while len(completion_scores) != 1:
    completion_scores.remove(max(completion_scores))
    completion_scores.remove(min(completion_scores))
print(f'Completion Score: {completion_scores[0]}')
