'''
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
'''
s = "abcabcbb"

#暴力遍历方法
class Solution1:
    def lengthOfLongestSubstring(self, s):
        count = max_count = (1 if len(s) else 0) #注意程序需满足空字符串输入
        mark = 0
        while count+mark < len(s):
            if s[mark+count] in s[mark:mark+count]:
                mark += 1
                count -= 1
            else:
                count += 1
            max_count = max(max_count, count)
        return max_count

#改进：通过标记重复字符的位置跳过不必要的遍历
class Solution2:
    def lengthOfLongestSubstring(self, s):
        count = max_count = (1 if len(s) else 0) #注意程序需满足空字符串输入
        mark = 0
        while count+mark < len(s):
            if s[mark+count] in s[mark:mark+count]:
                temp = mark
                mark += s[mark:mark+count].index(s[mark+count])+1
                count -= s[temp:temp+count].index(s[temp+count])
            else:
                count += 1
            max_count = max(max_count, count)
        return max_count

#官方方法，利用set集合来判断是否有重复的字符，性能低于Solution2
class Solution3:
    def lengthOfLongestSubstring(self, s):
        hashset = set()
        rk, ans = -1, 0
        for i in range(len(s)):
            if i!=0:
                hashset.remove(s[i-1])
            while rk+1 < len(s) and s[rk+1] not in hashset:
                hashset.add(s[rk+1])
                rk += 1
            ans = max(ans, rk-i+1)
        return ans

#利用字典减少一层循环，通过字符重复位置的字典赋值来移动标识位，时间复杂度最低
class Solution:
    def lengthOfLongestSubstring(self, s):
        hashdict = {}
        rk, ans = -1, 0
        for i, c in enumerate(s):
            if c in hashdict and hashdict[c] > rk:
                rk = hashdict[c]
                hashdict[c] = i
            else:
                hashdict[c] = i
                ans = max(ans, i-rk)
        return ans

a = Solution()
print(a.lengthOfLongestSubstring(s))