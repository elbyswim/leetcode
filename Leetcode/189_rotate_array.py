def rotate(nums, k):
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1

            if start == current:
                break
        start += 1


test = [1, 2, 3, 4, 5, 6, 7]
rotate(test, 3)
print(test)
