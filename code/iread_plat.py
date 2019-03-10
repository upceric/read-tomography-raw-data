def plateau(filename='60KV_100mmA_1s_1avg_06_03_2019_fdd739370_fod450.raw'):
    '''
    base on the filename, read the raw image and get the plateau
    '''
    import numpy as np
    image=np.empty((2332,2240),np.uint16)#image dimension is 2332*2240
    A=np.fromfile(filename,dtype='uint16',sep="")
    #print(A,len(A[1024:]))
    B=A[1024:]#skip header
    B=B.reshape([2240,2332])
    #print(np.mean(B[0:100,0:100]))#mean of roi
    i0=np.mean(B[0:100,0:100])#mean of roi
    to,bo=460,2000#to,bo top pixel,bottom pixel
    #plot gray against thickness
    if 1:
        thick,C=[],np.ones([bo-to,1]);
        sum=0
        for i in C:
            thick.append(sum*np.tan(np.deg2rad(30.96)))
            sum=sum+30.84*i
        bb=B[to:bo,1700]/i0
        x,y=[],[]
        for (i,j) in enumerate(thick):
            if j>20000:#threshold is 20000
                pass
            else:
                x.append(float(thick[i]))
                y.append(float(bb[i]))
        return([np.mean(y),i0])
