public class LeetCode75 {
    public void sortColors(int[] nums) {
        int i = 0;
        int j = nums.length - 1;
        int split_pos = Integer.MAX_VALUE;
        int split = 1;
        while (i <= j){
            if (nums[j] > split)
                j--;
            else if (nums[i] < split && i < split_pos)
                i++;
            else if(nums[i] > split){
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j--] = temp;
                }
            else if(nums[i] < split){
                    int temp = nums[i];
                    nums[i++] = nums[split_pos];
                    nums[split_pos++] = temp;
            }
            else if(nums[i] == split){
                    if(i < split_pos)
                        split_pos = i;
                    i++;
            }
        }
    }

    public static void main(String[] args){
        int[] nums = {2,2,2,0,0,0};
        new LeetCode75().sortColors(nums);
        for(int num : nums){
            System.out.print(num+" ");
        }
    }
}
