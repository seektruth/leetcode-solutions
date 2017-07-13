/**
 * Created by smileMan on 2017/7/13.
 */
public class Leetcode62 {
    public int uniquePaths(int m, int n) {
        if(m > n){
            m = m + n;
            n = m - n;
            m = m - n;
        }
        double uniqueNum = 1;
        for(int i = 1; i < n; i++){
            uniqueNum = uniqueNum * (m + i - 1) / i;
        }
        return (int)uniqueNum;
    }

    public static void main(String[] args){
        Leetcode62 leetcode62 = new Leetcode62();
        for(int i = 1;i <= 10;i++){
            for(int j = 1;j <= 10;j++){
                System.out.println(i + " " + j + ":" +leetcode62.uniquePaths(23,12));
            }
        }
    }
}
