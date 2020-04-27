# def subarraySum(nums, k):
#     sum = 0
#     memo = {}
#     for i in range(len(nums)):
#         sum += nums[i]
#         memo[sum] = memo.get(sum, []) + [i]
#     count = 0
#     for sum in memo:
#         if k + sum in memo:
#             for i in memo[sum]:
#                 for j in memo[k + sum]:
#                     count += 1 if i < j else 0
#     return count

def subarraySum(nums, k):
    sum = 0
    memo = {0: 1}
    count = 0
    for x in nums:
        sum += x
        count += memo.get(sum - k, 0)
        memo[sum] = memo.get(sum, 0) + 1
    return count


print(subarraySum([-1, -1, 1], 0))
