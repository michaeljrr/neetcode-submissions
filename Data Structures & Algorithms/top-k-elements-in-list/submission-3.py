class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            store[i] = store.get(i,0) + 1
        for num, freq in store.items():
            bucket[freq].append(num)
        result = []
        for j in range(len(bucket) - 1, -1, -1):
            if k > len(result):
                for l in range(min(k - len(result), len(bucket[j]))):
                    result.append(bucket[j][l])
            else:
                return result
