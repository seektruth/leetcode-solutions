import java.util.ArrayList;
import java.util.List;

/**
 * Created by smileMan on 2017/7/11.
 */

class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }

    @Override
    public String toString() {
        return start + "," + end;
    }
}

public class Leetcode56 {
    static class Solution {
        public List<Interval> merge(List<Interval> intervals) {
            ArrayList<Interval> merged = new ArrayList<>();
            while (intervals.size() > 0){
                Interval curr = intervals.get(0);
                intervals.remove(0);
                ArrayList<Interval> newMerged = new ArrayList<>();
                for(Interval interval : merged){
                    if(!(curr.end < interval.start || interval.end < curr.start)){
                        curr.start = Integer.min(interval.start,curr.start);
                        curr.end = Integer.max(interval.end, curr.end);
                    }
                    else{
                        newMerged.add(interval);
                    }
                }
                newMerged.add(curr);
                merged = newMerged;
            }
            return merged;
        }
    }

    public static void main(String[] args){
        List<Interval> intervals = new ArrayList<Interval>(){{
            add(new Interval(0,4));
            add(new Interval(2,5));
            add(new Interval(8,10));
            add(new Interval(15,18));
        }};
        Solution solution = new Solution();
        System.out.println(solution.merge(intervals));
    }
}
