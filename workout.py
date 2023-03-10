def main(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
main
def div():
    number=int(input("Enter the number"))

    if number%2==0:
        print("flase")
    elif number%3==0:
        print("false")
    elif number%5==0:
        print("Flase")
    elif number%7==0:
        print("Flase")
    else:
        print("True")
div
def num():
    i=500
    while(i>0):
        print(i, end="")
        print("\r")
        if i==200:
            break
        i-=2
    
        
num

'''def char():
    a=[0]
    for i in range(10):
        print(i)
        evennum=[]
        if i%2==0:
            evennum.append(i)
            print(evennum)
            print("\r")

char()'''

'''a=0
for i in range(200,500):
    for j in range(0,i%2==0):
        print(i,end="")
        print("\r")'''


'''a=0
for i in range(0,5):
    for j in range(0,i+1):
        print("P ",end="")
        print("\r")'''

'''list=[1,2,3,4,5,8,9,10]

odd=[]
even=[]
for i in range (0,len(list)):
    if i%2==0:
        even.append(list[i])
        print(f"Even Number Are:{odd}")
    else:
        odd.append(list[i])
        print(f"Odd Number Are:{even}")'''



'''for i in range(4):
    for space in range(0,-6):
        
            print(i,end="")
            for j in range(0,i+1):  
                i-=1   

            
    print("\r")'''


'''num1=1
string="krithiv"

covert=str(num1)
print(covert)
print(type(covert))
add=string+covert

print(add)'''
number="1"
convert=int(number)
print(convert)
print(type(convert))
convertf=float(number)
print(type(convertf))


'''user=input("Enter the Day:")

if user=="monday":
    
    time=input("Enter the time:")
    if time=="mrng":
        print("dosa")
    elif time=="afternoon":
        print("rice")
    elif time=="night":
        print("idly")
elif user=="tuesday":
    
    time1=input("Enter the time")
    if time1=="mrng":
        print("idly")
    elif time1=="afternoon":
        print("briyani")
    else:
        print("chapathi")
else:
    print("Sorry the incovinence")'''

'''for i in range(1,100):
    if i%3==0:
        print("Nav")
    if i%7==0:
        print("Gurkul")
    if i%3==0 and i%7==0:
        print("NavGurkul")
    else:
        print(i)'''

'''i=1
while i<100:
    if i%3==0:
        print("Nav")
    if i%7==0:
        print("Gurkul")
    if i%3==0 and i%7==0:
        print("NavGurkul")
    else:
        print(i)
    i=i+1'''

'''i=0
sum=0
while i<10:
    user=int(input("Enter the Number:"))
    sum+=user
    i+=1
print(sum)'''

'''i=156
while i<166:
    
    print(i-156)
    i=i+1'''
'''s=0
# j=0
for i in range(3):
    s=s+10
print(s)'''
'''s=0
for i in range(7):
    s=s+7
print(s)'''
'''a=0
user1=int(input("Enter the Number:"))
user2=int(input("Enter the SecondNumber:"))
for i in range(user1):
    a=a+user2
print(a)'''
'''i=0
d=0
user3=int(input("Enter the Number:"))
user4=int(input("Enter the Second Number:"))
while i<user3:
    d=d+user4
    i=i+1
print(d)'''

'''i=0

while i<100:
    if i%2==0:
        print(i*-1,end=" ")
    else:
        print(i,end=" ")
    i=i+1'''

'''user=int(input("Enter the Number:"))
if user>1:
    for i in range(2,user):
        if user%i==0:
            print(f"{user}not a prime")
            break
        
    else:
        print(f"{user}is a prime")'''

'''user1=int(input("Enter the Number:"))
i=2

while i>=2 and user1:

    if user1%i==0:
        print(f"{user1}is not a prime")
        break
    i=i+1
else:
        print(f"{user1}prime Number")'''
    
'''user=int(input("Enter the Number:"))

for i in range(2,user):
    if user%i==0:
        print(f"{user}its a notprime number")
        break
else:
    print(f"{user}its  prime")'''

'''user1=int(input("Enter the Number1:"))
user2=int(input("Enter the Number2:"))
s=0
for i in range(user1):
    s=user2+s
print(s)'''

'''user=int(input("Enter the Number:"))

for i in range(2,user):
    if user%i==0:
        print(f"{user}not a prime")
        break
else:
    print(f"{user}is a prime")'''


'''s=0
for i in range(1):
    num1=int(input("Enter the Number you want:"))
    
    s=s+i
print(s)'''
a = '1 2'

x = '1'
y = '2'

q=int(x)
w=int(y)

print(int(x),int(y))

print("check")

            



