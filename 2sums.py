from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans1 = 0
        ans2 = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                j += i
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    ans1 = i
                    ans2 = j

        return [ans1, ans2]

    print(twoSum(0, [2, 7, 11, 15], 9))
