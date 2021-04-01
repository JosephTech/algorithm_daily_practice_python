"""
【面试题】Python的浅拷贝与深拷贝
https://blog.csdn.net/weixin_45081575/article/details/104603779?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242

"""
import copy  # 导入模块


def main():
    a = [1, 2, 3, [4, 5]]
    b = copy.copy(a)

    print(id(a))
    print(id(b))
    print("浅拷贝只对 内层地址做一个引用:")
    print(id(a[3]))
    print(id(b[3]))

    c = copy.deepcopy(a)
    print("深拷贝，直接新建一份数据，与原数据再无瓜葛：")
    print(id(c))
    print(id(a))
    print("再无关系")
    print(id(c[3]))
    print(id(a[3]))



if __name__ == '__main__':
    main()