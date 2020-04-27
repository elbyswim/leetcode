class Solution:
    def maximalSquare(self, matrix) -> int:
        max_s = 0
        def printSquare(matrix, i, j, s):
            print('Square at ({}, {}) with s = {}'.format(i, j, s))
            for x in range(i, i + s + 1):
                print(' '.join(matrix[x][j:j + s + 1]))


        def searchSquare(matrix, i, j, s):
            # if s in {3}:
            #     print(i, j, 3)
            if i + s >= len(matrix) or j + s >= len(matrix[0]):
                return s
            else:
                for x in range(j, j + s):
                    if matrix[i + s][x] != '1':
                        return s
                    # else:
                    #     if s == 3:
                    #         print(matrix[i + s][j])
                for y in range(i, i + s + 1):
                    if matrix[y][j + s] != '1':
                        return s
                    # else:
                    #     if i == 3:
                    #         print(matrix[y][j + s])
            if s in {2}:
                print('s = {}:'.format(s), i, j)
                printSquare(matrix, i, j, s)
            return searchSquare(matrix, i, j, s + 1)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    max_s = max(max_s, searchSquare(matrix, i, j, 1))
        return max_s ** 2


soln = Solution()
test = [["0", "1", "1", "0", "0", "1", "0", "1", "0", "1"], ["0", "0", "1", "0", "1", "0", "1", "0", "1", "0"],
        ["1", "0", "0", "0", "0", "1", "0", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "0", "1", "0"],
        ["0", "0", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0", "1", "1", "1", "1", "0"],
        ["0", "0", "0", "1", "1", "0", "0", "0", "1", "0"], ["1", "1", "0", "1", "1", "0", "0", "1", "1", "1"],
        ["0", "1", "0", "1", "1", "0", "1", "0", "1", "1"]]
print(soln.maximalSquare(test))
