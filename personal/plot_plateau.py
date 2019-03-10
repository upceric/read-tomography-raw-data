from iread_plat import plateau 
from matplotlib import pyplot as plt
voltage=[40,60,80,100,120]
sca_to_total,total=[],[]
sca_to_total_120,total_120=[],[]
for i in voltage:
    filename=str(i)+'KV_100mmA_1s_1avg_06_03_2019_fdd739370_fod450.raw'
    sca_to_total.append(plateau(filename)[0])
    total.append(plateau(filename)[1])
    filename=str(i)+'KV_120mmA_1s_1avg_06_03_2019_fdd739370_fod450.raw'
    sca_to_total_120.append(plateau(filename)[0])
    total_120.append(plateau(filename)[1])
print(sca_to_total)
print(total)
#print(sca_to_total_120)
f1=plt.figure(1)
f2=plt.figure(2)
plt.figure(1)
plt.plot(voltage,sca_to_total,'ro-',label='100mmA 1s 1avg no filter')
plt.plot(voltage,sca_to_total_120,'bo-',label='120mmA 1s 1avg no filter')
plt.figure(2)
plt.plot(total,sca_to_total,'ro-',label='100mmA 1s 1avg no filter')
plt.plot(total_120,sca_to_total_120,'bo-',label='120mmA 1s 1avg no filter')
voltage=[80,100,120]
sca_to_total=[]
sca_to_total_120=[]
total,total_120=[],[]
for i in voltage:
    filename='../keil_absorption_copper_filter/'+str(i)+'KV_100mmA_1s_1avg_05_03_2019_fdd739370_fod450.raw'
    sca_to_total.append(plateau(filename)[0])
    total.append(plateau(filename)[1])
    filename='../keil_absorption_copper_filter/'+str(i)+'KV_120mmA_1s_1avg_05_03_2019_fdd739370_fod450.raw'
    sca_to_total_120.append(plateau(filename)[0])
    total_120.append(plateau(filename)[1])
plt.figure(1)
plt.plot(voltage,sca_to_total,'r^-',label='100mmA 1s 1avg copper filter')
plt.plot(voltage,sca_to_total_120,'b^-',label='120mmA 1s 1avg copper filter')
plt.legend(loc='best')

plt.figure(2)
plt.plot(total,sca_to_total,'r^-',label='100mmA 1s 1avg copper filter')
plt.plot(total_120,sca_to_total_120,'b^-',label='120mmA 1s 1avg copper filter')
plt.legend(loc='best')
plt.show()
