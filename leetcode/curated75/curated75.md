# leetcode: curated75

Numbering as per [Leetcode: Blind Curated 75](https://leetcode.com/list/xoqag3yj/)

## (1) Two Sum [Array]

- hash map (dict) used for index lookup of diffrence (target-firstNumber)

```python
  def twosum1(nums, target):
      lookup_dict = {n: i for i, n in enumerate(nums)}
      for i, num in enumerate(nums):
          difference = target - num
          if difference in lookup_dict:
              if i != lookup_dict.get(difference):  # looked up yourself?
                  return [i, lookup_dict.get(difference)]
  ```

## (2) Longest Substring Without Repeating Characters [String]

- sliding window with left, right pointer (indeces) of current longest substr

```python
  def longest_substring(s):
      if not len(s):
          return 0
      left = 0
      right = 0
  
      curr_substr = set(s[0])
      max_length = 1
  
      for i in range(1, len(s)):
          right = i
          right_char = s[right]
          if right_char not in curr_substr:
              curr_substr.add(right_char)
              max_length = max(max_length, len(curr_substr))
          else:
              while c := s[left]:  # delete all chars occuring left of found duplicate
                  curr_substr.remove(c)
                  left += 1
                  if c == right_char:
                      break
              curr_substr.add(right_char)
  
      return max_length
  ```

## (14) Maximum Subarray [Array, DP]

- sliding window (sort of), dynamic programming

```python
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
```

## (20) Climbing Stairs [Dynamic Programming]

> You are climbing a staircase. It takes n steps to reach the top.
> Each time you can either climb 1 or 2 steps. In how many distinct
> ways can you climb to the top?

Framework for Solving DP Problems:

1. Define the objective function
2. Identify base cases
3. Write down a recurrence relation for the optimized objective function e.g `f(n) = f(n-1) + f(n-2)`
4. What's the order of execution?  e.g.bottom-up
5. Where to look for the answer? e.g. f(n)

```python
        if n == 1: return 1
        if n == 2: return 2
        dp: List = [None]  * (n + 1)
        dp[0] = 1  # also just one distinct way to get here
        dp[1] = 1
        dp[2] = 2  #  = dp[1] + dp[0]
        dp[3] = 3  #  = dp[2] + dp[1]
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```

## (30) Best Time to Buy and Sell Stock [Array, DP]

> `prices[i]` is the price of a given stock on the ith day.
> You want to maximize your profit by choosing a single day to buy
> one stock and choosing a different day in the future to sell that stock.

- Complexity:
  - Time- _O(n)_ only a single pass is needed
  - Space _O(1)_ two variables

```python
# e.g. prices = [7, 1, 5, 3, 6, 4]  # result: 5

  # Solution 1
  max_profit, buy = 0, sys.maxsize
  
  for _, sell in enumerate(prices):
      if sell < buy:
          buy = sell
      else:
          profit = sell - buy
          max_profit = max(max_profit, profit)
  return(max_profit)
  
  # Solution 2
  min_price = prices[0]
  max_profit = 0
  for i in range(1, len(prices)):
      if prices[i] < min_price:
          min_price = prices[i]
      profit = prices[i] - min_price
      max_profit = max(profit, max_profit)
  return max_profit
```

## (32) Valid Palindrome [String]

```python
    s = "A man, a plan, a canal: Panama"
    # normalize str e.g. to "amanaplanacanalpanama"
    p = str()
    for c in s:
        if c.isalnum():
            p += c.lower()

    length = len(p)

    if length in [0, 1]:
        return True

    for i in range(length):
        left = i
        right = (length - 1) - i
        if not left <= right:
            return True
        if p[left] != p[right]:
            return False
```

## (40) Reverse Bits [Binary]

> Reverse bits of a given 32 bits unsigned integer.

```python
        # n = 43261596  # result: 964176192
        result = 0
        number_of_bits = 32
        for b in reversed(range(number_of_bits)):  # righmost excl ie. reversed 0..31
            # get rightmost bit, and reverse index position
            # bit at index 0, becomes new index 31 i.e. shift left by 'b' positions
            result |= (n & 1) << b
            # move orinigal number one to the right
            # i.e. just processed bit 'falls off'
            n >>= 1
        return result

        # alternative leveraging python bin/str functions
        reversed_binary = ''.join(reversed(bin(n)[2:].zfill(32)))
        return int(reversed_binary, 2)
```

## (41) Number of 1 bits [Binary]

> Write a function that takes an unsigned integer and returns the
> number of '1' bits it has (also known as the _Hamming weight_).

```python
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")
```

## (42) House Robber [Dynamic Programming]

> the only constraint stopping you from robbing each of them is that adjacent houses have
> security systems connected and it will automatically contact the police if two adjacent
> houses were broken into on the same night.
> Given an integer array nums representing the amount of money of each house, return the maximum
> amount of money you can rob tonight without alerting the police.

```python
        # example: nums = [1,2,3,1]    output: 4
        # index=0   nums[0]
        # index=1   max( nums[0], nums[1])
        # index=2   max(r[i-2] + nums[i] or r[1])
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
            
        dp = [None]*len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(dp[0]+nums[2], dp[1])

        for i in range(3, len(nums)):
            max_rob_so_far = max(dp[i-2]+nums[i], dp[i-1])
            dp[i] = max_rob_so_far
        
        return max(dp) # max not necessary (is in last element)

        #
        # ...same but slightly different formatting/code:
        #
        length = len(nums)
        if not length:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])

        dp = [0 for i in range(length)]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max( nums[i]+dp[i-2], dp[i-1])

        return dp[length-1]
```

## (50) Contains Duplicate [Array]

> Given an integer array nums, return true if any value appears
> at least twice in the array, and return false if every element is distinct.

```python
    # solutions using 'Set'
    return len(nums) > len(set(nums))

    # solution iterating through sorted list
      nums.sort()
      for i in range(len(nums)-1):
          if nums[i]==nums[i+1]:
              return True
      return False
```

## (55) Valid Anagram [String]

> Given two strings s and t, return true
> if t is an anagram of s, and false otherwise.

```python
        # s = "anagram", t = "nagaram" 
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)
        diff = s_counter - t_counter
        return not diff
```

## (56) Missing Number [Array]

> Given an array nums containing n distinct numbers in the range [0, n],
> return the only number in the range that is missing from the array.

```python
    # solution with requiring sorting
    length = len(nums)
    nums.sort()
    for i in range(0, length + 1):
        try:
            if i != nums[i]:
                return i
        except IndexError:
            return i

    # solution using sum 'trick'
    nums_length = len(nums)
    sum_of_range = int(nums_length * (nums_length+1) / 2)
    sum_of_nums = sum(nums)
    return sum_of_range - sum_of_nums
```

## (69) Sum of Two Integers

```python
    for i in range(32):
        # (1) if bin representations are completely opposite, XOR operation will directly
        # produce sum of numbers ( in this case carry is 0 )
        xor_sum = a ^ b

        # (2) if numbers bin representation is not completely opposite,
        # XOR will only have part of the sum and remaining will be carry;
        # carry-over can be produced by AND operation followed by left shift operation.
        # e.g. 10, 11 => 1010, 1011 => (a&b)<<1 => 10100
        carry = (a & b) << 1

        # (3) now find sum of (1) and (2) i.e a is replace 'a' with XOR result
        # and 'b' is replaced wth carry result
        a = xor_sum
        b = carry
    # enforce 32bit length in case of overflow
    if b > 0:
        return a & 0b11111111111111111111111111111111
    else:
        return a
```

## (71) Longest Repeating Character Replacement [Sliding window, String]

> You are given a string s and an integer k. You can choose any character
> of the string and change it to any other uppercase English character.
> You can perform this operation at most k times. Return the length of the longest
> substring containing the same letter you can get after performing the above operations.

- sliding window

```python
    max_substring_length = 0
    letter_count = {}

    left = 0
    for right in range(len(s)):
        letter = s[right]
        letter_count[letter] = letter_count.get(letter, 0) + 1
        substr_length = right - left + 1
        most_frequent_letter = max(letter_count.values())
        if substr_length - most_frequent_letter > k:
            current_left_letter = s[left]
            letter_count[current_left_letter] -= 1
            left += 1
            substr_length = right - left + 1

        max_substring_length = max(max_substring_length, substr_length)

    return max_substring_length
```

## (72) Non-overlapping Intervals [Interval]

> Given an array of intervals intervals where intervals[i] = [start\_i, end\_i], return
> the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

- "mininum intervals you need to remove" _same as_  "maximum set of non-overlapping"
- similar as maximise 'list of activities' problem (with start/end time):
  - sort the `activities` into ascending order by finishing time
  - choose any `activity` with the earliest finishing time.
  - remove from all `activities` that overlap S.

```python
    # e.g. intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals.sort(key=lambda i: i[1])
    skipped_list = []
    curr_end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval_start = intervals[i][0]
        if (interval_start < curr_end): # check if overlap
            skipped_list.append(i)
        elif interval_start >= curr_end:
            curr_end = intervals[i][1]

    return len(skipped_list)
```
