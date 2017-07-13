/**
 * Created by smileMan on 2017/7/13.
 */
public class LeetCode64 {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(i == 0 && j == 0)
                    continue;
                grid[i][j] = Integer.min(i - 1 >= 0? grid[i - 1][j] + grid[i][j] : Integer.MAX_VALUE,
                        j - 1 >= 0? grid[i][j - 1] + grid[i][j]: Integer.MAX_VALUE);
            }
        }
        return grid[m - 1][n - 1];
    }
}
