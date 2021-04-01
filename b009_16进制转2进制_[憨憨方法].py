

class Solution:
    def hex2bin(self, hex_value: str) -> str:  # 输入str，  返回str
        bin_dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                   '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                   '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
                   'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
        lis = []
        length = len(hex_value)
        for it in hex_value:
            bin_str = bin_dic[it]
            lis.append(bin_str)
        for item in lis:
            print(item)
        return ''.join(lis)


if __name__ == '__main__':
    solve = Solution()
    res = solve.hex2bin('0fff')
    print(res)