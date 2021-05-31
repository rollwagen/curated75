def max_subarray(nums):
    if len(nums) == 0:
        return 0

    max_subarr_sum = nums[0]
    curr_subarr_sum = nums[0]
    #  for right in range(1, len(nums)):
    for number in nums[1:]:
        if number > (curr_subarr_sum + number):
            curr_subarr_sum = number
        else:
            curr_subarr_sum += number
        max_subarr_sum = max(max_subarr_sum, curr_subarr_sum)

    return max_subarr_sum


if __name__ == "__main__":
    nums = [1]  # expected 1
    nums = [1, 2]  # expected 3
    nums = [5, 4, -1, 7, 8]  # expected 23
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # expected 6
    r = max_subarray(nums)
    print(r)
