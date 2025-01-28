class Solution:
    def findMaxFish(self, grid):
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            fish = grid[r][c]
            grid[r][c] = 0  

            fish += dfs(r + 1, c)
            fish += dfs(r - 1, c)
            fish += dfs(r, c + 1)
            fish += dfs(r, c - 1)

            return fish 
        m, n = len(grid), len(grid[0]) 
        max_fish = 0  

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:  
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish
