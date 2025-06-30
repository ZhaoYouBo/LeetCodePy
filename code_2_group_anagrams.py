"""
Brief: Group Anagrams problem solution.
Author: ZhaoRongBo
Date: 2024-06-30
Version: 1.0
"""
from typing import List


class GroupAnagrams:
    """
    Solution class for Group Anagrams problem.
    """
    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together.

        Args:
            strs (List[str]): List of strings.

        Returns:
            List[List[str]]: List of lists of anagrams.
        """
        dictionary = {}
        if not strs:
            return []
        for word in strs:
            # Generate normalized key by sorting characters
            sorted_word = "".join(sorted(word))
            if sorted_word in dictionary:
                dictionary[sorted_word].append(word)
            else:
                dictionary[sorted_word] = [word]
        return list(dictionary.values())

def main():
    group_anagrams = GroupAnagrams()
    print(group_anagrams.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

if __name__ == "__main__":
    main()