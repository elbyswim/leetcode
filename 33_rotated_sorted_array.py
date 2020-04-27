def search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while left < right:
        if nums[mid] == target:
            return mid
        elif nums[right] == target:
            return right
        elif nums[left] < nums[right]:
            break
        elif nums[left] < target < nums[mid]:
            right = mid - 1
            mid = (left + right) // 2
        elif nums[left] <= nums[mid]:
            left = mid + 1
            mid = (left + right) // 2
        elif nums[mid] < target < nums[right]:
            left = mid + 1
            mid = (left + right) // 2
        elif nums[mid] <= nums[right]:
            right = mid - 1
            mid = (left + right) // 2
    while left < right:
        if nums[mid] == target:
            return mid
        elif nums[right] == target:
            return right
        elif target < nums[mid]:
            right = mid - 1
            mid = (left + right) // 2
        elif nums[mid] < target:
            left = mid + 1
            mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    return -1


print(search([3, 5, 1], 3))
