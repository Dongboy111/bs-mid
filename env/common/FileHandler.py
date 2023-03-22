import xlwings as xw

app = xw.App(visible=False)

wb = app.books.open('js.xlsx')

#原始数据
_ = wb.sheets[0]

#原始数据
yssj = wb.sheets[1]

#平衡电位
phdw = wb.sheets[2]

#腐蚀电位
fsdw = wb.sheets[3]

#服饰电位2
fsdw2 = wb.sheets[4]

#电流密度
dlmd = wb.sheets[5]

#电流密度2
dlmd2 = wb.sheets[6]

#M1完全溶解的层数
M1Count = wb.sheets[7]

#M1完全溶解层数2
M1Count2 = wb.sheets[8]

#溶解电流密度
rjdlD = wb.sheets[9]

#溶解电流密度2
rjdlD2 = wb.sheets[10]

#Gd离子浓度
GdD = wb.sheets[11]

#Mg离子浓度
MgD = wb.sheets[12]

#Nd离子浓度
NdD = wb.sheets[13]

#Ln浓度
LnD = wb.sheets[14]

#Oh 离子浓度
OhD = wb.sheets[15]

#图界面离子浓度-沉积图
PictureInterfaceD = wb.sheets[16]

#沉积线
cjx = wb.sheets[17]

#过度饱和
gdbh = wb.sheets[18]

#图-过饱和度
PS = wb.sheets[19]

#形核速率
xhsl = wb.sheets[20]

#图-形核速率
PXhsl = wb.sheets[21]

#图-形核速率2
PXhsl2 = wb.sheets[22]

#晶体生长速率
jtszsl = wb.sheets[23]

#图-晶体生长速率
PJtszsl = wb.sheets[24]

#晶体生长速率2
jtszsl2 = wb.sheets[25]

#图-晶体生长速率2
PJtszsl2 = wb.sheets[26]

#覆盖面积与厚度
fgmjyhd = wb.sheets[27]

#图-覆盖率与厚度
PFglyhd = wb.sheets[28]

#腐蚀速率
fssl = wb.sheets[29]

#图-腐蚀速率
PFssl = wb.sheets[30]

#形核速率2
xhsl2 = wb.sheets[31]

def close():
    wb.close()
    app.quit()