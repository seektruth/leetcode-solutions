import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.regex.Pattern;

/**
 * Created by smileMan on 2017/7/10.
 */
public class Leetcode10 {
    static class Solution {
        ArrayList<String> ps = new ArrayList<>();
        String s;
        int curr = 0;

        boolean match(int i){
            loop: while (i < ps.size() && curr < s.length()){
                String pattern = ps.get(i);
                if(pattern.length() == 2){
                    char c = pattern.charAt(0);
                    int temp = curr;
                    while (!match(i + 1)){
                        if(curr < s.length() && (c=='.' || s.charAt(temp) == c)) {
                            temp = temp + 1;
                            curr = temp;
                        }
                        else{
                            break loop;
                        }
                    }
                    return true;
                }
                else{
                    char c = pattern.charAt(0);
                    if(c == '.' || c == s.charAt(curr)){
                        curr++;
                        i++;
                    }
                    else {
                        return false;
                    }
                }
            }
            while (i < ps.size() && ps.get(i).length() == 2)
                i++;
            return curr == s.length() && i == ps.size();
        }

        public boolean isMatch(String s, String p) {
            int i = 0;
            this.s = s;
            while (i < p.length()){
                if(i == p.length() - 1 || p.charAt(i + 1) != '*') {
                    ps.add(p.substring(i, i + 1));
                    i += 1;
                }
                else{
                    ps.add(p.substring(i, i + 2));
                    i += 2;
                }
            }
            return match(0);
        }
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        System.out.println(solution.isMatch("a", "ab*"));
    }
}
