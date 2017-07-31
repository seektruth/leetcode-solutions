import java.util.HashMap;

public class LeetCode70 {
    int[] cache;

    public int climbStairs(int n) {
        cache = new int[n + 1];
        cache[0] = 1;
        cache[1] = 2;
        for(int i = 2; i <= n; i++){
            cache[i] = cache[i - 1] + cache[i - 2];
        }
        return cache[n - 1];
    }

    public static void main(String[] args){
        System.out.println(new LeetCode70().climbStairs(3));
    }
}
