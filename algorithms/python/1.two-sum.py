'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''

nums = [2, 7, 11, 15]
target = 18

# 常规思路，遍历循环求解
class Solution1:
    def twoSum(self, nums, target):
        temp = nums.copy()
        ans = []
        for i in range(len(nums)):
            temp.pop(0)
            for j in range(len(temp)):
                if nums[i] + temp[j] == target:
                    ans.append(i)
                    ans.append(j+i+1)
                    return ans  #返回函数，跳出多层循环

# target生成补列表进行查询      
class Solution2():
    def twoSum(self, nums, target):
        templist = [target-nums[i] for i in range(len(nums))]
        temp = nums.copy()
        ans = []
        for i in range(len(nums)):
            temp.pop(0)
            if templist[i] in temp:
                ans.append(i)
                ans.append(temp.index(templist[i])+i+1)
                return ans

# 利用字典提高查找效率
class Solution():
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if target-num in hashmap:   #in操作符用于判断键是否存在于字典中
                return [hashmap[target-num], i]
            hashmap[num] = i

a = Solution()
print(a.twoSum(nums, target))
