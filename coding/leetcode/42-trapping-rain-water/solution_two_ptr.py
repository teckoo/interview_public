def trap(height):  # height: int[]
    if not height: return 0
    left, right = 0, len(height) - 1
    res = 0
    l_max, r_max = height[0], height[right]
    
    while left <= right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        
        if l_max < r_max:
            res += l_max - height[left]
            left += 1 
        else: 
            res += r_max - height[right]
            right -= 1
    return res