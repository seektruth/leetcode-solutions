import java.util.ArrayList;
import java.util.HashSet;

public class LeetCode80 {
    public int removeDuplicates(int[] nums) {
        HashSet<Integer> table = new HashSet<>();
        HashSet<Integer> table2 = new HashSet<>();
        int p = 0;
        for(int c: nums){
            if(!table.contains(c)){
                table.add(c);
                nums[p++] = c;
            }
            else if(!table2.contains(c)){
                table2.add(c);
                nums[p++] = c;
            }
        }
        return p;
    }

    public static void main(String[] args){
        int[] nus = {1, 1, 1, 2, 2, 3};
        System.out.println(new LeetCode80().removeDuplicates(nus));
        for(int n : nus){
            System.out.print(n + " ");
        }
    }
}
