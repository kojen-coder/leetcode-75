class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt, n = 0, len(grid)

        row_counter = collections.Counter(tuple(row) for row in grid)

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            cnt += row_counter[tuple(col)]
        return cnt