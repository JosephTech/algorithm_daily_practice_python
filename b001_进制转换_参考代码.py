"""
参考资料：
 python间进制转换（二进制、八进制、十进制，十六进制）（使用内置库函数）
 https://blog.nowcoder.net/n/aaaf09d960f24c3eba7c9fd80f1fb344
 python十进制和二进制的转换 (含浮点数)
 https://blog.nowcoder.net/n/27b47f8966934b47b296873169fee146
 python中end=" "的含义
 https://blog.csdn.net/JohnJim0/article/details/105077443
 Python | 不使用库函数将十进制数转换为二进制
 https://blog.csdn.net/cumt951045/article/details/107767410
 Python | 不使用库函数将二进制数转换为十进制
 https://blog.csdn.net/cumt30111/article/details/107767411?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&dist_request_id=1328740.15413.16168483142230147&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control
 Python进制转换10进制转换为16进制，不使用hex函数 （好好好）
 https://blog.csdn.net/ly_58/article/details/102869051
 """

# Python code to convert decimal to binary


# 十进制转二进制 function definition
# it accepts a decimal value
# and prints the binary value
class Solution:
    # def __init__(self):
    #     self.count = 0
    #     self.bin_value = ''
    #
    # # decimal to binary 十进制转二进制
    # def dec2bin(self, dec_value):  # 输入十进制
    #     # logic to convert decimal to binary
    #     # using recursion
    #     if dec_value > 1:  # if dec_value = 2,3,4....
    #         self.count += 1
    #         print(self.count)
    #         self.dec2bin(dec_value // 2)  # put 商 into recursion
    #     # print(dec_value % 2, end='')
    #     self.bin_value += str(dec_value % 2)  # 余数部分，除2取余法。  这行就是取余数，从最后一个余数添加到bin_value
    #     print(self.bin_value)
    #     if len(self.bin_value) == self.count + 1:  # 后序。 recursion end condition。
    #         # count是除了几次2。 bin_value是长度
    #         print('hello')
    #         return self.bin_value  # 这个返回的是str
    #
    # # binary to dicimal 二进制转十进制，不用内置函数int(string_num, 2)
    # def bin2dec(self, bin_value):  # binary to decimal。 输入二进制
    #     cnt = 0
    #     result = 0
    #     while bin_value != 0:
    #         digit = bin_value % 10 # 余数作为幂
    #         bin_value = bin_value // 10 # 商作为新的被除数
    #         result += digit * 2 ** cnt
    #         cnt += 1
    #     return result

    # 第二种 十进制转2进制，不用递归
    def dec2bin2(self, dec_value: int) -> str:  # 传入有符号十进制int。  return str
        bin_dic = {0: '0', 1: '1'}
        lis = []  # 存放结果，元素时str
        if dec_value == 0:
            return '0'
        else:
            if dec_value < 0:  # 处理负数
                dec_value += 2**32
            while dec_value > 0:
                lis.append(bin_dic[dec_value % 2])  # 取余
                dec_value //= dec_value  # 商 循环
            lis.reverse()
            result = ''.join(lis)
            return result


# main code
if __name__ == '__main__':
    # decimal = int(input("Input a decimal number: "))
    # print("Binary of the decimal ", decimal, "is: ", end='')
    # d2b = DecToBin()  # python类实例化要有括号
    # res = d2b.dec2bin2(dec_value=decimal)

    # bin_value = int(input("Input a binary number:"))
    # b2d = DecToBin()
    # result = b2d.bin2dec(bin_value)

    solve = Solution()
    result = solve.dec2bin2(6)

    print("result = ", result)
    # print("type of result: ", type(result))