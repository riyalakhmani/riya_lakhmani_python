class Solution:
    def maxWater(self, arr):
        # code here
        if not arr:
            return 0
            
        left, right = 0, len(arr) - 1
        left_max, right_max = 0, 0
        total_water = 0
        
        while left <= right:
            # We process the smaller side because it's the limiting factor
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    total_water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    total_water += right_max - arr[right]
                right -= 1
                
        return total_water
        