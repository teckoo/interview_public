class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10: 
            carry = 1
            digits[-1] = 0
        else:
            carry = 0 
        result = [digits[-1]]
        for n in digits[-2::-1]:
            r = carry + n 
            if r > 9:
                r = 0
                carry = 1 
            else:
                carry = 0    
            result.append(r)    
        return result[::-1] if carry == 0 else [1] + result[::-1]
