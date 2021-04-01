"""
题目：
    二进制转十进制，
    传入二进制str
    传出十进制str
"""

class Solution:
    def bin2dec(self, bin_value:str) -> int:  # 传入str。  返回int
        dec_dict = {'0': 0, '1': 1}
        result = 0  # 累加
        count = 0  # 幂
        idx = len(bin_value) - 1
        bin_num = 0
        for item in bin_value:  # str二进制 变 int二进制
            digit = dec_dict[item]
            bin_num += digit * 10**idx
            idx -= 1
        while bin_num != 0 : # 二进制str变十进制str
            digit = bin_num % 10  # 余数
            result += digit * 2**count  # 累加
            bin_num //= 10  # 整数部分作为新的被除数
            count += 1
        return result


if __name__ == '__main__':
    solve = Solution()
    res = solve.bin2dec('1111')
    print('res = ', res)
    print(type(res))
