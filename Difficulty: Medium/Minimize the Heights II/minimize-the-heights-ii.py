class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        if n == 1:
            return 0
        
        # 1. Sort the array
        arr.sort()
        
        # 2. Initial maximum possible difference
        res = arr[n-1] - arr[0]
        
        # 3. Iterate through the array to find the minimum possible difference
        for i in range(n - 1):
            # Important: Resulting height cannot be negative
            if arr[i+1] < k:
                continue
                
            # Potential new smallest and largest heights
            curr_min = min(arr[0] + k, arr[i+1] - k)
            curr_max = max(arr[n-1] - k, arr[i] + k)
            
            # Update the minimum difference found so far
            res = min(res, curr_max - curr_min)
            
        return res
        