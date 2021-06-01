def missing_number(nums):
    length = len(nums)
    nums.sort()
    for i in range(0, length + 1):
        try:
            if i != nums[i]:
                return i
        except IndexError:
            return i


def missing_number2(nums):
    nums_length = len(nums)
    sum_of_range = int(nums_length * (nums_length+1) / 2)
    sum_of_nums = sum(nums)
    return sum_of_range - sum_of_nums


nums = [0, 1]  # output: 2
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # output: 8
print(missing_number2(nums))
