from matplotlib import pyplot as plt
import numpy as np
image=np.empty((2332,2240),np.uint16)#image dimension is 2332*2240
A=np.fromfile('60KV_100mmA_1s_1avg_06_03_2019_fdd739370_fod450.raw',dtype='uint16',sep="")
print(A,len(A[1024:]))
B=A[1024:]#skip header
B=B.reshape([2240,2332])
print(np.mean(B[0:100,0:100]))#mean of roi
i0=np.mean(B[0:100,0:100])#mean of roi
#plt.imshow(B[0:2240,1:1000],cmap='gray')
plt.imshow(B,cmap='gray')
to,bo=460,2000#to,bo top pixel,bottom pixel
plt.plot([700,700],[to,bo],'or-')
plt.plot([1000,1000],[to,bo],'ob-')
plt.plot([1300,1300],[to,bo],'og-')
plt.plot([1700,1700],[to,bo],'oy-')
plt.xlim([0,2240])
plt.ylim([0,2332])
plt.gca().invert_yaxis()
#plt.show()
plt.figure()
#plot log(gray)
bc=150
if 0:
    plt.plot(np.log(B[to:bo,700]-bc),'or-',label='Fe')
    plt.plot(np.log(B[to:bo,1000]-bc),'ob-',label='Al')
    plt.plot(np.log(B[to:bo,1300]-bc),'og-',label='C')
    plt.plot(np.log(B[to:bo,1700]-bc),'oy-',label='Cu')
#plot gray value 
if 0:
    plt.plot(B[to:bo,700],'or-',label='Fe')
    plt.plot(B[to:bo,1000],'ob-',label='Al')
    plt.plot(B[to:bo,1300],'og-',label='C')
    plt.plot(B[to:bo,1700],'oy-',label='Cu')
#plot gray against thickness
if 0:
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(11.53)))
        sum=sum+30.84*i
    plt.plot(thick,B[to:bo,700],'or-',label='Fe')
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(30.96)))
        sum=sum+30.84*i
    plt.plot(thick,B[to:bo,1000],'ob-',label='Al')
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(45.17)))
        sum=sum+30.84*i
    plt.plot(thick,B[to:bo,1300],'og-',label='C')
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(30.96)))
        sum=sum+30.84*i
    plt.plot(thick,B[to:bo,1700],'oy-',label='Cu')
