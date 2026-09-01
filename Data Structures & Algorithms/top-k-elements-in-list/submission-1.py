from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        keys = list(freq.keys())

        for i in range(len(keys)):
            heapq.heappush(heap, (freq[keys[i]], keys[i]))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = list()

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans