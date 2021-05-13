class Solution:
    def minSumOfLengths(self, arr, target):
        target_arrays = []
        # other = []
        i = j = 0
        window = 0
        while i < len(arr):
            if window < target:
                if j == len(arr):
                    break
                window += arr[j]
                j += 1
            elif window == target:
                # other.append(arr[i:j])
                target_arrays.append(((i, j), j - i))
                # if len(target_arrays) < 2:
                #     target_arrays.append(((i, j), j - i))
                # elif j - i < max(target_arrays):
                #     target_arrays = [j - i, min(target_arrays)]

                window -= arr[i]
                i += 1
            else:
                window -= arr[i]
                i += 1
        # return sum(target_arrays) if len(target_arrays) == 2 else -1
        # print(other)
        # print(target_arrays)
        if len(target_arrays) < 2:
            return -1
        else:

            target_arrays.sort(key=lambda x: x[1])
            length = None
            i = 0
            j = 1
            print(target_arrays)
            while j < len(target_arrays):
                if target_arrays[j][0][0] >= target_arrays[i][0][1] or target_arrays[i][0][0] >= target_arrays[j][0][1]:
                    if length:
                        length = min(length, target_arrays[i][1] + target_arrays[j][1])
                    else:
                        length = target_arrays[i][1] + target_arrays[j][1]
                    i += 1
                else:
                    j += 1
            return length if length else -1

    def minDistance(self, houses, k):
        houses.sort()

        def part_wrapper(houses, k):
            ans = part(houses, k)
            while len(ans) < k:
                ans.sort(key=lambda x: len(x))
                new = ans.pop()
                ans.extend(part(new, k - len(ans)))
            return ans

        def part(houses, k):
            dist = (houses[-1] - houses[0]) / k
            ans = []
            base = houses[0]
            group = []
            for house in houses:
                if house <= base + dist:
                    group.append(house)
                else:
                    if len(group) > 0:
                        ans.append(group)
                    group = [house]
                    base = house
            if len(group) > 0:
                ans.append(group)
            return ans

        def single(houses):
            best = sum(houses)
            for i in range(houses[0], houses[-1] + 1):
                best = min(best, sum(map(lambda x: abs(i - x), houses)))
            return best

        groups = part_wrapper(houses, k)
        print(groups)
        ans = 0
        for group in groups:
            ans += single(group)

        return ans
        # return single(houses)


# tests = [
#     ([3, 2, 2, 4, 3], 3),
#     ([7, 3, 4, 7], 7),
#     ([4, 3, 2, 6, 2, 3, 4], 6),
#     ([5, 5, 4, 4, 5], 3),
#     ([3, 1, 1, 1, 5, 1, 2, 1], 3),
#     ([1, 6, 1], 7),
#     ([78, 18, 1, 94, 1, 1, 1, 29, 58, 3, 4, 1, 2, 56, 17, 19, 4, 1, 63, 2, 16, 11, 1, 1, 2, 1, 25, 62, 10, 69, 12, 7, 1,
#       6, 2, 92, 4, 1, 61, 7, 26, 1, 1, 1, 67, 26, 2, 2, 70, 25, 2, 68, 13, 4, 11, 1, 34, 14, 7, 37, 4, 1, 12, 51, 25, 2,
#       4, 3, 56, 21, 7, 8, 5, 93, 1, 1, 2, 55, 14, 25, 1, 1, 1, 89, 6, 1, 1, 24, 22, 50, 1, 28, 9, 51, 9, 88, 1, 7, 1,
#       30, 32, 18, 12, 3, 2, 18, 10, 4, 11, 43, 6, 5, 93, 2, 2, 68, 18, 11, 47, 33, 17, 27, 56, 13, 1, 2, 29, 1, 17, 1,
#       10, 15, 18, 3, 1, 86, 7, 4, 16, 45, 3, 29, 2, 1, 1, 31, 19, 18, 16, 12, 1, 56, 4, 35, 1, 1, 36, 59, 1, 1, 16, 58,
#       18, 4, 1, 43, 31, 15, 6, 1, 1, 6, 49, 27, 12, 1, 2, 80, 14, 2, 1, 21, 32, 18, 15, 11, 59, 10, 1, 14, 3, 3, 7, 15,
#       4, 55, 4, 1, 12, 4, 1, 1, 53, 37, 2, 5, 72, 3, 6, 10, 3, 3, 83, 8, 1, 5], 97)]

tests = [
    ([1], 1, 0),
    ([1, 2, 4, 5], 2, 2),
    ([1, 4, 8, 10, 20], 3, 5),
    ([2, 3, 5, 12, 18], 2, 9),
    ([7, 4, 6, 1], 1, 8),
    ([3, 6, 14, 10], 4, 0),
    ([19, 28, 10, 30, 11, 6, 5, 17], 4, 6),
    ([8, 14, 20, 23, 4, 25], 3, 9)
]

soln = Solution()
# for i, test in enumerate(tests):
#     assert soln.minDistance(test[0], test[1]) == test[2], test
print(soln.minDistance([8, 14, 20, 23, 4, 25], 3))
