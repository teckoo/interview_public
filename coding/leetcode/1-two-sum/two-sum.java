/**
 Runtime: 2 ms, faster than 98.94% of Java online submissions for Two Sum.
 Memory Usage: 37.3 MB, less than 98.95% of Java online submissions for Two Sum.
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>(); 
        for (int i=0; i<nums.length; i++){
            int other = target - nums[i];
            if (map.containsKey(other)){
                return new int[]{map.get(other), i};
            } else {
                map.put(nums[i], i);
            }
        }
        return new int[]{ -1, -1};
    }
}
