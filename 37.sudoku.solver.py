class Solution(object):
    global board_size
    board_size = 9
    def solveSudoku(self, board):
        b = self.construct_board(board)
        if (self.solve(b)):
            # return self.reconstruct_answer(b)
            print 'yay'
        return ''


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """        
        # for all the non '.' grids

        for i in xrange(9):
            for j in xrange(9):
                if (board[i][j] == '.'):
                    continue

                # fill one number and try, k = 1 to 9
                for k in xrange(1, 9+1):
                    if self.check_valid(board, i, j, k) == False:
                        continue
                    board[i][j] = `k`;
                    
                    # continue with this selection
                    if (self.solve(board)):
                        return True

                    else:
                        # revert the change
                        board[i][j] = '.'
                # if we exit this loop without finding one answer, it's
                # impossible
                return False
        # terminating  condition for the the board with/o blank
        return True


    def check_valid(self, board, row, col, num):
        """
        Check whether the filled number can be accepted, i.e.
        no duplicate in the row, column and box
        """
        for i in xrange(9):
            if board[row][i] == `num`:
                return False
        for i in xrange(9):
            if board[i][col] == `num`:
                return False
        row_bound = row - row % 3
        col_bound = col - col % 3

        for i in xrange(3):
            for j in xrange(3):
                if board[row_bound + i][col_bound + j] == `num`:
                    return False

        return True

    def construct_board(self, board):
        b = []
        for i in xrange(9):
            b.append(list(s for s in board[i]))
        return b

    def reconstruct_answer(self, b):
        ans = []
        for i in xrange(9):
            ans.append(''.join(s for s in b[i]))
        return ans
if __name__ == '__main__':
    print Solution().solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
