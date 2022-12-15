def twoSum(nums, target: int):
    for i in range(len(nums)):
        for x in range(i + 1, len(nums)):
            if (nums[i] + nums[x] == target):
                return [i, x]
    return -1

arr = [2,7,11,15]
target = 26
print(twoSum(arr, target))