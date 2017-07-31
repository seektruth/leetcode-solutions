import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class LeetCode73 {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        Set<Integer> listRow = new HashSet<>();
        Set<Integer> listColumn = new HashSet<>();
        for(int i = 0; i<m;i++){
            for(int j = 0; j < n; j++){
                if(matrix[i][j] == 0){
                    listRow.add(i);
                    listColumn.add(j);
                }
            }
        }
        for(int i = 0; i<m;i++){
            for(int j = 0; j < n; j++){
                if(listRow.contains(i) || listColumn.contains(j)){
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
