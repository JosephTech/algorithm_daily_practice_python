"""
题目：
    16进制转2进制
    先转十， 再转2
    输入16进制str，return二进制str
"""

class Solution:
    def hex2bin(self, hex_value: str) -> str:  # 输入str， 返回str
        hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3,
                    '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'a': 10, 'b': 11,
                    'c': 12, 'd': 13, 'e': 14, 'f': 15}
        dec_num = 0  # 十进制整数，累加
        length = len(hex_value)
        for i in range(0, length, 1):  # i是幂
            digit_str = hex_value[length - i - 1]  # 当i=0时，取十六进制str的最后一个
            dec_num += hex_dict[digit_str] * 16**i  # 累加为10进制int
        result = self.dec2bin(dec_num)  # 转化为二进制str
        return result

    def dec2bin(self, dec_num: int) -> str: # 传入十进制int， 返回二进制str
        bin_dict = {0: '0', 1: '1'}
        lis = []
        if dec_num == 0:
            return '0'
        # 可以再写一行有符号数的
        while dec_num > 0:
            lis.append(bin_dict[dec_num % 2])  # 余数 对应的str添加到 lis中
            dec_num //= 2  # 商 继续循环
        lis.reverse()  # 颠倒
        return ''.join(lis)  # 取出lis的，连接成字符串


if __name__ == '__main__':
    solve = Solution()
    res = solve.hex2bin('3e')
    print('res = ', res)