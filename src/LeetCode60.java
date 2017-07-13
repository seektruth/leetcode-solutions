import java.util.ArrayList;

/**
 * Created by smileMan on 2017/7/13.
 */
public class LeetCode60 {
    public String getPermutation(int n, int k) {
        ArrayList<Integer> integers = new ArrayList<Integer>(){{
           for(int i = 1;i <= n;i++){
               add(i);
           }
        }};
        String consquence = "";
        int[] factorials = {1, 1, 2, 6, 24, 120, 720, 5040, 40320};
        for(int i = n - 1;i >= 1; i--){
            int t = (k - 1) / factorials[i];
            k = (k - 1) % factorials[i] + 1;
            consquence = consquence + integers.get(t);
            integers.remove(t);
        }
        consquence = consquence + integers.get(0);
        return consquence;
    }

    public static void main(String[] args){
        LeetCode60 leetCode60 = new LeetCode60();
        for(int i = 1; i <= 24;i++)
            System.out.println(leetCode60.getPermutation(4,i));
    }

}
