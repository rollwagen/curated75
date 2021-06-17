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
            while c := s[left]:
                curr_substr.remove(c)
                left += 1
                if c == right_char:
                    break
            curr_substr.add(right_char)

    return max_length


if __name__ == "__main__":
    s = "pwwkew"  # expected: 3
    solution = 3
    s = "bbbbb"  # expected: 1
    solution = 1

    r = longest_substring(s)
    print(f's={s}  r: {r}  expected: {solution}')
