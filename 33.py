class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []: return -1
        # minIdx = self.searchMin(nums, 0, len(nums - 1))
        return self.searchHelper(nums, target, 0, len(nums) - 1)

#     def searchMin(self, nums, start, end):
#         mid = (int)((end - start) / 2)
#         if nums[mid] > nums[mid + 1]:
#             return mid
#         else:
#             return self.searchMin()




    def searchHelper(self, nums, target, start, end):
        if end < start:
            return -1

        mid = (int) ((end + start) / 2)
        print start
        print mid
        print end
        print nums[mid]
        print ''
        if nums[mid] == target:
            return mid
        else:
            if nums[start] <= nums[mid]: #left sorted
                if nums[start] <= target < nums[mid]:
                    return self.searchHelper(nums, target, start, mid - 1)
                else:
                    return self.searchHelper(nums, target, mid + 1, end)
            else: #right sorted
                if nums[mid] < target <= nums[end]:
                    return self.searchHelper(nums, target, mid + 1, end) #search right
                else:
                    return self.searchHelper(nums, target, start, mid - 1)





