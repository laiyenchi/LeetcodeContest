"""
Problem:
Find Resultant Array After Removing Anagrams
https://leetcode.com/contest/weekly-contest-293/problems/find-resultant-array-after-removing-anagrams/
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
"""



from copy import copy
from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        pre_word = ""
        remove_words = []
        for w in words:
            sorted_w = "".join(sorted(w))

            if sorted_w == pre_word:
                remove_words.append(w)
                
            pre_word = sorted_w
        
        for w in remove_words:
            words.remove(w)
        
        return words


class Solution2:
    """
    using Counter, but Runtime is slower (225ms)
    """
    def removeAnagrams(self, words: List[str]) -> List[str]:
        copied_words = copy(words)
        for i in range(1, len(words)):
            if Counter(words[i-1]) == Counter(words[i]):
                copied_words.remove(words[i])
                print(copied_words)
        return copied_words

# words = ["abba","baba","bbaa","cd","cd"]
# words = ["a","b","c","d","e"]
words = ["yjonq","yqnoj","oyqjn","nqoyj","onjqy","joqyn","qynjo","jynoq"]
# words = ["a","b","a"]
print(Solution().removeAnagrams(words))
print(Solution2().removeAnagrams(words))
