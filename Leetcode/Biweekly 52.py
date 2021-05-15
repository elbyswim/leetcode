# def rotateRow(row):
#     row = ''.join(row)
#     sections = row.split('*')
#     new = list(map(lambda x: ''.join(sorted(list(x), reverse=True)), sections))
#     return list('*'.join(new))
#
#
# box = [["#", "#", "*", ".", "*", "."],
#        ["#", "#", "#", "*", ".", "."],
#        ["#", "#", "#", ".", "#", "."]]
#
# for row in box:
#     print(rotateRow(row))
#
# rotated = list(map(rotateRow, box))
#
# newBox = [[row[i] for row in reversed(rotated)] for i in range(len(box[0]))]
# print(newBox)


def sumOfFlooredPairs(nums):
    # nums = sorted(nums)
    # return sum(map(lambda i: sum(map(lambda x: (x // i), nums)), nums)) % (10 ** 9 + 7)
    nums = sorted(nums)
    ans = 0
    for i in nums:
        ans += len(list(filter(lambda x: x == i, nums)))
        ans += sum(list(map(lambda x: x // i, list(filter(lambda x: x > i, nums)))))
    return ans % (10 ** 9 + 7)


print(sumOfFlooredPairs(list(range(10 ** 5, 0, -1))))
print(sumOfFlooredPairs([7] * 7))
