import java.util.LinkedList;
import java.util.List;

/**
 * Created by smileMan on 2017/7/10.
 */

public class Leetcode54 {
    static class Solution {
        int m;
        int n;
        boolean[][] visited;

        int[] nextPosition(int i, int j){
            if(i <= j+1 && j + 1< n && !visited[i][j+1]){
                return new int[]{i, j + 1};
            }
            else if(i + 1 < m && !visited[i+1][j]){
                return new int[]{i + 1, j};
            }
            else if(j - 1 >= 0 && !visited[i][j-1]){
                return new int[]{i, j - 1};
            }
            else if(i - 1 >= 0 && !visited[i - 1][j]){
                return new int[]{i - 1, j};
            }
            else
                return new int[]{0, 0};
        }

        public List<Integer> spiralOrder(int[][] matrix) {
            m = matrix.length;
            if(m > 0)
                n = matrix[0].length;
            if(m == 0)
                return new LinkedList<>();
            visited = new boolean[m][n];
            int i = 0;
            int j = 0;
            List<Integer> cons = new LinkedList<>();
            while (!visited[i][j]){
                cons.add(matrix[i][j]);
                visited[i][j] = true;
                int[] next = nextPosition(i, j);
                i = next[0];
                j = next[1];
            }
            return cons;
        }
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int[][] sample = {
                {1,2,3,4},
                {5,6,7,8},
                {9,10,11,12},
                {13,14,15,16},
                {17,18,19,20}
        };

        List<Integer> c = solution.spiralOrder(sample);
        System.out.println(c);
    }
}
