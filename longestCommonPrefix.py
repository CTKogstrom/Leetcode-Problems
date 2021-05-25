'''
Given a list of strings find the longest common prefix among them.
Ex. ['florida', 'flower', 'flint'] - 'fl'
'''


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Running accumulation of the longest prefix in the list
        prefix = ''

        # This acts as a counter for the index of the strings within the list
        i = 0

        # This loop runs as many times as there are letters in a common prefix
        while True:
            try:
                # Take the ith letter from each word and count the number of unique
                letters = len(set([s[i] for s in strs]))
            except:
                # Index out of bounds errors occur because an entire word is the prefix so the loop continues passed the
                # length of that word
                break
            else:
                if letters > 1:
                    # if there are more than 1 unique letter then the prefix has ended
                    break
                else:
                    # if there is only one unique letter than the prefix continues
                    prefix = prefix + strs[0][i]

                i += 1

        return prefix