

class Solution:
    def dec2oct(self, num:int)->str:  # 输入int类型(有符号整型)，返回str
        oct_dict = {0:'0', 1:'1', 2:'2', 3:'3',
                    4:'4', 5:'5', 6:'6', 7:'7'}  # 用字典映射，避免使用str
        lis = []  # 新建列表
        if num == 0:
            return '0'
        else:
            if num < 0:  # （先处理负数） 有符号整型，负数，首位是1。
                # 就是0 ~ 2**32前边一半是正数，后边一半是负数，中间一个0
                num += 2**32

            while num > 0:  # num作为被除数
                lis.append(oct_dict[num % 8])  # 取余
                num = num // 8  # 商 作为被除数
            lis.reverse()
            return ''.join(lis)

if __name__ == '__main__':
    solve = Solution()
    result = solve.dec2oct(15)
    print("result = ", result)


