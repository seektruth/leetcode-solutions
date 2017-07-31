

public class LeetCode76 {
        public String minWindow(String s, String t) {
            int[] map = new int[128];
            for(char c: t.toCharArray()){
                map[(int)c]++;
            }
            int begin = 0,end = 0,counter = t.length(),d = Integer.MAX_VALUE, head = 0;
            while (end < s.length()){
                if(map[(int)s.charAt(end++)]-- > 0) counter--;
                while (counter == 0){
                    if(end - begin < d){
                        head = begin;
                        d = end - begin;
                    }
                    if(map[(int)s.charAt(begin++)] ++ == 0){
                        counter++;
                    }
                }
            }
            return d == Integer.MAX_VALUE? "" : s.substring(head, head + d);
        }

    public static void main(String[] args){
        System.out.println(new LeetCode76().minWindow("ADOBECODEBANC","ABC"));
    }
}
