class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range (1, len(digits) + 1):
            if digits[-i] != 9:
                digits[-i] += 1
                break
            else: #digit is 9
                digits[-i] = 0
                if i >= len(digits):
                    digits = [1] + digits
                    break
                # else continue
        return digits