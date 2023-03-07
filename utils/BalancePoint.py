

from res.CommonArgs import *

balabce_point = []

def get_bp():
    for i in range(YN):
        # print("dong")
        # print(math.log(KSXS[i], 10))
        balabce_point.append(round(BZDW[i]+(2.303*R*T)/ZYDZ[i]/(F)*math.log(Mn, 10),7))
    for i in range(Y_N):
        balabce_point.append(round(-0.0591*Ph,7))
    return balabce_point

# -2.438
# -2.398
# -0.456
# -2.534
# -0.414
# for i in get_bp():
#     print(i)