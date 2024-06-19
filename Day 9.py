

'''


#          1                                         1
#         212                I/P=3   Explanation    212
#        32123               o/p=17                32123
#       4321234                          sum=1+2+1+2+3+2+1+2+3=17
#     543212345
#N________212________N



s=0
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i,1,-1):
        print(k,end=" ")
        s+=k
    for l in range(1,i+1):    
        print(l,end=" ")
        s+=l
    print()
print(s)
'''


'''
n=int(input())
o=1
res=0
s=0
for i in range(1,n+1):
    d=sum(range(2,i+1))
    s=o+2*d
    res+=s
print(res)
'''
#sirs solution
'''
row=int(input())
ans=0
for i in range(2,row+1):
    n=i
    while n>1:
        ans+=2*n
        n=n-1
ans+=row
print(ans)    
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

#robo
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
'''


