import numpy as np
import random, math
'''kd树的实现：建立树，查找最近邻点的实现'''
class KD_node:
    def __init__(self, elt=None, split=None, LL=None, RR=None):
        '''
        elt:数据点
        split:划分域
        LL, RR:节点的左儿子跟右儿子
        '''
        self.elt = elt
        self.split = split
        self.left = LL
        self.right = RR
    def createKDTree(self, data_list):
        '''
        方差 + 二分查找
        root:当前树的根节点
        data_list:数据点的集合(无序)
        return:构造的KDTree的树根
        '''
        LEN = len(data_list)
        if LEN == 0:
            return
        # 数据点的维度
        dimension = len(data_list[0])
        # 方差
        max_var = 0
        # 最后选择的划分域
        split = 0
        for i in range(dimension):
            items = []
            for t in data_list:
                items.append(t[i])
            var = computeVariance(items)
            if var > max_var:
                max_var = var
                split = i
        #根据划分域的数据对数据点进行排序
        data_list.sort(key=lambda x: x[split])
        #选择下标为len / 2的点作为分割点
        elt = data_list[LEN//2]
        root = KD_node(elt,split)
        root.left = self.createKDTree(data_list[0:LEN//2])
        root.right = self.createKDTree(data_list[LEN//2+1:LEN])
        return root

def computeVariance(arrayList):
    '''
    arrayList:存放的数据点
    return:返回数据点的方差
    '''
    for ele in arrayList:
        ele = float(ele)
    LEN = float(len(arrayList))
    array = np.array(arrayList)
    sum1 = array.sum()
    array2 = array * array
    sum2 = array2.sum()
    mean = sum1 / LEN
    #    D[X] = E[x^2] - (E[x])^2
    variance = sum2 / LEN - mean**2
    return variance

def findNN(root, query):
    '''
    root:KDTree的树根
    query:查询点
    return:返回距离data最近的点NN，同时返回最短距离min_dist
    '''

    NN = root.elt
    min_dist = computeDist(query, NN)
    nodeList = []
    temp_root = root

    ## 二分查找建立路径
    while temp_root:
        nodeList.append(temp_root)
        dist = computeDist(query, temp_root.elt)
        if min_dist > dist:
            NN = temp_root.elt
            min_dist = dist

        # 当前节点的划分域
        splt = temp_root.split
        if query[splt] <= temp_root.elt[splt]:
            temp_root = temp_root.left
        else:
            temp_root = temp_root.right

        # 回溯查找
    while nodeList:
        #使用list模拟栈，后进先出
        back_elt = nodeList.pop()
        splt = back_elt.split
        print("back.elt = ", back_elt.elt)
        ## 判断是否需要进入父亲节点的子空间进行搜索
        if abs(query[splt] - back_elt.elt[splt]) < min_dist:
            if(query[splt] <= back_elt.elt[splt]):
                temp_root = back_elt.right
            else:
                temp_root = back_elt.left

            if temp_root:
                nodeList.append(temp_root)
                curDist = computeDist(query,temp_root.elt)
                if min_dist > curDist:
                    min_dist = curDist
                    NN = temp_root.elt
    return NN, min_dist

def computeDist(pt1, pt2):
    '''
    计算两个数据点的距离
    return：pt1和pt2之间的距离
    '''
    sum = 0.0
    for i in range(len(pt1)):
        sum = sum + (pt1[i]-pt2[i]) * (pt1[i]-pt2[i])
    return math.sqrt(sum)

# data = [[random.randint(1,100) for _ in range(2)] for _ in range(100)]
data = [[2,3], [4,7], [5,4], [7,2], [8,1], [9,6]]
kdtree = KD_node()
root = kdtree.createKDTree(data)
# 查找最近邻
NN, min_dist = findNN(root, [2,4.5])
print('end')