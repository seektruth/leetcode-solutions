import java.util.LinkedList;
import java.util.List;
import java.util.stream.StreamSupport;

public class LeetCode78 {
    int n;
    int[] nums;
    LinkedList<List<Integer>> consequence = new LinkedList<List<Integer>>(){{add(new LinkedList<>());}};

    public void dfs(LinkedList<Integer> l, int t){
        l.addLast(nums[t]);
        consequence.addLast(new LinkedList<Integer>(){{addAll(l);}});
        for(int i = t + 1; i < n;i++)
            dfs(l,i);
        l.removeLast();
    }

    public List<List<Integer>> subsets(int[] nums) {
        this.n = nums.length;
        this.nums = nums;
        LinkedList<Integer> init = new LinkedList<>();
        for(int i = 0; i < n; i++){
            dfs(init, i);
        }
        return consequence;
    }

    public static void main(String[] args){
        for(List l: new LeetCode78().subsets(new int[]{})){
            System.out.println(l);
        }
    }
}
