def maxArea(height) -> int:
    max = 0
    n = len(height)
    for left in range(n - 1):
        for right in range(left, n):
            area = (right - left) * min(height[left], height[right])
            if area > max:
                max = area
    return max

print(maxArea([1,8,6,2,5,4,8,3,7]))