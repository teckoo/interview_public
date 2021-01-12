def backtrack(nums):
    if not nums: return []
    if len(nums) == 1: return [nums]
    result = []
    for i in range(len(nums)):
        new_candidates = nums[:i] + nums[i+1:]
        for path in backtrack(new_candidates):
            # print(f"i={i}, path={path}")
            result.append([nums[i]] + path)
        # no restoration
    print(f"input={nums}, result={result}")
    return result

assert backtrack([]) == [] 
assert backtrack([1]) == [[1]] 
assert backtrack([1, 2]) == [[1,2], [2, 1]]
assert len(backtrack([1, 2, 3])) == 6
