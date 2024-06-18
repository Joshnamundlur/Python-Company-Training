'''
#encode the number 

def en(n):
    result=0
    factor=1
    while n>0:
        digit=n%10
        sq=digit*digit
        if sq<10:
            result=sq*factor+result
            factor*=10
        else:
            result=sq*factor+result
            factor*=100
        n//=10
    return result
n=int(input())
en1=en(n)
print(en1)
'''


''' 
#Toss a coin to calculate if H then 2 if T -1 score,if continuos 3 heads end and if all are tails end game

cnt1=0
cnt2=0
Score1=0
string=input()
for i in string:
    if i=='H':
        cnt2=0
        cnt1=cnt1+1
        Score1=Score1+2
        if cnt1==3:
           break
    elif i=='T':
        cnt1=0
        cnt2=cnt2+1
        Score1=Score1-1
        if cnt2==len(string):
            break
print(Score1)

                
'''

'''

#find the Missing and Repeated values 

r=3
c=3
a=[]
d={}
ans=[]
for i in range(0,r):
    sub=[]
    print("Enter the values of row",i )
    for j in range(0,c):
        print("Enter the values of column",j)
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] in d:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
        else:
            d[a[i][j]]=1
print(d)
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)
    
'''

'''
#  encrypt of given number (523)=555=5+5+5=15   [10,21,31]=[11,22,33]=11+22+33=66

def encrypt(n):
    c=0
    mx=0
    ans=0
    while n>0:
        digit=digit%10
        if digit>mx:
            mx=digit
            c+=1
            n=n//10
    while c>0:
        ans=ans*10+mx
        c=c-1
    return(ans)
n=list(map(int,input().split()))
fn_ans=0

'''
'''
# Vowel Repetation  Problem
s=input()
mx=0
ans=0
d={}
for j in s:
    if j in d:
        if j=='a'or j=='e' or j=='i' or j=='o' or j=='e':
            d[j]+=1
        if d[j]>mx:
            mx=d[j]
            ans=j
    else:
        d[j]=1
print(d)
print(ans)

s=input()
d={}
ans=0
v="aeiou"
mx=0
for j in s:
    if j in v:
        if j not in d:
            d[j]=1
            
        else:
            d[j]+=1
        if d[j]>mx:
            mx=d[j]
            ans=j
print(ans)            

'''

'''
#prime factors of given positive number and its index of factors is multiplied with power of factors and provide the sum


def pf(n):
    ans=[]
    i=2
    while i<=n:
        if n%i==0:
            ans.append(i)
            n=n//i
        else:
            i=i+1
    return ans

ans=pf(6)
s=0
a=[11,12,13,14,15,16]
for i in ans:
    s=s+a[i]
print(s)
'''
          

