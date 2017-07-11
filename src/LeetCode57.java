import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by smileMan on 2017/7/11.
 */
public class LeetCode57 {
    static class Solution {
        public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
            List<Interval> merged = new LinkedList<>();
            boolean added = false;
            for(Interval interval : intervals){
                if(newInterval.start > interval.end){
                    merged.add(interval);
                }
                else if(!(newInterval.end < interval.start)){
                    newInterval.start = Integer.min(interval.start,newInterval.start);
                    newInterval.end = Integer.max(interval.end, newInterval.end);
                }
                else{
                    if(!added)
                        merged.add(newInterval);
                    merged.add(interval);
                    added = true;
                }
            }
            if(!added)
                merged.add(newInterval);
            return merged;
        }
    }

    public static void main(String[] args){
        List<Interval> intervals = new ArrayList<Interval>(){{
            //add(new Interval(1,2));
            add(new Interval(2,5));
            add(new Interval(6,7));
            add(new Interval(8,9));
            //add(new Interval(12,16));
        }};
        Solution solution = new Solution();
        System.out.println(solution.insert(intervals,new Interval(0,1)));
    }
}
