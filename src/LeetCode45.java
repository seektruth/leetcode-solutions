import java.lang.reflect.Array;
import java.util.Arrays;

/**
 * Created by smileMan on 2017/7/8.
 */

public class LeetCode45 {
    static class Solution {
        public int jump(int[] nums) {
            int pre = -1;
            int curr = 0;
            int step =0;
            while(curr != nums.length - 1){
                int end =0;
                for(int i = pre + 1;i < curr +1; i++){
                    if(i + nums[i] > end)
                        end = i + nums[i];
                }
                curr = end < nums.length? end : nums.length - 1;
                step = step + 1;
            }
            return step;
        }
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int[] a = {2,3,1,1,4};
        System.out.println(solution.jump(a));
    }
}
