class Solution:
    def commonElements(self, a, b, c):
        # code here
        i, j, k = 0, 0, 0
        res = []
        
        while i < len(a) and j < len(b) and k < len(c):
            # If all three elements are equal
            if a[i] == b[j] == c[k]:
                # Avoid duplicates: only add if res is empty or 
                # if current element is different from the last added element
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
                k += 1
            
            # If a[i] is the smallest, it can't be common with current b[j] or c[k]
            elif a[i] < b[j]:
                i += 1
            # If b[j] is smaller than c[k], move j
            elif b[j] < c[k]:
                j += 1
            # Otherwise, c[k] must be the smallest relative to the others
            else:
                k += 1
                
        return res