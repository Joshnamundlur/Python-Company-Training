'''    
#basket ball
max_score=-1
goals=int(input())
sub_array=int(input())
array=list(map(int,input().split()))
for i in range(0,len(array)-sub_array+1):
    temp=array[i:i+sub_array]
    k=1
    s=0
    for j in temp:
        s=s+(j*k)
        k=k+1
    if s>max_score:
        max_score=s
print(max_score)

'''
'''
#Space Counter
cnt=0
word=input()
for i in word:
    if i==' ':
        cnt=cnt+1
print(cnt)


word=input()
h=word.split()
print(len(h)-1)
'''

'''
#Encoded the number
n=int(input())
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    return c
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod(sq)+sq)
        n=n//10
    return(ans)
ans=rev(n)
def rev2(n):
    while n>0:
        ans2=0
        digit=n%10
        ans2=ans2*10+digit
        n=n//10
    return ans2
print(rev2(ans))
'''

'''
#Farthest Distance
n=list(map(int,input().split()))
s=0
mx=-1
for i in n:
    s=s+i
    if s>mx:
        mx=s   
print(mx)    
'''

'''
#Minimum Array sum


n=list(map(int,input().split()))
mx=0
mx1=0
sum1=0
for i in n:
    if i>mx:
        mx=i
for j in n:
    if j>mx1 and j<=mx:
        mx1=j
avg=(mx+mx1)//2
for k in n:
    if k>avg:
        sum1=sum1+k
print(sum1)
'''

'''
n=list(map(int,input().split()))
mx=0
mx1=0
sum1=0
for i in n:
    if i>mx:
        mx=i
for i in n:
    if i>mx1 and i!=mx:
        mx1=i
avg=(mx+mx1)//2
for i in n:
    if i>avg:
        sum1=sum1+i
print(sum1)
'''