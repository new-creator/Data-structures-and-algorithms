class Solution():
    def addtion(self, nums, t):
        a = dict()
        for i in range(len(nums)):
            if (t - nums[i]) in a:
                return i, a[(t-nums[i])]
            else:
                a[nums[i]] = i

nums = [1,'3',5,6]
t = 11
nums1 = range(10)
solu = Solution()
print(solu.addtion(nums, t))