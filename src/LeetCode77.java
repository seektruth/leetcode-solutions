import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LeetCode77 {
    int n,k;
    LinkedList<List<Integer>> consequence = new LinkedList<>();

    public static void main(String[] args) {
        for(List<Integer> t: new LeetCode77().combine2(20,16)){
            System.out.println(t);
        }
    }

    public void dfs(LinkedList<Integer> l, int t){
        l.addLast(t);
        if (l.size() == k)
            consequence.addLast(new LinkedList<Integer>(){{addAll(l);}});
        else{
            for(int i = t + 1; i <= n - k + l.size() + 1;i++)
                dfs(l,i);
        }
        l.removeLast();
    }

    public List<List<Integer>> combine2(int n, int k) {
        this.n = n;
        this.k = k;
        LinkedList<Integer> init = new LinkedList<>();
        for(int i = 1; i <= n - k + 1; i++){
            dfs(init, i);
        }
        return consequence;
    }

    public List<List<Integer>> combine(int n, int k) {
        LinkedList<LinkedList<Integer>> Q = new LinkedList<LinkedList<Integer>>() {{
            add(new LinkedList<>());
        }};

        while (!Q.isEmpty()) {
            LinkedList<Integer> l = Q.removeFirst();
            int last = l.isEmpty() ? 0 : l.getLast();
            for (int i = last + 1; i <= n - k + l.size() + 1; i++) {
                LinkedList<Integer> newList = (LinkedList<Integer>) l.clone();
                newList.add(i);
                if (newList.size() < k)
                    Q.addLast(newList);
                else
                    consequence.addLast(newList);
            }
        }
        return consequence;
    }
}
