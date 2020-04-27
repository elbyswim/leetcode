def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j = 0, 0
    while i + j < m + n:
        if nums1[i] > nums2[j]:
            nums1.pop()
            nums1.insert(i, nums2[j])
            j += 1
        if i == j + m:
            nums1 = nums1[:i] + nums2[j:]
            break
        i += 1


nums1 = [1,2,7,0,0,0]
nums2 = [2,5,6]


merge(nums1, 3, nums2, 3)
print(nums1)
