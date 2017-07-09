import java.util.Arrays;

/**
 * Created by smileMan on 2017/7/9.
 */
public class Leetcode53 {
    static class Solution {
        public int maxSubArray(int[] nums) {
            int max = Integer.MIN_VALUE;
            int[] maxUphere = new int[nums.length + 1];
            maxUphere[0] = Integer.MIN_VALUE ;
            System.arraycopy(nums,0,maxUphere,1,nums.length);
            for(int i = 0; i<nums.length;i++){
                maxUphere[i + 1] = maxUphere[i] < 0? maxUphere[i + 1]: maxUphere[i] + nums[i];
                max = Integer.max(max,maxUphere[i + 1]);
            }
            return max;
        }
    }

    public static void main(String[] args){
        Solution solution =new Solution();
        int[] sample = {1,-2,3,-3,4};
        System.out.println(solution.maxSubArray(sample));
    }

}
