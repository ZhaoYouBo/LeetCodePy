"""
Brief: Move Zeroes problem solution.
Author: ZhaoRongBo
Date: 2024-07-03
Version: 1.0
"""
from typing import List

class MoveZeroes:
    @staticmethod
    def move_zeroes(nums: List[int]) -> None:
        """
        Move all zeroes to the end of the list.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            None
        """
        zero_count = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums.extend([0] * zero_count)

def test():
    nums = [0, 1, 0, 3, 12]
    MoveZeroes.move_zeroes(nums)
    print(nums)

if __name__ == "__main__":
    test()