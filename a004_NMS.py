import torch
"""
NMS算法详解（附Pytorch实现代码）
https://zhuanlan.zhihu.com/p/54709759

pytorch源码
"""


class Test_NMS:
    #def __init__(self):

    def iou(self, box1, box2):  # 假设box1维度为[N, 4]    box2维度为[M, 4]
        N = box1.size(0)
        M = box2.size(0)

        lt = torch.max(
            # 第1个框，左上角坐标xmin1,ymin1 =  box1[1, :2]
            box1[:, :2].unsqueeze(1).expand(N, M, 2),  # [N, 2] -> [N, 1, 2] -> [N, M, 2]
            # 第二个框，左上角坐标xmin2, ymin2 = box2[1, :2]
            box2[:, :2].unsqueeze(0).expand(N, M, 2)   # [M, 2] -> [1, M, 2] -> [N, M, 2]
        )
        # N=1, M=1时找最大作为inter_xmin, inter_ymin；
        # N=1, M=2时找最大作为inter_xmin, inter_ymin；
        # N=1, M=3时候，找最大
        # N=2, M=1.。。

        rb = torch.min(
            # 第1个框， 右下角坐标 xmax1, ymax1 = box1[1, 2:]
            box1[:, 2:].unsqueeze(1).expand(N, M, 2),
            # 第2个框， 右下角坐标 xax2, ymax2 = bbox[1, 2:]
            box2[:, 2:].unsqueeze(0).expand(N, M, 2)
        )

        # [N, M, 2]
        wh = rb - lt  # 对应相减， 第一个框[1, 1, w和h] = rb[1, 1, 2:] - lt[1, 1, 2:]
        wh[wh < 0] = 0  #wh<0返回索引，。挑出来 没有重叠的 = 0
        inter = wh[:, :, 0] * wh[:, :, 1]  # [N, M]

        # (xmax1 - xmin1) * (ymax1 - ymax1)
        area1 = (box1[:, 2] - box1[:, 0]) * (box1[:, 3] - box1[:, 1])  # (N,)
        area2 = (box2[:, 2] - box2[:, 0]) * (box2[:, 3] - box2[:, 1])  # (M,)

        area1 = area1.unsqueeze(1).expand(N, M)  # (N, M)
        area2 = area2.unsqueeze(0).expand(N, M)  # (N, M)

        iou = inter / (area1+area2-inter)
        return iou

    def nms(self, bboxes, scores, threshold=0.5):
        x1 = bboxes[:, 0]  # 左上角坐标。 比如第一个框左上角横坐标 x1 = bboxes[1, 0]
        y1 = bboxes[:, 1]
        x2 = bboxes[:, 2]  # 右下角坐标
        y2 = bboxes[:, 3]

        areas = (x2 - x1) * (y2 - y1)  # [N,]  每个元素代表每个bbox的面积
        _, order = scores.sort(0, descending=True)  # 降序排列，返回位置索引

        keep = []
        while order.numel() > 0:  # torch.numel()是这个tensor的总元素个数
            if order.numel() == 1:  # 如果只有1个框，就保留。返回
                i = order.item()  # tensor.item()把tensor元素取出作为numpy数字
                keep.append(i)
                break
            else:
                i = order[0].item()  # 保留scores最大的那个框box[i]，  它的索引i放到keep[]中
                keep.append(i)

            # 计算box[i]与其余各框的IoU
            # order[1:]是order中第1、第2..个， 是框的索引号
            # .clamp(min = x1[i])   小于x1[i]的值，都改成了x1[i]。  再赋值给xx1
            # 而大于x1[i]的值，仍保持不变，赋值给xx1
            # 相当于求x1[i] 和 x1[order[1:]] 中的较大值，两两求
            # 这可太秀了
            xx1 = x1[order[1:]].clamp(min=x1[i])  # torch.clamp(min, max) 设置上下限
            yy1 = y1[order[1:]].clamp(min=y1[i])
            xx2 = x2[order[1:]].clamp(max=x2[i])  # 相当于 两两求 较小值
            yy2 = y2[order[1:]].clamp(max=y2[i])

            inter = (xx2 - xx1).clamp(min=0) * (yy2-yy1).clamp(min=0)  # [N-1,]

            iou = inter / (areas[i] + areas[order[1:]] - inter)  # [N-1,]。  广播相加
            idx = (iou <= threshold).nonzero().squeeze()
            # iou <= threshold返回了 每个位置true和false，即每个位置0或1
            # .nonzero()是返回[Q, 1]的索引，所以要squeeze()一下
            # 此时idx为[n-1]， 而原索引是[n]
            # 抑制其它框
            if idx.numel() == 0:
                break
            order = order[idx+1]  # 修补索引之间的差值
            # 就是把<=threshold的， 重新放进order，再循环
        return torch.LongTensor(keep)  # Pytorch的索引值为LongTensor


if __name__ == '__main__':
    box1 = torch.tensor([[0., 0., 10., 10.],
                         [1., 1., 10., 10.]])
    box2 = torch.tensor([[9., 9., 10., 10.],
                         [8., 8., 10., 10.],
                         [7., 7., 10., 10.]])
    nms = Test_NMS()  # 实例化

    print(box1.size())
    print(box2.size())
    iou = nms.iou(box1=box1, box2=box2)
    print(iou.shape)
    print(iou)


