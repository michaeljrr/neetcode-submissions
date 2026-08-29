class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product = 1
        result = []
        zero_set = set()
        for j in range(len(nums)):
            if nums[j] != 0:
                max_product *= nums[j]
            else:
                zero_set.add(j)
        for i in range(len(nums)):
            if len(zero_set) > 1 or (zero_set and i not in zero_set):
                result.append(0)
            elif nums[i] == 0:
                result.append(max_product)
            else:
                result.append(max_product//nums[i])
        return result