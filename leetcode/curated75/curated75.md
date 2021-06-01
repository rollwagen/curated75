# leetcode: curated75

Numbering as per [Leetcode: Blind Curated 75](https://leetcode.com/list/xoqag3yj/)

## (1) Two Sum [Array]

* hash map (dict) used for index lookup of diffrence (target-firstNumber)

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

* sliding window with left, right pointer (indeces) of current longest substr

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

* sliding window (sort of), dynamic programming

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

## (32) Valid Parlindrome [String]

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

## (41) Number of 1 bits [Binary]

> Write a function that takes an unsigned integer and returns the
> number of '1' bits it has (also known as the _Hamming weight_).

```python
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")
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

## (71) Longest Repeating Character Replacement [Sliding window, String]

> You are given a string s and an integer k. You can choose any character
> of the string and change it to any other uppercase English character.
> You can perform this operation at most k times. Return the length of the longest
> substring containing the same letter you can get after performing the above operations.

* sliding window

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

* "mininum intervals you need to remove" _same as_  "maximum set of non-overlapping"
* similar as maximise 'list of activities' problem (with start/end time):
  * sort the `activities` into ascending order by finishing time
  * choose any `activity` with the earliest finishing time.
  * remove from all `activities` that overlap S.

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
