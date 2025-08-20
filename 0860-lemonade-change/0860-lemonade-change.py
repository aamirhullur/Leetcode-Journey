class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bill, ten_bill = 0,0

        for bill in bills:
            if bill == 5:
                five_bill += 1
            elif bill == 10:
                if five_bill:
                    five_bill -= 1
                    ten_bill += 1
                else:
                    return False
            else:
                if five_bill and ten_bill:
                    five_bill -= 1
                    ten_bill -= 1
                elif five_bill >= 3:
                    five_bill-=3
                else:
                    return False
        
        return True