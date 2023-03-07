"""
这个文件里头主要定义了一些 常规计算函数
"""
import math



from res.CommonArgs import *



#获取Ee
def getEe(ETheta,n):
    return ETheta + (2303*R*T)/(n*F)

#腐蚀单位阴极计算计算
def getCorrosionPointC(alpha, Ic_h0, n, E, Ee):

    Ic_h = Ic_h0 * math.exp(-(alpha * n * F * (E-Ee))/(R * T))
    Ec = -0.1183 * math.log(Ic_h, 10) - 1.05259
    return Ec


#腐蚀单位阳极计算计算
def getCorrosionPointM(alpha:float, Ic_m0:list, n:int, E:list, Ee:list):
    # Ia_m = Ic_m0 * math.exp((alpha*n*F*(E-Ee))/(R*T))
    pass


#计算Ecorr参数
def getEcorr():
    return
#
# from skimage import data,io
# import matplotlib.pyplot as plt
# import numpy as np
# # img=data.coffee()
# img1 = data.camera()
# # img = np.array([[0,1,2,3,4,5],[0,6,3,8,0]])
#
# arr1 = img1.flatten()
# # plt.figure('image')
# # io.imshow(img)
# # plt.title('coffee')
# # plt.show()
#
# plt.figure('hist')
# arr=img1.flatten()# 二维数组序列化成一维数组
# arr1 = data.coffee().flatten()
# plt.hist(arr1, bins=256, density=1,edgecolor='None',facecolor='blue')
# plt.hist(arr, bins=256, density=1,edgecolor='None',facecolor='red')
#
# plt.title('histogram')
# plt.show()


