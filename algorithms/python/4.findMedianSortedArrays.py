'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
'''

nums1 = []
nums2 = [2,3]

#暴力求解
class Solution1():
    def findMedianSortedArrays(self, nums1, nums2):
        pos = (len(nums1) + len(nums2))//2 + 1
        flag = (len(nums1) + len(nums2))%2
        count = 0
        nums = []
        while(count < pos):
            if len(nums1) == 0 or len(nums2) == 0:
                break
            if nums1[0]<=nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))
            count += 1
            
        if count < pos:
            nums.extend(nums1[:pos-count] if len(nums1)>0 else nums2[:pos-count])
        if flag:
            return nums[-1]
        else:
            return (nums[-1]+nums[-2])/2
        
#二分法
class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1) > len(nums2)):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        len1, len2 = len(nums1), len(nums2)
        leftlen = round((len1 + len2)/2+0.1)
        flag = (len1 + len2)%2
        start, end = 0, len1
        while(start <= end):
            count1 = start + round((end - start)/2+0.1)
            count2 = leftlen - count1
            if count1 > 0 and nums1[count1-1] > nums2[count2]:
                end = count1 - 1
            elif count1 < len1 and nums2[count2-1] > nums1[count1]:
                start = count1 + 1
            else:
                if count1 == 0:
                    if flag:
                        return nums2[count2 - 1]
                    elif count2 == len2:
                        return (nums1[count1] + nums2[count2-1])/2
                    else:
                        return (nums2[count2-1]+(min(nums1[count1], nums2[count2]) if len1 else nums2[count2]))/2
                elif count1 == len1:
                    if flag:
                        return (max(nums1[count1-1], nums2[count2-1]))
                    elif count2 == 0:
                        return (nums1[count1-1] + nums2[count2])/2
                    else:
                        return (max(nums1[count1-1], nums2[count2-1])+nums2[count2])/2
                else:
                    if flag:
                        return(max(nums1[count1-1], nums2[count2-1]))
                    else:
                        return((max(nums1[count1-1], nums2[count2-1])+min(nums1[count1], nums2[count2]))/2)
                    
       
a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))
