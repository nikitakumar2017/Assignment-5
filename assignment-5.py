#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter year "))
if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year! ")
        else:
            print("Not a leap year! ")
    else:
        print("Leap Year!! ")
else:
    print("Not a leap year") 

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("Enter length of quadrilateral "))
breadth=int(input("Enter breadth of quadrilateral "))
if(length==breadth):
    print("These dimensions are of a square ")
else:
    print("These dimensions are of a rectangle ") 

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
p1=int(input("Enter age of person 1 "))
p2=int(input("Enter age of person 2 "))
p3=int(input("Enter age of person 3 "))
if(p1>p2 and p1>p3):
    print("The oldest person is person 1")
elif(p2>p1 and p2>p3):
    print("The oldest person is person 2")
else:
    print("The oldest person is person 3")
if(p1<p2 and p1<p3):
    print("The youngest person is person 1")
elif(p2<p1 and p2<p3):
    print("The youngest person is person 2")
else:
    print("The youngest person is person 3")    

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 
#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR". 
age=int(input("Enter age "))
sex=input("Enter gender M or F ")
mar_stat=input("Enter marital status Y or N ")
if(sex=='F' and age>=20 and age <=60):
    print("Place of service: Urban Area's Only")
elif(sex=='M'):
    if(age>=20 and age<40):
        print("Place of service: Anywhere")
    elif(age>=40 and age<=60):
         print("Place of service: Urban Area's Only")
    else:
        print("ERROR")
else:
    print("ERROR")
        
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity.
#Suppose, one unit will cost 100.Judge and print total cost for user.
qty=int(input("Enter quantity of item "))
cost=100
totalcost=cost*qty
if(totalcost>1000):
    totalcost=(totalcost-(totalcost*0.1))
print("Total Cost = ",totalcost) 

#LOOPS 
#Q.1- Take 10 integers from user and print it on screen.
list1=[]
i=0
for i in range(10):
    num=int(input("Enter number "))
    list1.append(num)
for i in list1:
    print(i,end=' ') 

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
a=1
while(a>0):
    a+=1 

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
list1=[]
list2=[]
n=int(input("Enter number of elements you want to enter "))
for i in range(n):
    num=int(input("Enter element "))
    list1.append(num)
    list2.append(num**2)
print(list2) 

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
list1=[1,"Nikita",6.0,"Pankaj",8.95,407.2,580,"Yes"]
list_int=[x for x in list1 if isinstance(x,int)]
list_f=[x for x in list1 if isinstance(x,float)]
list_s=[x for x in list1 if isinstance(x,str)]
print(list_int)
print(list_f)
print(list_s)

#Q.5- Using range(1,101), make a list containing only prime numbers.
list1=[]
for i in range(1,101):
    if(i==1):
        pass
    else:
        j=2;
        flag=0
        while(j<i and flag==0):
            if(i%j!=0):
                flag=0
            else:
                flag=1
            j+=1
        if(flag==0):
            list1.append(i)
print(list1)

#Q.6- Print the following patterns: 
'''
* 
** 
*** 
****
'''
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end='')
    print()

#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
#Iterate over list using for loop.
list1=[]
flag=0
n=int(input("Enter number of elements you want to enter "))
for i in range(n):
    num=int(input("Enter element "))
    list1.append(num)
num=int(input("Enter number you want to search "))
for i in range(len(list1)):
    if(list1[i]==num):
        flag=1
if(flag==1):
    list1.remove(num)
    print(list1)
else:
    print("Element not found ")

        
    
