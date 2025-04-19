from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        answer = ""

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return answer
            else:
                answer += first[i]

        return answer

    print(longestCommonPrefix(0, ["dogs", "dog", "dogs"]))
