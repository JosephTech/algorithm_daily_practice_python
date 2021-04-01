"""
PyTorch实现VGG亲身实践
https://zhuanlan.zhihu.com/p/263527295
一文读懂VGG网络
https://zhuanlan.zhihu.com/p/41423739
"""
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary


class VGG(nn.Module):
    """
    VGG builder
    """
    def __init__(self, arch: object, num_classes=1000) -> object:
        # 构造函数， 传入list对象， 传出VGG对象
        super(VGG, self).__init__()
        self.in_channels = 3
        self.conv3_64 = self.__make_layer(64, arch[0])
        self.conv3_128 = self.__make_layer(128, arch[1])
        self.conv3_256 = self.__make_layer(256, arch[2])
        self.conv3_512a = self.__make_layer(512, arch[3])
        self.conv3_512b = self.__make_layer(512, arch[4])
        self.fc1 = nn.Linear(7*7*512, 4096)
        self.bn1 = nn.BatchNorm1d(4096)
        self.bn2 = nn.BatchNorm1d(4096)
        self.fc2 = nn.Linear(4096, 4096)
        self.fc3 = nn.Linear(4096, num_classes)

    def __make_layer(self, channels, num):
        layers = []
        for i in range(num):
            layers.append(nn.Conv2d(self.in_channels, channels, 3, stride=1, padding=1, bias=False))  # same padding
            layers.append(nn.BatchNorm2d(channels))  # ctrl+b或者鼠标放上去，就能看到函数说明 和
            layers.append(nn.ReLU())
            self.in_channels = channels
        return nn.Sequential(*layers)

    def forward(self, x):
        out = self.conv3_64(x)
        out = F.max_pool2d(out, 2)
        out = self.conv3_128(out)
        out = F.max_pool2d(out, 2)
        out = self.conv3_256(out)
        out = F.max_pool2d(out, 2)
        out = self.conv3_512a(out)
        out = F.max_pool2d(out, 2)
        out = self.conv3_512b(out)
        out = F.max_pool2d(out, 2)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = self.bn1(out)
        out = F.relu(out)
        out = self.fc2(out)
        out = self.bn2(out)
        out = F.relu(out)
        return F.softmax(self.fc3(out))

def VGG_11():
    return VGG([1, 1, 2, 2, 2], num_classes=1000)

def VGG_13():
    return VGG([1, 1, 2, 2, 2], num_classes=1000)

def VGG_16():
    return VGG([2, 2, 3, 3, 3], num_classes=1000)

def VGG_19():
    return VGG([2, 2, 4, 4, 4], num_classes=1000)

def test():
    # net = VGG_11()
    # net = VGG_13()
    # net = VGG_16()
    net = VGG_19()
    summary(net, (3, 224, 224))

if __name__ == '__main__':
    net = vgg16()  # 接收VGG实例

    net = net.cuda()  # 放到gpu上防止报错  https://blog.csdn.net/weixin_44776845/article/details/104888287

    # 降低pytorch到1.2才能用  https: // blog.csdn.net / peacefairy / article / details / 108024537
    # 这个方法好 http://www.qishunwang.net/news_show_16560.aspx

    summary(net, (3, 224, 224))  # input_size = (3, 224, 224)