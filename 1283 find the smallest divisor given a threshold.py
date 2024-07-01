from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        right = max(nums)
        left = 1
        while left<=right:
            mid = (left+right)//2
            s = 0
            for i in nums:
                if i % mid != 0:
                    s += i//mid + 1
                else:
                    s += i//mid
            if s <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left
        '''rng = max(nums)
        for i in range(1, rng+1):
            if sum(ceil(j / i) for j in nums) <= threshold:
                return i
        return -1'''
        '''nums.sort()
        ans = max(nums)
        f = 0
        for num in nums:
            s = 0
            for i in nums:
                if i % num != 0:
                    s += i//num + 1
                else:
                    s += i//num
            print(s)
            if s <= threshold:
                return num
        return -1'''
        '''for i in range(0, len(nums)):
            if nums[i] % threshold != 0:
                nums[i] = nums[i]//threshold + 1
            else:
                nums[i] = nums[i]//threshold            
        sum = 0
        for num in nums:
            sum += num
        return sum'''