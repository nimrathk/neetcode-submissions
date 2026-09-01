from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        keys = list(freq.keys())

        for i in range(len(keys)):
            heapq.heappush(heap, (-1 * freq[keys[i]], keys[i]))

        ans = list()

        for i in range(k):
            ans.append(heap[0][1])
            heapq.heappop(heap)
        
        return ans