class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]) == 1:
                    self.dfs(grid, i, j)
                    result += 1
        return result


    def dfs(self, grid, i, j):
#       if out of bound or already visited/no val, just return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or int(grid[i][j]) != 1:
            return
#       mark as read
        grid[i][j] = -1
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)