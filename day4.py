def main():
    nums, boards = get_data()
    bingo_boards = []
    for board in boards:
        bingo_boards.append(Bingo_board(board))

    boards_won = 0
    for num in nums:
        for board_index, bingo_board in enumerate(bingo_boards):
            if bingo_board.won == True:
                continue
            if num in bingo_board.nums:
                result = bingo_board.nums[num]
                bingo_board.row_counts[result['row_index']] += 1
                bingo_board.col_counts[result['col_index']] += 1
                bingo_board.nums[num]['marked'] = True

            # check if win
            if bingo_board.size in bingo_board.row_counts or bingo_board.size in bingo_board.col_counts:
                bingo_board.won = True
                boards_won += 1
                if len(bingo_boards) == boards_won:
                    bingo_board.last_won = True
            
        if len(bingo_boards) == boards_won:
            for board_index, bingo_board in enumerate(bingo_boards):
                if bingo_board.last_won == True:
                    print(f'Board {board_index} is the last board!')
                    score = 0
                    for board_num in bingo_board.nums:
                        if bingo_board.nums[board_num]['marked'] == False:
                            score += int(board_num)
                    print(f'Score: {score * int(num)}')
                    return               

def get_data():
    with open('input/day4.txt') as file:
        nums = file.readline().strip().split(',')
        file.readline() # trash empty line

        boards = []
        board = []
        line = file.readline()
        while line:
            if line == '\n':
                boards.append(board)
                board = []
            else:
                board.append(line.split())

            line = file.readline()
        boards.append(board)
        return nums, boards
    
class Bingo_board:
    def __init__(self, board):
        self.nums = {}
        self.row_counts = [0] * len(board)
        self.col_counts = [0] * len(board)
        self.size = len(board)
        self.won = False
        self.last_won = False
        self.set_nums(board)

    def set_nums(self, board):
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                self.nums[value] = {
                    'marked': False,
                    'row_index': row_index,
                    'col_index': col_index
                }

main()