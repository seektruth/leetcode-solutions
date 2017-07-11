/**
 * Created by smileMan on 2017/7/10.
 */
public class Leetcode55 {
    static class Solution {
        public boolean canJump(int[] nums) {
            int nextNotReach = 1;
            int curr = 0;
            while (curr < Integer.min(nextNotReach, nums.length) ){
                nextNotReach = Integer.max(nextNotReach,nums[curr] + curr + 1);
                if(nextNotReach >= nums.length)
                    break;
                curr++;
            }
            return nextNotReach >= nums.length;
        }
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        System.out.println(solution.canJump(new int[]{3,2,1,0,4}));
    }
}
