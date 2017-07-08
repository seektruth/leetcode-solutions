import java.util.*;

/**
 * Created by smileMan on 2017/7/8.
 * 47题同样可解
 */

public class LeetCode46 {
    static class Solution {
        StringBuilder builder = new StringBuilder();
        LinkedList<Integer> integerList = new LinkedList<>();
        Set<List<Integer>> set = new HashSet<>();
        Set<String> visited = new HashSet<>();
        Set<Integer> inIndexs = new HashSet<>();
        int[] nums;

        public List<List<Integer>> permute(int[] nums) {
            this.nums = nums;
            for(int i = 0;i<nums.length;i++)
                forward(i);
            return new LinkedList<List<Integer>>(){{
                addAll(set);
            }};
        }

        private void forward(int i){
            String ns = nums[i] + " ";
            builder.append(ns);
            String s = builder.toString();
            visited.add(s);
            integerList.addLast(nums[i]);
            inIndexs.add(i);
            if(inIndexs.size() < nums.length) {
                for (int j = 0; j < nums.length; j++) {
                    if (!inIndexs.contains(j) && !visited.contains(s + nums[j] + " "))
                            forward(j);
                }
                builder.delete(builder.length() - ns.length(),builder.length());
                inIndexs.remove(i);
                integerList.removeLast();
            }
            else{
                List<Integer> nlist = new LinkedList<Integer>(){{
                    addAll(integerList);
                }};
                set.add(nlist);
                builder.delete(builder.length() - ns.length(),builder.length());
                inIndexs.remove(i);
                integerList.removeLast();
            }
        }
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int[] sample = {1,1,2};
        for(List<Integer> s: solution.permute(sample)){
            System.out.println(s);
        }
    }
}
