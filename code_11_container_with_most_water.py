"""
Brief: LeetCode Container With Most Water problem solution.
Author: ZhaoRongBo
Date: 2024-07-07
"""

from typing import List

class Solution:
    @staticmethod
    def max_area(height: List[int]) -> int:
        """


        Parameters:
            height (List[int]):

        Returns:
            int:

        """
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(len(height) - 1, -1, -1):
                length = abs(j - i)
                width = height[j] if height[i] > height[j] else height[i]
                if length * width > max_area: max_area = length * width
                if i >= j: break

        return max_area

def test():
    print(Solution.max_area([1, 1]))

if __name__ == "__main__":
    test()