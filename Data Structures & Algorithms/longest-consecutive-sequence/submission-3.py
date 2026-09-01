class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        counter = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                while current + 1 in nums_set:
                    counter += 1
                    current += 1
                if counter > longest:
                    longest = counter
                counter = 1
        return longest

           
            