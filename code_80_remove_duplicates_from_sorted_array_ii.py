class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums
        p1 = 1 # where i want to dump the next number
        v1 = nums[0] # let's get the party started
        is_already_matched = False
        for p2 in range(1,n):
            if v1 == nums[p2]:
                if is_already_matched:
                    continue
                is_already_matched = True
                nums[p1] = v1
                p1+=1
            else:
                nums[p1] = v1 = nums[p2]
                p1 += 1
                is_already_matched = False
        for i in range(p1,n):
            nums[i] = '_'
        return p1
