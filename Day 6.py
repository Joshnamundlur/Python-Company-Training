
'''
# Pizza Party
s=0
ans=0
a,y=list(map(int,input().split()))
while True:
    if a%y!=0:
        y=y+1
    else:
        ans=y
        break
while ans>0:
    r=ans%10
    s=s+r
    ans=ans//10
print(s)
        
'''
'''
#Equilibrium or not
sm=0
s1=0
flag=0
n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    s=sum(lst)
    d=s//2
for j in range(1,len(lst)+1):
    if d>sm:
        sm=lst[j]+sm
        equ=j
        flag=1
    else:
        equ1=(n//2)+1
        flag=0
if flag==1:
    print(equ)
else:
    print(equ1)



a=list(map(int,input().split()))
for i in range(0,len(a)):
    i1=1
    j=i+1
    s1=0
    s2=0
    #left side
    while i>=0:
        s1+=a[i]
        i=i-1
    #right side
    while j<len(a):
        s2+=a[j]
        j=j+1
    if s1==s2:
        f=1
        break
if f==0:
    print(len(a//2)+1)

'''


'''
# Peak Value of the given array
mx = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(1,len(a)-1):
    if a[i-1] <= a[i] and a[i]>=a[i+1]:
        peak = a[i]
        if peak>mx:
            mx=peak

print(mx)
'''

'''
#find the unique triplets ip=5 3 20 10 1 4 2 
#and find the product which is matching to prooduct

n=int(input())
a=list(map(int,input().split()))
prdt=int(input())
triplet_cnt=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]*a[j]*a[k]==prdt:
                print(a[i],a[j],a[k])
                triplet_cnt+=1
print(triplet_cnt)
'''
'''
#contiguos sub array with max value
#kadanes algorithm

a=list(map(int,input().split()))
c_sum=0
mx_sum=0
for i in a:
    c_sum+=i
    if c_sum<0:
        c_sum=0
    if c_sum>mx_sum:
        mx_sum=c_sum
print(mx_sum)

'''
'''
#Target sum,calculate the sum of array elements eqaul to the target sum

a=list(map(int,input().split()))
target_s=int(input())
a.sort
i=0
j=len(a)-1
while i<j:
    curr_s=a[i]+a[j]
    if curr_s==target_s:
        print(i,j)
        i=i+1
        j=j-1
    elif curr_s<target_s:
        i+=1
    else:
        
        j-=1
'''
'''

#minimum no of keys pressed for 0 cnt is 1 and rest numbers from 10-9 cnt is 1
cnt=0
cnt2=0
cnt3=0
s=input()
for i in range(0,len(s)-1):
    if s[i]+s[i+1]=="00":
        i=i+2
        cnt=cnt+1
    if i<len(s):
        cnt=cnt+1        

    else:
        cnt=cnt+1
        i=i+1

print(cnt)
'''

'''
s=input()
i=0
c=0
while i<len(s):
    if s[i]=='0' and s[i+1]=='0':
        c+=1
        i+=2
    else:
        c+=1
        i+=1
    if i<len(s):
        c=c+1     
print(c)

'''

'''
#string consisting of small letters convert all letters into same letter using 
#magic string by replacing all letters with the maximum letters which are present
#aaabbbccdddd=dddddddd=8

mx=0
c=0
s=input()
d={}
for i in s:
    if i in d:
        d[i]+=1
        if d[i]>mx:
            mx=d[i]
        m=len(s)-mx
    else:
        d[i]=1

print(m)        

'''

