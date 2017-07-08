/**
 * Created by smileMan on 2017/7/8.
 */
public class Leetcode48 {
    static class Solution {
        public void rotate(int[][] matrix) {
            int n = matrix.length;
            for(int i = 0; i < n/2; i++){
                for(int j = i; j - i < n - 2 * i -1;j++){
                    int lt = matrix[i][j];
                    int rt = matrix[j][n - i - 1];
                    int rb = matrix[n - i - 1][n - j - 1];
                    int lb = matrix[n - j - 1][i];
                    matrix[j][n - i - 1] = lt;
                    matrix[n - i - 1][n - j - 1] = rt;
                    matrix[n - j - 1][i] = rb;
                    matrix[i][j] = lb;
                }
            }
        }
    }

    public static void main(String[] args){
        int[][] matrix = {};
        Solution solution = new Solution();
        solution.rotate(matrix);
        for(int[] a : matrix){
            for(int b : a)
                System.out.print(b+" ");
            System.out.print("\n");
        }
    }
}
