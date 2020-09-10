'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
'''

s = "L"
numRows = 1

#常规解法
class Solution():
    def convert(self, s, numRows):
        #按行建立空字符串列表
        listRow = [''] * numRows
        #单行直接返回
        if numRows == 1:
            return s
        for i in range(len(s)):
            #对于前进列的数值正向赋值
            if i%(2*numRows-2) <= numRows-1:
                listRow[i%(2*numRows-2)] += (s[i])
            #对于返回列的数值反向赋值
            else:
                listRow[2*numRows-i%(2*numRows-2)-2] += (s[i])
        res = ''
        for i in listRow:
            res += i
        return res


a = Solution()
print(a.convert(s, numRows))
