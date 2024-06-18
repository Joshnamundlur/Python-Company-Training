'''#To find next greatest number

def next_greatest_element(nums):
    stack=[]
    result=[-1]*len(nums)
    for i in range(len(nums)):
        while stack and nums[i]>nums[stack[-1]]:
            result[stack.pop()]=nums[i]
        stack.append(i)
    return result
nums=[14,2,16,4,3,5]
print(next_greatest_element(nums))            
            
 '''
''' 
  #Election commission 

 
num=int(input())
l=[]
d={}
a=list(map(int,input().split()))
if num==1:
    print(a[0])
else:
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
ans=-1 
vals=list(d.items())
print(vals)
vals.sort(reverse=True,key=lambda x:x[1])
print(vals)
if vals[0][1]==vals[1][1]:
    ans=-1
else:
    ans=vals[0][0]
print(ans)    
 '''

'''
#smallest prime  number
count=0
num=int(input())
for i in range(2,num//2):
    if num%i==0:
        count=0
    else:
        count=1
if count==0:
    print("not prime")
else:
    print("prime")          
        
'''
'''
#next Smallest number for the given number grater than the number

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
k=n+1
while True:
    if isprime(k):
        print(k)
        break
    k+=1
    
   '''
'''          
#series n6,28,66,120,190,,276,378
n=6
k=22
for i in range(1,7):
    print(n)
    n=n+k
    k=k+16
    '''
'''        
a=2
b=3
for i in range(1,7):
    n=a*b
    print(n)
    a=a+2
    b=b+4
'''

