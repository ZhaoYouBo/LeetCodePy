"""
Brief: Longest Consecutive Sequence problem solution.
Author: ZhaoRongBo
Date: 2024-07-01
Version: 1.0
"""

from typing import List

class LongestConsecutiveSequence:

    @staticmethod
    def longest_consecutive(nums: List[int]) -> int:
        """
        Description: Find the length of the longest consecutive sequence in a given list of numbers.
        Parameters:
            nums (List[int]): A list of integers.
        Returns:
            int: The length of the longest consecutive sequence.
        """
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

def test():
    nums = [100, 4, 200, 1, 3, 2]
    print(LongestConsecutiveSequence.longest_consecutive(nums))

if __name__ == "__main__":
    test()
