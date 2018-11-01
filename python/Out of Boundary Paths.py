class Solution:
    def findPaths(self, m, n, N, i, j):
        if N == 0:
            return 0
        dp = [[0 for i in range(m)] for j in range(n)]
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        global counter
        counter = 0

        def dfs(i2, j2, N2):

            for i in range(4):
                x1 = i2 + x[i]
                y1 = j2 + y[i]

                if (x1 < 0 or y1 < 0 or x1 == m or y1 == n) and N2:
                    global counter
                    counter = (counter + 1) % (10 ** 9 + 7)

                elif N2:
                    dfs(x1, y1, N2 - 1)

        dfs(i, j, N)
        return counter


result = Solution().findPaths(2, 5, 9, 1, 3)
print(result)
