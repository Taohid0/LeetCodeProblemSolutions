class Solution:
    row = [1,-1,0,0]
    col = [0,-1,1,-1]
    def maxAreaOfIslam(self, grif):
        visited = [[0 for i in range(51) for j in range(51)]]
        