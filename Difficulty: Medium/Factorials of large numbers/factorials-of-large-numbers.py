#User function Template for python3

class Solution:
    def factorial(self, n):
        #code here
        res = [1] # Stores digits in reverse order
        
        for i in range(2, n + 1):
            carry = 0
            # Multiply every digit currently in res by i
            for j in range(len(res)):
                prod = res[j] * i + carry
                res[j] = prod % 10
                carry = prod // 10
            
            # If carry remains, add it to the list
            while carry:
                res.append(carry % 10)
                carry //= 10
                
        # Reverse to get the correct order
        return res[::-1]