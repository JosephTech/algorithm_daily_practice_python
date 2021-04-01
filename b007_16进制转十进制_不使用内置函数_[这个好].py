"""
题目：
    输入16进制str
    转换成十进制int，无符号
"""

class Solution:
    def hex2dec(self, hex_value: str) -> int:  # 传入str十六进制, return十进制int
        dec_dict = {'0': 0, '1': 1, '2': 2, '3': 3,
                    '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'a': 10, 'b': 11,
                    'c': 12, 'd': 13, 'e': 14, 'f': 15}
        length = len(hex_value)
        result = 0
        for i in range(0, length, 1):  # 16进制str转 10进制int
            digit = dec_dict[hex_value[length - i - 1]]  # i=0时候，取最后一位
            result += digit * 16 ** i
        return str(result)


if __name__ == '__main__':
    solve = Solution()
    res = solve.hex2dec('ffff')
    print('res = ', res)
    print('type of res', type(res))