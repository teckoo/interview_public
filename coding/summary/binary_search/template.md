# Binary search template

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

```python
def binarySearch(nums, target):
    left = 0, right = len(nums) - 1
    while(left <= right):
        int mid = left + (right - left) / 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else  # check meet_condition():
            # return mid
            # right = mid -1  # search left boundary
            # left = mid + 1  # search right boundary
    # need to check boundary
    if left >= len(nums) || nums[left] != target:
    # or
    if right < 0 || nums[right] != target:
        return -1
    return left or right
```

Notes:

1. search **ONE item**, use `[left, right]`
2. search **a range**, use `[left, right)`
