def twoSum(nums, target):
    seen = {}
    n = len(nums)
    for x in range(n):
        d = target - nums[x]
        if d in seen:
            return [seen[d], x]
        else:
            seen[nums[x]] = x
    return False


test1 = [1, 2, 3, 5]
test2 = [1, 1, 1]

print(twoSum(test1, 3))
print(twoSum(test1, 4))
print(twoSum(test1, 5))
print(twoSum(test1, 6))
print(twoSum(test1, 7))
print(twoSum(test1, 8))
print(twoSum(test1, 2))
