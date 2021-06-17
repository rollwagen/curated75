
n = 43261596  # 964176192
n = 4294967293  # 3221225471
print(f'n: {bin(n)[2:].zfill(32)}\n')
ret, power = 0, 31
# print(bin(ret)[2:])
while n:
    # print(f'n: {bin(n)[2:].zfill(32)}')
    # ret += (n & 1) << power
    ret |= ((n & 1) << power)
    # print(f'r: {bin(ret)[2:]}\n')
    n = n >> 1
    power -= 1
print(ret)


n = 4294967293  # 3221225471
result = 0
number_of_bits = 32
for b in reversed(range(number_of_bits)):  # righmost excl ie. reversed 0..31
    # get rightmost bit, and reverse index position
    # bit at index 0, becomes new index 31 i.e. shift left by 'b' positions
    result |= (n & 1) << b
    # move orinigal number one to the right
    # i.e. just processed bit 'falls off'
    n >>= 1
print(result)

