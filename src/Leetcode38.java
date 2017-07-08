/**
 * Created by smileMan on 2017/7/8.
 */

public class Leetcode38 {
    static class Solution {
        public String countAndSay(int n) {
            if (n == 1)
                return "1";
            else {
                String pre = countAndSay(n - 1);
                char[] chars = pre.toCharArray();
                char p = '.';
                int count = 0;
                StringBuilder builder = new StringBuilder();
                for (char c : chars) {
                    if (c != p && count > 0) {
                        builder.append(count);
                        builder.append(p);
                        count = 0;
                    }
                    count += 1;
                    p = c;
                }
                if (count > 0) {
                    builder.append(count);
                    builder.append(p);
                }
                return builder.toString();
            }
        }
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        System.out.println(solution.countAndSay(5));
    }
}

