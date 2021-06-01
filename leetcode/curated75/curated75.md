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
