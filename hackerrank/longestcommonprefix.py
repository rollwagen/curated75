from typing import List
# from itertools import zip


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_length = len(strs)
        prefix_index = -1
        common_denom_max_index = min([len(s) for s in strs])
        for index_pos in range(common_denom_max_index):
            string_set = set()
            for string_index in range(strs_length):
                string_set.add(strs[string_index][index_pos])
            print(string_set)
            if len(string_set) == 1:
                prefix_index += 1
            else:
                break
        print(f'prefix_index = {prefix_index}')
        return strs[0][:prefix_index+1]


if __name__ == "__main__":

    # strs = ["flower", "flow", "flight"]  # output: "fl:
    # strs = ["dog", "racecar", "car"]  # output: ""
    strs = ["cir", "car"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
