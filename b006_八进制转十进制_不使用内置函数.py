"""
题目：
    八进制转十进制，传入str八进制， 返回int十进制
"""

class Solution:
    def oct2dec(self, oct_value: str) -> int:  # 传入八进制str，返回十进制int
        dec_dict = {'0': 0, '1': 1, '2': 2, '3': 3,
                    '4': 4, '5': 5, '6': 6, '7': 7}
        length = len(oct_value)
        oct_num = 0  # int八进制
        # str八进制转为 int八进制
        for i in range(0, length, 1):  # 0到len-1
            digit = dec_dict[oct_value[length - i - 1]]  # i=0取str的最后一个,转为int
            oct_num += digit * 10**i
        result = 0
        cnt = 0  # 幂
        while oct_num > 0:
            yushu = oct_num % 10
            result += yushu * 8 ** cnt
            oct_num //= 10  # 整数部分，循环
            cnt += 1
        return result


if __name__ == '__main__':
    solve = Solution()
    res = solve.oct2dec('777')
    print(res)