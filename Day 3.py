
'''      
 # next smallest number for the given array
def next_greatest_element(nums):
    stack=[]
    result=[-1]*len(nums)
    for i in range(len(nums)):
        while stack and nums[i]<nums[stack[-1]]:
            result[stack.pop()]=nums[i]
        stack.append(i)
    return result
nums=[12,14,2,16,5,3]
print(next_greatest_element(nums))    
'''

'''     
def previous_smallest_element(arr):
    n=len(arr)
    ans=[0]*n
    stack=[-1]
    for i in range(1,n+1):
        curr=arr[i]
        while stack[-1]!=-1 and stack[-1]<=curr:
            stack.pop()
        ans[i]=stack[-1] 
        stack.append(curr)
    return ans
top=[-1]
arr=[12,14,2,16,5,3]
print(previous_smallest_element(arr))
'''
'''def previous_greatest_element(arr):
    n=len(arr)
    ans=[0]*n
    stack=[-1]
    for i in range(1,n+1):
        curr=arr[i]
        while stack[-1]!=-1 and stack[-1]>=curr:
            stack.pop()
        ans[i]=stack[-1] 
        stack.append(curr)
    return ans
top=[-1]
arr=[12,14,2,16,5,3]
print(previous_greatest_element(arr))
'''


'''        
# Ant and Rail        
steps=int(input())
a=list(map(int,input().split()))
sp=0
ans=0
for i in a:
    sp=sp+i
    if sp==0:
        ans=ans+1
print(ans)        
 '''
'''       
 #Chocolate Jar


qnt_choc=list((map(int,input().split())))
N=int(input())
a=0
for i in qnt_choc:        
    a=(i//3)+a
    if(i%3)==0:
        a=a+0 
    else:
        a=a+1
print(a)      
 '''
''' 
#Dog Age

n=int(input()) 
a=n*7
print(a)   
 '''


'''   
#Diwali Problem

qns_time=0
solved=0
n=int(input())
time=int(input())
left_time=240-time
for i in range(1,n+1):
    qns_time=5*i+qns_time
    if (qns_time<=left_time):
        solved=solved+1
print(solved) 
'''
'''
#other way
c=0
s=0
tot=int(input())
n=int(input())
rt=240-tot 
for i in range(1,n+1):
    s=s+5*i
    if s>rt:
        break
    c=c+1
print(c)
 '''

