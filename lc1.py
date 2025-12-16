def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return[i, j]


numbers = [2,7,11,15]
target_number = 9

output = two_sum(numbers, target_number)

print(output)
