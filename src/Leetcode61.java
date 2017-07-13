import java.util.ArrayList;

/**
 * Created by smileMan on 2017/7/13.
 */
public class Leetcode61 {

    static class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }

        @Override
        public String toString() {
            return val + " " + next;
        }
    }

    public ListNode rotateRight(ListNode head, int k) {
        ArrayList<ListNode> nodes = new ArrayList<ListNode>(){{
           ListNode curr = head;
           while (curr != null){
               add(curr);
               curr = curr.next;
           }
        }};
        if(nodes.size() == 0 || (k % nodes.size())== 0)
            return head;
        k = k % nodes.size();
        ListNode start = nodes.get(nodes.size() - k);
        ListNode preEnd = nodes.size() - k - 1 >= 0? nodes.get(nodes.size() - k - 1): null;
        ListNode end = nodes.get(nodes.size() - 1);
        end.next = head;
        if(preEnd != null)
            preEnd.next = null;
        return start;
    }

    public static void main(String[] args){
        Leetcode61 leetcode61 = new Leetcode61();
        for(int i = 0; i< 10;i++) {
            ListNode a = new ListNode(1);
            a.next = new ListNode(2);
            a.next.next = new ListNode(3);
            System.out.println(leetcode61.rotateRight(a, i));
        }
    }
}
