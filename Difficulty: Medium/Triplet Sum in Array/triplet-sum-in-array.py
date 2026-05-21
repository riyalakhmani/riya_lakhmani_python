class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        n = len(arr)
        # 1. Sort the array first
        arr.sort()
        
        # 2. Fix the first element of the triplet
        for i in range(n - 2):
            # Optimization: Use two pointers for the rest of the array
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1  # Need a larger sum
                else:
                    right -= 1 # Need a smaller sum
                    
        return False
        