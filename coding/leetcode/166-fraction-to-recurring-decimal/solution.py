# These code is mainly based on the idea described here (https://leetcode.com/discuss/42159/0ms-c-solution-with-detailed-explanations)

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, den = numerator, denominator
        if den == 0:  # denominator is 0
            return
        if num == 0:  # numerator is 0
            return "0"
        res = []
        if (num < 0) ^ (den < 0):  # XOR check sign
            res.append("-")
        num, den = abs(num), abs(den)
        div, rmd = divmod(num, den)
        res.append(str(div))
        if rmd == 0:
            return "".join(res)  # only has integral part
        res.append(".")  # has frational part
        dic = {}
        while rmd:
            if rmd in dic:   # the remainder recurs
                res.insert(dic[rmd], "(")
                res.append(")")
                break
            dic[rmd] = len(res)
            div, rmd = divmod(rmd*10, den)
            res.append(str(div))
        return "".join(res)
