class Solution:
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]

    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        visited = [[0 for i in range(col)] for j in range(row)]

        def dfs(xx, yy, counter=0):
            visited[xx][yy] = 1
            counter = counter + 1

            for i in range(len(self.x)):
                x1 = xx + self.x[i]
                y1 = yy + self.y[i]

                if 0 <= x1 < row and 0 <= y1 < col and not visited[x1][y1] and grid[x1][y1]:
                    counter = dfs(x1, y1, counter)

            return counter


        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]:
                    result = max(result, dfs(i, j))

        return result