#plot -ln(gray/background) against thickness
if 0:
    bcv=0.0
    #Fe
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(11.53)))
        sum=sum+30.84*i
    plt.plot(thick,-np.log(np.abs((B[to:bo,700]-bcv))/(i0-bcv)),'r+',label='Fe')
    print(-np.log(np.abs((B[to:bo,700]-bcv))/(i0-bcv)))
    #get linear fit for the beginning
    bb=-np.log((B[to:bo,700]-bcv)/(i0-bcv))
    x,y=[],[]
    for (i,j) in enumerate(thick):
        if j>500:#threshold is 20000
            pass
        else:
            x.append(float(thick[i]))
            y.append(float(bb[i]))
    x=np.asarray(x)
    y=np.asarray(y)
    z=np.polyfit(x,y,1)
    print("z<500:",z)
    print("fe,mu/rho:",z[0]/7.87*10000)
    fit_fn=np.poly1d(z)
    plt.plot(x,fit_fn(x),'-k',linewidth=1)


    #Al
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(30.96)))
        sum=sum+30.84*i
    plt.plot(thick,-np.log(np.abs((B[to:bo,1000]-bcv))/(i0-bcv)),'b-',label='Al')

    #get linear fit for aluminium
    bb=-np.log((B[to:bo,1000]-bcv)/(i0-bcv))
    x,y=[],[]
    for (i,j) in enumerate(thick):
        if j<20000:#threshold is 20000
            pass
        else:
            x.append(float(thick[i]))
            y.append(float(bb[i]))
    x=np.asarray(x)
    y=np.asarray(y)
    z=np.polyfit(x,y,1)
    print("z>20000:",z)
    print("al,mu/rho:",z[0]/2.7*10000)
    fit_fn=np.poly1d(z)
    plt.plot(x,fit_fn(x),'-k',linewidth=3)

    #get linear fit for the beginning
    x,y=[],[]
    for (i,j) in enumerate(thick):
        if j>3000:#threshold is 20000
            pass
        else:
            x.append(float(thick[i]))
            y.append(float(bb[i]))
    x=np.asarray(x)
    y=np.asarray(y)
    z=np.polyfit(x,y,1)
    print("z<5000:",z)
    print("al,mu/rho:",z[0]/2.7*10000)
    fit_fn=np.poly1d(z)
    plt.plot(x,fit_fn(x),'-k',linewidth=1)


    #Carbon
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(45.17)))
        sum=sum+30.84*i
    plt.plot(thick,-np.log((B[to:bo,1300]-bcv)/(i0-bcv)),'g-',label='C')
    #get linear fit for carbon at the end
    bb=-np.log((B[to:bo,1300]-bcv)/(i0-bcv))
    x,y=[],[]
    for (i,j) in enumerate(thick):
        if j<40000:#threshold is 20000
            pass
        else:
            x.append(float(thick[i]))
            y.append(float(bb[i]))
    x=np.asarray(x)
    y=np.asarray(y)
    z=np.polyfit(x,y,1)
    print("z>40000:",z)
    print("carbon end,mu/rho:",z[0]/2.266*10000)
    fit_fn=np.poly1d(z)
    plt.plot(x,fit_fn(x),'-k',linewidth=3)

    #get linear fit for the beginning
    x,y=[],[]
    for (i,j) in enumerate(thick):
        if j>10000:#threshold is 20000
            pass
        else:
            x.append(float(thick[i]))
            y.append(float(bb[i]))
    x=np.asarray(x)
    y=np.asarray(y)
    z=np.polyfit(x,y,1)
    print("z<10000:",z)
    print("carbon,begin,mu/rho:",z[0]/2.266*10000)
    fit_fn=np.poly1d(z)
    plt.plot(x,fit_fn(x),'-k',linewidth=3)


    #Cu
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(30.96)))
        sum=sum+30.84*i
    import sys
    plt.plot(thick,-np.log((B[to:bo,1700]-bcv+sys.float_info.epsilon)/(i0-bcv)),'y+',label='Cu')
    #get linear fit for the beginning
    bb=-np.log((B[to:bo,1700]-bcv)/(i0-bcv))
    x,y=[],[]
    for (i,j) in enumerate(thick):
        if j>100:#threshold is 20000
            pass
        else:
            x.append(float(thick[i]))
            y.append(float(bb[i]))
    x=np.asarray(x)
    y=np.asarray(y)
    z=np.polyfit(x,y,1)
    print("z<100:",z)
    print("copper,mu/rho:",z[0]/8.96*10000)
    fit_fn=np.poly1d(z)
    plt.plot(x,fit_fn(x),'-k',linewidth=1)

#plot -ln(gray/background) against thickness
if 1:
    #Fe
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(11.53)))
        sum=sum+30.84*i
    plt.plot(thick,-np.log(B[to:bo,700]/i0),'r+',label='Fe')

    #Al
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(30.96)))
        sum=sum+30.84*i
    plt.plot(thick,-np.log(B[to:bo,1000]/i0),'b-',label='Al')

    #Carbon
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(45.17)))
        sum=sum+30.84*i
    plt.plot(thick,-np.log(B[to:bo,1300]/i0),'g-',label='C')

    #Cu
    thick,C=[],np.ones([bo-to,1]);
    sum=0
    for i in C:
        thick.append(sum*np.tan(np.deg2rad(30.96)))
        sum=sum+30.84*i
    plt.plot(thick,-np.log(B[to:bo,1700]/i0),'y+',label='Cu')


plt.legend()
plt.show()
