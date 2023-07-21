class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or "" in strs:
            return ""
        a=min(len(s) for s in strs)
        new_strs=""
        for i in range(a): #0
            current= strs[0][i] #str[0][0] #f
            for string in strs:
               if len(string) <= i or string[i] != current:
                    return new_strs
            new_strs+=current
        return new_strs
