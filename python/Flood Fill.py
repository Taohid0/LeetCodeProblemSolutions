class Solution:
    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]

    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return image

        row = len(image)
        col = len(image[0])
        visited = [[0 for i in range(col)] for j in range(row)]
        color = image[sr][sc]

        def dfs(sr2, sc2):
            visited[sr2][sc2] = 1
            image[sr2][sc2] = newColor

            for i in range(len(self.x)):
                x1 = sr2 + self.x[i]
                y1 = sc2 + self.y[i]

                if x1 >= 0 and y1 >= 0 and x1 < row and y1 < col and not visited[x1][y1] and image[x1][y1] == color:
                    dfs(x1, y1)

        dfs(sr, sc)
        return image
