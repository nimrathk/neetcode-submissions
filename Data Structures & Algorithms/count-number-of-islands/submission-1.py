class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def dfs(r, c):
            visited.add((r, c))
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in dirs:
                if r + d[0] in range(len(grid)) and c + d[1] in range(len(grid[0])) and (r+d[0], c+d[1]) not in visited and grid[r+d[0]][c+d[1]] == "1":
                    dfs(r+d[0], c+d[1])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    count += 1

        return count