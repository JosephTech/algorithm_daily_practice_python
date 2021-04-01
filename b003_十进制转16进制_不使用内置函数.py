#Python进制转换10进制转换为16进制，不使用hex函数

class Solution:
    def dec2hex(self, num: int) -> str:  # 传入int型的，return str类型
        hex_dict = {0:'0', 1:'1', 2:'2', 3:'3',
                    4:'4', 5:'5', 6:'6', 7:'7',
                    8:'8', 9:'9', 10:'a', 11:'b',
                    12:'c', 13:'d',14:'e', 15:'f'}
        lis = []
        if num == 0:  # 整型 数字
            return '0'
        else:
            if num < 0:
                num += 2**32  # 输入是32位有符号？
                # 例如输入是8位有符号，即输入位于-128~127，共256个数
                # 正数第一位是0。 负数第一位是1
                # 输入-15， 首先 -15 + 256 = 241
                # 将241转成16进制 有符号
                # 【意思就是】，意思就是 有符号，首位是1，
                # 比如有符号8位，  -2是10000010
                # 把这个数直接转化为16进制即可（题目不要求16进制带符号，因为，最终都要转换成有符号的2进制）
            while num > 0:
                lis.append(hex_dict[num % 16])  # 除16取余数
                num //= 16  # 商
            lis.reverse()  # 颠倒
            return ''.join(lis)  # list转换为str

if __name__ == '__main__':
    solve = Solution()
    result = solve.dec2hex(15)
    print('result = ', result)