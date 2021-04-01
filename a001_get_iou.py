"""
『算法动手学』Python极简实现IoU
https://zhuanlan.zhihu.com/p/197895548
"""


def get_iou(bbox1, bbox2):
    xmin1, ymin1, xmax1, ymax1 = bbox1
    xmin2, ymin2, xmax2, ymax2 = bbox2

    s1 = (xmax1 - xmin2) * (ymax1 - ymin1)  # bbox1面积
    s2 = (xmax2 - xmin2) * (ymax2 - ymin2)  # bbox2面积

    inter_xmin = max(xmin1, xmin2)
    inter_ymin = max(ymin1, ymin2)
    inter_xmax = min(xmax1, xmax2)
    inter_ymax = min(ymax1, ymax2)

    inter_w = inter_xmax - inter_xmin
    inter_h = inter_ymax - inter_ymin

    inter_s = inter_w * inter_h  # 交集面积

    iou = inter_s / (s1 + s2 - inter_s)

    return iou


def main():
    bbox1 = [0, 0, 10, 10]
    bbox2 = [9, 9, 10, 10]
    iou = get_iou(bbox1, bbox2)
    print('iou = %f\n' %(iou))


if __name__ == '__main__':
    main()
