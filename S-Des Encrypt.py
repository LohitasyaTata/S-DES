print("Please enter the CP")
x=str(input())
e64 = ""
import base64
pt = base64.b64decode(x)
if(pt==b'tata'):
    print("Access granted welocome to RESYST")
else:
    print("Sorry your access has denied")
    exit(0)
'''S-Des Encryption'''
import numpy as exor
from numpy import *
pt=[1,0,0,1,0,1,1,1] #8-bit plaintext
k1=[1,0,1,0,0,1,0,0]#Keys K1 
k2=[0,1,0,0,0,0,1,1]# Key k2
ip=[2,6,3,1,4,8,5,7]#intial premuatation question given
ap=[2,4,3,1]#Permutataion for p4
ip_1=[4,1,3,5,7,2,8,6]
ptip=[] # its the PT after the premutation IP
rs=[] #its the right side of ptip
ls=[]  #its the left side of ptip
cp=[] #its the cipher text after encryption
for i in range(8): #Encountering the intial premutataion stage-1
    count = ip[i]
    ptip.append(pt[count-1])
print("------------------------------------------------------------------")
print("printing the stage-1")
print("------------------------------------------------------------------")
print("Plain text after intal permutation",ptip)
rshalf=[1,1,0,1]
lshalf=[0,1,0,1]
#rshalf=ptip[:len(ptip)//2]
#lshalf=ptip[len(ptip)//2:]
print("The left half:",lshalf,"The right half:",rshalf)
#permuation on Right half
ep=[4,1,2,3,2,3,4,1]
for i in range(8):
    count = ep[i]
    rs.append(rshalf[count-1])
print("Right half after permutation:",rs)
#operating ex-or operation
outexor = exor.bitwise_xor(rs,k1)
print("After the Ex-OR opertion on RS:",outexor)
rows0=(str(outexor[0])+str(outexor[3]))
cols0=(str(outexor[1])+str(outexor[2]))
rows1=(str(outexor[4])+str(outexor[7]))
cols1=(str(outexor[5])+str(outexor[6]))
#binary to decimal
# Declaring the s0,s1 matrix
s0 = [[1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,1]]
s1 = [[0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]]
#print(rows0,cols0)
os0=(s0[int(rows0,2)][int(cols0,2)])
os1=(s1[int(rows1,2)][int(cols1,2)])
print("Intersection of row&col in s0:",os0," Intersection of row&col in s1:",os1)
#combining os0 and os1 i.e..,p4
p4 = str("{0:b}".format(os0))+str("{0:b}".format(os1))
p4 = [int(x) for x in str(p4)] 
print("P4:",p4)
#Ex-OR with left half with p4
outexor = exor.bitwise_xor(lshalf,p4)
print("Ex-OR operation on lshalf and p4 stage-1",outexor)
swap=[]
for i in range(8):
    if(i<=3):
        swap.append(rshalf[i])
    else:
        swap.append(outexor[i-4])
print("swapping stage-1",swap)
print("------------------------------------------------------------------")
rshalf=[1,0,1,0]
lshalf=[1,1,0,1]
rs2=[]
#----------------------------------------
import time
from tqdm import tqdm
for i in tqdm(range(10)):
    time.sleep(0.25)
#-----------------------------------------
print("printing the stage 2")
print("------------------------------------------------------------------")
print("The left half:",lshalf,"The right half:",rshalf)
#permuation on Right half
ep=[4,1,2,3,2,3,4,1]
for i in range(8):
    count = ep[i]
    rs2.append(rshalf[count-1])
print("Right half after permutation:",rs2)
#operating ex-or operation
outexor = exor.bitwise_xor(rs2,k2) # point to be noted using k2
print("After the Ex-OR opertion on RS:",outexor)
rows0=(str(outexor[0])+str(outexor[3]))
cols0=(str(outexor[1])+str(outexor[2]))
rows1=(str(outexor[4])+str(outexor[7]))
cols1=(str(outexor[5])+str(outexor[6]))
#binary to decimal
# Declaring the s0,s1 matrix
s0 = [[1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,1]]
s1 = [[0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]]
#print(rows0,cols0)
os0=(s0[int(rows0,2)][int(cols0,2)])
os1=(s1[int(rows1,2)][int(cols1,2)])
print("Intersection of row&col in s0:",os0," Intersection of row&col in s1:",os1)
#combining os0 and os1 i.e..,p4
p4 = str("{0:b}".format(os0))+str("{0:b}".format(os1))
p4 = [int(x) for x in str(p4)] 
print("P4:",p4)
#Ex-OR with left half with p4
outexor = exor.bitwise_xor(lshalf,p4)
print("Ex-OR operation on lshalf and p4 stage-2",outexor)
swap=[]
for i in range(8):
    if(i<=3):
        swap.append(outexor[i])
    else:
        swap.append(rshalf[i-4])
print("Swapping stage-2",swap)
#ip-1 permutation on swapped 
for i in range(8):
    count = ip_1[i]
    cp.append(swap[count-1])
print("CIPHERTEXT ->",cp)
