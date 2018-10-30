class Solution:
    row = [0, 0, 1, -1]
    col = [1, -1, 0, 0]

    def numIslands(self, grid):

        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '*'
        for k in range(len(self.row)):
            self.dfs(grid, i + self.row[k], j + self.col[k])
