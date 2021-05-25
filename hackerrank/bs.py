#!/bin/python3


if __name__ == '__main__':
    n = 3  # int(input().strip())

    a = [3, 2, 1]  # list(map(int, input().rstrip().split()))

    # Write your code here
    num_of_swaps = 0
    swaps_in_current_round = 0
    while True:
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                tmp = a[i+1]
                a[i+1] = a[i]
                a[i] = tmp
                swaps_in_current_round += 1

        num_of_swaps += swaps_in_current_round
        if swaps_in_current_round == 0:
            break
        else:
            swaps_in_current_round = 0

    print(f'Array is sorted in {num_of_swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1:][0]}')
