'''
#Boring Arra:The difference of 2 max numbers and sum of diff values  

n=int(input())
a=list(map(int,input().split()))
s=0
i=0
j=len(a)-1
a.sort()
print(a)
while i<=j:
    d=a[j]-a[i]
    #d=abs(a[i]-a[j])
    s=s+d
    i+=1
    j-=1
print(s)

'''
'''
#Basket ball problem

#for(0,len(a)-sa+1) because sa is subarray size ,as we require
#last subarray we are suppose to do len(a)-sa
#eg: 7 8 9 4 2 1
#[7 8 9][8 9 4][9 4 2][4 2 1]

n=int(input())
sa=int(input())
a=list(map(int,input().split()))
mx=0
for i in range(0,len(a)-sa+Score1):
    t=a[i:i+sa]
    k=1 
    s=0
    for j in t:
        s=s+(j*k)
        k=k+1
    if s>mx:
        mx=s
print(s)

'''
'''
#a^2+b^2+ab+bc+ca=N
flag=0
n=int(input())
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if (i**2+j**2+k**2+i*j+j*k+k*i)==n:
                print(i,j,k)
                flag=1
if flag==0:
    print("None of the values are supported")
'''

'''
#Finding no of commas for a given number eg=5000=4001=1000-2000=1000 commas---
#as 5000 is not included +1 
c=0
n=int(input())
if n>1000:
    for i in range(1,n+1):
        if n>1000:
            d=len(str(i))
            t=(d//3)
            c=c+t
print(c)


n=int(input())
k=1
c=1000
ans=0
while c<n:
    milestone=c*1000
    nums=min(n-c+1,milestone-c)
    ans=ans+nums*k
    c=milestone
    k=k+1
print(ans)

'''
'''
#small leters ASCII 97-122 capital letters 65-90
#minimum distance b/w letters and their sum
#abcd   (97-120)=23----
#xyz    (a-x)-------

n=input()
n1=input()
s=0
m=999
for i in range(len(n)):
    for j in range(len(n1)):
       d=abs(ord(n[i])-ord(n1[j]))
       if d<m:
           m=d
           s=s+d
print(s)

'''

'''
#*
#**
#***
#****

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''
'''
#1
#12
#123
#1234

c=1
for i in range(1,5):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()
'''
'''
#   *
#  **
# ***
#****
r=4
for i in range(1,5):
    for j in range(1,r-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
'''


