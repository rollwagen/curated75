def is_palindrom(s):

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
