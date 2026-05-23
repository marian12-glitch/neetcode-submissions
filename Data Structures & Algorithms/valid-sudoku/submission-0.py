class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows ={}
        column = {}
        box = {}

        #initialize nested for loop:
        for r in range(0, 9):
            

            for c in range(0, 9):
                rows.setdefault(r, set())
                column.setdefault(c, set())
                box.setdefault((r//3, c//3), set())

                if board[r][c] == ".":
                    continue

                #check if cell is already in the row
                if (board[r][c] in rows[r]):
                    return False

                #check is cell is in column
                if (board[r][c]  in column[c]):
                    return False

                #check if cell is in box
                if board[r][c] in box[(r//3,c//3)]:
                    return False

                rows[r].add(board[r][c])
                column[c].add(board[r][c])
                box[(r//3,c//3)].add(board[r][c])

                

        return True


                    


        