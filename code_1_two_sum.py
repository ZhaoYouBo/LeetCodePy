"""
Brief: Two Sum problem solution.
Author: ZhaoRongBo
Date: 2024-06-26
Version: 1.0
"""

from typing import List

class TwoSum:
    """
    Solution class for TwoSum problem.
    """

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """
        Find two elements in `nums` that sum up to `target`, and return their indices.

        Parameters:
            nums (List[int]): Input list of integers.
            target (int): Target sum.

        Returns:
            List[int]: A list containing the indices of the two elements.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Avoid using same element twice
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return first valid pair found
        return []  # Return empty list if no solution found


if __name__ == "__main__":
    # Test case: [2,7,11,15], target = 9
    two_sum = TwoSum()
    print(two_sum.two_sum([2, 7, 11, 15], 9))  # Expected output: [0, 1]