class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums=nums

        for i in range(len(self.nums)-1):
            if self.nums[i]+self.nums[i+1]==target:
                return [i,i+1]


        
        



nums=Solution()
print(nums.twoSum([2,7,11,15],9))


print(" I am interested in learning something new right now ")
print("Something that is going to be considered useful")