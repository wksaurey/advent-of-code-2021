def main():
    nums, boards = get_data()

def get_data():
    with open('input/day4_test.txt') as file:
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
    

main()