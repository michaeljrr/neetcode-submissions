class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store value and count
        store = {}
        # iterate one by one, store in dictionary
        for i in nums:
            store[i] = store.get(i, 0) + 1
        # sort in order of most to least frequent
        sorted_store = sorted(store.items(), key = lambda x:x[1], reverse = True)
        # return top k
        return [x[0] for x in sorted_store[:k]]