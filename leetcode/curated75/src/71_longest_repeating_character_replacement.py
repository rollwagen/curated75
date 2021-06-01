def lrcr(s, k):
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
