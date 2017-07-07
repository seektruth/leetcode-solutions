class Solution(object):
    def myAtoi(self, str):
        str.replace(" ","")
        cons = 0
        while str:
            try:
                cons = int(str)
                break
            except Exception:
                str = str[:-1]
        if cons >= 2147483648:
            cons = 2147483647
        elif cons < -2147483648:
            cons = -2147483648
        return cons