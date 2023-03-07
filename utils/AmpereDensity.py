#计算电流密度

import numpy as np
from CorrosionPoint import AFE
from CorrosionPoint import PHDW
from res.CommonArgs import *

from CorrosionPoint import Ecorr

ecorr = Ecorr()

#计算电流密度
def ampereDensity():

    GDW = [ecorr-PHDW[i] for i in range(4)]
    DLMD = [JHDLDEN[i]*math.exp(GDW[i]/AFE[i]) for i in range(4)]
    return DLMD.index(min(DLMD))

print(LZ[ampereDensity()])



