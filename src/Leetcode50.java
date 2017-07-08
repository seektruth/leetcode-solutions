/**
 * Created by smileMan on 2017/7/8.
 */
public class Leetcode50 {
    static class Solution {
        public double myPow(double x, int n) {
            if(n==0)
                return 1;
            if(x==1)
                return 1;
            if(x==-1)
                return n % 2 == 0? 1: -1;
            if(n < 0) {
                x = 1 / x;
                n = Math.abs(n);
                if(n == Integer.MIN_VALUE)
                    n = Integer.MAX_VALUE;
            }
            double cons = x;
            int powered = 1;
            double p = x;
            int multiply = 1;
            while(powered < n){
                if(cons < 0.0000001 && -0.0000001 < cons && x > 0)
                    return 0;
                if(multiply + powered <= n){
                    cons *= p;
                    p *= p;
                    powered += multiply;
                    multiply *= 2;
                }
                else{
                    if(multiply > 2)
                        p = Math.sqrt(p);
                    else
                        p = x;
                    multiply = multiply/2;
                }
            }
            return cons;
        }
    }

    public static void main(String[] args){
        System.out.println(new Solution().myPow(2, Integer.MIN_VALUE));
    }
}
