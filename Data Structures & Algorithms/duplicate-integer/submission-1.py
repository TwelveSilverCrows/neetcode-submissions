class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #best data structure is a set, keeps unique values
        seen = set()

        #iterate through array O(n) time and space
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        