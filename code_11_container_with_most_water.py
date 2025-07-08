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
        Calculate the maximum amount of the water that can be held by the container

        Parameters:
            height (List[int]): The height of each pillar

        Returns:
            int: The maximum amount of water

        """
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(len(height) - 1, -1, -1):
                length = abs(j - i)
                width = height[j] if height[i] > height[j] else height[i]
                if length * width > max_area: max_area = length * width
                if i >= j: break

        return max_area

    @staticmethod
    def max_area_two_pointers(height: List[int]) -> int:
        """
        Calculate the maximum amount of the water that can be held by the container

        Parameters:
            height (List[int]): The height of each pillar

        Returns:
            int: The maximum amount of water

        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

def test():
    print(Solution.max_area_two_pointers([1, 1]))

if __name__ == "__main__":
    test()