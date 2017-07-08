import java.util.*;

/**
 * Created by smileMan on 2017/7/8.
 */
public class LeetCode49 {
    static class Solution {
        public List<List<String>> groupAnagrams(String[] strs) {
            Map<String, List<String>> map = new HashMap<>();
            for(String str: strs){
                char[] chars = str.toCharArray();
                Arrays.sort(chars);
                String sorted = String.valueOf(chars);
                if(map.containsKey(sorted)){
                    map.get(sorted).add(str);
                }
                else{
                    map.put(sorted, new LinkedList<String>(){{add(str);}});
                }
            }
            return new LinkedList<List<String>>(){{addAll(map.values());}};
        }
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> lists = solution.groupAnagrams(strs);
        for(List<String> list : lists){
            System.out.println(list);
        }
    }
}
