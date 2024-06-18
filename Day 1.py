'''
n=int(input())
i=0
j=0
a=[]
for i in range(n):
    if a[i]!=0:
        a[j]=a[i]
        j=j+1
while j<n:
    a[j]=0
    j=j+1    
'''


'''    
#Classes and objects Examples
class cse1:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        self.a=20
        self.b=30
        print("i am the constructor")
    def strength(self):
        print("the strength of a classs is 101")
        self.s=101
    def kn(self,c,d):
        print("the knowledge is good")
        self.know="good"
        pro=c*d
        print(pro)
    def details(self):
        c_s=self.s-10
        print(c_s,self.know)
        print(self.a+self.b)
day_2=cse1(30,40)
day_2.strength()
day_2.kn(10,20)
day_2.details()

 '''

'''
   #single level
class faculty:
    def __init__(self,f_name,dpartment,f_id):
         self.f_name=f_name
         self.dpartment=dpartment
         self.f_id=f_id
    def print_info(self) :
        print('faculty information =',self.f_name,self.dpartment,self.f_id)
obj=faculty("ashish","computer_science",1001)
obj.print_info()

#class child_classname(parent_classname):
        #child parent
class cse(faculty):  #faculty classB
    pass  #no statement
obj1=cse("Jyothi mam","computer_science",1002)
obj1.print_info()

'''
'''
Zero one to sort

a=[2,1,0,1,1,2,0,0]  #==[0,0,0,1,1,1,2,2,2]   
c0=0
c1=0
c2=0
for i in range(len(a)):
    if a[i]==0:
        c0=c0+1
    elif a[i]==1:
        c1=c1+1
    else:
        c2=c2+1
j=0
while c0>0:
    a[j]=0
    j=j+1
    c0=c0-1
while c1>0:
    a[j]=1
    j=j+1
    c1=c1-1
while c2>0:
    a[j]=2
    j=j+1
    c2=c2-1 
    
print(a)
'''


'''
#Grouping all non-zeros at beginning and zeros at one place
l=[4,0,5,0,1,9,0,0]
j=0
for i in range(0,len(l)):
    if l[i]!=0:
        l[j]=l[i]
        j=j+1
while j<len(l):
    l[j]=0 
    j+=1
print(l)  

'''

'''
#2 Factorial

def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1) 
n=int(input()) 
print(fact(n))      
'''

'''
#3 fibonacci


def p(base,expo):
    if expo==0:
        return 1
    return base*p(base,expo-1)

base=int(input())
expo=int(input())
print(p(base,expo))
'''

'''
#4 Sum of given digits using recursion
def sum(n):
    if n==0:
        return 0
    else:
        return n%10+sum(n//10)
n=int(input()) 
print(sum(n))   
'''


'''
#5 concept of class,object,functions,keywords
class cse1:
    def _init_(self,a,b):
        self.a1=a
        self.b1=b
        self.a=20
        self.b=30
        print("im constructor")
    def strength(self):
        print("The Strength is 101")
        self.s=101
    def kn(self,c,d):
        print("Knowledge is good")
        self.know="good"
        pro=c*d
        print(pro)
    def details(self):
        print("current strength and knowledge")
        c_s=self.s-10
        print(c_s,self.know)
        print(self.a+self.b)
day_2=cse1()
print("from below in making function calls")
day_2.strength()
day_2.kn(10,20)
day_2.details()
'''


'''#6 single level inheritance
class faculty:#parent classA
  def _init_(self,f_name,dpartment,f_id):
      self.f_name=f_name
      self.dpartment=dpartment
      self.f_id=f_id
  def print_info(self):
      print('faculty information=',self.f_name,self.dpartment,self.f_id)
obj=faculty("Ashish","computer_sciene",1001)
obj.print_info()
'''
''' 
#class child_classname(parent_classname):
  #child #parent
class cse(faculty):#child classB
  pass #no statement
obj1=cse("Jyoti mam","computer_science",1002)
obj1.print_info() 

#7 Multiple inheritance
class SubjMarks:#class-1
   math=int(input("Enter paper marks of math"))
   DE=int(input("Enter paper marks of design engineering")) 
   c=int(input("Enter paper marks of c language"))
   english=int(input("Enter paper marks of english"))
   
 #parent class-1  
class PractMarks:#class-2
 cpract=int(input("Enter practicals marks of c languafe"))
#parent class-2
class Result(subjMarks,PractMarks):
'''



'''
#carshowroom
class car:
    def __init__(self):
        self.cgst=5555
        self.sgst=5555
        self.insurance = 5555
    def company (self):
         while True:
             print("Toyota, Mercedes")
             self.n = input("enter the car company")
             if self.n=="Toyota":
                 print("welcome to toyo")
                 self.model()
                 break
             elif self.n=="Mercedes":
                 print("welcome to merc")
                 self.model()
                 break
    
             else:
                print("enter valid company")
    def model(self):
        if self.n=="Toyota":
            while True:
                print("Select from Fortuner and LC")
                self.choice = input("Enter the car model")
                if self.choice=="Fortuner":
                    self.price(self.choice)
                    break
                elif self.choice =="LC":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid")
        elif self.n=="Mercedes":
            while True:
                print("Select from amg and gw")
                self.choice = input("Enter the car model")
                if self.choice == "amg":
                    self.price(self.choice)
                    break
                elif self.choice == "gw":
                    break
                else:
                    print("enter valid")
    def price(self, choice):
        if choice=="Fortuner":
            self.p=4500000
        elif choice=="LC":
            self.p=1000000
        elif choice=="amg":
            self.p=24432874
        elif choice=="gw":
            self.p=843726837
        tot_p=self.p+self.sgst + self.cgst +self.insuranci
        print(tot_p)
c=car()
c.company()
'''

