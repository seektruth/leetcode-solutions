/**
 * Created by smileMan on 2017/7/12.
 */
public class Leetcode59 {
    boolean[][] visited;
    int n;

    int[] nextPosition(int i, int j){
        if(i <= j+1 && j + 1< n && !visited[i][j+1]){
            return new int[]{i, j + 1};
        }
        else if(i + 1 < n && !visited[i+1][j]){
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

    public int[][] generateMatrix(int n) {
        this.n = n;
        visited = new boolean[n][n];
        int[][] matrix = new int[n][n];
        int i = 0;
        int j = 0;
        int num = 1;
        while (i < n && j <n && !visited[i][j]){
            visited[i][j] = true;
            matrix[i][j] = num++;
            int[] newPositon = nextPosition(i,j);
            i = newPositon[0];
            j = newPositon[1];
        }
        return matrix;
    }

    public static void main(String[] args){
        Leetcode59 leetcode59 = new Leetcode59();
        int[][] matrix = leetcode59.generateMatrix(0);
        for (int[] a: matrix){
            for(int b: a)
                System.out.print(b+" ");
            System.out.println();
        }
    }
}
