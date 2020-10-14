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
'''S-des key generation'''

#---------------------------------------------------------------------------------------------
# Creating array taking input from user
'''key=[]
print("enter the 10 bit key")
for i in range(0,10):
    x=int(input())
    key.append(x)
    i+=1'''

#---------------------------------------------------------------------------------------------
#creating and declaring the array and premutation
per10 = [3,5,2,7,4,10,1,9,8,6]
key = [1,0,1,0,1,1,0,0,1,0]
per8 = [6,3,7,4,8,5,10,9]
k1=[]
k2=[]
temp=[]
p10key=[]
i=0
count = 0
while(i<10):
    count = per10[i]
    p10key.append(key[count-1])
    i = i+1
print("\nprinting the key after permutation on key: \n",p10key)

#---------------------------------------------------------------------------------------------
#shifting level-1 on ls1
for i in range(5):
    if(i==4):
        p10key[i]=p10key[0]
    else:
        p10key[i]=p10key[i+1]

#shifting level-1 on rs1
for i in range(5,10):
    if(i==9):
        p10key[i]=p10key[5]
    else:
        p10key[i]=p10key[i+1]
print("\nprinting the p10key after shift-1: \n",p10key)

#-----------------------------------------------------------------------------------------------
#permutation on p10key with p8 -->> k1 per8 = [6,3,7,4,8,5,10,9]
for i in range(8):
    count = per8[i]
    k1.append(p10key[count-1])
    i = i+1
    #print(k1)
print("\nprinting the k1 after permutation on p10key: \n",k1)

#-----------------------------------------------------------------------------------------------
#shifting level-2 on ls1 2-times
for j in range(0,2):
    x=p10key[0]
    for i in range(0,5):
        if(i==4):
            p10key[i]=x
        else:
            p10key[i]=p10key[i+1]
#shifting level-2 on rs1 2-times
for j in range(0,2):
    y=p10key[5]
    for i in range(5,10):
        if(i==9):
            p10key[i]=y
        else:
            p10key[i]=p10key[i+1]
print("\nprinting the p10key after shift-1.1: \n",p10key)

#-----------------------------------------------------------------------------------------------
#permutation on p10key with p8 -->> k1 
for i in range(8):
    count = per8[i]
    k2.append(p10key[count-1])
    i = i+1
    #print(k1)
print("\nprinting the k2 after permutation on p10key: \n",k2)
print("\nthe two keys are \n",k1,k2)


