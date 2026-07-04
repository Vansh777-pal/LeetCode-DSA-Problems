class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        if (1 <= len(nums) <= 2000):
            for i in nums:
                if i > 0 and -2000 <= i <= 2000:
                    pos += 1
                elif i < 0 and -2000 <= i <= 2000:
                    neg += 1

            if pos >= neg:
                return pos
            return neg









        # low = 0
        # high = len(nums) - 1
        # pos = 0
        # neg = 0
        # while (low <= high):
        #     mid = (low + high) // 2
        #     if (nums[mid] < 0):
        #         low = mid + 1
        #     elif (nums[mid] > 0):
        #         high = mid -1
        #     else :
        #         if (nums[mid+1] > 0):
        #             pos = len(nums[mid:])
        #             mid 
        #         elif(nums[mid -1] < 0):
        #             neg = len(nums[:mid])
        #         else:
                    
                    
        # if (pos >= neg):
        #     return pos
        # return neg