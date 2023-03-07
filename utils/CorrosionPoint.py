
from res.CommonArgs import *
alpha= 0.5

#艾菲尔斜率
AFE = [round(R*T/alpha/i/F,4) for i in ZYDZ]




#计算腐蚀电位
from BalancePoint import get_bp
#平衡电位
PHDW = get_bp()

# 训练参数 电压 阳极
b15 = -1.7
# 训练参数 电压 阴极
b16 = -1.8

# 这个文件差点意思
# 计算不是那么准确



ia_1 = [JHDLDEN[i]*(math.exp((b15-PHDW[i])/AFE[i])) for i in range(4)]
ia_2 = [JHDLDEN[i]*(math.exp((b16-PHDW[i])/AFE[i])) for i in range(4)]
# print(JHDLDEN,PHDW,AFE)
# print(ia_1)
def Ecorr():

    #下面是电流的总和 阳极阴极 需要计算
    h15 =math.log(sum(ia_1),10)
    # print(h15)

    h16 = math.log(sum(ia_2),math.e)



    g10 = JHDLDEN[-1]
    g8 = PHDW[-1]
    c19 = (b15-b16)/(h15-h16)



    g9 = AFE[-1]

    d20 = 2.303*g9*math.log((g10),10)+g8


    d19 = c19*h15 + b15
    # print(c19,h15,b15)
    # print(d20,d19,g8)


    c20 = -2.303*g9
    c21 = (d20-d19)/(c19-c20)


    ecorr = c20*c21 + d20
    return ecorr

# print(Ecorr())