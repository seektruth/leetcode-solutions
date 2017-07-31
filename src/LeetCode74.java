public class LeetCode74 {
    public boolean searchMatrix(int[][] matrix, int target) {
        double lo = 0;
        double hi = matrix.length;
        if(matrix.length == 0)
            return false;
        if(matrix[0] == null)
            return false;
        while (hi - lo > 1){
            if(target == matrix[(int)lo][0])
                return true;
            else if(matrix[(int)lo][0] < target){
                double mi = lo + (hi - lo) / 2;
                if(target < matrix[(int)mi][0])
                    hi = mi;
                else if(target == matrix[(int)mi][0])
                    return true;
                else
                    lo = mi;
            }
            else return false;
        }

        double lo2 = 0;
        double hi2 = matrix[(int)lo].length;
        while (hi2 - lo2 >= 1){
            double mid = lo2 + (hi2 - lo2) / 2;
            if(target < matrix[(int)lo][(int)mid])
                hi2 = mid;
            else if(target == matrix[(int)lo][(int)mid])
                return true;
            else
                lo2 = mid;
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1},
                {3},
                {5}
        };

        System.out.println(new LeetCode74().searchMatrix(matrix,3));
    }
}
