/**
 * Created by smileMan on 2017/7/13.
 */
public class Leetcode63 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] uniquePathNum = new int[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(obstacleGrid[i][j] == 1)
                    uniquePathNum[i][j] = 0;
                else if(i == 0 && j== 0)
                    uniquePathNum[i][j] = 1;
                else
                    uniquePathNum[i][j] = (j - 1 >= 0? uniquePathNum[i][j - 1]: 0) + (i - 1 >= 0? uniquePathNum[i-1][j]: 0);
            }

        }
        return uniquePathNum[m - 1][n - 1];
    }

    public static void main(String[] args){
        int[][] matrix = new int[3][3];
        matrix[1][1] = 1;
        System.out.println(new Leetcode63().uniquePathsWithObstacles(matrix));
    }
}
