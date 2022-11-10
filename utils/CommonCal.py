"""
这个文件里头主要定义了一些 常规计算函数
"""
import math

from res.CommonArgs import *

#获取Ee
def getEe(ETheta,n):
    return ETheta + (2303*R*T)/(n*F)

#腐蚀单位计算
def getCorrosionPoint(alpha,Ic_h0,n,E,Ee):
    Ic_h = Ic_h0*math.exp(-(alpha*n*F*(E-Ee))/(R*T))
    Ec = -0.1183*math.log(Ic_h,10)-1.05259
    return Ec

