print("Please enter the Key to access!")
x=str(input())
e64 = ""
import base64
pt = base64.b64decode(x)
if(pt==b'tata'):
    print("Access granted welocome to RESYST")
else:
    print("Sorry your access has denied")
    exit(0)
from numpy import *
k1=[1,0,1,0,0,1,0,0]#Keys K1 
k2=[0,1,0,0,0,0,1,1]# Key k2
ip=[2,6,3,1,4,8,5,7]#intial premuatation question given
ap=[2,4,3,1]#Permutataion for p4
ip_1=[4,1,3,5,7,2,8,6]
cp=[0, 0, 1, 1, 1, 0, 0, 0]#CipherText
ep=[4,1,2,3,2,3,4,1] #permutation on rs
perp4=[2,4,3,1]
ap=[]
# Declaring the s0,s1 matrix
s0 = [[1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,1]]
s1 = [[0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]]
def per(pkey,arr):
    ap = []
    for i in range(len(pkey)): #Encountering the intial premutataion stage-1
        count = pkey[i]
        ap.append(arr[count-1])
        #print(ap)
    return ap
def exor(a1,a2):
    import numpy as exor
    a3 = exor.bitwise_xor(a1,a2)
    return a3
ipcp = per(ip,cp)
print("\n",ipcp)
rs = [1,0,1,0] #right side 
ls = [0,0,1,0] #left side
rsep = per(ep,rs)
print("\n",rsep)
outexor = exor(rsep,k2) #Ex-OR operation 
print("\n",outexor)
rows0=(str(outexor[0])+str(outexor[3]))
cols0=(str(outexor[1])+str(outexor[2]))
rows1=(str(outexor[4])+str(outexor[7]))
cols1=(str(outexor[5])+str(outexor[6]))
os0=(s0[int(rows0,2)][int(cols0,2)])
os1=(s1[int(rows1,2)][int(cols1,2)])
print("Intersection of row&col in s0:",os0," Intersection of row&col in s1:",os1)
p4 = str("{0:b}".format(os0))+str("{0:b}".format(os1))
p4 = [int(x) for x in str(p4)]
p4 = per(perp4,p4)
print("\n",p4)
p4ls = exor(p4,ls)
print(p4ls)
swap=[]
for i in range(8):
    if(i<=3):
        swap.append(rs[i])
    else:
        swap.append(p4ls[i-4])
print(swap)
#stage-2---------------------------------------------------------------------------
ls=[1,0,1,0]
rs=[1,1,0,1]
s_2_rs = per(ep,rs)
print("\n",s_2_rs)
outexor = exor(s_2_rs,k1)
print("\n",outexor)
rows0=(str(outexor[0])+str(outexor[3]))
cols0=(str(outexor[1])+str(outexor[2]))
rows1=(str(outexor[4])+str(outexor[7]))
cols1=(str(outexor[5])+str(outexor[6]))
os0=(s0[int(rows0,2)][int(cols0,2)])
os1=(s1[int(rows1,2)][int(cols1,2)])
print("Intersection of row&col in s0:",os0," Intersection of row&col in s1:",os1)
p4 = str("{0:b}".format(os0))+str("{0:b}".format(os1))
p4 = [int(x) for x in str(p4)]
p4 = per(perp4,p4)
print("\n",p4)
p4ls = exor(p4,ls)
print(p4ls)
swap = []
for i in range(8):
    if(i<=3):
        swap.append(p4ls[i])
    else:
        swap.append(rs[i-4])
print("\n",swap)
pt = per(ip_1,swap)
print("\n",pt)





