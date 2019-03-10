from matplotlib import pyplot as plt
import numpy as np
#image dimension is 2332*2240
image=np.empty((2332,2240),np.uint16)
#read image to A, filetype is unsigned 16
A=np.fromfile('60KV_100mmA_1s_1avg_06_03_2019_fdd739370_fod450.raw',dtype='uint16',sep="")
#skip header
B=A[1024:]
B=B.reshape([2240,2332])
#choose a roi region and claculate the mean value
i0=np.mean(B[0:100,0:100])
plt.imshow(B,cmap='gray')
plt.show()
