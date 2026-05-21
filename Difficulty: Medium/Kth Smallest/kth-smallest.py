import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # We use a Max-Heap to keep track of the k smallest elements seen so far.
        # Python's heapq is a Min-Heap by default, so we multiply by -1 to simulate a Max-Heap.
        max_heap = []
        
        for num in arr:
            heapq.heappush(max_heap, -num)
            # If heap size exceeds k, remove the largest element
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # The root of the max-heap is the kth smallest element
        return -max_heap[0]
        
