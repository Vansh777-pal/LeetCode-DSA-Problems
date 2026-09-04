class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        

        i = 0
        while i < n:
            arr = nums[0:i+1]
            r_arr = nums[i:n]
            max_el = max(arr)
            min_el = min(r_arr)
            

            if max_el - min_el <= k:
                return i

            i += 1
        return -1