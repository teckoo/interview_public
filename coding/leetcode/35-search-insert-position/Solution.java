import java.util.*;


class Solution {
    public int searchInsert(int[] nums, int target) {
        // since the array is sorted, choose binary/divide and conqur
        if (nums.length == 0) return 0;
        if (nums.length == 1){
            return nums[0] < target? 1 : 0;
        }
        int middle = nums.length/2;
        if (nums[middle] == target) return middle;
        else if (target < nums[middle]) return searchInsert(Arrays.copyOfRange(nums, 0, middle), target);
        else return middle + searchInsert(Arrays.copyOfRange(nums, middle, nums.length), target);
    }

    public static void main(String[] args){
        int[] nums = {1, 3, 5, 6};
        int target = 2;

        Solution s = new Solution();
        int result = s.searchInsert(nums, target);
        assert result == 1;
    }
}
