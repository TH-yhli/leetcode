'''
给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度为 1000。
'''
s = "babad"

#采用了向字符串两端延伸的思想
class Solution():
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0:
            return ""
        res = s[0]
        def extend(i, j, s):
            while(i>=0 and j<len(s) and s[i]==s[j]):
                i -= 1
                j += 1
            return s[i+1:j]
        for i in range(n-1):
            r1 = extend(i,i,s)
            r2 = extend(i,i+1,s)
            if max(len(r1), len(r2)) > len(res):
                res = r1 if len(r1)>len(r2) else r2
        return res

a = Solution()
print(a.longestPalindrome(s))

