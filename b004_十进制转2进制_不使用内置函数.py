"""
题目：
  输入10进制有符号整型，32位
  输出2进制
"""

class Solution:
    def dec2bin(self, dec_value: int) -> str:  # 传入int十进制。 返回8进制str
        bin_dict = {0: '0', 1: '1'}
        lis = []
        if dec_value == 0:
            return 0
        else:
            if dec_value < 0: #处理负数
                dec_value += 2**32
            while dec_value > 0:
                lis.append(bin_dict[dec_value % 2])  # 取余
                dec_value //= 2  # 整数部分 循环
            lis.reverse()
            result = ''.join(lis)
            return result


if __name__ == '__main__':
    solve = Solution()
    res = solve.dec2bin(6)
    print("res = ", res)
    print("type of res: ", type(res))