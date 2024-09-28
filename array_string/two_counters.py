'''
   Source: Leetcode - Prob 1768: Merge Strings Alternately
   Description: Merge two strings, word1 and word2, by adding ltters in alternating order, 
                starting with word1. If a string is longer than the other, append additional letters
   Output: Merged string
   Techniques Used: Two counters for each word, accessing characters of a string, joining of list
   Lessons Learned: Don't need to make a new copy of modified string every time, can just access the
                    characters and use it 
   Author: Jackie Chan
   Known Bugs: None
   Date: 09/28/2024
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        i, j = 0, 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2): 
                result += word2[j]
                j += 1
    
        return result