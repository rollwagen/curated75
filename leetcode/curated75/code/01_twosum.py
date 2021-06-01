#
# hashmap index lookup of difference
#
def twosum1(nums, target):
    lookup_dict = {n: i for i, n in enumerate(nums)}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in lookup_dict:
            if i != lookup_dict.get(difference):
                return [i, lookup_dict.get(difference)]


if __name__ == "__main__":

    nums = [3, 2, 4]
    target = 6

    r = twosum1(nums, target)
    print(f'twosum1: {r} (expected: [1,2])')
