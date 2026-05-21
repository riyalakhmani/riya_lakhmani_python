class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If the array has only one element, we are already at the end.
        if n <= 1:
            return 0
        
        # If the first element is 0, we can't move anywhere.
        if arr[0] == 0:
            return -1
        
        farthest = 0
        end = 0
        jumps = 0
        
        # We loop until n-1 because we don't need to jump once we reach the last index.
        for i in range(n - 1):
            # Update the farthest point reachable from current index i
            farthest = max(farthest, i + arr[i])
            
            # If we've reached the end of the current jump range
            if i == end:
                jumps += 1
                end = farthest
                
                # If at any point the 'end' reaches or exceeds the last index
                if end >= n - 1:
                    return jumps
            
            # If we can't move forward any further and haven't reached the end
            if i >= farthest:
                return -1
                
        return -1
	    