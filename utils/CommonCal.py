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
    Ic_h = Ic_h0*math.exp(-(alpha*n*F*(E-Ee))/(R*T))
    Ec = -0.1183*math.log(Ic_h,10)-1.05259

    return Ec
#腐蚀单位阳极计算计算
def getCorrosionPointM(alpha:float, Ic_m0:list, n:int, E:list, Ee:list):
    Ia_m = Ic_m0 * math.exp((alpha*n*F*(E-Ee))/(R*T))

#计算ecorr参数
def getEcorr():
    return


