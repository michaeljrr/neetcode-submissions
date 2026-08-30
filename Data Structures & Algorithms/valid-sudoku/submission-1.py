class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_check = set()
        size = 9

        # row check
        for i in range(size):
            for j in range(size):
                if board[i][j] in num_check and board[i][j] != ".":
                    return False
                num_check.add(board[i][j])
            num_check.clear()

        # column check
        for k in range(size):
            for l in range(size):
                if board[l][k] in num_check and board[l][k] != ".":
                    return False
                num_check.add(board[l][k])
            num_check.clear()

        # sub-box check
        for row in range(0, size, 3):
            for col in range(0, size, 3):
                for count in range(3):
                    if board[row + count][col] in num_check and board[row + count][col] != ".":
                        return False
                    num_check.add(board[row + count][col])

                    if board[row + count][col + 1] in num_check and board[row + count][col + 1] != ".":
                        return False
                    num_check.add(board[row + count][col + 1])

                    if board[row + count][col + 2] in num_check and board[row + count][col + 2] != ".":
                        return False
                    num_check.add(board[row + count][col + 2])
                num_check.clear()
        return True

             



                

