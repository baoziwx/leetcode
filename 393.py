class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        if not data or len(data) == 0:
            return True

        one_zero_bytes_to_check = 0
        data_len = len(data)
        for i in range(data_len):
            bin_str = "{0:08b}".format(data[i])
            # print bin_str
            # print one_zero_bytes_to_check
#           part of previous char
            if one_zero_bytes_to_check > 0:
                if bin_str[:2] == '10':
                    one_zero_bytes_to_check -= 1
                    continue
                else:
                    # print one_zero_bytes_to_check
                    # print bin_str
                    return False

#           new char
            zero_idx = bin_str.find('0')
            if zero_idx == 0:
#               ok, one character, continue to next
                continue
            elif zero_idx == 1 or zero_idx > 4:
#               just not right
                return False
            else:
                one_zero_bytes_to_check = zero_idx - 1
        print one_zero_bytes_to_check
        return one_zero_bytes_to_check == 0
