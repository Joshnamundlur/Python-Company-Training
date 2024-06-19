#missing alphabets :
'''
s=input()
v="abcdefghijklmnopqrstuvwxyz"
for i in v:
    if i not in s:
        print(i,end="")
'''
#take x and y 2 numbers such that y shd bcm 0 .if y =0 return x . else x<y interchange x and y
#else t=x-y and set x=y and y=t
'''
x=int(input())
y=int(input())
t=0
temp=0
while True:
    if x<y:
        temp=x #x,y=y,x
        x=y
        y=temp
    elif y==0:
        print(x)
        break
    elif x>=y:
        t=x-y
        x=y
        y=t
        '''

#fellis function using recurrsion
'''
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return f(n-1)+7*f(n-2)+(n//4)%(10**9+7)    
n=int(input())
print(f(n))
        
'''

#using for loop
'''
n=int(input())
lst=[1,1]
for i in range(2,n+1):
    ans=(lst[i-1]+7*lst[i-2]+i//4)%(10**9+7)
    lst.append(ans)
print(lst[n])
        
'''
#corner seat
'''
s=input()
l=list(map(str,input().split()))
n=l.index(s)
m=0
ans=0
#left
for i in range(0,n):
    if l[i]=="-":
        if abs(n-i)-1<m:
            m=abs(n-i)-1
#right
for i in range(n+1,len(s)):
    if l[i]=="-":
        if abs(i-n)-1<m:
            m=abs(i-n)-1
        
print(m)        
 '''
#spl fibbo
'''
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return (f(n-1)*2+(n-2)*2)%47    
n=int(input())
print(f(n))       
'''
# using for
'''
n=int(input())
lst=[1,1]
for i in range(2,n+1):
    ans=(lst[i-1]*2+(i-2)*2)%47
    lst.append(ans)
print(lst[n])
 '''
# maximiz sum product the sum of a pair shd be 18 and a>b and their product shd be greatest
'''
n=int(input())
l=list(map(int,input().split()))
l.sort()
mx=0
r=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]+l[j]==18:
            if l[i]>l[j]:
                r=l[i]*l[j]
                if mx<r:
                    mx=r
                    print(l[i],l[j])
'''
#give the minimum bitterness
'''
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=[]
for i in range(0,n):
        sm=a[i]+b[i]
        m.append(sm)
print(min(m))
'''                
#prefix and suffix:
'''
n=int(input())
l=list(map(int,input().split()))
ls=sum(l)
sm=0
res=[]
for i in range(0,n):
    sm=sm+l[i]
    ts=ls-sm
    res.append(abs(ts-sm))
print(res)    
'''        


'''
3 3 3 2 2 2 1 1 1 
3 3 2 2 1 1 
3 2 1
for i in range(3,0,-1):
    for j in range(3,0,-1):
        k=i
        while k>0:
            print(j,end=" ")
            k=k-1
    print()

'''



'''

#  abcdefg
#  3
#  2
#  a
#  cbadefg
a=input()
lst=list(a)
print(lst)
p=int(input())
k=int(input())
s=0
e=len(lst)
mini=999
if abs(p-k-1)>=0:
    s=abs(p-k-1)
if p+k<len(lst):
     e=p+k
print(s,e)
for i in range(s,e):
    mini=min(ord(lst[i]),mini)
store=lst[p-1]
lst[p-1]=lst[lst.index(chr(mini))]
lst[lst.index(chr(mini))]=store
print(mini)
print(''.join(lst))
'''    

'''
#gcd and lcm

def gcd(n1,n2):
    if n2==0:
        return n1
    
    return gcd(n2,n1%n2)
n1=int(input())
n2=int(input())
res=gcd(n1,n2)
print(res)
lcm=n1*n2//res
print(lcm)

      
#other way

a=12
b=18
while b!=0:
    temp=a
    a=b
    b=b%temp    
print(a)

'''

'''
x,n,y,m=map(int(input().split())
time=max(x,y)
while True:
    if time>=x and (time-x)%n==0 and time>=y and (time-y)%m==0:
        print(time)
        break
    time+=1

'''  
'''  
#generating numbers using permutations and combinations
n,a,b=map(int,input().split())
cnt=0
a1=n//a
b1=n//b
for i in range(0,a1+1):
    for j in range(0,b1+1):
        if i*a+j*b<10:
            cnt+=1
print(cnt)
'''
'''
#reverse the string
a=input()
s=a[::-1]
print(*s,sep="")


a=input().split()
s=a[::-1]
print(*s,sep="")


a=input()
s=list(a)
i=0
j=len(s)-1
while i<=j:
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    i=i+1
    j=j-1
print(''.join(s))
'''
'''
#Number of remaining toys
a,b=map(int,input().split())
print("the remaining of toys =",{a-b})
'''

#3 3 3 2 2 2 1 1 1 
#3 3 2 2 1 1 
#3 2 1


for i in range(3,0,-1):
    for j in range(3,0,-1):
        k=i
        while k>0: 
            print(j,end='')
            k=k-1
    print()









