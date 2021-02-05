def trap(height): 
    if not height: return 0
    n = len(height)
    res = 0
    # 数组充当备忘录
    l_max, r_max = [0] * n, [0] * n
    # 初始化 base case
    l_max[0] = height[0]
    r_max[n - 1] = height[n - 1]
    # 从左向右计算 l_max
    for i in range(1, n, 1):
        l_max[i] = max(height[i], l_max[i - 1])
    # 从右向左计算 r_max
    for i in range(n - 2, -1, -1):
        r_max[i] = max(height[i], r_max[i + 1])
    # 计算答案
    for i in range(1, n):
        res += min(l_max[i], r_max[i]) - height[i]
    return res
