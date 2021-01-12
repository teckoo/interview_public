public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> num_idx = new Dictionary<int, int>();
        for (int i=0; i<nums.Length; i++)
        {
            int match_part = target - nums[i];
            if (num_idx.ContainsKey(match_part))
            {
                return new int[] {num_idx[match_part], i};
            }
            num_idx.TryAdd(nums[i], i);
        }
        return new int[]{-1, -1};
    }
}
